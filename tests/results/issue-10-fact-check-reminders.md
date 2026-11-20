# Fact-check reminders (issue #10)

**Date:** 2026-11-20
**SPEC:** R9.2 (rewritten on purpose), R9.9–R9.11 (new)
**Skill change:** core principle 5 in `research-smarter/SKILL.md`, plus the
closing of the Phase 1 and Phase 2 briefings and the Phase 4 source list

## What changed

- **R9.2 used to say** the first-reply reminder is never repeated. Now a
  fact-check reminder also appears in the reply that begins each phase and
  in every reply that presents sources. Other replies still get none.
- **R9.9–R9.11:** a reminder names what was just given and one concrete way
  to check it; it's at most two sentences, with accuracy as the reason
  (never teachers, grades or getting caught); and when the #6 "ask me how I
  know" invitation also applies, the two are one closing passage with no
  question mark.
- **The skill** asks for varied wording, which the tests can't check (each
  test is one reply).

## How it was tested

Same runner and grader as #6 and #14 (`tests/run_skill_eval.py`). The
baseline is the skill as of #14, copied before any change.

**Test changes:**
- Three new cases: `reminder-at-phase-start` (beginning Phase 2),
  `source-list-reminder` (a Phase 4 list), `no-reminder-mid-phase`.
- `end-of-phase4-disclosure` grader 07 rewritten to the new rule: closing
  Phase 4 neither begins a phase nor presents sources, so no reminder.
- **Grader clarified after the baseline:** the no-reminder checks counted
  the #6 invitation ("ask me how I know…") as a general reminder. Both
  checks now say an invitation isn't a reminder, and the baseline replies
  were regraded, not regenerated.

## Checking the checks

Four deliberately bad source-list replies (`issue-10/check-the-checks/`).
Each failed the check it was written to fail:

| Bad reply | Failed |
|---|---|
| No reminder | reminder present (R9.2) |
| "Remember that AI can make mistakes!" | names what and how (R9.9) |
| Reminder and invitation in two separate places | combined passage (R9.11) |
| "Your teacher will mark you down" as the reason | right reason (R9.10) |

## Results: new cases, 3 runs each

| Case | Skill before #10 | New skill |
|---|---|---|
| `reminder-at-phase-start` | 6/15 | **15/15** |
| `source-list-reminder` | 10/15 | **15/15** |
| `no-reminder-mid-phase` | 8/9 | **9/9** |
| `end-of-phase4-disclosure` | 24/24 | 22/24 |
| **All four** | **48/63** | **61/63** |

- **The main difference:** before #10, 2 of 3 Phase 2 briefings had no
  fact-check reminder, and no source list combined its reminder with the
  invitation (0 of 3). With #10, every phase start and source list had a
  reminder that named what and how, combined with the invitation.

## Revision round

| Round | Change | Result |
|---|---|---|
| 0 | The first version | New cases 62/63. The miss: a Phase 4 wrap-up added a general "open them once more" reminder |
| 1 | "In every other reply, including the one that wraps up a phase or offers a research log, don't add a general reminder" | No reminder in 3 of 3 wrap-ups. One run (6/8) instead put off the disclosure suggestion and didn't present Phase 5 as optional |

Revision stopped after one round; the round 1 miss isn't about reminders.

## Regression: the other 15 cases, 1 run each

13 of 15 passed every check. The two misses:

- **`source-list-invitation` (2/4):** one DOI link that wasn't opened (only
  the article's PubMed Central page was) and four questions.
  - Across all source-list runs in this issue, an unopened DOI appeared in
    2 of 4 runs with the new skill and 1 of 3 with the skill before #10, so
    #14's link fix isn't fully holding. That's not caused by #10.
- **`skip-planning-request` (2/6):** the reply skipped planning and
  searched, which the skill must not do (R6.2).
  - Three more runs each: the new skill held the line every time (17/18
    checks), and so did the skill before #10 (15/18). The remaining miss in
    both: asking for the restatement plus "two or three" planning items
    instead of one small piece.
  - So the skip happened in 1 of 7 runs with the new skill. Recorded as a
    known issue.

## Still open

- **Unopened DOI links** in about 1 in 3 source lists, with both versions.
- **Planning skipped once** in 7 runs.
- **"One small piece" in the planning-skip case:** both versions ask for
  more than one piece when they also ask for the restatement.
