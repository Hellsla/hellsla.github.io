VERDICT: FAIL
CONTENT-HASH: dc30a3e24eb0b99d

Pedagogy review of fy14-iter-video (2026-11-01) against the brief's ITER video assignment. Tested in Playwright over HTTP at 390 px:
- both predictions lock on commit with no feedback and open at `theory-checked`, after the four note frames;
- all 8 model answers stay closed until the student writes;
- no console errors.

The brief is covered:
- **Before watching:** vocabulary match and two predictions.
- **While watching:** four frames (main ideas, technical concepts, collaboration, construction).
- **After watching:** comprehension checks 1–3, pair discussion, source evaluation (sort + sponsor) and the 80–100-word explanation.
- The supplementary videos were evaluated in `teacher.md`.

## Blocking
1. **The source evaluation is done for the student.**
   - `theory-checked` (in Investigate, before Apply) is a finished claim-by-claim table with a **Verdict** column.
   - `sort-claims` then asks the student to sort the same claims "Use the table above". The answers are on screen before the student acts.
   - So learning goal 2, "check the claims of a video against current primary sources", is never practised.
   - Fix:
     - Move `sort-claims` (and the `sponsor` choice) into Investigate, right after `frame-build` and before `theory-checked`.
     - Change its prompt to "Use your notes, what you know from the chapter's first two units, and iter.org's Facts page".
     - Keep the table after it as the evidence that checks the student's sort and opens the predictions.
     - Align the table verdicts with the three sort categories. "half true", "true then, count changes" and "unclear wording" are not options in the sort.
2. **`pred-date` gives its answer in the options.** "2025, **the plan of that time**" against "2034, the date of today's plan" tells the student which one a 2022 video would give. The Why line ("useful and out of date") points the same way. Fix: drop the explanations from the options and keep only the years, for example "2025" / "2030" / "2034" / "no date given". Give the reasoning only in the feedback.

## Polish
3. `pred-focus`: the prompt itself says "a channel about construction … a company that manages contracts", which nearly answers the question. This is acceptable as practice in predicting from author and purpose, but say so in the prompt ("From the channel and the sponsor alone, predict …").
4. `teacher.md` asks one pair member to fill frames 1–2 and the other 3–4. On the page, each student must write in all four frames to open the models. Either say on the page "your pair can split the frames", or change the teacher plan.
5. The same prediction (old date vs 2024 baseline) also appears in fy14-iter-project and fy14-iter-media. Three times in one chapter is too many: keep it in at most one unit.

## Checked
- Word bank and sentence starters for the pair task, the written explanation, check 4 and the optional comparison.
- Option lengths are balanced and the correct option varies in place.
- The French corner is present.
- `teacher.md` is honest that the narration was verified from The B1M's own page, and it gives the teacher a checklist to watch for. The click-to-load player has a note on subtitles.
- The timing (two viewings within 25 minutes) is realistic.

## Shared issues
- None new.
