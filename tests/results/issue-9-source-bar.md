# The source bar (issue #9)

**Date:** 2026-11-22
**SPEC:** R5.5–R5.10 (new)
**Skill change:** a "Source bar" section in
`research-smarter/references/sources.md`; the Phase 4 source list and
`SKILL.md`'s research section point to it

## What changed

- **Allowed sources:**
  - peer-reviewed articles
  - scholarly books
  - government and international agency reports and data
  - research organization reports
  - preprints, labeled as not yet peer reviewed
  - reputable news, for current events or background
- **Never presented as a source:** blogs, content farms, opinion sites,
  social media, AI-generated pages, company marketing pages, or Wikipedia.
- **Every source is labeled with its kind.** Peer review is claimed only
  after the journal is confirmed, and the journal is named.
- **Primary sources** may be used when the project calls for them, labeled
  as primary.
- **No padding:** when evidence is thin, the skill says so and points to a
  library database or librarian.
- **A student's own weak source:** the student assesses it first. Then the
  skill says plainly whether it meets the bar and asks how they'll use it.
  The student decides.
- **Spec clarification after approval:** R5.5's list didn't include
  preprints, though R5.6–R5.7 assume they can appear when labeled. The bar
  check failed a correctly labeled preprint, which exposed the gap. R5.5 and
  the check now allow labeled preprints.

## Checking the checks

Four deliberately bad replies (`issue-9/check-the-checks/`), graded against
`src-popular-ai`. Each failed the check it was written to fail:

| Bad reply | Failed |
|---|---|
| A Medium blog post in the list | meets the bar (R5.5) |
| An arXiv preprint labeled "peer-reviewed article" | meets the bar, preprints labeled (R5.7) |
| A short list padded with a content-farm listicle | meets the bar (R5.5, R5.8) |
| "Peer-reviewed study" with no journal named | names the venue (R5.7) |

**Code check:** `tests/check_source_links.py` scans every link for blog and
self-publishing platforms. The first pattern missed `blogs.` subdomains, so
it was widened.

## Results: five new cases, 3 runs each

| Case | Before #9 | New skill |
|---|---|---|
| `src-popular-ai` (blogs, company pages and preprints in search) | 15/18 | **17/18** |
| `src-history-primary` | 11/15 | **15/15** |
| `src-narrow-thin` | 9/15 | **15/15** |
| `src-student-blog` | 6/12 | **12/12** |
| `src-how-know-peer-reviewed` | 11/12 | 11/12 |
| **All five** | **52/72** | **70/72** |

**What changed in practice:**
- **The student's blog.** Before, the skill never said plainly that a
  wellness blog falls short or asked how the student would use it (0 of 3).
  Now it does both every time, and leaves the decision to the student.
- **Padding.** Before, on the narrow topic, it padded the list with an
  opinion piece and a dissertation. Now it says the evidence is thin and
  suggests band-director and music-education sources to look into.
- **History.** Before, it cited blogs (including the Library of Congress's
  blog) and popular-history sites, with only section headings. Now each
  source has its own label, and primary sources are labeled as primary.
- **Blog links (code check):** 0 in the new skill's 15 replies, 2 in the
  old skill's.

**The two misses are both unopened links (R5.1):**
- Two EconPapers working-paper links in the "how do you know" case.
- "eric.ed.gov" named as a place to search, which the grader read strictly.

## Regression: 10 cases that read the changed files, 1 run each

56 of 57 checks. The one miss is the known slip: a mind map listed a DOI the
skill said it couldn't open.

The link scan flagged one link: a Flinders University news blog. The skill
cited the peer-reviewed article itself, and said its summary came from the
university's write-up because the publisher blocked it. That's transparent
use, not a violation, so the scan works as a pointer for a person to check.

## Still open

- **Unopened links still slip through occasionally** (R5.1), in about 1 in 6
  runs here, mostly DOIs or working-paper pages.
