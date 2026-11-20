# What makes a good research question (issue #8)

**Date:** 2026-11-20
**SPEC:** R12 (new): the definition, R12.1–R12.7
**Skill change:** `research-smarter/references/question-framework.md`
rewritten; the Phase 1 and Phase 2 exit checks point to it

## What changed

- **The definition** combines Noa's criteria and acceptance checks with two
  kept from the old file: clear, focused, concise, complex, open (and
  arguable when the assignment calls for an argument), neutral in tone,
  answerable with authoritative evidence, researchable in time, adds
  something, and matters.
- **`question-framework.md`** now has:
  - how to use the criteria: pick the one or two that matter most (one at
    the "lighter" level); ask, don't fix or announce; say what's strong and
    stop there; judge from the assignment, not the person
  - each criterion with a question the skill might ask
  - the four question types as a lens, with the evidence each needs
  - Noa's weak and good examples and the sleep set, marked for the model's
    understanding only
- **Not yet:** the discipline frameworks (#7). The file says they're still
  to come.

## Checking the checks

Six deliberately bad replies (`issue-8/check-the-checks/`). Each failed the
check it was written to fail:

| Bad reply | Failed |
|---|---|
| Gives the "good" version of the diabetes question | no wording (R12.1), none of the example's details (R12.6) |
| Quotes a reference example "for comparison" | no reference examples (R12.6) |
| Demands a descriptive lab report question be arguable | no arguable demand (R12.4) |
| Calls the question weak without asking anything | asks about scope (R12.1) |
| Runs through every criterion | at most two weaknesses (R12.1) |
| Invents a weakness in the "just right" question | says what's strong, no invented weakness (R12.2) |

## Results: ten new cases, 3 runs each

| Case | Before #8 | New skill |
|---|---|---|
| `q-too-broad` | 14/15 | **15/15** |
| `q-too-narrow` | 14/15 | **15/15** |
| `q-just-right` | 10/15 | **15/15** |
| `q-yes-no-diabetes` | 15/18 | **18/18** |
| `q-arguable-missing` | 15/15 | 15/15 |
| `q-arguable-not-needed` | 12/12 | 12/12 |
| `q-causal-correlational` | 15/15 | 15/15 |
| `q-loaded-tone` | 7/12 | **12/12** |
| `q-no-evidence` | 11/12 | 11/12 |
| `q-lighter-just-tell-me` | 12/12 | 12/12 |
| **All ten** | **125/141** | **140/141** |

- **Where the skill already did well.** The old general criteria already
  covered arguability, question types, and evidence.
- **The biggest gains:**
  - not inventing weaknesses in a well-scoped question
  - asking about a loaded question instead of announcing it
  - never handing over an example question (the skill before #8 did once:
    "For example, what happens to people who…")
- **The one miss:** a third question in `q-no-evidence`.
- **Examples never leaked.** No reply contained or adapted a reference
  example (R12.6), in 30 runs.

## Diagnose, revise, retest

| Round | Change | Result |
|---|---|---|
| 0 | The rewritten reference file | 126/141 before the grader fix below. Still pushed the "just right" question narrower ("which kind of memory?"), and announced the loaded tone instead of asking |
| 1 | "Ask, don't fix, and don't announce"; "Say what's strong, and stop there," naming the "just right" example as focused enough | The four affected cases: 53/54 (round 0: 44/54) |

**Test fixes found along the way:**
- **The sleep cases' assignment.** At first all three sleep cases were set
  in an argumentative paper. The skill before #8 then rightly said the "just
  right" question wasn't arguable, which R12.4 requires there. The calibration
  set is about scope, so the cases became a literature review, and the
  baseline was rerun (the first runs are kept in `before-log-fix/`).
- **The two-weakness check counted strengths.** "Raises no more than two
  criteria" failed replies that named what was good and then one problem,
  which is what the spec asks for. It now counts only weaknesses but still
  fails a full checklist (the bad reply above still fails it). Both
  versions' replies were regraded, not regenerated.
- **Usage limit:** 9 baseline runs were cut off and rerun; 2 more had real
  replies whose grading failed, and were regraded.

## Regression: the other 19 cases, 1 run each

18 of 19 passed every check. The exception is `no-search-tool`, and it's the
test runner's fault, not the skill's:

- **The runner never blocked web search.** `--allowed-tools` only
  pre-approves tools. So this case, meant to run without search, could
  search in every run since #6, and did in some.
- **The runner now blocks WebSearch and WebFetch** when a case doesn't allow
  them. Three reruns made no web-tool calls.
- **But Claude then searched through Bash.** It used `curl` to query
  OpenAlex and fetch pages (3 of 3 runs). The case allows Bash for the mind
  map file, and Bash has network access. With a working research tool, the
  skill rightly didn't say it couldn't search.
- **Testing "no search" needs an environment with no network.** Recorded in
  SPEC's known issues.

## Still open

- **`no-search-tool`** needs an environment without network access.
- **The discipline frameworks** (#7).
- **R12.3** (judged from the assignment, never age, grade or school) has no
  direct check yet.
