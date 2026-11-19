# Source library view (issue #3)

**Date:** 2026-11-18
**Page:** `notebook/notebook.html`, published privately at
https://claude.ai/artifact/NT8int2Sc3zA22P1AXcsha (version 4)
**SPEC:** R10.5, R2.4, R10.4 (and the start of R10.6)

## What was built

- **Tabs:** My Research and Sources (with a count). My Research shows a
  summary of the sources, with counts by reading status and how many aren't
  labeled yet.
- **A card for each source:** citation, link or DOI, the sub-question it
  helps with, and two choices the student makes:
  - **How far I've read it:** found, skimmed, read closely, or verified.
  - **Supports or complicates my position:** starts at "Not labeled yet".
- **Add a source:** a short form. A new source starts as "found" and
  unlabeled.
- **Remove:** asks the student to confirm first.
- **Read this source:** opens the Read a Source view. It's a placeholder
  until the Reader is built (issue #4); Back returns to the sources.
- **How edits are stored:** in the log's sources table, which gains a
  "Reading status" column. Only that table is rewritten; every other line
  of the log stays exactly as written.

## Results

| Acceptance check | Result | Evidence |
|---|---|---|
| Each source shows citation, link or DOI, status, and the student's own label | **Pass** | Example project and Noa's live project. A label the log records in the student's own words ("3 support, 2 complicate") is shown as written. |
| The notebook never sets supports or complicates itself | **Pass** | `test_sources.py`: a new source is unlabeled before and after saving, on all 9 example logs. Live: the added source showed "Not labeled yet" until Noa chose "supports". |
| Each source has a Read a Source button | **Pass** | Live: Read this source, then Back to the sources. Browser test at phone width: same. |
| Changes appear in the next saved log | **Pass** | Live: the stored notebook and the saved file have the source with "supports" and "skimmed". Every line outside the sources table matches the original log, and the saved file differs from the stored notebook only in "Last updated" (local date). |
| The skill reads the edited log | **Pass** | A fresh skill session correctly picked out the source marked "read closely" and the one the student labeled "complicates", and treated the labels as the student's own. |

**Automated tests:** `notebook/tests/test_sources.py` has 95 checks, all
passing, and `test_log_format.py` still passes. Editing sources keeps every
other line of the log, a citation containing `|` survives, writing the same
sources twice changes nothing, and saving an edited log changes only the
date.

### Checking the checks

| Deliberately broken copy | Checks that failed |
|---|---|
| New sources get labeled "supports" automatically | 18 |
| Citations containing `\|` aren't escaped | 36 |
| Blank lines elsewhere in the log are dropped | 9 |
| A missing reading status is filled in as "found" | 2 |

### Problems found and fixed during the build

1. **Invented reading status.** A row with no reading status was saved as
   "found". The skill then told the student that five sources they had
   already evaluated were "found, not read". The notebook had put a claim in
   the student's log they never made. Missing statuses now stay blank and
   show as "Not recorded" (version 4).
2. **Blocked view switching.** Views switched by changing the page address
   (`#sources`), which some viewers block, so the click did nothing. The
   page's own state now switches views, and the address follows where it's
   allowed (version 3).

## Live run (Noa, version 4)

1. The reopened notebook showed "Welcome back" and the Sources (0) tab.
2. Noa added a source, which showed "Not labeled yet".
3. Noa set it to Skimmed and Supports my position.
4. Both choices were still there after reopening the notebook.
5. Read this source, then Back, worked.
6. Saving the research log worked.

Stored data and the saved file were checked as described above. The save
dialog again chose the last folder used (this time the repo's top folder);
the file was moved out so it isn't committed.

## Not covered here

- **The Reader itself, and R10.6 from every view.** Both come with issue #4.
- **Second-person privacy and missing-capability messages.** Still open from
  issue #1.
