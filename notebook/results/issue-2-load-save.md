# Notebook: load and save a research log (issue #2)

**Date:** 2026-11-18
**Page:** `notebook/notebook.html`, published privately at
https://claude.ai/artifact/NT8int2Sc3zA22P1AXcsha (version 2)
**SPEC:** R10.1, R10.3, R10.4, R10.7, R10.8

## What was built

- **My Research view:** current phase on a six-phase track, what the student
  was in the middle of, their research question, working position and
  counterargument in their own words, the assignment, sources, and key
  decisions.
- **Loading:** a log file or pasted text. Loading anything that isn't a
  Research Smarter log shows a message and changes nothing.
- **Saving:** offers the log as a Markdown file. The log's text is kept
  exactly as loaded; only "Last updated" changes, to the student's local
  date (the fix from issue #1). If file saving isn't available, the page
  shows the text with a Copy button instead.
- **Keeping the project:** the loaded log is stored in the student's private
  space (`data/users/<id>/project`) and restored on the next visit.
- **Example project:** a clearly labeled example for first-time visitors,
  which is never saved.

## Results

| Acceptance check | Result | Evidence |
|---|---|---|
| Loading each example log shows its question, position, phase and sources, with question and position word for word | **Pass** (parsing) | `notebook/tests/test_log_format.py`: 68 of 68 checks pass on all 9 example logs. The page's own parsing code runs in macOS's JavaScript engine. |
| Saving produces a log the skill resumes from at the right phase and step | **Pass** | A log saved by the notebook's own code (date changed to 2026-11-18, nothing else) was given to the skill in a fresh session. It recapped the project, asked for the question and position in the student's own words, and resumed at Phase 3, sub-questions, matching the log (R7.4). Reply below. |
| Loading a file that isn't a log shows a message and changes nothing | **Pass** (parsing) | README.md, GUIDE.md, SPEC.md and DESIGN.md are all rejected. |
| No sideways scrolling at phone width | **Pass** | At 375 px wide, the page width was exactly 375 px with the example project loaded. |
| Live published page | **Pass** (after a fix) | Noa's run of version 2, checked against stored data and the saved file (below). |

### Checking the checks

The tests were run against two deliberately broken copies of the page:
- **Saving rewrites the research question:** four "saving changes only the
  date" checks failed.
- **The date is in UTC:** the local-date check failed.

So the tests do catch these failures.

### Problems found and fixed during the build

1. **Wrong current phase.** "Phase 0 complete; ready to start Phase 1"
   highlighted no current phase. Phase 1 is now current.
2. **Placeholder counted as a question.** "not written yet (topic: …)" was
   shown as a written question. It now shows as not written.
3. **Broken labels on phones.** Phase labels broke mid-word at phone width
   ("Resear ch"). Narrow screens now show phase numbers only, with the full
   name in the heading above.
4. **File picker blocked.** Load a log file did nothing on the live page
   (version 1). Found in Noa's live run and fixed in version 2.

### The skill's reply to the notebook-saved log

> **Phase 3 of 5 · Plan the research**
>
> Welcome back! Here's where you left off: you're writing an 8-page
> argumentative sociology essay on school-day phone bans, and you've already
> passed the checks for intake, exploring your direction, and the stress test.
> You were just about to start Phase 3 by breaking your question into
> sub-questions. […]
>
> Before we pick up, could you tell me your current research question and
> your working position, in your own words? […]

## Live page run (Noa)

Noa ran the published page as its owner. Claude checked each step that
leaves evidence.

| Step | Result | Evidence |
|---|---|---|
| See an example | Pass | Noa saw the labeled example. By design it isn't saved: storage stayed empty afterward. |
| Load a log file (version 1) | **Fail** | Nothing opened, and storage stayed empty. The button opened the file picker from script, which Claude's page frame can block. |
| Load a log file (version 2) | Pass | The button is now a real file-picker label the student clicks directly. The stored project matched the original log byte for byte, with `savedOn` 2026-11-18 (local date). |
| Reload restores the project | Pass | Noa saw "Welcome back" with the same project. |
| Save research log | Pass | The saved file differs from the original only in "Last updated" (2026-11-08 → 2026-11-18). |
| Load README.md | Pass | Noa saw the "not a research log" message. The stored project was unchanged (still version 1). |

**Note:** the save dialog put the file in the last folder Noa had used, the
test case's `files` folder, not Downloads. The file was moved out so it
wouldn't be copied into future test runs. Students may hit the same thing;
the save message tells them the filename to look for.

## Not covered here

- **Sources view (issue #3).** Sources only show as a simple list here.
- **R10.6.** Read a Source comes with the Reader (issue #4).
- **Second-person privacy and missing-capability messages.** Still open
  from issue #1.
