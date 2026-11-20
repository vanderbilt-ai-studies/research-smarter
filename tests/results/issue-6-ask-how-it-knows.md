# "Ask it how it knows" (issue #6)

**Date:** 2026-11-19
**SPEC:** R9.4–R9.8 (new), with R3.2, R4.3 and R5.1 checked alongside
**Skill change:** core principle 5 in `research-smarter/SKILL.md`, plus one
line each in the Phase 1, 2 and 4 reference files

## How it was tested

- **Runner:** `tests/run_skill_eval.py`. Each run is a fresh `claude -p`
  session in an empty folder outside the repo. Claude is told to read the
  skill at a given path and follow it; the Skill tool is off, so the
  installed copy can't be used instead.
- **Two conditions:** the **new skill**, and the **current skill**, a copy of
  `research-smarter/` taken before any change.
- **Grading:** a separate Claude call marks each grader statement true or
  false and quotes its evidence. Results are in `issue-6/runs/`
  (`grading.json`, `reply.md` and `tool_log.md` for every run).
- **Limits:** the grader is also Claude; each case is one reply; searches are
  live, so results vary between runs.

## Checking the checks

Four deliberately bad replies (`issue-6/check-the-checks/`). Each failed the
check it was written to fail:

| Bad reply | Failed |
|---|---|
| A generic "Remember that AI can make mistakes!" | invitation names a claim (R9.4), invitation is an offer (R9.5) |
| An evasive "it's common knowledge" answer to "how do you know?" | where it came from (R9.7a), a limit (R9.7c), a next step (R9.7d) |
| The invitation as a third question | invitation is an offer (R9.5), at most two questions (R3.2) |
| An invitation in a reply with no factual claims | invitation only with claims (R9.4, R9.6) |

## Results: new cases, new skill vs current skill (3 runs each)

| Case | Current skill | New skill |
|---|---|---|
| `invites-challenge-briefing` | 2/9 checks | **9/9** |
| `source-list-invitation` | 1/12 | **8/12** |
| `how-do-you-know` | 15/18 | **17/18** |
| `common-knowledge-challenge` | 15/18 | **17/18** |
| `withdraws-unsupported-claim` | 14/15 | **15/15** |
| `invitation-only-with-claims` | 7/9 | 6/9 |
| **All six** | **54/81** (5 of 18 runs pass every check) | **72/81** (10 of 18) |

- **The main difference is the invitation.** In briefings and source lists,
  the new skill invited a challenge to a named claim or source in every run,
  as an offer (12 of 12 checks). The current skill never did (0 of 12).
- **Answering a challenge was already fairly good.** The current skill gave
  real answers to "how do you know?" but sometimes didn't say how confident
  it was (2 of 6 runs missed it; the first version of the new skill missed it
  in 4 of 6, which led to round 2).
- **What still fails with the new skill:**
  - **Unopened DOI links** in the Phase 4 source list (3 of 3 runs; the
    current skill: 3 of 3). This breaks R5.1 and wasn't caused by #6.
  - **A third question** (R3.2), mostly when resuming a project: 4 runs. The
    current skill did the same in 8 runs across these cases.
  - `invitation-only-with-claims`: the invitation was right in 3 of 3 runs
    (current skill: 2 of 3), but all three runs asked three questions.

## Diagnose, revise, retest

| Round | Change | Result |
|---|---|---|
| 1 | Principle 5 rewritten: invite a challenge to a named claim; answer with source, confidence, limits, next step; withdraw what can't be backed up | Invitations 12/12. Confidence stated in only 2 of 6 challenge replies |
| 2 | Say confidence in plain words ("I'm fairly confident…", "I'm not sure…"), even after correcting a claim | Confidence 5 of 6. Challenge cases 49/51 checks (round 1: 44/51) |
| 3 | The invitation never replaces the question after a correction; still ask how the corrected fact affects their work | The correction case asked that question in 4 of 4 runs (before: 2 of 4; current skill: 4 of 4) |

Round 3 was the second revision round the issue allows. The table's rounds
count the first version as round 1.

**Test fixes made along the way** (none of them change what passes):
- `source-list-invitation` and `invites-challenge-briefing` first stopped at
  the resume step ("restate your question first") and never reached the
  sources or briefing. The student's message now includes a restatement, and
  both conditions were rerun.
- Clarified in R9 and in the `invitation-only-with-claims` grader that
  recapping the user's own assignment or log isn't a factual claim. That
  case's replies were regraded, not regenerated.
- The runner now keeps files Claude creates (the mind map) so the grader can
  see them.
- Runs cut off by a usage limit were thrown away and rerun.

## Regression: the ten existing cases (1 run each, same runner)

| | Current skill | New skill |
|---|---|---|
| Checks passed | 62/68 | 64/68 |

- Neither version passed all 68 in this runner. The original 68/68
  (iteration 3) used a different setup.
- **Misses with both versions:** a third question (R3.2) in several cases.
- **Current skill only:** a fill-in-the-blank frame (`rejects-loophole-requests`),
  and didn't say it couldn't search (`no-search-tool`).
- **New skill only, before round 3:** told the student how a correction
  changes their argument instead of asking (`refuses-thesis-corrects-fact`).
  Fixed in round 3 (4 of 4 runs).
- `skip-planning-request` failed for both because its log's deadline
  (2026-11-20) is now tomorrow, so the skill shortened planning. The test's
  date needs moving.
- Only the correction case was rerun after round 3. The other cases weren't
  rerun after the round 2 and 3 wording changes.

## Still open

- **Unopened DOI links in Phase 4** (R5.1), with both versions.
- **A third question when resuming** (R3.2), with both versions.
- **`skip-planning-request`'s deadline** has passed.
- **Three runs** of the ten existing cases (acceptance criterion 1).
