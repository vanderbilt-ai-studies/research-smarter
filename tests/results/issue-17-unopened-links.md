# Unopened links and DOIs (issue #17)

**Date:** 2026-11-23
**SPEC:** R5.1 (reworded), R5.16 (new)
**Skill change:** `references/sources.md` (DOI rule, notes as you open, a
final check), `phase-4-research.md`, `mind-map.md`, and one line in
`SKILL.md`'s research section

## The short version

Since #14, results files reported the skill linking pages or DOIs it hadn't
opened in roughly 1 in 3 to 1 in 6 source runs. This issue found that most of
that wasn't real.

- **The old rule.** R5.1 counted a DOI as unopened unless the skill opened
  the `doi.org` link itself, even when it had read the DOI on the article's
  own page. Most failures were exactly that.
- **The grader couldn't see page contents.** It knew which pages were
  opened, not what they said.

With the rule reworded and the test runner able to see page text, the skill
from before #17 had **no unopened links or DOIs in 15 runs**, and neither did
the final skill. The value of #17 is a clearer, citation-friendly rule and a
check that can actually verify it, not a change in behavior.

## What changed

- **R5.1:** every link must be a page Claude opened. Every DOI must have been
  opened itself, or appear character for character on an official page
  Claude opened (publisher, journal, PubMed or PubMed Central, Crossref,
  OpenAlex). Never from a search snippet, a mirror site, or memory.
- **R5.16:** a final self-check before sending, matching every link and DOI
  against what was opened, and unlinking anything that doesn't match, saying
  so.
- **The skill:**
  - take notes (title, authors, venue, link, DOI) at the moment a page is
    opened, and build the list from those notes
  - never build a DOI from a web address or numbering pattern
  - a page seen only in search results isn't opened
  - the final check is in `SKILL.md` as well as `sources.md`, and covers the
    mind map
- **The runner** (`tests/run_skill_eval.py`) now saves the text of every page
  Claude opened (`opened.jsonl`), and gives the grader the DOIs found on
  those pages.
- **The code check** (`tests/check_links_opened.py`) checks every link and
  DOI in a reply and in any files it made against the opened pages.
- **The link graders** in eight cases were reworded to the new R5.1.

## Checking the checks

Five deliberately bad replies (`issue-17/check-the-checks/`) all fail the
code check, and a good one passes:

| Bad reply | Caught |
|---|---|
| A DOI on no opened page | yes |
| A DOI one digit off from the opened page's | yes |
| A working-paper page that wasn't opened | yes |
| An unopened DOI in the mind map | yes |
| A truncated DOI that's the start of a real one | yes |

**A bug in the check itself, found and fixed.** Crossref and OpenAlex return
JSON, which writes `/` as `\/`. The first version of the check missed DOIs
written that way, and flagged some DOIs the skill had really seen. Before
spotting this, I told Noa that rounds 0 and 1 had "mixed-up DOIs." They
didn't. The check and the grader's DOI list now read escaped slashes, and
every run was rechecked.

## Results: five link-heavy cases, 3 runs each, same runner and checks

Cases: `src-popular-ai`, `rub-source-list-order`, `source-list-invitation`,
`src-how-know-peer-reviewed`, `phase1-briefing-and-mind-map`.

| Version | Runs with an unopened link or DOI (code check) | Grader checks |
|---|---|---|
| Skill before #17 | 0 of 15 | 88/90 |
| #17 round 0 | 0 of 15 | not comparable (graded before the slash fix) |
| #17 round 1 | 1 of 15 (a Wikipedia link seen only in search results) | not comparable |
| **#17 final (round 2)** | **0 of 15** | **89/90** |

**The grader misses:**
- **Final skill:** an arXiv version not labeled "not yet peer reviewed"
  (R5.7).
- **Skill before #17:**
  - a mind-map label phrased as a question
  - an EconPapers link the grader thought unopened. The code check, which
    sees the full commands, confirmed it was opened.

**Rounds:**
- **Round 1:** put the final check in `SKILL.md` and banned building DOIs
  from web addresses.
- **Round 2:** added notes as you open and the search-results rule.

Neither round changed the results measurably. Rounds 0 and 1 looked worse
at the time only because of the slash bug.

**Usage limit:** 11 round-2 runs were cut off and rerun, and one was
regraded.

## Regression

Three other cases whose link checks were reworded, 1 run each: 14/15
grader checks, and no blog links.

- **`src-narrow-thin`:** listed two doctoral dissertations, which the source
  bar doesn't include (R5.5). That's not a link problem.
- **`src-history-primary`:** the code check flagged three newspaper-archive
  pages. They were opened: the skill fetched them in a shell loop (`for s in
  1918-10-03/... 1918-10-07/... 1918-10-10/...; do curl ...`), which the
  check couldn't expand. Verified by hand from the tool log. The runner now
  expands simple loops and saves the full command, so this is checked
  automatically from now on.

## What this means for earlier results

The unopened-link counts in the #9, #10, #14 and #15 results used the old
rule and a grader that couldn't see page text, so they overstate the
problem. SPEC's known issues now say so. Those files aren't rewritten; this
note corrects them.
