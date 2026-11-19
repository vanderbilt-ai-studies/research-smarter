# Reader: load an article and run the guided reading coach (issue #4)

**Date:** 2026-11-18
**Page:** `notebook/notebook.html`, published privately at
https://claude.ai/artifact/NT8int2Sc3zA22P1AXcsha (version 6)
**SPEC:** R11.1–R11.11, R10.6

## What was built

- **Read a source:** reachable from every view through a header button, and
  from each source card with its citation filled in. Back returns to the
  view the student came from; leaving with unsaved answers asks first.
- **Loading the article:** paste the text, or open a PDF or text file. PDFs
  are read in the browser with pdf.js 3.11.174 from cdnjs. A PDF with almost
  no text, such as a scanned image, gets a plain message. The article stays
  in the browser only: it's never stored or shared.
- **Six fixed questions,** asked one at a time. The sixth, "How does this
  source relate to your research question?", is skipped when there's no
  project. The questions are written into the page, so the coach can't
  speak before the student answers.
- **The coach:** Claude, called from the page after each answer, with rules
  that mirror the skill. It corrects misread facts with a quote, asks about
  interpretations, declines "just tell me", never writes the student's
  words, asks at most two questions, and stays under 90 words.
- **Quote checking by the page:** every passage the coach quotes is checked
  against the article. One that isn't there word for word is never shown,
  and the student sees a note that it was dropped.
- **Reading card:** "What this source can and can't tell me," with the
  student's answers word for word.
  - **With a project:** saved to a "Reading cards" section of the research
    log, and the source is marked "read closely".
  - **Without a project:** saved as its own file.
- **When the coach can't run:** the page says why (still connecting, no
  permission, not available in this window, or turned off) and how to fix
  it. Answers are still saved.

## Results

| Acceptance check | Result | Evidence |
|---|---|---|
| Pasting text or opening a text PDF loads the article; a scanned PDF gets a plain message | **Partly** | Pasting: browser test and live run. A text file through "Open a PDF": live run. A real PDF and a scanned PDF: **not tested**. |
| Six questions in order, one at a time; the last is skipped without a project | **Pass** | `test_reader.py`; browser test: 6 questions with a project, 5 without. |
| A misstated number gets corrected next, with a quote that's in the article | **Pass** (stand-in) | Coach run 1, `misread-number`: corrected "4,000 students… all over the country" with two quotes, both verified in the article. |
| A correlation read as a cause gets a question, not a verdict | **Pass** (stand-in) | Coach run 1, `correlation-as-cause`: asked whether the design lets you say the restrictions caused it, with no verdict and no fallacy named. |
| "Just tell me what it says" is declined, with ownership as the reason and a small next step | **Pass** (stand-in) | Coach run 1, `just-tell-me`: "The reading needs to be yours…" plus a pointer to the Measures paragraph. No mention of teachers or grades. |
| Finishing saves a card word for word; Back returns to the view left | **Partly** | Card logic: `test_reader.py` (answers come back word for word, including a line break, a dash and a `\|`). Card view and Back: browser test. Saving a card to the live notebook: **not tested live**. |
| The coach runs on the live page | **Pass** (after a fix) | Noa's live run, version 6: "it works". |

**Coach run 1** (`notebook/results/coach-run-1.md`): 5 of 5 cases behaved as
expected, on one run each, through the command-line stand-in. Every reply was
the right kind, under 90 words, asked at most two questions, didn't mention
teachers, grades or fallacies, and didn't call the student wrong. Repeated
runs and the comparison with plain Claude come in issue #5.

**Automated tests:** `notebook/tests/test_reader.py` has 23 checks, all
passing. `test_log_format.py` and `test_sources.py` still pass.

### Checking the checks

| Deliberately broken copy | Checks that failed |
|---|---|
| The quote checker accepts any quote | 4 |
| The prompt shows the coach all six questions | 2 |
| Saving a card flattens the student's line breaks | 1 |

### Problems found and fixed

1. **The coach never ran in Noa's first live run.** The notebook was already
   open when the version that asks for Claude access was published, so it
   kept its old access. Worse, the page silently switched to saving answers
   without feedback. It now says exactly why the coach is unavailable and
   how to fix it (close and reopen the notebook, or allow access). An answer
   sent before the coach connects is no longer saved without feedback.
   Version 6.

### Observations to discuss

- **The coach sometimes points ahead.** For example: "conversation time
  wasn't the only thing the study measured. What was the other outcome?"
  This doesn't summarize the article, but it does hint at what to look for.
  It's worth deciding whether that counts as helping too much.

## Not covered here

- **A real PDF, a scanned PDF, and saving a card live.** Not tried yet.
- **Repeated coach runs and the plain-Claude comparison.** Issue #5.
- **Second-person privacy.** Still open from issue #1.
