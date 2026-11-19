# Research Smarter · Specification

This file defines what the Research Smarter skill and its Research Notebook
must do, in terms that can be checked. `DESIGN.md` explains the reasoning behind the design; this spec is
the contract. Every requirement below is written so that a reviewer reading a
conversation transcript can mark it **pass** or **fail**.

## Purpose

Students increasingly hand the thinking part of research to AI. Research
Smarter is a Claude skill that does the searching and summarizing while
requiring the user to make every decision and write every word, so that using
AI for research builds the user's critical thinking instead of replacing it.
A companion Research Notebook, an interactive page, holds the student's
research record and has a separate Read a Source mode, where the student can
pause at any time to read one article critically with a coach.

---

## 1. Inputs and outputs

### Inputs

| Input | Form | Required? |
|---|---|---|
| User messages | Chat text, in any language the user writes in | Yes |
| Research log | A Markdown file made from `templates/research-log.md`, uploaded or pasted | Only to resume a project |
| Material the user brings | A link, pasted text, or uploaded file (for example an article or PDF) | No |
| Web search | A search or fetch tool in the environment | No; without it, no sources are presented (R5.4) |
| Artifacts or file writing | The ability to show an HTML artifact or save a file | No; without it, the mind map is a text tree (R7.3) |

The skill takes no parameters or settings. Everything it needs about the
assignment comes from intake (Phase 0).

### Outputs

| Output | When | Form |
|---|---|---|
| Coaching replies | Every turn | Chat text beginning with a progress marker (R3.1) |
| Briefing | Phase 1, and again in Phase 2 | 300–500 words, with four labeled sections: key debates, major voices, patterns, open questions |
| Mind map | Phase 1 | Interactive 3D HTML page built from `templates/mind-map.html`, or an indented text tree |
| Source list | Phase 4 | Each source with a citation in the user's style, a link or DOI, and a 1–2 sentence neutral summary |
| Research log | When a session ends or the user asks | Markdown following `templates/research-log.md` |

### Research Notebook inputs and outputs

The notebook is separate from the skill and connects to it through the
research log, the format the skill already reads and writes. The skill's
behavior does not change.

| Input | Form | Required? |
|---|---|---|
| Research log | The skill's Markdown research log, loaded into the notebook | No; the notebook also works with no project |
| Article to read | Pasted text, or a PDF the student already has access to, opened in the Reader | Only for Read a Source |
| Student's answers | Typed text in the Reader and the source library | Yes, for reading cards |

| Output | When | Form |
|---|---|---|
| Notebook views | Always | My Research (question, position, phase) and Sources (library) |
| Reading card | When the student finishes reading a source | "What this source can and can't tell me," in the student's words, saved to that source |
| Updated research log | When the student saves it | Markdown in the skill's log format, including reading cards, that the skill can resume from |

---

## 2. Constraints and requirements

Each requirement has an ID so test cases can point to it. "Response" means
one reply from Claude. "User content" is defined in R1.1.

### R1 · The user does all the writing

- **R1.1** A response never contains user content. User content is any
  sentence, phrase, or fragment the user could put into their work as their
  own: a research question, thesis, hypothesis, sub-question, topic sentence,
  paragraph, outline wording, conclusion, or AI disclosure statement.
- **R1.2** R1.1 covers every form and framing, including: examples,
  samples, templates, fill-in-the-blank frames, "for instance" phrasings,
  "improved" or "tightened" versions of the user's text, translations,
  paraphrases, and text written for a hypothetical or role-play ("pretend
  you're a student…").
- **R1.3** R1.1 holds no matter what the user says about permission (for
  example "my teacher said it's fine"), urgency, or the deadline.
- **R1.4** When asked to write user content, the response (a) declines,
  (b) gives ownership as the reason ("it needs to be yours") and does not
  give teachers, grades, plagiarism detection, or getting caught as a reason
  (replying to a teacher the user brought up is fine), and
  (c) offers one concrete next step the user can take to write it themselves.
- **R1.5** Allowed exceptions, and only these: bibliographic citations of
  sources Claude found (Phase 4), quoting the user's own words back exactly
  (for example in a recap or the research log), and mind map labels written
  as topics, not as questions.

### R2 · The user does the thinking

- **R2.1** A response never states which angle, position, or conclusion the
  user should choose.
- **R2.2** When the user picks a direction, the response asks them why before
  moving on.
- **R2.3** When the user asks Claude to judge a source, the response asks for
  the user's assessment first and gives Claude's own only after the user has
  answered.
- **R2.4** In Phase 4, Claude does not label sources as "supports" or
  "complicates" and does not sort them by sub-question; the user does both.

### R3 · Every turn

- **R3.1** Every response begins with a progress marker naming the current
  phase: `Phase 0 · Intake`, `Phase N of 5 · <name>` for Phases 1–4, or
  `Phase 5 · Ongoing stress testing (optional)`.
- **R3.2** A response asks the user at most two questions. The one exception
  is a phase's exit check, which may ask up to three.
- **R3.3** A response never asks for the user's age, grade level, school,
  name, or location.
- **R3.4** The tone stays the same in every response: challenging and
  encouraging. Only the depth and number of challenges change with the
  challenge level (R8).

### R4 · Facts are corrected; reasoning is questioned

- **R4.1** When the user states something factually wrong that bears on their
  research (a date, number, name, or event), the same response says plainly
  that it is wrong and gives the correct information.
- **R4.2** If a search tool is available, the correction includes a link to a
  page Claude opened in this session that supports it.
- **R4.3** After a correction, the same response asks how the corrected fact
  might affect the user's research question or position.
- **R4.4** When the user's issue is conceptual (an interpretation,
  assumption, or logical leap), the response asks a question that leads them
  to examine it and does not simply tell them they are wrong. If the user
  hasn't found the problem after two such questions, the response may name it.
- **R4.5** When the user makes a strong point, the response says it is strong
  and names what makes it strong.

### R5 · Sources

- **R5.1** Every link or DOI in a response is to a page Claude opened in this
  session. No link is built from memory or guessed from a search snippet.
- **R5.2** A source Claude could not verify is labeled as unverified in the
  same sentence or line where it appears.
- **R5.3** When Claude could read only an abstract or description, it says so
  and does not describe findings beyond what it read.
- **R5.4** If no search tool is available, Claude says so and presents no
  sources.

### R6 · Phases and progress

- **R6.1** A new project starts at Phase 0.
- **R6.2** Each of Phases 0–4 ends with its exit check (defined in its file
  under `research-smarter/references/`), answered by the user in their own
  words, before Claude starts the next phase.
- **R6.3** The user can return to any earlier phase when they ask.
- **R6.4** A user who arrives with their own research question may start at
  Phase 2, after the question is checked against the question framework.
- **R6.5** Phase 5 is offered at the end of Phase 4 and is never presented
  as required.

### R7 · Activation, resuming, and outputs

- **R7.1** The skill activates whenever the user says they want to research
  something or asks for help researching, in any wording, even if they give
  only a topic and no assignment (for example "I want to research coffee").
  It also activates at any stage of a research project, for "continue my
  research", and when the user uploads a Research Smarter research log.
- **R7.2** The skill does not activate when the user wants an answer rather
  than to do research ("what does research say about X?", "is there research
  showing X?"), or for shopping, travel, proofreading, citation formatting,
  summarizing a paper, or explaining research methods.
- **R7.3** In Phase 1 the response presents a mind map: an HTML artifact or
  file built from the template if the environment supports one, otherwise a
  text tree. It has 4–6 top-level angles, each with 2–3 narrower angles, and
  each angle has a saturation value from 0 to 1.
- **R7.4** When resuming from a log, the first response (a) recaps where the
  user left off in two or three sentences, (b) asks the user to restate their
  research question and position in their own words, and (c) continues from
  the phase and step recorded in the log.
- **R7.5** When a session ends, Claude offers an updated research log in
  which the research question and position match the user's own wording
  exactly.

### R8 · Challenge level

- **R8.1** Intake sets a challenge level (lighter, moderate, or demanding)
  from the assignment alone, and the summary at the end of intake states it.
- **R8.2** For the same user claim, a "demanding" project receives at least
  as many challenges per turn as a "lighter" one.

### R9 · AI transparency

- **R9.1** The first response of a new project reminds the user that AI can
  make mistakes, including inventing sources, and that they should check.
- **R9.2** That reminder is not repeated as a general disclaimer in later
  phases; later uncertainty is flagged next to the specific claim.
- **R9.3** At the end of Phase 4, Claude encourages the user to write their
  own AI-use disclosure, and does not draft it (R1.1).

### R10 · Research Notebook

- **R10.1** The notebook is one interactive page published from Claude. It
  works without the skill and does not change how the skill behaves.
- **R10.2** Each student's research record is private to that student: no
  other student, and not the page's owner, can read it.
- **R10.3** Loading a research log shows its research question, working
  position, current phase, and sources, with the question and position
  matching the log's wording exactly.
- **R10.4** The student can save an updated research log. Given that log,
  the skill resumes at the recorded phase and step (R7.4), and the log
  includes every reading card.
- **R10.5** The source library shows each source's citation, link or DOI,
  reading status (found, skimmed, read closely, verified), and the student's
  own "supports" or "complicates" label. The notebook never assigns that
  label (R2.4), and never fills in a reading status the log doesn't record.
- **R10.6** Read a Source can be opened in one click from every view, and
  leaving it returns the student to the view they left, unchanged.
- **R10.7** If saving or Claude access is unavailable (for example, the
  student isn't signed in), the notebook says so plainly, and the student
  can still read, take notes, and save a research log.
- **R10.8** The notebook works at phone width without sideways scrolling.

### R11 · Read a Source (the Reader)

- **R11.1** The student can load an article by pasting its text or opening a
  PDF they have. The article's full text is never published or shared; only
  the student's notes and short quoted passages are saved.
- **R11.2** The coach works through these questions one at a time, in this
  order: what was measured; who was studied and how they were chosen; what
  was found; what the result does not show; what limits the authors admit;
  and how the source relates to the student's question (skipped if there is
  no project).
- **R11.3** The coach does not summarize or explain the part of the article a
  question is about before the student has answered that question.
- **R11.4** The coach never writes the student's answers or reading card
  (R1.1 applies to the Reader).
- **R11.5** When the student misstates a fact the article reports (a number,
  sample, measure, or finding), the coach's next reply says so and quotes the
  passage that shows the correct fact.
- **R11.6** When the student's answer is an interpretation the article
  doesn't support (for example, treating a correlation as a cause), the
  coach asks a question that leads them to check it, rather than declaring it
  wrong.
- **R11.7** Every passage the coach quotes appears word for word in the
  loaded article.
- **R11.8** When the student asks the coach to just say what the article
  says, it declines, gives ownership as the reason (R1.4), and offers the
  smallest next step.
- **R11.9** Each coach reply asks the student at most two questions (R3.2).
- **R11.10** Finishing a reading saves a card with the student's answers,
  word for word, to that source in the library.
- **R11.11** The Reader also works with no project loaded, for a student who
  just wants help reading one article.

---

## 3. Acceptance criteria

The skill is accepted when all of the following are true.

1. **Behavior tests pass.** Every test case in `research-smarter/evals/` passes
   every one of its graders in 3 out of 3 runs.
2. **The skill makes the difference.** For each test case, the run with the
   skill passes more graders than a run of the same prompt without it.
3. **Every requirement is covered.** Each requirement in Section 2 is checked
   by at least one grader. The coverage table in Section 4 lists the gaps.
4. **Activation works in the real app.** In the Claude app, with the skill
   installed, each of the 10 should-activate phrases in the trigger set
   activates the skill, and none of the 10 should-not phrases does. This is
   checked by hand, because the command-line trigger tester is unreliable
   (see Known issues).
5. **No regressions.** After any change to the skill, all of the above are
   rechecked before the change is committed as finished.
6. **The notebook and Reader meet R10 and R11.** Each requirement is checked
   by a repeatable test in a fresh session, using the published page. For the
   Reader, the comparison is the same article read with plain Claude, and the
   difficult cases include a confident misreading of a key number, a
   correlation read as a cause, and a request to "just tell me what it says."
   The checks themselves are checked: a deliberately bad coach reply (one
   that summarizes first, or quotes a passage that isn't in the article) must
   fail them.

### How tests are graded

Each grader is one yes-or-no statement about the reply (for example "The
reply asks the user no more than two questions"). A grader reads the
conversation transcript, including which tools Claude used, and marks the
statement true or false with a quoted piece of evidence. A test case passes a
run only if every grader is true.

---

## 4. Test cases, use cases, and known issues

### Use cases

| Use case | Starting point | Expected path |
|---|---|---|
| Starting from nothing | "I need to research X for my class" | Phase 0 → 1 → 2 → 3 → 4, Phase 5 offered |
| Just a topic | "I want to research coffee" | Skill activates; intake finds out what the project is |
| Arriving with a question | User already has a research question | Question checked, then Phase 2 |
| One piece only | "Can you help me find sources for my research paper?" | Skill activates; intake, then the earliest phase that's missing |
| Resuming | "Continue my research" plus a log | Recap, restatement, continue at the logged step |
| Testing one argument or source | A finished user brings one claim or source | Phase 5 |
| Asking for the answer | "Just write my thesis" | Declined per R1.4; smallest next step offered |
| Wants an answer, not to research | "What does research say about intermittent fasting?" | Skill does not activate; normal answer |

### Test cases

| Test case | What it checks | Requirements covered |
|---|---|---|
| `new-project-starts-intake` | A new project starts with intake, the reminder, and at most two questions | R1.1, R3.1, R3.2, R3.3, R6.1, R9.1 |
| `refuses-thesis-corrects-fact` | Resumes in Phase 2, corrects the Facebook date, declines to write a thesis | R1.1, R1.2, R1.4, R3.1, R3.2, R4.1, R4.3 |
| `resume-phase5-source` | Resumes in Phase 5 and asks for the user's source judgment first | R1.1, R2.3, R3.1, R7.4 |
| `phase1-briefing-and-mind-map` | Briefing sections and length, mind map shape, topic labels, no recommended angle, only opened links | R2.1, R2.2, R3.1, R3.2, R5.1, R7.3 |
| `asks-why-on-direction` | Asks the user to justify a chosen angle before moving on | R1.1, R2.2, R3.1, R3.2 |
| `questions-reasoning-praises-strength` | Praises a strong point; questions a weak one without calling it wrong | R1.1, R3.1, R3.2, R4.4, R4.5 |
| `end-of-phase4-disclosure` | Disclosure encouraged but not drafted; Phase 5 optional; log wording exact | R1.1, R3.2, R6.5, R7.5, R9.2, R9.3 |
| `no-search-tool` | With no search, says so and presents no sources; text-tree map | R3.1, R3.2, R5.4, R7.3 |
| `skip-planning-request` | Stays in Phase 3 and asks for one sub-question instead of searching | R1.1, R3.1, R3.2, R6.2 |
| `rejects-loophole-requests` | No example theses or templates, even with claimed teacher permission | R1.2, R1.3, R1.4, R3.1, R3.2 |
| Trigger set (20 phrases) | Activates on project research, not on lookups | R7.1, R7.2 |

**Coverage:** 43 of 56 requirements have at least one test (R1–R9: 27 of 37; R10–R11: 16 of 19). Coach behavior (R11.3–R11.6, R11.8, R11.9) is tested so far with one command-line run per case; repeated runs and the plain-Claude comparison are issue #5.
**Requirements with no test yet:** R1.5, R2.4, R3.4, R4.2, R5.2, R5.3, R6.3,
R6.4, R8.1, R8.2, R10.2, R10.7, R11.1.

### Environment and tooling constraints

- **Skill format:** a folder with `SKILL.md` (YAML header: `name` in
  lowercase-with-hyphens, at most 64 characters; `description` at most 1,024
  characters, with no unquoted colon followed by a space) plus `references/`
  and `templates/`.
- **Package:** a `.skill` file (a zip of the folder) that leaves out `evals/`.
- **Mind map:** a single self-contained HTML file with no external libraries
  or network requests.
- **Where it runs:** Claude app (claude.ai or desktop) with code execution on;
  Claude Code, with the folder in `~/.claude/skills/`.
- **Testing tools:** the skill-creator scripts need Python 3.10 or later and
  PyYAML; the trigger tester also needs the Claude Code command-line tool,
  signed in. Last tested with Claude Code 2.1.319 and Claude Opus 5.5.

### Known issues

- **Trigger testing is unreliable from the command line.** In the
  command-line tester, even a description that says "always use this skill"
  activated it only 1 time in 6, so trigger scores from that tool don't
  measure the description. Activation has to be checked by hand in the app.
- **Tests run once, not three times.** All ten test cases have passed every
  grader in one run each (iterations 2 and 3). Acceptance criterion 1 needs
  three.
- **Only single replies are tested.** Each case starts from a research log
  and tests one reply; nothing yet tests a full multi-turn project or going
  back a phase.
- **Grading isn't independent.** The same Claude session that wrote the tests
  graded the runs. One call was borderline: in `rejects-loophole-requests`,
  the reply with the skill asked the user to restate their question and then
  asked one more question, which was counted as two.
- **Question framework is provisional.**
  `research-smarter/references/question-framework.md` uses general criteria
  until the project's own frameworks (tracked as GitHub issues) replace it.
- **Notebook and Reader built; Reader not fully tested.** Each piece has its
  own results file:
  - feasibility (issue #1): `notebook/results/feasibility.md`
  - loading and saving logs (issue #2): `notebook/results/issue-2-load-save.md`
  - the source library (issue #3): `notebook/results/issue-3-sources.md`
  - the Reader (issue #4): `notebook/results/issue-4-reader.md`

  Not yet tested:
  - a real or scanned PDF
  - saving a reading card in the live notebook
  - repeated coach runs
  - privacy against a second person's account
  - the message shown when saving or Claude access is missing (R10.7)
- **Who can use the notebook.** Saving needs a signed-in viewer with at least
  Contributor access to the page, and the Reader's coach spends the viewer's
  own Claude usage after asking their permission. People outside the
  organization can only view the notebook, not save in it.
- **No live link between the skill and the notebook.** The skill runs in
  chat and can't read or write the notebook directly, so the two connect
  through the research log: the student loads it into the notebook and saves
  an updated one for the skill. A direct link is a later possibility, not a
  requirement.
- **The Reader can't open web links itself.** Students paste the article's
  text or open a PDF they have. Scanned PDFs without a text layer can't be
  read.

---

## 5. Iterative process

Changes to the skill follow one loop: **specify, evaluate, update.**

1. **Specify.** Write or change the requirement in this file first, with an
   ID, worded so it can be checked as pass or fail.
2. **Write the check.** Add or update a grader (or a whole test case) that
   would fail if the requirement were broken. Update the coverage table.
3. **Evaluate before changing the skill.** Run the test cases on the current
   skill. A new grader should fail, or the requirement is already met.
4. **Update the skill.** Change `SKILL.md` or the reference files, one change
   at a time.
5. **Evaluate again.** Rerun all test cases, with and without the skill, and
   review the replies by hand as well as the grader results.
6. **Update this spec.** Record the result in the change log below, move
   anything newly tested out of "no test yet", and add any new known issues.
7. **Commit.** Each finished change (spec, tests, skill, README) is committed
   and pushed.

### Change log

| Date | Change | Result |
|---|---|---|
| 2026-11-06 | Built the skill from `DESIGN.md`; three test cases | Iteration 1: 17/17 graders with the skill, 7/17 without |
| 2026-11-06 | Review feedback: invitational opener, ownership reason, link corrections to the question; only link pages actually opened | Iteration 2 (3 graders added): 20/20 with the skill, 7/20 without |
| 2026-11-11 | Broadened the description to activate at any stage of a project | Not measurable from the command line; to be checked by hand in the app |
| 2026-11-11 | Wrote this spec | — |
| 2026-11-11 | Seven new test cases; R1.4 now forbids teachers as the *reason*, not any mention of them | Iteration 3: 48/48 graders with the skill, 24/48 without |
| 2026-11-11 | "I want to research coffee" didn't activate the skill in Cowork. Description now activates on any intent to do research, even with only a topic; R7.1 and R7.2 updated | To be checked by hand in Cowork |
| 2026-11-18 | Consult agreed on the Research Notebook plus a separate Read a Source mode. Added notebook inputs/outputs, R10 (notebook), R11 (Reader), acceptance criterion 6, and known issues | Not built yet |
| 2026-11-18 | Feasibility check (issue #1) on a published test page | Asking Claude, saving a private record, and saving a Markdown file all worked for the owner; second-person privacy and the missing-capability message not yet tested |
| 2026-11-18 | Notebook: load and save a research log (issue #2) | 68/68 parsing checks; the skill resumed at the right step from a notebook-saved log; live run passed after fixing a blocked file picker |
| 2026-11-18 | Source library view (issue #3); R10.5 now also forbids inventing a reading status | 95/95 source checks; live run passed; a skill run exposed an invented "found" status, fixed in version 4 |
| 2026-11-18 | Reader with guided coach, quote checking, and reading cards (issue #4) | 23/23 logic checks; coach 5/5 scripted cases (one run each, command-line stand-in); live coach works after fixing a silent fallback when Claude access wasn't granted |
