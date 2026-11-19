# Research Smarter · guidance for the development agent

Noa's AI 1010 final project: a Claude skill that coaches students through
research, plus a Research Notebook page with a separate Read a Source mode.
The consult agreed on the notebook plus the Reader. Due December 11.

## Read first

- `SPEC.md`: the contract. Every change traces to a requirement ID; R10 is
  the notebook, R11 the Reader.
- `README.md`: the project proposal. `GUIDE.md`: how the skill works and
  installs. `DESIGN.md`: the reasoning and an example walkthrough.

## Where things live

- `research-smarter/`: the skill. Its coaching flow stays as it is. Don't
  change its behavior unless an issue says so and Noa approves.
- `notebook/`: the Research Notebook page and its Reader (to be created).
- `research-smarter/evals/`: skill test cases. Put notebook and Reader tests
  under `notebook/tests/`, with observed results in `notebook/results/`.
- `research-smarter-workspace/`: local test runs; git ignores it. Never
  commit it.

## Rules that always apply

- The student does all the thinking and writing. Neither the skill nor the
  Reader writes their question, thesis, answers, or reading cards (R1, R11).
- Never invent sources, quotes, test results, or access. Quote only text
  that exists in the source.
- Students may be minors. Keep each student's record private, and never
  store or publish an article's full text.
- Keep the notebook connected to the skill through the research log format
  in `research-smarter/templates/research-log.md`.

## How to work

1. Work from one bounded issue at a time. Read its acceptance criteria and
   the SPEC requirements it names.
2. Build, then test the actual published page or skill in a fresh session.
   For the Reader, compare against plain Claude reading the same article.
3. Check the checks: a deliberately bad result must fail them.
4. Revise and retest until the criteria pass, or stop and report a blocker
   or an agreed limit. Record what you observed, including failures.
5. Update `SPEC.md` (coverage, known issues, change log) and the README
   when what they say changes.

## Commits and publishing

- Show Noa each change and commit only after Noa approves. Then push to
  `vanderbilt-ai-studies/research-smarter`. End commit messages with
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Ask before publishing a page, creating or posting GitHub issues, or
  making a release.
- After changing `research-smarter/`, re-copy it to
  `~/.claude/skills/research-smarter/` so Claude Code uses the new version.

## When to stop and ask

Stop and report if something needs access you don't have (for example, an
org admin setting), if a requirement seems wrong, or if a fix would change
the skill's coaching flow.
