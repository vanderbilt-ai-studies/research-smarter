"""Tests the notebook's research-log parsing and saving (issue #2; SPEC R10.3, R10.4).

Runs the page's own LogFormat code (the <script id="log-format"> block in
notebook/notebook.html) with macOS's built-in JavaScript engine, on every
example log in research-smarter/evals plus files that are not logs.

Run from the repository root:  python3 notebook/tests/test_log_format.py
"""
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HTML = os.environ.get("NOTEBOOK_HTML", os.path.join(ROOT, "notebook", "notebook.html"))

RUNNER = r"""
ObjC.import('Foundation');
function read(p){return $.NSString.stringWithContentsOfFileEncodingError(p,$.NSUTF8StringEncoding,null).js;}
var dir = $.NSProcessInfo.processInfo.environment.objectForKey('NBT').js;
eval(read(dir + '/logformat.js'));
var inputs = JSON.parse(read(dir + '/inputs.json'));
var out = {};
Object.keys(inputs).forEach(function (f) {
  var p = LogFormat.parse(inputs[f]);
  out[f] = p.ok ? {ok: true, parsed: p, saved: LogFormat.save(inputs[f], "2099-01-02")} : {ok: false};
});
out.__localDate = LogFormat.localDate(new Date(2026, 10, 18, 23, 30));
JSON.stringify(out);
"""

# Expected phase display for each example log: (current phase, completed phases).
EXPECTED_PHASES = {
    "asks-why-on-direction": (1, [0]),
    "end-of-phase4-disclosure": (4, [0, 1, 2, 3]),
    "no-search-tool": (1, [0]),
    "phase1-briefing-and-mind-map": (1, [0]),
    "questions-reasoning-praises-strength": (2, [0, 1]),
    "refuses-thesis-corrects-fact": (2, [0, 1]),
    "rejects-loophole-requests": (2, [0, 1]),
    "resume-phase5-source": (None, [0, 1, 2, 3]),
    "skip-planning-request": (3, [0, 1, 2]),
}
NOT_LOGS = ["README.md", "GUIDE.md", "SPEC.md", "DESIGN.md"]


def expected_field(raw, label):
    m = re.search(r"^- \*\*" + re.escape(label) + r":\*\*\s*(.*)$", raw, re.M)
    v = m.group(1).strip() if m else ""
    return v[1:-1] if len(v) >= 2 and v[0] == '"' and v[-1] == '"' else v


def main():
    html = open(HTML, encoding="utf-8").read()
    code = re.search(r'<script id="log-format">(.*?)</script>', html, re.S).group(1)
    logs = sorted(glob.glob(os.path.join(ROOT, "research-smarter/evals/*/files/research-log.md")))
    others = [os.path.join(ROOT, n) for n in NOT_LOGS]
    inputs = {f: open(f, encoding="utf-8").read() for f in logs + others}

    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "logformat.js"), "w", encoding="utf-8").write(code)
        open(os.path.join(d, "inputs.json"), "w", encoding="utf-8").write(json.dumps(inputs))
        open(os.path.join(d, "run.js"), "w", encoding="utf-8").write(RUNNER)
        res = subprocess.run(["osascript", "-l", "JavaScript", os.path.join(d, "run.js")],
                             env=dict(os.environ, NBT=d), capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stderr)
        sys.exit(2)
    out = json.loads(res.stdout)

    failures = []

    def check(cond, msg):
        print(("PASS  " if cond else "FAIL  ") + msg)
        if not cond:
            failures.append(msg)

    check(out.pop("__localDate") == "2026-11-18", "localDate uses the local calendar date (23:30 on Nov 18 -> 2026-11-18)")

    for f in logs:
        case = f.split(os.sep)[-3]
        r, raw = out[f], inputs[f]
        check(r["ok"], f"{case}: recognized as a research log")
        if not r["ok"]:
            continue
        p = r["parsed"]
        check(p["question"]["text"] == expected_field(raw, "Research question"), f"{case}: research question matches the log word for word")
        check(p["position"]["text"] == expected_field(raw, "Working position"), f"{case}: working position matches the log word for word")
        q_placeholder = expected_field(raw, "Research question").startswith("not written yet")
        check(p["question"]["written"] == (not q_placeholder), f"{case}: 'not written yet' question shown as not written")
        want_current, want_done = EXPECTED_PHASES[case]
        check(p["phase"]["current"] == want_current, f"{case}: current phase is {want_current}")
        check(p["phase"]["exitChecks"] == want_done, f"{case}: completed phases are {want_done}")
        a = raw.replace("\r\n", "\n").split("\n")
        b = r["saved"].split("\n")
        diff = [(x, y) for x, y in zip(a, b) if x != y]
        check(len(a) == len(b) and len(diff) == 1 and diff[0][1] == "**Last updated:** 2099-01-02",
              f"{case}: saving changes only the Last updated date")

    for f in others:
        check(not out[f]["ok"], f"{os.path.basename(f)}: rejected as not a research log")

    print(f"\n{len(failures)} failed" if failures else "\nAll checks passed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
