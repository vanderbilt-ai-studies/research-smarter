# Research Smarter

In 2024, the American Psychological Association said in
[an article](https://www.apa.org/topics/artificial-intelligence-machine-learning/ai-research-writing)
that, when it comes to research, "Ideally, AI tools will progress to the
point that they can enable researchers to focus on the more complex and
cognitively demanding elements of scholarship."

Research Smarter is a research assistant skill that works with the user to
refine their research topic, stress-test their arguments, and do the mental
work of engaging with the research process. The goal is for the skill to
develop the user's critical thinking skills as AI becomes more prevalent as
a research tool.

## What I built

After my consult, we agreed to build two connected parts:

1. **The Research Smarter skill** (`research-smarter/`). Claude coaches a
   student through a research project in six phases. Claude does the
   searching and summarizing; the student makes every decision and writes
   every word.
2. **The Research Notebook** (`notebook/notebook.html`), an interactive
   page published from Claude. It holds the student's research record:
   their phase, their question and position in their own words, and a
   source library where they mark how far they've read each source and
   whether it supports or complicates their position. It also has a
   separate **Read a Source** mode for reading one article critically. A
   coach asks six fixed questions, one at a time, and checks the student's
   answers against the article. It corrects misread facts with quotes the
   page verifies, questions interpretations, and never explains the
   article for them. The result is a reading card in the student's words.

The two connect through the research log the skill already writes, so the
skill's coaching flow didn't have to change.

## How to try it

- **The skill:** see [GUIDE.md](GUIDE.md) to install it, then say "I want
  to research…" in a new chat.
- **The notebook:** https://claude.ai/artifact/NT8int2Sc3zA22P1AXcsha. It's
  a Claude page, so it opens only for people it's been shared with. Load a
  research log, or click **See an example**, and use **Read a source** with
  the fictional test article in `notebook/tests/fixtures/`.

## What the evidence shows

- **The skill:** across ten test cases, the skill passed 68 of 68 checks;
  plain Claude passed 31 of 68 ([SPEC.md](SPEC.md)).
- **Three runs of every test:** all 16 test cases, 3 runs each, passed 282
  of 285 checks, and 45 of 48 runs passed every check
  ([results](tests/results/issue-14-leftovers.md)). Getting there meant
  fixing two problems the tests caught: the skill linked sources it hadn't
  opened, and it asked more than two questions when resuming a project.
- **The Reader's coach vs plain Claude:** same article, same student
  answers, 3 runs each. The coach passed every check in **14 of 15**
  replies; plain Claude passed **0 of 15**. Plain Claude summarized the
  study every time, wrote answers for the student, and answered "just tell
  me what it says" with a full summary
  ([results](notebook/results/issue-5-reader-tests.md)).
- **"Ask it how it knows":** the skill now invites students to challenge
  its claims and answers honestly when they do. With the change, briefings
  and source lists invited a challenge to a named claim or source in every
  run (12 of 12 checks, against 0 of 12 before). Across six new test cases,
  3 runs each, the new skill passed 72 of 81 checks and the previous version
  54 of 81 ([results](tests/results/issue-6-ask-how-it-knows.md)). Testing
  also found two older problems, addressed in issue #14: unopened DOI
  links in Phase 4 source lists (now fixed), and a third question when
  resuming a project (now 2 of 48 runs).
- **Fact-check reminders:** the skill now reminds students to check what it
  gives them at the start of each phase and with every source list, naming
  what to check and how. Phase 2 briefings had that reminder in 3 of 3 runs,
  against 1 of 3 before; across four test cases, 3 runs each, the skill
  passed 61 of 63 checks, against 48 of 63 before
  ([results](tests/results/issue-10-fact-check-reminders.md)).
- **What makes a good research question:** the skill now checks every
  draft question against one definition (clear, focused, complex, neutral,
  answerable, and more), asks about the one or two that matter most, and
  never rewords the question or shows example questions. Across ten test
  cases, 3 runs each, it passed 140 of 141 checks, against 125 of 141
  before ([results](tests/results/issue-8-good-research-question.md)).
- **Checking the checks:** the tests catch deliberately broken versions of
  the notebook and two deliberately bad coach replies. Two flawed checks
  were found and fixed before the results were trusted.
- **Iteration:** I decided the coach shouldn't hint at parts of the article
  a student hadn't raised. Fixing that took two rounds of revision: the
  first fix caused extra questions (12/15), and the second brought it back
  to 14/15. All rounds are kept.
- **Bugs that live testing caught:**
  - the file picker was blocked inside Claude's page frame
  - the notebook invented a "found" reading status that misled the skill
  - the coach silently didn't run when Claude access wasn't granted
  - a save said "Saved" before storage confirmed

  Each was diagnosed and fixed. The build history is in the
  [closed issues](https://github.com/vanderbilt-ai-studies/research-smarter/issues?q=is%3Aissue)
  and each issue's results file in `notebook/results/` or `tests/results/`.

## Limits and what's still open

- **Single replies, not whole projects:** the tests check one reply at a
  time, on a short fictional article. There hasn't been a trial with a
  real student yet.
- **The grader is also Claude:** coach replies were graded by a separate
  Claude grader that quotes its evidence, and checked by hand.
- **One known coach failure in 15:** a correction can quote a second
  passage that gives away the next part of the answer.
- **Not yet confirmed live:** saving a reading card in the live notebook,
  and privacy against a second person's account.
- **Who can use it:** the notebook needs a Claude account with access to the
  page, and the coach uses the student's own Claude usage.
- **Activation isn't confirmed in Cowork:** in early tests, "I want to
  research matcha" didn't bring up the skill, possibly because it wasn't
  installed there yet.

All requirements, coverage and known issues are in [SPEC.md](SPEC.md).

---

*The proposal I brought to my consult follows.*

## What I want to make possible, and why it matters

Right now, the easiest way for a student to use AI for a research paper is to
ask it for the answer: the topic, the thesis, the sources, sometimes the
paper. AI models can easily write full research papers, or do deep--dives to pull up detailed information and sources in minutes.  That saves time, but it skips the part of research that engages the student intellectually. If "research" as a skill no longer means being able to find good sources, then I want to build a Claude skill that redefines what it means to do research in the age of AI. 

I want students (high school, college, or anyone doing a research project)
to get AI's real advantage, which is fast searching and summarizing, while
they still choose the direction, form a position, weigh the evidence, and
write every word. Success isn't a finished paper -- it's a student who thinks
more sharply about their topic than when they started and can say every idea
in their work is their own. 

It's so easy to be passive and let AI do the thinking for you. AI can also easily feed confirmation bias. I'm passionate about students using AI as a tool to sharpen their thinking, not as a weapon to erode it. 

## What makes it a stretch

The skill has to be genuinely helpful while refusing to do the thing students
most often ask for: doing the work for them. It has to hold that line when a student pushes back ("my
teacher said it's fine," "just give me an example"), correct false facts
directly but only question reasoning, and push back honestly without being
contrarian. It also has to work for any kind of research, from an
argumentative essay to a lab report or a literature review, scale its
challenge to the assignment, never invent a source, and pick up a project
days later from a saved log.

## What AI enables, and what I bring

AI can search, summarize, and coach in real time, which used to take a
teacher or librarian sitting next to each student. It can also build an
interactive 3D mind map of possible angles on a topic. What I bring is the human discernment to decide what makes a good research tool, and when an AI model is being to agreeable or too contrarian. I also plan to add my own research frameworks/processes to guide how the skill is designed. 
I made the design decisions: what the AI may and may not do, the six phases and
their exit checks, and how hard it should push.

## Approach and early test

I built the skill as a Claude skill with six phases: intake, explore and
choose a direction, a pre-research stress test, planning, research, and
optional ongoing stress testing. My early tests ran the same prompts with and
without the skill, starting from realistic points in a project.

## What success looks like

Success means the skill does what a good research coach would, observably:

- it never writes the student's question, thesis, or any of their text,
  including examples and fill-in-the-blank templates;
- it corrects factual errors with a source, then asks how the correction
  affects the student's question;
- it only cites sources it actually opened.

`SPEC.md` lists 37 testable requirements like these.

- **Comparison:** the same prompts with no skill. So far, across ten test
  cases, the skill passed 68 of 68 checks and plain Claude passed 31 of 68.
  Without the skill, Claude wrote research questions and a sample thesis,
  skipped the student's planning, and listed sources from memory.
- **Cases that could expose a weakness:** a student claiming their teacher
  allows it, no web search available, and a request to skip planning. One
  real weakness has already shown up. Saying "I want to research matcha" in
  Cowork didn't activate the skill.

## Questions I want to discuss

- **Measuring thinking.** How can I test whether students actually think
  better, not just whether the skill follows its rules?
- **Testing whole conversations.** My tests check single replies. What's the
  best way to test a full multi-turn project, or to run a trial with a real
  student?
- **Activation.** How can I make the skill come up reliably in Cowork when
  someone says they want to research something?
- **Timing.** I built and tested a first version before this consult. How
  should that fit the course's plan-then-build process?
- **Sharing.** Can I keep a public copy so other students can install the
  skill?

---

Details: [GUIDE.md](GUIDE.md) (how it works, installing, using it) ·
[SPEC.md](SPEC.md) (requirements and test results) ·
[DESIGN.md](DESIGN.md) (full design and an example walkthrough)
