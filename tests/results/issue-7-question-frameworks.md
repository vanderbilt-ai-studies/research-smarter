# Research-question frameworks by discipline (issue #7)

**Date:** 2026-11-20 to 2026-11-22
**SPEC:** R12.8–R12.12 (new)
**Skill change:** a "Frameworks by discipline" section in
`research-smarter/references/question-framework.md`; a framework table in
`research-types.md`; the Phase 1 and Phase 2 exit checks point to it

## Checking the frameworks against real sources

Each of the 13 frameworks in Noa's notes was checked against a university
library guide or the original paper, opened this session. An agent did the
first pass. I then opened six of its sources myself: Midwestern University,
University College Dublin, Washington and Lee, UC Merced, Virginia Tech, and
Waikato. All six said what it reported, except one credit, corrected below.

| Framework | Result | Source used |
|---|---|---|
| FINER | Confirmed | Waikato; Midwestern |
| PICO | Confirmed | Midwestern; UCD |
| PEO / PECO | Confirmed (PEO's stated use varies by guide) | Midwestern; UC Merced (PECO) |
| SPIDER | Confirmed | Midwestern; UCD |
| SPICE | Confirmed | Midwestern; UCD |
| ECLIPSE | Confirmed | Midwestern; UCD |
| CoCoPop | Confirmed | Midwestern; Virginia Tech |
| PCC | Confirmed | Midwestern; UCD |
| CIMO | Confirmed. Virginia Tech credits Denyer & Tranfield (2009), not the 2008 paper the agent named | Virginia Tech |
| BeHEMoTh | Confirmed | UCD |
| Who/What/When/Where | Confirmed with a correction: the source has five Ws, adding Why. It's library advice, not a named framework | Washington and Lee |
| "4-element topic formula" | **Not confirmed**: only content-farm pages | Left out |
| "Sequential funnel" | **Not confirmed as described**: the closest source (a 2024 chapter on "funnelling") has different, non-linear stages | Left out |

Per the issue, I stopped and asked Noa about the two unconfirmed ones. Noa
decided to leave them out. The funnel's later questions (what gap in the
literature, what theory is tested) stay at the "demanding" level as the
project's own guidance.

## What changed in the skill

- **Frameworks as guides:** the skill notices which part that matters is
  missing and asks about it. It may name a framework and its parts, but
  never fills one in or shows a template.
- **Depth by challenge level:**
  - "lighter": general criteria only
  - "moderate": adds the framework that fits
  - "demanding": may also ask about the literature gap and theory
- **A table for choosing a framework,** from what the question is about.
- **Each of the 11 confirmed frameworks** (counting PEO and PECO as one),
  with a question the skill might ask about each part.
- **A source line for each,** with the date checked.
- **`research-types.md`** maps each research type to the frameworks that
  often fit.

## Checking the checks

Four deliberately bad replies (`issue-7/check-the-checks/`). Each failed the
check it was written to fail:

| Bad reply | Failed |
|---|---|
| Rewrites the student's question in PICO form | no template (R12.10), no wording, asks about a missing element (R12.9) |
| Shows a worked PICO example on another topic | no template (R12.10), no wording |
| Asks all five FINER questions at once | at most two weaknesses, at most two questions |
| Marches through all five SPIDER elements | at most two weaknesses, at most two questions |

The SPIDER checklist reply first failed only the question count, because the
qualitative case had no "no checklist" check. One was added, and the reply
now fails it too.

## Results: five new cases, 3 runs each

| Case | Before #7 | New skill |
|---|---|---|
| `fw-clinical-no-comparison` | 15/15 | 14/15 |
| `fw-qualitative-experiences` | 15/15 | 15/15 |
| `fw-give-me-pico` | 17/18 | **18/18** |
| `fw-lighter-no-anchor` | 15/15 | 15/15 |
| `fw-strong-covers-framework` | 14/15 | **15/15** |
| **All five** | **76/78** | **77/78** |

- **Most of this was already covered.** #8's criteria and the existing
  rules already asked about missing comparisons, kept qualitative questions
  qualitative, and declined "just give me a PICO question." So the measured
  gain is small.
- **What the section adds:** the frameworks themselves, sourced, for the
  skill to draw on.
- **Before #7, one miss:** the skill once offered P/I/C/O blanks to "fill
  in," which is a template.
- **With #7, one borderline miss.** A reply named PICO and said the student
  had "the P and the I," then raised the other two. The spec allows naming
  the parts, and it raised exactly two missing elements, but the grader read
  it as walking through a checklist. No revision was made for it.

**Test fix:** the "strong question" case first said "lower blood sugar."
All three baseline runs rightly asked which measure that meant, since "blood
sugar" can mean several. It now says "fasting blood glucose," and the
baseline was rerun (the first runs are kept in `before-question-fix/`).

## Regression: 26 other cases, 1 run each

24 of 26 passed every check (139/141 checks). Not rerun: the two long Phase
4 source-list cases and `no-search-tool`, which can't be tested faithfully
yet; none of them reads the changed files.

The two misses, neither tied to #7's changes:
- **`rejects-loophole-requests`:** a sentence starter for the user to finish
  ("bans seem to help some, but I'm not sure about..."), which R1.2 forbids.
  It happened once in #14's first pass too, before that fix.
- **`skip-planning-request`:** asks for the restatement plus "two or three
  things," where the check wants one small piece. This is a known issue,
  seen with both versions in #10.

**Usage limit:** four regression runs were cut off and rerun.

## Still open

- **Sentence starters:** they still slip through occasionally (R1.2).
- **R12.3** (judged from the assignment) and R12.8 beyond the qualitative
  case have no direct checks.
