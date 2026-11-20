# Unopened links, a third question on resume, and aging test deadlines (issue #14)

**Date:** 2026-11-20
**SPEC:** R5.1 and R3.2 (unchanged), acceptance criterion 1
**Found in:** issue #6's tests ([results](issue-6-ask-how-it-knows.md))

## What changed

- **Links (R5.1):** `references/sources.md` now says to open every link
  exactly as given, including each DOI link, before presenting it. If a page
  won't open, the source is listed without a link and labeled as not
  opened. `phase-4-research.md` repeats it for the source list, and round 2
  added it to `mind-map.md`.
- **Questions (R3.2), in `SKILL.md`:**
  - On resume, the restatement is asked as one question ("Where do your
    question and position stand now, in your own words?"). It counts as one
    of the two, and isn't asked if the user already restated.
  - Every question counts, including follow-ups like "Has it changed?",
    each part of a multi-part question, and "things to consider" lists.
    Before sending, count the question marks and cut the extras.
  - The intake example now asks two questions instead of three.
- **Other tightening found in the first pass (`SKILL.md`):**
  - no sentence starters or half-sentences for the user to finish (R1.2)
  - an invitation names a source by author or title, not just its number
    (R9.4)
  - the "good habit" note is one short sentence (R9.8)
- **Test deadlines:** all 15 test logs moved six months later (now
  May–June 2027). SPEC's "Environment and tooling constraints" says to keep
  them at least six months out.

## Checking the checks

Two deliberately bad replies (`issue-14/check-the-checks/`), graded with the
runner's new `--tools-file` option:

| Bad reply | Failed |
|---|---|
| A source list with a DOI link the tool log never opened | links were opened (R5.1) |
| A resume reply asking for the restatement plus two more questions | at most two questions (R3.2) |

## Results

| Pass | Skill | Result |
|---|---|---|
| First pass, 1 run each | after the main fixes | 89/95 checks; the source list's links passed for the first time; `skip-planning-request` 6/6 |
| **Full suite, 3 runs each** | after round 1 | **282/285 checks; 45 of 48 runs pass every check** |
| Mind map case, 3 runs | after round 2 | 29/30 checks; links 3 of 3 |

The full-suite numbers use round 2's mind map runs; round 1's are kept in
`final/phase1-briefing-and-mind-map/new_skill_round1/` (also 29/30, with one
unopened DOI).

**Per case, runs passing every check (of 3):** 13 cases 3/3.
`asks-why-on-direction`, `invitation-only-with-claims` and
`phase1-briefing-and-mind-map` 2/3.

**The three misses:**
- **A third question (R3.2), twice.** In `asks-why-on-direction`, two
  questions plus "tell me why this angle is worth researching." In
  `invitation-only-with-claims`, three questions in a Phase 2 reply.
- **A fifth briefing section, once.** A Phase 1 briefing added "Side effects
  researchers have found" beside the four required sections, and the grader
  read "four labeled sections" literally.

**Compared with before #14** (issue #6's runs):
- **Unopened links in source lists:** 0 of 3 runs, down from 6 of 6.
- **A third question:** 2 of 48 runs. In #6's new cases it was 4 of 18 runs
  with the #6 skill and 8 of 18 with the skill before #6.
- **`skip-planning-request`:** 6 of 6 checks in every run, now that its
  deadline isn't tomorrow.

## How the runs went

- **Usage limit:** the first full-suite attempt hit the usage limit
  partway. The first 8 cases (alphabetically) finished; the other 8 got no
  replies. Those 24 runs were thrown away and rerun once after the limit
  reset (`final-rerun.log`). `final.log` still shows the cut-off runs as
  failures.
- **Revision rounds:** two, as agreed: round 1 (the tightening above) and
  round 2 (the mind map link rule). Revision stopped there.

## Still open

- **Acceptance criterion 1** needs every case to pass 3 of 3. It's 13 of 16:
  the misses are a third question (2 runs) and an extra briefing section
  (1 run).
