# Phase 4 deep dive (issue #16)

**Date:** 2026-11-23
**SPEC:** R5.17–R5.20 (new)
**Skill change:** `research-smarter/references/phase-4-research.md` ("Search
deeply," "Present a manageable set," a coverage report);
`credibility-rubric.md` (one line)

## What changed

- **Search deeply.** Every sub-question is searched at least three ways,
  using a scholarly database when reachable. The skill follows what good
  sources cite and what cites them, and keeps going until new searches turn
  up nothing new. It aims for variety, and quality still comes first: the
  source bar holds, and no padding.
- **A manageable chat.** At most five sources per sub-question in total
  (ten for two sub-questions), grouped by kind of source, never by
  sub-question. It includes any source that cuts against the student's
  position, without labeling it.
- **The full list goes into the research log,** written in the same reply,
  and the chat says how many more are there.
- **A coverage report:** what was searched, where evidence is plentiful or
  thin, and what couldn't be reached.
- **Spec fix before the skill change.** As first drafted (and approved),
  R5.20 said to show sources "for each sub-question," which would break
  R2.4: the student, not Claude, sorts sources by sub-question. Noa chose
  to keep R2.4, so the cap became a total, with sources grouped by kind.

## Tools added

- `tests/check_log_loads.py` runs the notebook's own log parser on any
  research log the skill writes, to confirm it still loads. Tested on a real
  log and a non-log file.
- The runner's per-run time limit went from 15 to 25 minutes, for long
  searches.

## Checking the checks

Three deliberately bad deep-dive replies (`issue-16/check-the-checks/`).
Each failed the check it targets:

| Bad reply | Failed |
|---|---|
| Four sources, all from one journal and site | variety (R5.18), plus depth and database |
| Fourteen sources in one list | manageable set (R5.20) |
| No coverage report | coverage report (R5.19) |

Padding with weak sources and unopened links are already caught by the #9
bar check and the #17 link check.

## Baseline

The current skill's three recent runs of the same prompt (#17's final round
of `src-popular-ai`), regraded with the deep-dive checks: **26/33**. It
missed the coverage report in all 3 runs, and one run listed a single
source.

## Results: `deep-dive-ai`, 3 runs per round

| Round | Change | Checks | What still failed |
|---|---|---|---|
| Before #16 | — | 26/33 | coverage report (3), variety, a complicating source |
| 0 | Deep search, the cap, the coverage report | 27/33 | "why it's here" notes that hinted at sorting ("fits your idea," "close to your sub-question 2"), in 2 runs; the coverage report once left out what couldn't be reached |
| 1 | Notes describe the source, never how it fits the student; always say what couldn't be reached | 30/33 | promised to add sources to the log without writing it (2 runs) |
| **2** | Write the log in the same reply | **32/33** | one grader doubt about links that the code check confirmed were opened |

**How much deeper:**
- **Distinct pages and API calls opened per run** (from the saved
  commands): **46–51** with the new skill, against **15–27** before. The
  before runs were recorded before the runner expanded `curl` loops, so
  their counts may be slightly low.
- **Research logs:** written with **16–18 sources**, and each loads in the
  notebook (`check_log_loads.py`).
- **Unopened links (code check):** 0 in every round.

**`src-narrow-thin`** (thin topic, no padding), 3 runs: 14/15. The current
skill's three most recent runs scored 12/15. The one miss was a policy
magazine piece labeled "not peer reviewed," which the bar check failed.

## Regression: 7 Phase 4 cases, 1 run each

38/40, with no unopened links (code check) and no blog links.
- **The grader doubted arXiv and Pew links** that the code check confirmed
  were opened.
- **The known "one small piece" issue** in `skip-planning-request`.

## Still open

- **The grader's tool log is cut to 200 characters per call.** For links,
  the code check is the reliable one. Recorded in SPEC's known issues.
- **"Search until nothing new turns up"** can't be checked directly; the
  tests check the floor (three searches per sub-question, a database).
