"""Check that research logs the skill wrote still load in the Research Notebook.

Runs the notebook's own LogFormat code (the <script id="log-format"> block in
notebook/notebook.html) with macOS's built-in JavaScript engine on each log
file found, and reports whether it parsed and how many sources it holds.

Usage: python3 tests/check_log_loads.py RESULTS_DIR [RESULTS_DIR ...]
Looks for research-log*.md files under each run's outputs/ folder.
"""
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "notebook", "notebook.html")
RUNNER = r"""
ObjC.import('Foundation');
function read(p){return $.NSString.stringWithContentsOfFileEncodingError(p,$.NSUTF8StringEncoding,null).js;}
var dir = $.NSProcessInfo.processInfo.environment.objectForKey('NBT').js;
eval(read(dir + '/logformat.js'));
var inputs = JSON.parse(read(dir + '/inputs.json'));
var out = {};
Object.keys(inputs).forEach(function (f) {
  var p = LogFormat.parse(inputs[f]);
  out[f] = p.ok ? {ok: true, sources: (p.sources || []).length} : {ok: false};
});
JSON.stringify(out);
"""


def main(dirs):
    html = open(HTML).read()
    js = re.search(r'<script id="log-format">(.*?)</script>', html, re.S).group(1)
    logs = {}
    for d in dirs:
        for f in glob.glob(os.path.join(d, "**", "outputs", "research-log*.md"), recursive=True):
            logs[os.path.relpath(f, d)] = open(f).read()
    if not logs:
        print("no research logs found")
        return
    with tempfile.TemporaryDirectory() as t:
        open(os.path.join(t, "logformat.js"), "w").write(js)
        open(os.path.join(t, "inputs.json"), "w").write(json.dumps(logs))
        open(os.path.join(t, "run.js"), "w").write(RUNNER)
        r = subprocess.run(["osascript", "-l", "JavaScript", os.path.join(t, "run.js")],
                           capture_output=True, text=True, env={**os.environ, "NBT": t})
    out = json.loads(r.stdout)
    for f, res in sorted(out.items()):
        print(f"{f}: {'loads' if res['ok'] else 'DOES NOT LOAD'}" + (f", {res['sources']} sources" if res["ok"] else ""))
    sys.exit(0 if all(v["ok"] for v in out.values()) else 1)


if __name__ == "__main__":
    main(sys.argv[1:] or ["."])
