"""Run Research Smarter test cases with the Claude command line, then grade them.

Each run starts a fresh `claude -p` session in an empty work folder outside the
repo (so the repo's CLAUDE.md and memory don't leak in), copies the case's input
files there, and tells Claude to read the skill at --skill and follow it. The
Skill tool is turned off so the installed copy in ~/.claude/skills can't be used
instead. A separate Claude call grades every grader statement with quoted
evidence.

Each run also saves opened.jsonl: the text of every page Claude opened, so
tests/check_links_opened.py can verify links and DOIs. Those pages are often
copyrighted articles, so keep opened.jsonl in the gitignored workspace and
never commit it.

Usage (from the repo root):
  python3 tests/run_skill_eval.py --skill research-smarter --label new \
      --cases how-do-you-know common-knowledge-challenge --runs 3 \
      --out research-smarter-workspace/iteration-4
  python3 tests/run_skill_eval.py --grade-only FILE.md --cases CASE   # grade a hand-written reply
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVALS = os.path.join(ROOT, "research-smarter", "evals")
CLAUDE = os.path.expanduser("~/.local/bin/claude")
BASE_FLAGS = ["--no-session-persistence", "--strict-mcp-config", "--disallowed-tools", "Skill"]


def read_case(name):
    d = os.path.join(EVALS, name)
    raw = open(os.path.join(d, "prompt.md")).read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
    front, body = m.group(1), m.group(2).strip()
    tools = re.search(r"allowed_tools:\s*\[(.*?)\]", front).group(1)
    tools = [t.strip() for t in tools.split(",") if t.strip() and t.strip() != "Skill"]
    graders = []
    for f in sorted(os.listdir(os.path.join(d, "graders"))):
        text = open(os.path.join(d, "graders", f)).read().split("---", 2)[-1].strip()
        graders.append({"id": f[:-3], "text": text})
    return {"name": name, "dir": d, "prompt": body, "tools": tools, "graders": graders}


def build_prompt(case, skill):
    user = case["prompt"].replace("Input files: research-log.md", "").strip()
    has_log = os.path.exists(os.path.join(case["dir"], "files", "research-log.md"))
    return (
        f"You have the Research Smarter skill at {skill}. Before replying, read "
        f"{skill}/SKILL.md and follow it exactly, reading its reference files as it "
        "directs. Reply to the user as the skill directs, as your final message.\n\n"
        + ("The user attached research-log.md, which is in the current folder.\n\n" if has_log else "")
        + "The user's message:\n\n" + user
    )


def expand_loop_urls(command):
    """URLs in a shell command, with simple `for x in a b c; do ... $x ...` loops expanded."""
    urls = re.findall(r"https?://[^\s'\"]+", command)
    for var, values in re.findall(r"for\s+(\w+)\s+in\s+(.+?);\s*do", command):
        vals = [v.strip("'\"") for v in values.split()]
        for u in list(urls):
            for form in ("${%s}" % var, "$" + var):
                if form in u:
                    urls += [u.replace(form, v) for v in vals]
    return urls


def run_once(case, skill, out_dir):
    work = tempfile.mkdtemp(prefix="rs-eval-")
    files = os.path.join(case["dir"], "files")
    if os.path.isdir(files):
        shutil.copytree(files, work, dirs_exist_ok=True)
    # --allowed-tools only pre-approves tools; it doesn't block the rest, so
    # web tools a case doesn't list must be disallowed explicitly.
    blocked = [t for t in ("WebSearch", "WebFetch") if t not in case["tools"]]
    cmd = [CLAUDE, "-p", "--output-format", "stream-json", "--verbose",
           "--add-dir", skill, "--allowed-tools", *case["tools"], *BASE_FLAGS, *blocked]
    t0 = time.time()
    r = subprocess.run(cmd, input=build_prompt(case, skill), capture_output=True,
                       text=True, cwd=work, timeout=900)
    secs = round(time.time() - t0, 1)
    reply, tool_log = "", []
    calls, opened = {}, []  # tool_use id -> (name, input); pages Claude opened, with what it saw
    for line in r.stdout.splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "assistant":
            for c in ev["message"].get("content", []):
                if c.get("type") == "tool_use":
                    inp = c.get("input", {})
                    calls[c.get("id")] = (c["name"], inp)
                    detail = inp.get("url") or inp.get("query") or inp.get("file_path") or inp.get("command") or ""
                    tool_log.append(f"{c['name']}: {str(detail)[:200]}")
        if ev.get("type") == "user":
            content = ev.get("message", {}).get("content", [])
            for c in content if isinstance(content, list) else []:
                if c.get("type") != "tool_result":
                    continue
                name, inp = calls.get(c.get("tool_use_id"), ("", {}))
                body = c.get("content", "")
                if isinstance(body, list):
                    body = "\n".join(b.get("text", "") for b in body if isinstance(b, dict))
                if name == "WebFetch":
                    opened.append({"tool": name, "urls": [inp.get("url", "")], "text": str(body)[:400000]})
                elif name == "Bash" and re.search(r"\b(curl|wget)\b", inp.get("command", "")):
                    urls = expand_loop_urls(inp.get("command", ""))
                    opened.append({"tool": name, "urls": urls, "command": inp.get("command", "")[:4000],
                                   "text": str(body)[:400000]})
        if ev.get("type") == "result":
            reply = ev.get("result", "")
    os.makedirs(out_dir, exist_ok=True)
    # Keep files Claude created (for example the mind map) so the grader can see them.
    inputs = set(os.listdir(files)) if os.path.isdir(files) else set()
    made = os.path.join(out_dir, "outputs")
    for name in os.listdir(work):
        src = os.path.join(work, name)
        if name in inputs or not os.path.isfile(src):
            continue
        os.makedirs(made, exist_ok=True)
        shutil.copy(src, made)
    with open(os.path.join(out_dir, "opened.jsonl"), "w") as f:
        for page in opened:
            f.write(json.dumps(page) + "\n")
    open(os.path.join(out_dir, "reply.md"), "w").write(reply)
    open(os.path.join(out_dir, "tool_log.md"), "w").write(
        "# Tool log\n\n" + "\n".join(f"{i+1}. {t}" for i, t in enumerate(tool_log)) + "\n")
    shutil.rmtree(work, ignore_errors=True)
    return reply, tool_log, secs, r.stderr[-500:]


GRADER_PROMPT = """You are grading one reply from a research-coaching assistant against a list of statements.
For each statement, decide whether it is TRUE of the reply, and quote the shortest piece of the
reply (or tool log) that shows it. Be strict and literal. Judge only what is written.

THE USER'S MESSAGE:
{prompt}

TOOLS THE ASSISTANT USED THIS SESSION (searches and pages opened):
{tools}

DOIS ON OPENED PAGES (found in the text of pages the assistant opened; search results excluded):
{dois}

THE REPLY:
<<<
{reply}
>>>

FILES THE ASSISTANT CREATED (shortened):
{files}

STATEMENTS:
{statements}

Answer with only a JSON array, one object per statement, in order:
[{{"id": "...", "passed": true or false, "evidence": "short quote or reason"}}]"""


def made_files(out_dir):
    d = os.path.join(out_dir or "", "outputs")
    if not out_dir or not os.path.isdir(d):
        return "(none)"
    parts = []
    for name in sorted(os.listdir(d)):
        text = open(os.path.join(d, name), errors="replace").read()
        if name.endswith(".html"):  # the mind map's data is what matters, not the template
            i = text.find("const DATA =")
            text = text[i:] if i >= 0 else text[-6000:]
        parts.append(f"--- {name} ---\n{text[:6000]}")
    return "\n".join(parts)


def opened_dois(out_dir):
    path = os.path.join(out_dir or "", "opened.jsonl")
    if not out_dir or not os.path.exists(path):
        return "(not recorded for this run)"
    found = set()
    for line in open(path):
        page = json.loads(line)
        text = page.get("text", "").replace("\\/", "/") + " " + " ".join(page.get("urls", []))
        found.update(d.rstrip(".,;:").lower() for d in re.findall(r"10\.\d{4,9}/[^\s)<>\]\"'`,;]+", text))
    return "\n".join(sorted(found)) or "(none)"


def grade(case, reply, tool_log, out_dir=None):
    statements = "\n".join(f'- id "{g["id"]}": {g["text"]}' for g in case["graders"])
    prompt = GRADER_PROMPT.format(prompt=case["prompt"], reply=reply, files=made_files(out_dir),
                                  dois=opened_dois(out_dir),
                                  tools="\n".join(tool_log) or "(none)", statements=statements)
    for _ in range(2):
        r = subprocess.run([CLAUDE, "-p", "--no-session-persistence", "--strict-mcp-config",
                            "--disallowed-tools", "Bash", "Read", "Write", "Edit", "Glob", "Grep",
                            "WebSearch", "WebFetch", "Skill"],
                           input=prompt, capture_output=True, text=True, timeout=300,
                           cwd=tempfile.gettempdir())
        m = re.search(r"\[.*\]", r.stdout, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except ValueError:
                pass
    return [{"id": g["id"], "passed": False, "evidence": "GRADER ERROR"} for g in case["graders"]]


def job(case, skill, label, run, out_root):
    out_dir = os.path.join(out_root, case["name"], label, f"run-{run}")
    reply, tool_log, secs, err = run_once(case, skill, out_dir)
    results = grade(case, reply, tool_log, out_dir) if reply else [
        {"id": g["id"], "passed": False, "evidence": "NO REPLY: " + err} for g in case["graders"]]
    json.dump({"case": case["name"], "label": label, "run": run, "seconds": secs,
               "expectations": [{"text": g["text"], "passed": res.get("passed"), "evidence": res.get("evidence")}
                                for g, res in zip(case["graders"], results)]},
              open(os.path.join(out_dir, "grading.json"), "w"), indent=2)
    passed = sum(1 for x in results if x.get("passed"))
    print(f"{case['name']} [{label} run {run}] {passed}/{len(results)} in {secs}s", flush=True)
    return case["name"], label, run, results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", help="path to the skill folder to test")
    ap.add_argument("--label", default="new")
    ap.add_argument("--cases", nargs="+", required=True)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--out", default=os.path.join(ROOT, "research-smarter-workspace", "iteration-4"))
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--grade-only", help="grade a hand-written reply file instead of running")
    ap.add_argument("--tools-file", help="with --grade-only: a text file listing the tools used, one per line")
    a = ap.parse_args()

    if a.grade_only:
        case = read_case(a.cases[0])
        tools = open(a.tools_file).read().splitlines() if a.tools_file else []
        res = grade(case, open(a.grade_only).read(), tools)
        print(json.dumps(res, indent=2))
        return

    skill = os.path.abspath(a.skill)
    cases = [read_case(c) for c in a.cases]
    for c in cases:
        os.makedirs(os.path.join(a.out, c["name"]), exist_ok=True)
        json.dump({"eval_name": c["name"], "prompt": c["prompt"], "assertions": [g["text"] for g in c["graders"]]},
                  open(os.path.join(a.out, c["name"], "eval_metadata.json"), "w"), indent=2)
    jobs = [(c, r) for c in cases for r in range(1, a.runs + 1)]
    with cf.ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda cr: job(cr[0], skill, a.label, cr[1], a.out), jobs))


if __name__ == "__main__":
    main()
