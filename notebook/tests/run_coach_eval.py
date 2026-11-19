"""Reader coach evaluation and plain-Claude comparison (issue #5; SPEC R11, acceptance criterion 6).

For each case in notebook/tests/coach_cases.json, runs:
  - the Reader's coach: the exact prompt the page builds (Coach.buildInput), and
  - plain Claude: the same article and the same student message, asked as
    "help me understand this study",
each RUNS times through the Claude command line, then grades every reply
with the same checks:
  - code checks: quotes really in the article, question marks, mentions of
    teachers or grades, fallacy names, references to a research question;
  - a separate Claude grader for judgments code can't make (each verdict
    comes with quoted evidence).

The command line is a stand-in for the page's own call to Claude: same
prompt, different connection.

Usage (from the repository root):
  python3 notebook/tests/run_coach_eval.py                 # full run
  python3 notebook/tests/run_coach_eval.py --check-checks  # grade known-bad replies only
Outputs go to notebook/results/coach-eval/.
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HTML = os.path.join(ROOT, "notebook", "notebook.html")
ARTICLE_PATH = os.path.join(ROOT, "notebook", "tests", "fixtures", "mock-study.txt")
CASES_PATH = os.path.join(ROOT, "notebook", "tests", "coach_cases.json")
OUT = os.path.join(ROOT, "notebook", "results", "coach-eval")
CITATION = "Mock (2026). Lunchroom talk after school-day phone restrictions."
PROJECT = {
    "question": "How have school-day phone bans changed how high school students interact with each other in person?",
    "position": "Phone bans increase face-to-face interaction during the school day, but they don't reduce social conflict, they just move it to after school.",
}
CLAUDE = os.path.expanduser("~/.local/bin/claude")
NO_TOOLS = ["--disallowed-tools", "Bash", "Read", "Write", "Edit", "Glob", "Grep",
            "WebSearch", "WebFetch", "Skill", "Task", "NotebookEdit"]

COMMON = [
    ("no_summary", "R11.3",
     "The reply does not summarize, explain or paraphrase details or findings of the article that the student did not already state. Quoting one passage to correct a factual error the student made does not count as summarizing. Pointing to where in the article to look (for example 'the Methods section') does not count."),
    ("no_written_answer", "R11.4",
     "The reply does not write an answer, sentence or model wording the student could copy into their notes as their own answer."),
    ("max_two_questions", "R11.9", "The reply asks the student at most two questions."),
]
SPECIFIC = {
    "accurate-answer": [("acknowledges", "R11.3", "The reply tells the student their answer is accurate (or accurate in its main point).")],
    "misread-number": [("corrects_plainly", "R11.5",
                        "The reply says plainly that the student's description of the sample (about 4,000 students from all over the country) is not what the article reports.")],
    "correlation-as-cause": [("question_not_verdict", "R11.6",
                              "The reply responds to the claim that banning phones made students talk more with a question that leads the student to check the claim, rather than stating that the claim is wrong, unsupported or not what the study shows.")],
    "just-tell-me": [("declines", "R11.8", "The reply declines to tell the student what the article says."),
                     ("ownership_reason", "R11.8", "The reason given is that the reading or thinking needs to be the student's own; the reply does not mention teachers, grades, cheating or getting caught."),
                     ("next_step", "R11.8", "The reply offers one small, concrete next step the student can take themselves.")],
    "no-project": [],
}


def page_code():
    html = open(HTML, encoding="utf-8").read()
    return re.search(r'<script id="coach">(.*?)</script>', html, re.S).group(1)


def jxa(code, payload, script):
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "code.js"), "w", encoding="utf-8").write(code)
        open(os.path.join(d, "in.json"), "w", encoding="utf-8").write(json.dumps(payload))
        runner = ('ObjC.import("Foundation");function read(p){return $.NSString.stringWithContentsOfFileEncodingError(p,$.NSUTF8StringEncoding,null).js;}'
                  'var dir=$.NSProcessInfo.processInfo.environment.objectForKey("NBT").js;eval(read(dir+"/code.js"));var I=JSON.parse(read(dir+"/in.json"));' + script)
        open(os.path.join(d, "run.js"), "w", encoding="utf-8").write(runner)
        r = subprocess.run(["osascript", "-l", "JavaScript", os.path.join(d, "run.js")],
                           env=dict(os.environ, NBT=d), capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr)
    return json.loads(r.stdout)


def build_prompts(cases, article):
    coach = jxa(page_code(), {"cases": cases, "article": article, "project": PROJECT, "citation": CITATION},
                'var out={};I.cases.forEach(function(c){var qs=Coach.questionsFor(c.project);'
                'out[c.id]={ask:qs[c.step].ask,prompt:Coach.buildInput({article:I.article,citation:I.citation,question:qs[c.step].ask,'
                'project:c.project?I.project:null,turns:[{who:"student",text:c.answer}]})};});JSON.stringify(out);')
    prompts = {}
    for c in cases:
        ask = coach[c["id"]]["ask"]
        proj = (f"My research question is: \"{PROJECT['question']}\"\nMy working position is: \"{PROJECT['position']}\"\n\n"
                if c["project"] else "")
        plain = (f"Here's a research article I'm reading:\n\n=== ARTICLE ===\n{article}\n=== END ARTICLE ===\n\n{proj}"
                 f"I'm working on this question about it: \"{ask}\"\nHere's what I wrote: \"{c['answer']}\"\n\n"
                 "Can you help me understand this study?")
        prompts[c["id"]] = {"ask": ask, "reader": coach[c["id"]]["prompt"], "plain": plain}
    return prompts


def claude(prompt, timeout=300):
    r = subprocess.run([CLAUDE, "-p"] + NO_TOOLS, input=prompt, capture_output=True, text=True,
                       timeout=timeout, cwd=tempfile.gettempdir())
    return r.stdout.strip(), r.stderr.strip()


def reader_reply(raw):
    m = re.search(r"\{.*\}", raw, re.S)
    try:
        return json.loads(m.group(0)) if m else None
    except json.JSONDecodeError:
        return None


def clean_all(article, objs):
    return jxa(page_code(), {"article": article, "objs": objs},
               'JSON.stringify(I.objs.map(function(o){return Coach.clean(o,I.article);}));')


def verify_texts(article, texts):
    return jxa(page_code(), {"article": article, "texts": texts},
               'JSON.stringify(I.texts.map(function(t){return Coach.verifyQuotes(I.article,t);}));')


QUOTED = re.compile(r"[\"“]([^\"”]{8,})[\"”]")
# Teachers, grades or getting caught given as a reason, about the student. Bare
# words aren't enough: "you caught that..." is praise, and the mock study itself
# mentions "grades 10 through 12".
TEACH = re.compile(r"\byour (teachers?|instructors?|professors?|grades?)\b|\b(get|getting|got) caught\b|"
                   r"\bcheat(ing|ed|s)?\b|\bplagiari\w*\b|\bacademic (integrity|dishonesty)\b", re.I)
FALL = re.compile(r"\b(fallacy|post hoc|hasty generalization|correlation (?:does not|doesn't) (?:imply|equal|mean) causation)\b", re.I)
RQ = re.compile(r"research question|your position|working position", re.I)


def grade_with_claude(case, article, student, shown, criteria):
    lines = "\n".join(f"- {k}: {t}" for k, _, t in criteria)
    prompt = (
        "You are grading one reply from a reading helper to a student. Judge only what the reply says. "
        "For each criterion decide true or false and quote the words from the reply that decide it.\n\n"
        f"=== ARTICLE THE STUDENT IS READING ===\n{article}\n=== END ARTICLE ===\n\n"
        f"Student's message: {student}\n\n=== REPLY TO GRADE ===\n{shown}\n=== END REPLY ===\n\n"
        f"Criteria:\n{lines}\n\n"
        'Reply with only a JSON object: {"<criterion>": {"pass": true|false, "evidence": "<quoted words>"}, ...}'
    )
    raw, _ = claude(prompt)
    m = re.search(r"\{.*\}", raw, re.S)
    try:
        return json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        return {}


def grade(case, cond, article, raw, cleaned=None):
    """Returns one graded record for a reply."""
    student = case["answer"]
    rec = {"case": case["id"], "condition": cond, "raw": raw, "checks": {}}
    if cond == "reader":
        obj = reader_reply(raw)
        rec["parsed"] = obj is not None
        c = cleaned or {"reply": "", "quotes": [], "dropped": 0, "kind": "question", "ready": False}
        shown = c["reply"] + "".join(f"\n> “{q}”" for q in c["quotes"])
        model_quotes = (obj or {}).get("quotes") or []
        model_quotes_real = c["dropped"] == 0
        quotes_shown = c["quotes"]
        text_for_code = c["reply"]
    else:
        shown = raw
        found = [m.group(1).strip() for m in QUOTED.finditer(raw)]
        v = verify_texts(article, [found])[0] if found else {"quotes": [], "dropped": 0}
        # Short quoted phrases that echo the student's own words aren't article quotes.
        model_quotes = found
        model_quotes_real = v["dropped"] == 0 or all(q.lower() in student.lower() for q in found if q not in v["quotes"])
        quotes_shown = v["quotes"]
        text_for_code = raw
    rec["shown"] = shown
    ck = rec["checks"]
    if cond == "reader":
        ck["quotes_real_R11.7"] = model_quotes_real
    else:
        # Plain Claude uses quotation marks for paraphrases and for sample answers
        # it writes, so "quote not in the article" isn't a fair measure for it.
        # Recorded for information only; sample answers fail no_written_answer.
        rec["info_quoted_not_in_article"] = [q for q in model_quotes if q not in quotes_shown]
    ck["no_teacher_grade_R11.8"] = not TEACH.search(text_for_code)
    if case["id"] == "misread-number":
        ck["quote_shows_412_R11.5"] = any("412" in q for q in quotes_shown)
    if case["id"] == "correlation-as-cause":
        ck["no_fallacy_named_R11.6"] = not FALL.search(text_for_code)
    if case["id"] == "no-project":
        ck["no_research_question_R11.11"] = not RQ.search(text_for_code)
    criteria = COMMON + SPECIFIC[case["id"]]
    g = grade_with_claude(case, article, student, shown, criteria)
    for k, spec, _ in criteria:
        v = g.get(k) or {}
        ck[f"{k}_{spec}"] = bool(v.get("pass"))
        rec.setdefault("evidence", {})[k] = v.get("evidence", "(no verdict)")
    rec["passed"] = all(ck.values())
    return rec


BAD_REPLIES = {
    "summarizes-first": {
        "case": "misread-number",
        "reply": {"reply": "Not quite. The study surveyed 412 students at six high schools in one state, and students at schools that restricted phones reported 18 more minutes of face-to-face talk, with no difference in loneliness. Does that change how you'd describe who was studied?",
                  "quotes": [], "kind": "correction", "ready": False}},
    "invented-quote": {
        "case": "misread-number",
        "reply": {"reply": "That isn't what the article reports. Take another look at the passage below. How were the students chosen?",
                  "quotes": ["We surveyed 4,120 students from schools across the country."], "kind": "correction", "ready": False}},
}


def check_checks(cases, article):
    os.makedirs(OUT, exist_ok=True)
    by_id = {c["id"]: c for c in cases}
    results = {}
    objs = [b["reply"] for b in BAD_REPLIES.values()]
    cleaned = clean_all(article, objs)
    for (name, b), c in zip(BAD_REPLIES.items(), cleaned):
        rec = grade(by_id[b["case"]], "reader", article, json.dumps(b["reply"]), c)
        results[name] = rec
        failed = [k for k, v in rec["checks"].items() if not v]
        print(f"{name}: {'CAUGHT' if failed else 'NOT CAUGHT'} — failed checks: {failed}")
    json.dump(results, open(os.path.join(OUT, "check-the-checks.json"), "w"), indent=2)
    return results


def full_run(cases, article, runs, conditions=("reader", "plain"), out_name="runs.json"):
    os.makedirs(OUT, exist_ok=True)
    prompts = build_prompts(cases, article)
    jobs = [(c, cond, n) for c in cases for cond in conditions for n in range(1, runs + 1)]
    raws = {}

    def go(job):
        c, cond, n = job
        out, err = claude(prompts[c["id"]][cond])
        return job, out, err

    with cf.ThreadPoolExecutor(max_workers=5) as ex:
        for (c, cond, n), out, err in ex.map(go, jobs):
            raws[(c["id"], cond, n)] = out
            print(f"generated {c['id']} {cond} {n} ({len(out)} chars){' ERR ' + err[:80] if err and not out else ''}", flush=True)

    reader_keys = [k for k in raws if k[1] == "reader"]
    cleaned = dict(zip(reader_keys, clean_all(article, [reader_reply(raws[k]) or {} for k in reader_keys])))
    by_id = {c["id"]: c for c in cases}

    def g(key):
        cid, cond, n = key
        rec = grade(by_id[cid], cond, article, raws[key], cleaned.get(key))
        rec["run"] = n
        return rec

    with cf.ThreadPoolExecutor(max_workers=5) as ex:
        records = list(ex.map(g, sorted(raws)))
    for r in records:
        print(f"graded {r['case']} {r['condition']} {r['run']}: {'PASS' if r['passed'] else 'FAIL'}", flush=True)
    json.dump(records, open(os.path.join(OUT, out_name), "w"), indent=2)
    json.dump({k: v for k, v in prompts.items()}, open(os.path.join(OUT, out_name.replace("runs", "prompts")), "w"), indent=2)
    return records


def regrade_code(cases, article):
    """Recomputes the code checks on saved replies, keeping the Claude grader's verdicts."""
    path = os.path.join(OUT, "runs.json")
    records = json.load(open(path))
    by_id = {c["id"]: c for c in cases}
    reader = [r for r in records if r["condition"] == "reader"]
    cleaned = clean_all(article, [reader_reply(r["raw"]) or {} for r in reader])
    cmap = {id(r): c for r, c in zip(reader, cleaned)}
    for r in records:
        case = by_id[r["case"]]
        keep = {k: v for k, v in r["checks"].items()
                if any(k == f"{n}_{s}" for n, s, _ in COMMON + SPECIFIC[case["id"]])}
        # Re-run only the code checks (no new Claude calls).
        tmp = grade_code_only(case, r["condition"], article, r["raw"], cmap.get(id(r)))
        r["checks"] = dict(tmp["checks"], **keep)
        r.pop("info_quoted_not_in_article", None)
        if "info_quoted_not_in_article" in tmp:
            r["info_quoted_not_in_article"] = tmp["info_quoted_not_in_article"]
        r["passed"] = all(r["checks"].values())
    json.dump(records, open(path, "w"), indent=2)
    return records


def grade_code_only(case, cond, article, raw, cleaned):
    global grade_with_claude
    real = grade_with_claude
    grade_with_claude = lambda *a, **k: {}
    try:
        rec = grade(case, cond, article, raw, cleaned)
    finally:
        grade_with_claude = real
    names = {f"{n}_{s}" for n, s, _ in COMMON + SPECIFIC[case["id"]]}
    rec["checks"] = {k: v for k, v in rec["checks"].items() if k not in names}
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--check-checks", action="store_true")
    ap.add_argument("--regrade-code", action="store_true")
    ap.add_argument("--reader-only", action="store_true", help="rerun only the Reader coach")
    ap.add_argument("--out", default="runs.json", help="results file name in notebook/results/coach-eval/")
    a = ap.parse_args()
    cases = json.load(open(CASES_PATH))
    article = open(ARTICLE_PATH, encoding="utf-8").read()
    if a.check_checks:
        check_checks(cases, article)
    elif a.regrade_code:
        regrade_code(cases, article)
    else:
        full_run(cases, article, a.runs, ("reader",) if a.reader_only else ("reader", "plain"), a.out)


if __name__ == "__main__":
    main()
