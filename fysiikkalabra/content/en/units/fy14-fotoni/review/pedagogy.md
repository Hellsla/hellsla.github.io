VERDICT: PASS
CONTENT-HASH: 9e9b8ad627a9f572

Pedagogy re-review of fy14-fotoni (2026-11-01) after commit ba3f91b8 ("Fixes after review" in review/developer.md). I rebuilt the page and tested it in Playwright at 390 and 1280 px.

## Earlier findings: all resolved
1. Old Blocking 1 is resolved: the results no longer open before the visit.
   - `theory-main` (Evidence and Key idea) is now inside a closed box, *Lesson 2: after visit*.
   - With the box closed and its heading on screen, none of the four committed predictions shows feedback, and the results text is hidden.
   - After a reload the predictions stay locked and their feedback stays closed.
   - Opening the box reveals each prediction's own feedback.
   - Each prediction now says where its feedback opens: "…with the box 'Lesson 2: after visit' in the Theory summary, after the Fotoni visit."
2. Lesson 2 now fits in 75 minutes:
   - `em-task` is optional and listed under fast pairs;
   - Apply has 25 minutes;
   - the French corner is "if time allows" and is in the running-out-of-time plan.
3. Printing: teacher.md now sends the teacher to `docs/fy14/fotoni-worksheet.md`, exported as PDF. The page section is for screens and laptops.
4. Lesson 1, 20–40 min, now includes the required double-slit video and the recommended photoelectric video (or the latter as homework).
5. The e/m worksheet has observation rows for prediction 2 ("U kept the same, coil current up") and for its control case, on the page and in the md file.
6. `report-order` no longer labels the parts. The prompt points students to tense and content as clues.

## Polish (not blocking)
1. `templates/lesson.js` opens every `<details>` on `beforeprint`, so the *Lesson 2: after visit* box opens if someone prints the page in lesson 1. The printed copy then shows the results. teacher.md already advises against printing the page. A shared fix would be to skip `details[data-type=theory]` folds of this kind on `beforeprint`.
2. The box *Lesson 2: after visit* uses the same tag style as "Optional" boxes. A student could take the after-visit summary as optional. A distinct style, or a lead line "Required in lesson 2", would help.

## Checked
- The split is clear for the teacher. Lesson 1, the visit and lesson 2 each map to named page sections, with timings, a plan for fast pairs and a plan for running out of time.
- Predictions lock on commit.
- The model answer of every explain task stays closed until the student writes a sentence.
- Plain choices give per-option feedback.
- The numerics give their mistake feedback.
- The worked example opens step by step.
- check_layout reports OK at 360 and 1280 px.
- No console errors, no raw `$`, no `.katex-error`.

## Shared issues
- `templates/lesson.js` `beforeprint`: see Polish 1.

Re-check 2026-11-01: typography-only change to hint 3 (inline $B^2r^2$ formula can now wrap); no change to meaning or pedagogy.

Hash updated 2026-11-01 for a photo-only change; per the teacher, photo changes get a visual review only.
