"""Tests the Reader's pure logic (issue #4; SPEC R11.2, R11.3, R11.7, R11.10, R11.11).

Runs the page's own Coach and LogFormat code from notebook/notebook.html with
macOS's built-in JavaScript engine. Uses the fictional article in
notebook/tests/fixtures/mock-study.txt.

Run from the repository root:  python3 notebook/tests/test_reader.py
Set NOTEBOOK_HTML to test a different copy of the page.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HTML = os.environ.get("NOTEBOOK_HTML", os.path.join(ROOT, "notebook", "notebook.html"))
ARTICLE = os.path.join(ROOT, "notebook", "tests", "fixtures", "mock-study.txt")
LOG = os.path.join(ROOT, "research-smarter", "evals", "skip-planning-request", "files", "research-log.md")

RUNNER = r"""
ObjC.import('Foundation');
function read(p){return $.NSString.stringWithContentsOfFileEncodingError(p,$.NSUTF8StringEncoding,null).js;}
var dir = $.NSProcessInfo.processInfo.environment.objectForKey('NBT').js;
eval(read(dir + '/code.js'));
var I = JSON.parse(read(dir + '/inputs.json'));
var A = I.article, out = {};

out.q6 = Coach.questionsFor(true).map(function (q) { return q.ask; });
out.q5 = Coach.questionsFor(false).map(function (q) { return q.ask; });

out.v = {};
Object.keys(I.quotes).forEach(function (k) { out.v[k] = Coach.verifyQuotes(A, [I.quotes[k]]).quotes.length === 1; });
out.vMax = Coach.verifyQuotes(A, I.many).quotes.length;

var input1 = Coach.buildInput({ article: A, citation: "Mock study", question: out.q6[0],
  project: { question: "Q?", position: "P." }, turns: [{ who: "student", text: "They measured phone use." }] });
out.input1 = input1;
out.inputNoProject = Coach.buildInput({ article: A, citation: "Mock study", question: out.q5[0], project: null,
  turns: [{ who: "student", text: "x" }] });

out.clean1 = Coach.clean({ reply: "  Look again.  ", quotes: [I.quotes.exact, I.quotes.fabricated], kind: "weird", ready: "yes" }, A);

var card = { citation: "Mock, A. (2026). Lunchroom talk.", date: "2026-11-18", answers: I.answers };
var md1 = LogFormat.withReadingCard(I.log, card);
var card2 = { citation: "Second source", date: "2026-11-19", answers: [{ label: "What was measured", answer: "Only one answer." }] };
var md2 = LogFormat.withReadingCard(md1, card2);
out.md1 = md1; out.md2 = md2;
out.cards1 = LogFormat.parse(md1).readingCards;
out.cards2 = LogFormat.parse(md2).readingCards;
out.parse2ok = LogFormat.parse(md2).ok;
out.q2 = LogFormat.parse(md2).question.text;
out.file = LogFormat.cardFile(card);
out.saved = LogFormat.save(md2, "2099-01-02");
JSON.stringify(out);
"""

QUOTES = {
    "exact": "412 of 3,050 invited students (13.5%) responded",
    "linebreaks": "Participation was voluntary, and 412 of\n3,050 invited students",
    "curly": "this correlation was weak (r = −0.12)".replace("−", "-"),
    "curly_quotes": "we cannot say whether conversation changed after the restrictions began",
    "fabricated": "Students at restricting schools were 40% less lonely",
    "altered_number": "412 of 3,050 invited students (31.5%) responded",
    "too_short": "412",
}
ANSWERS = [
    {"label": "What was measured", "answer": "Self-reported minutes of face-to-face talk per school day, and a 6-item loneliness scale."},
    {"label": "Who was studied", "answer": "412 students in grades 10-12 at six schools in one state.\nOnly 13.5% responded, so it's volunteers."},
    {"label": "What was found", "answer": "18 more minutes of talk at restricting schools; no difference in loneliness."},
    {"label": "What it doesn't show", "answer": "It doesn't show the bans caused the extra talk — the schools were smaller, too."},
    {"label": "Limits the authors admit", "answer": "Self-report, low response rate | one state, one point in time."},
    {"label": "How it relates to my question", "answer": "Supports the in-person part of my position but says nothing about after-school conflict."},
]


def outside(md, section):
    out, inside = [], False
    for l in md.split("\n"):
        if l.startswith("## "):
            inside = l.lower().startswith("## " + section)
        if not inside:
            out.append(l)
    while out and out[-1] == "":
        out.pop()
    return out


def main():
    html = open(HTML, encoding="utf-8").read()
    code = (re.search(r'<script id="log-format">(.*?)</script>', html, re.S).group(1) + "\n" +
            re.search(r'<script id="coach">(.*?)</script>', html, re.S).group(1))
    article = open(ARTICLE, encoding="utf-8").read()
    log = open(LOG, encoding="utf-8").read()
    many = [QUOTES["exact"], QUOTES["curly_quotes"], "Further research with stronger designs is needed"]
    inputs = {"article": article, "quotes": QUOTES, "many": many, "answers": ANSWERS, "log": log}
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "code.js"), "w", encoding="utf-8").write(code)
        open(os.path.join(d, "inputs.json"), "w", encoding="utf-8").write(json.dumps(inputs))
        open(os.path.join(d, "run.js"), "w", encoding="utf-8").write(RUNNER)
        res = subprocess.run(["osascript", "-l", "JavaScript", os.path.join(d, "run.js")],
                             env=dict(os.environ, NBT=d), capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stderr)
        sys.exit(2)
    o = json.loads(res.stdout)
    failures = []

    def check(cond, msg):
        print(("PASS  " if cond else "FAIL  ") + msg)
        if not cond:
            failures.append(msg)

    # R11.2 / R11.11: order and the project-only last question
    check(len(o["q6"]) == 6 and o["q6"][0].startswith("What did the study actually measure")
          and o["q6"][5].startswith("How does this source relate"), "six questions in the agreed order with a project")
    check(len(o["q5"]) == 5 and all(not q.startswith("How does this source relate") for q in o["q5"]),
          "without a project the last question is skipped")

    # R11.7: only real passages
    check(o["v"]["exact"], "an exact passage is accepted")
    check(o["v"]["linebreaks"], "a passage with different line breaks is accepted")
    check(o["v"]["curly"] and o["v"]["curly_quotes"], "passages with different punctuation styles are accepted")
    check(not o["v"]["fabricated"], "an invented passage is rejected")
    check(not o["v"]["altered_number"], "a passage with one number changed is rejected")
    check(not o["v"]["too_short"], "a fragment too short to check is rejected")
    check(o["vMax"] == 2, "at most two quotes are shown")
    c = o["clean1"]
    check(c["reply"] == "Look again." and c["quotes"] == [QUOTES["exact"]] and c["dropped"] == 1,
          "clean() keeps the real quote and drops the invented one")
    check(c["kind"] == "question" and c["ready"] is False, "clean() falls back safely on unexpected fields")

    # R11.3: the prompt carries only the current question, the rules, and the article
    inp = o["input1"]
    check(article.strip()[:200] in inp, "the coach sees the article")
    check("What did the study actually measure?" in inp and "What limits do the authors admit?" not in inp,
          "the coach sees only the current question")
    check("Never summarize" in inp and "Never mention teachers" in inp, "the coach's rules are in the prompt")
    check("research question, in their words: Q?" in inp, "the student's own question is passed in their words")
    check("research question" not in o["inputNoProject"].split("=== END ARTICLE ===")[1],
          "with no project, no research question is passed")

    # R11.10: the card keeps the student's answers word for word
    cards1, cards2 = o["cards1"], o["cards2"]
    check(len(cards1) == 1 and cards1[0]["citation"] == "Mock, A. (2026). Lunchroom talk." and cards1[0]["date"] == "2026-11-18",
          "the card is saved with its citation and date")
    got = [(a["label"], a["answer"]) for a in cards1[0]["answers"]]
    want = [(a["label"], a["answer"]) for a in ANSWERS]
    check(got == want, "every answer comes back word for word, including a line break, a dash and a '|'")
    check(len(cards2) == 2 and cards2[1]["citation"] == "Second source", "a second card is added after the first")
    check(outside(o["md2"], "reading cards") == outside(log, "reading cards"),
          "every line outside the reading cards section is unchanged")
    check(o["parse2ok"] and o["q2"] == "How have school-day phone bans changed how high school students interact with each other in person?",
          "the log still loads and keeps the question after adding cards")
    a, b = o["md2"].split("\n"), o["saved"].split("\n")
    diff = [(x, y) for x, y in zip(a, b) if x != y]
    check(len(a) == len(b) and len(diff) == 1, "saving a log with cards changes only the date")
    check(o["file"].startswith("# Research Smarter · Reading card") and "Mock, A. (2026). Lunchroom talk." in o["file"],
          "a card on its own can be saved as a file")

    print(f"\n{len(failures)} failed" if failures else "\nAll checks passed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
