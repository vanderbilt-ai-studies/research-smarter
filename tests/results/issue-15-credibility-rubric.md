# A credibility rubric for sources (issue #15)

**Date:** 2026-11-22 to 2026-11-23
**SPEC:** R5.11–R5.15 (new)
**Skill change:** new `research-smarter/references/credibility-rubric.md`;
`sources.md`'s credibility checklist folded into a pointer to it;
Phase 4, Phase 5 and `SKILL.md` point to it

## What changed

- **A rubric the skill uses, never shows.** It sorts sources that clear
  #9's bar into three levels: "strong evidence," "usable with care," and
  "not evidence on its own." A table sets what counts as strong for each
  research type.
- **Signals, each with how to check it:** peer review (with the warning
  signs of an untrustworthy journal), DOI, publisher or venue, author,
  evidence and methods, primary or secondary, date, and bias and
  corroboration. No single signal decides, and every signal relied on must
  be checked in this session.
- **The student never sees the rubric, a level name, or a score.** They get
  plain reasons why a source is strong or weak for their kind of research.
  The skill's view still comes after the student's, and is about
  credibility, not about whether the source supports them.
- **Sources for the rubric,** opened and checked: Cornell University
  Library's "Critically Analyzing Information Sources" and Think. Check.
  Submit.'s journal checklist.

## Checking the checks

Five deliberately bad replies (`issue-15/check-the-checks/`). Each failed the
check it was written to fail:

| Bad reply | Failed |
|---|---|
| "It has a DOI, so it's credible and peer reviewed" | DOI not enough (R5.12), peer review not assumed (R5.13) |
| "A famous outlet, so it's strong evidence" | study over news (R5.15) |
| A verdict on the CDC page before asking the user | asks the user first, no verdict yet (R5.15) |
| "Tier 1, strong evidence, 9/10" | no rubric shown (R5.11) |
| "Strong because it supports your position" | not about support (R5.15) |

## Results: six new cases, 3 runs each

| Case | Before #15 | New skill |
|---|---|---|
| `rub-doi-not-enough` | 12/12 | 12/12 |
| `rub-news-vs-study` | 12/12 | 12/12 |
| `rub-primary-strong` | 10/12 | **12/12** |
| `rub-student-first` | 11/12 | **12/12** |
| `rub-unconfirmed-peer-review` | 12/12 | 12/12 |
| `rub-source-list-order` | 11/18 | **17/18** |
| **All six** | **68/78** | **77/78** |

- **Single sources were already mostly handled** after #9.
- **The gains:**
  - **History paper:** the skill now says plainly that a 1918 newspaper is
    strong evidence for this kind of paper. Before, it only hinted.
  - **Source list:** it now says which sources meet the "at least 3
    peer-reviewed" requirement (3 of 3 runs; before, 1 of 3), and gives
    every weaker source a reason.
- **The one miss:** a DOI typo, where the reply gave a 2024 DOI but the
  page it had opened was the 2025 one.

## Revision round

| Round | Change | Source-list case |
|---|---|---|
| 0 | The rubric | 13/18: a survey report listed without a reason (2 runs); "eric.ed.gov" written as a place to search, read as an unopened link |
| 1 | Every non-peer-reviewed source gets one line on why it's there; name databases to search ("the ERIC database") instead of writing addresses | **17/18** |

**Usage limit:** the first baseline attempt was cut off entirely and rerun
after the limit reset.

## Regression: 8 source-related cases, 1 run each

35/39 checks, and the link scan found no blog links.

- **Three misses are the old unopened-link slip (R5.1):** DOIs or RePEc
  pages the reply said it hadn't opened but still linked. It's now the most
  frequent failure, with both versions, and needs its own fix.
- **One miss was the rubric's own mistake.** The history row listed "later
  popular histories" as usable with care. But #9's bar allows only
  scholarly books, so the skill presented a popular history book, labeled
  it honestly, and failed the bar. The row now says popular histories are
  below the bar (leads only), and the history case was rerun twice:
  5/5 both times.

## Still open

- **Unopened links (R5.1)** still slip through in roughly 1 in 3 source-list
  runs. That needs its own issue.
