VERDICT: PASS
CONTENT-HASH: 14be3bd2753d402e

Pedagogy re-review of fy14-iter-video (2026-11-01) after the "Fixes after review" in review/developer.md (commit c6532e4f). Rebuilt and tested in Playwright over HTTP at 390 px. The brief's before / while / after structure is still complete.

## Earlier findings
- **Old Blocking 1 is resolved.**
  - `sort-claims` and `sponsor` now come in Investigate, after frame 4 and before `theory-checked`. The prompt sends students to their notes, the first two units and iter.org.
  - The table follows as evidence. Its verdicts use exactly the sort's three categories, and the "35 nations" item was added to both.
- **Old Blocking 2 is resolved.** The `pred-date` options are bare years (2025 / 2030 / 2034 / 2039), and the reasoning appears only in the feedback.
- **Polish 3–5 are done.**
  - `pred-focus` says "from the channel and the sponsor alone".
  - The page and `teacher.md` agree that each student writes all four frames and that pairs share the listening.
  - The media unit's duplicate date prediction is gone. `pred-date` is kept as the coordinator asked; it tests what a 2022 source said, not the plan itself.
- Both predictions lock with no feedback and open at `theory-checked`.
- All 8 model answers stay closed until the student writes.
- No console errors.

## Polish (not blocking)
1. The Why line ("useful and out of date") still hints that the video's date is old. This is acceptable now that the options are bare years. It could be phrased more neutrally ("Why can a popular video about ITER be useful even years later?").
