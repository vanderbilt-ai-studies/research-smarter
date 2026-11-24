# Political topics: affiliations and the other side (issue #12)

**Date:** 2026-11-23 to 2026-11-24
**SPEC:** R5.21–R5.26 (new)
**Skill change:** a "Political topics" section in
`research-smarter/references/sources.md`; the Phase 1 and Phase 2
briefings and the Phase 4 source list point to it

## What changed

- **Recognizing a political topic.** The skill decides from the topic
  whether it's politically contested (policy, elections, laws, issues
  people divide on politically), and says so once.
- **Affiliation labels:**
  - **Who gets one:** partisan outlets, advocacy groups, think tanks with a
    known leaning, and campaigns. That includes ones named in passing in a
    briefing, and university centers that take a side.
  - **What the label shows:** where the affiliation was confirmed (the
    organization's own mission or "about" page, funding, or party ties).
  - **Limits:** bias-rating sites count as one view at most. A page that
    couldn't be opened is never described.
  - **Never labeled:** an individual's politics, unless they've held a
    political role or declared them.
- **Counterparts.** For every source arguing one side, for or against, and
  every affiliated source, the skill shows at least one credible source from
  the other side, or says it couldn't find one.
- **Settled evidence.** No invented balance on settled questions; the skill
  points to what is genuinely debated.
- **No steering.** Sources may be described as arguing for or against a
  policy, never as supporting the student. The skill never says which side
  is right.
- **One-sided student sources.** It points out the lean and asks what the
  other side would say.

## Checking the checks

Seven deliberately bad replies (`issue-12/check-the-checks/`). Each failed the
check it was written to fail:

| Bad reply | Failed |
|---|---|
| A political source list with no affiliation labels | affiliation labels (R5.22) |
| "Conservative" and "liberal" labels with nothing behind them | affiliation labels (R5.22) |
| "Both sides" of vaccines and autism, equally | settled, no invented balance, real debate (R5.25) |
| Labels, then "the evidence clearly favors" one side | no steering (R5.26) |
| An author called "a well-known progressive" | no author politics (R5.23) |
| Two labor-aligned sources and nothing from the other side | counterparts (R5.24) |
| "This one supports your position" | no steering (R5.26) |

## Results: six new cases, 3 runs each

| Case | Before #12 | New skill |
|---|---|---|
| `pol-min-wage-list` | 19/24 | **23/24** |
| `pol-briefing-counterpart` | 10/18 | **17/18** |
| `pol-one-sided-sources` | 7/12 | **12/12** |
| `pol-settled-evidence` | 11/12 | **12/12** |
| `pol-how-know-affiliation` | 12/12 | 12/12 |
| `pol-nonpolitical` | 9/9 | 8/9 |
| **All six** | **68/87** | **84/87** |

**The gains:**
- **Saying the topic is political:** in every political run, against 0 of
  6 before.
- **Labeled advocacy groups and think tanks** in briefings. Before, they
  went unlabeled or were called something vague like "an organization with
  views on school choice."
- **Counterparts** for one-sided sources.
- **Saying plainly** when a student's sources all lean one way.

The skill before #12 already handled settled evidence and "how do you
know" well.

**The three misses:**
- **A minimum-wage reply** asked four questions.
- **The Urban Institute went unlabeled.** It describes itself as
  nonpartisan, so this is borderline.
- **A bees reply** linked a PubMed Central page that wasn't opened. The
  link check caught it; the DOI had been confirmed through Crossref, but the
  page link itself wasn't.

## Revision round

| Round | Change | Briefing / affiliation cases |
|---|---|---|
| 0 | The "Political topics" section | 14/18 and 11/12: organizations named in passing in briefings went unlabeled, one source arguing against a program had no counterpart, and one reply described an organization's page it couldn't open |
| 1 | Every organization cited counts; never describe an unread page; counterparts for sources arguing against too | **17/18 and 12/12** |

**Usage limit:** the first attempt at the vaccines case was cut off and
rerun.

## Regression: 6 policy-topic cases, 1 run each

Many existing cases are on policy topics (phone bans, four-day weeks), so
the skill now treats them as political. 36/38, with no unopened links (code
check) and no blog links. Both misses came from test tooling:

- **The grader's shortened tool log** hid OpenAlex searches in
  `deep-dive-ai`.
- **A runner bug.** The skill saved its updated research log as
  `research-log.md`, the input file's name, and the runner skipped files
  with input names, so the updated log was thrown away. The runner now
  keeps an input-named file when Claude changed it. This may also explain
  two #16 runs that seemed to include the log only in the reply; those runs
  passed the log check either way.

## Still open

- **The Claude command line's sign-in expires December 1–4.** Run
  `claude auth login` before then for the tests to keep working.
