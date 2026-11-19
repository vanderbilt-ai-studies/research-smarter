# Reader test suite and plain-Claude comparison (issue #5)

**Date:** 2026-11-18
**Page:** `notebook/notebook.html`, published privately at
https://claude.ai/artifact/NT8int2Sc3zA22P1AXcsha (version 8)
**SPEC:** acceptance criterion 6, R11

## How it was tested

- **Cases:** `notebook/tests/coach_cases.json` has five student messages
  about the fictional mock study, each traced to R11 IDs:
  - an accurate answer
  - a confident misreading of the sample ("about 4,000 students from all
    over the country")
  - a correlation read as a cause ("Banning phones made students talk 18
    more minutes")
  - "just tell me what it says"
  - a reading with no project
- **Two conditions, the same input:**
  - **Reader coach:** the exact prompt the page builds.
  - **Plain Claude:** the same article and student message, asked as "Can
    you help me understand this study?"
- **Runs:** 3 per case per condition, through the Claude command line,
  which is a stand-in for the page's own connection to Claude (same
  prompt). Every reply is kept, failures included, in
  `notebook/results/coach-eval/`.
- **Grading:** `notebook/tests/run_coach_eval.py` uses two kinds of check:
  - **Code checks:** quotes really in the article (using the page's own
    checker), the "412" correction quote, mentions of teachers, grades or
    getting caught, fallacy names, and references to a research question.
  - **A separate Claude grader** for judgments code can't make: summarizing,
    writing the student's answer, question count, plain correction, question
    rather than verdict, declining, the ownership reason, and a next step.
    Each verdict comes with quoted evidence, in `runs*.json`.
- **Limits of this test:** the grader is also Claude, the article is
  fictional and short, and each case is a single reply rather than a whole
  conversation. These results are evidence about these cases, not a
  guarantee for every reading.

## Checking the checks

Two deliberately bad coach replies to the misread-number case
(`check-the-checks.json`):

| Bad reply | Caught? | Checks that failed |
|---|---|---|
| Summarizes the study before asking anything | Yes | no_summary (R11.3), no_written_answer (R11.4), quote_shows_412 (R11.5) |
| Quotes a passage that isn't in the article | Yes | quotes_real (R11.7), quote_shows_412 (R11.5) |

The checks themselves also had flaws, and they were fixed before the results
below were trusted (the replies were regraded, not regenerated):
- **"Teachers or grades" check:** it flagged "You *caught* that…", which is
  praise, and "grades 10 through 12" from the article itself. It now looks
  for how the reply talks about the student ("your teacher", "your grade",
  "getting caught").
- **Fake-quote check for plain Claude:** it counted paraphrases and sample
  answers in quotation marks as fake quotes. Plain Claude's sample answers
  already fail no_written_answer, so the quote check now applies only to the
  Reader, which marks its article quotes explicitly.

## Results: Reader coach vs plain Claude (round 1)

| Check | Reader | Plain Claude |
|---|---|---|
| **Replies passing every check** | **14 / 15** | **0 / 15** |
| Doesn't summarize the article (R11.3) | 14/15 | 0/15 |
| Doesn't write the student's answer (R11.4) | 15/15 | 2/15 |
| Says plainly the sample is wrong (R11.5) | 3/3 | 2/3 |
| Correction quotes the real figure, 412 (R11.5) | 3/3 | 0/3 |
| Causal claim: question, not verdict (R11.6) | 3/3 | 0/3 |
| No fallacy named (R11.6) | 3/3 | 3/3 |
| Every quote really in the article (R11.7) | 15/15 | n/a |
| Declines "just tell me" (R11.8) | 3/3 | 0/3 |
| Ownership as the reason (R11.8) | 3/3 | 0/3 |
| Offers a small next step (R11.8) | 3/3 | 3/3 |
| No teachers, grades or getting caught (R11.8) | 15/15 | 14/15 |
| At most two questions (R11.9) | 14/15 | 13/15 |
| No research question without a project (R11.11) | 3/3 | 3/3 |
| Acknowledges an accurate answer | 3/3 | 3/3 |

**What plain Claude did:** it explained the study at length, wrote model
answers and corrected sentences for the student, and answered "just tell me
what it says" with a full summary. In one reply it gave a section titled
"Other limitations, in case your teacher asks."

## Diagnose, revise, retest: the coach's hints

Round 1's one Reader failure: in a correlation-as-cause reply, the coach
said "the study measured a second outcome besides conversation time." It
didn't summarize, but it pointed the student at content they hadn't raised.
Noa decided the coach shouldn't do this.

| Round | Change to the coach's rules | Reader replies passing | What still failed |
|---|---|---|---|
| 1 | none | 14/15 | Hinted at an unmentioned outcome (1) |
| 2 | Rule 1a: never mention anything in the article the student hasn't raised; only point to where to look | 12/15 | Hinting gone from the correlation case, but pointing to places added a third question (2); praise added a detail the student hadn't written (1) |
| 3 | Count every question mark toward the two-question limit; praise only what the student wrote | **14/15** | A correction quoted a second passage that also answered the next part of the question (1) |

- **Results files:** `runs.json` (round 1, both conditions), `runs-v2.json`
  and `runs-v3.json` (Reader only).
- **Plain Claude** wasn't rerun, because its prompt didn't change.
- **Live:** round 3's rules are in version 7 and later.
- **Stopping point:** revisions stopped after round 3, to avoid chasing
  single-reply variations.

**Recommended next fix:** when correcting a fact, quote only the passage that
corrects that fact.

## Carried over from issue #4 (live, Noa)

| Check | Result |
|---|---|
| A real text PDF loads (`fixtures/mock-study.pdf`, made with macOS `cupsfilter`; about 2,900 characters of text) | **Pass**: loaded with question 1 |
| A scanned PDF is refused (`fixtures/mock-study-scanned.pdf`, image only, no text) | **Pass**: "may be a scanned image" message, no questions |
| Leaving with nothing typed doesn't ask first | **Pass**: by design, the Reader only asks when answers would be lost |
| Saving a reading card in the live notebook | **Unconfirmed**: the test wasn't finished, and the stored notebook has no card (its last write was the Sources test) |

### Bug found and fixed while testing the save

**What happened:** the card save marked itself "Saved to your notebook"
*before* storage confirmed the write. A write that stalled or failed would
still show "Saved", with nothing stored. A stalled write could also silently
hold up every later save.

**The fix (version 8):**
- Saves go out one at a time, and one with no answer in 15 seconds counts
  as failed.
- The page says "Saved" only after storage confirms.
- A failure shows a red message with a code.
- The notebook rolls back after a failure, so trying again can't add the
  card twice.

This is tested in code and in the browser; it isn't confirmed live yet.

## Still open

- **Saving a reading card live,** on version 8.
- **The recommended single-quote rule** for corrections.
- **Second-person privacy and missing-capability messages,** from issue #1.
- **A trial with a real student,** which the process guide recommends.
