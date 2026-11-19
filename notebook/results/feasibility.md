# Feasibility check (issue #1)

**Date:** 2026-11-18
**Question:** Can a published Claude page do the three things the Research
Notebook and Reader depend on: ask Claude (the Reader's coach), keep a
private record for each student, and save a research log file?
**Answer:** Yes, for the owner signed in to Claude. Two checks are still
open (below).

## How it was tested

- Test page: `notebook/tests/feasibility-page.html`, published privately at
  https://claude.ai/artifact/SBJhwFT9T8ndmBNnybBCog (version 1). It declares
  four page capabilities: asking Claude, a data store, the viewer's
  identity, and file saving.
- Noa opened the page in Claude, signed in as its owner, clicked each check
  once, and reloaded.
- Claude then read the stored data directly and checked the downloaded file.

## Results

| Check | SPEC | Result | Evidence |
|---|---|---|---|
| Ask Claude from the page | R11 (coach) | **Works** | Card 1 showed "Works" and the reply "Reader coach online." Claude asked for permission on the first call. |
| Save a private record and read it back | R10.2 | **Works** | The note was stored in Noa's private space (`data/users/<id>/probe`): `"Feasibility test note"`, saved 2026-11-19 02:35 UTC. The page read it back, and it appeared again after a reload. |
| Record is private | R10.2 | **Partly verified** | The note doesn't appear in the page's shared data. The platform documents each viewer's `data/users/<id>/` space as private, even from the page owner. **Not tested** with a second person's account. |
| Save a Markdown file | R10.4 | **Works** | `research-log-test.md` (128 bytes) arrived in Downloads with the expected research-log header. |
| Plain message when a capability is missing | R10.7 | **Not tested** | The page has a message for each missing capability, but nobody opened it signed out or declined a permission. |

## Findings to carry into the build

1. **Dates.** The saved file said "Last updated: 2026-11-19" while it was
   still November 18 locally, because the page used UTC time. The notebook
   must write the student's local date into the research log.
2. **Who can use the notebook.** Saving to a private space needs a signed-in
   viewer with at least Contributor access to the page. Asking Claude spends
   the viewer's own Claude usage and asks their permission first. So a
   student needs a Claude account and access to the shared notebook. People
   outside the organization get read-only access and can't save. This is a
   real limit on sharing beyond the course, and belongs in the SPEC's known
   issues.
3. **Permission prompts.** The first Claude call and each file save ask the
   viewer to confirm. The Reader should tell students to expect this the
   first time.

## Decision for issues #2–#5

Build option A as planned:
- The Reader's coach runs from the page.
- Each student's record lives in their private space.
- Research logs are saved as Markdown files.

The companion-skill fallback (option B) isn't needed.

**Still to do:**
- Test the two open checks during the first real-user trial: a second
  person's privacy, and the signed-out or declined-permission message.
