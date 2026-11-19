"""Tests the notebook's source library logic (issue #3; SPEC R10.5, R2.4, R10.4).

Runs the page's own LogFormat code (the <script id="log-format"> block in
notebook/notebook.html) with macOS's built-in JavaScript engine.

Run from the repository root:  python3 notebook/tests/test_sources.py
Set NOTEBOOK_HTML to test a different copy of the page.
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
  var md = inputs[f], p = LogFormat.parse(md), r = {};
  r.before = p.sources;
  r.header = p.sourcesHeader;
  r.rewriteSame = LogFormat.withSources(md, p.sources, p.sourcesHeader);

  // Edit: first source (if any) marked read closely and labeled complicates.
  var edited = p.sources.map(function (s, i) {
    var c = JSON.parse(JSON.stringify(s));
    if (i === 0) { c.status = "read closely"; c.label = "complicates"; }
    return c;
  });
  // Add: a new source whose citation contains a pipe.
  var added = LogFormat.newSource({ citation: "Doe, J. (2025). Bans | and belonging.", link: "10.1234/abcd.5678", subq: "Do students talk more?" });
  r.newSource = added;
  edited.push(added);
  r.afterMd = LogFormat.withSources(md, edited, p.sourcesHeader);
  var p2 = LogFormat.parse(r.afterMd);
  r.after = p2.sources;
  r.afterOk = p2.ok;
  r.afterQuestion = p2.question.text;
  r.afterPosition = p2.position.text;
  r.question = p.question.text;
  r.position = p.position.text;
  // Writing the same sources twice gives the same log (stable).
  r.stable = LogFormat.withSources(r.afterMd, p2.sources, p2.sourcesHeader) === r.afterMd;
  // Saved log after edits still changes only the date relative to the edited log.
  r.savedAfter = LogFormat.save(r.afterMd, "2099-01-02");
  out[f] = r;
});
JSON.stringify(out);
"""


def outside_sources(md):
    """All lines of the log except the '## Sources found…' section."""
    lines, keep, inside = md.replace("\r\n", "\n").split("\n"), [], False
    for line in lines:
        if line.startswith("## "):
            inside = line.lower().startswith("## sources found")
        if not inside:
            keep.append(line)
    while keep and keep[-1] == "":
        keep.pop()
    return keep


def main():
    html = open(HTML, encoding="utf-8").read()
    code = re.search(r'<script id="log-format">(.*?)</script>', html, re.S).group(1)
    logs = sorted(glob.glob(os.path.join(ROOT, "research-smarter/evals/*/files/research-log.md")))
    inputs = {f: open(f, encoding="utf-8").read() for f in logs}
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

    # The Phase 4 example log: its one row keeps the student's own wording.
    p4 = next(f for f in logs if "end-of-phase4-disclosure" in f)
    s0 = out[p4]["before"][0]
    check(s0["label"] == "3 support, 2 complicate", "Phase 4 log: the student's own label wording is shown as written")
    check(s0["status"] == "", "Phase 4 log: a source with no reading status stays blank (no invented 'found')")
    p4_after = [l for l in out[p4]["rewriteSame"].split("\n") if l.startswith("| (5 sources")]
    check(len(p4_after) == 1 and p4_after[0].rstrip().endswith("| yes |  |"),
          "Phase 4 log: the saved row leaves its reading status blank")

    for f in logs:
        case = f.split(os.sep)[-3]
        r = out[f]
        before, after = r["before"], r["after"]
        check(r["afterOk"], f"{case}: log still loads after editing sources")
        check(r["newSource"]["label"] == "", f"{case}: a newly added source has no supports/complicates label")
        check(after[-1]["label"] == "", f"{case}: the added source is still unlabeled after saving and reloading")
        check(after[-1]["citation"] == "Doe, J. (2025). Bans | and belonging.", f"{case}: a citation containing '|' survives saving")
        check(after[-1]["status"] == "found" and after[-1]["link"] == "10.1234/abcd.5678", f"{case}: added source keeps its status and DOI")
        check(len(after) == len(before) + 1, f"{case}: source count goes up by exactly one")
        if before:
            check(after[0]["status"] == "read closely" and after[0]["label"] == "complicates",
                  f"{case}: edited status and label are in the saved log")
            check(after[0]["citation"] == before[0]["citation"], f"{case}: edited source keeps its citation")
        check(outside_sources(r["afterMd"]) == outside_sources(inputs[f]),
              f"{case}: every line outside the sources section is unchanged")
        check(r["afterQuestion"] == r["question"] and r["afterPosition"] == r["position"],
              f"{case}: question and position unchanged after editing sources")
        check(r["stable"], f"{case}: writing the same sources again changes nothing")
        a, b = r["afterMd"].split("\n"), r["savedAfter"].split("\n")
        diff = [(x, y) for x, y in zip(a, b) if x != y]
        check(len(a) == len(b) and len(diff) == 1 and diff[0][1] == "**Last updated:** 2099-01-02",
              f"{case}: saving an edited log changes only the date")

    print(f"\n{len(failures)} failed" if failures else "\nAll checks passed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
