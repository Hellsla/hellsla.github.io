VERDICT: FAIL
CONTENT-HASH: 50ba844bc762df91

Pedagogy review of fy14-fotoni (2026-11-01). Page rebuilt and tested in Playwright at 390 px, the print layout checked as A4 PDF.

## Blocking
1. `unit.md` {Evidence} / `inquiry.json` `theory-main`: the visit's results and all four prediction feedbacks open **before the visit**. The section *After the visit: what the stations show* follows the worksheet directly on the same scrolling page. In Playwright, scrolling about 300 px past the last worksheet table (`record-help`) brought `theory-main` on screen and revealed `pred-current`, `pred-radius`, `pred-photons` and `pred-peak`. Students do this in lesson 1 (60–75 min, worksheet open) or on their laptops at Fotoni. Their own measurement is then no longer the evidence. Fix: put Evidence + Key idea in a closed fold ("After the visit: open in lesson 2"), like the Predict fold, so that the reveal fires only when the fold is opened. Do not rely on teacher.md's "students should not open the second half".

## Polish
2. `teacher.md`, lesson 2 workload: in 15–35 min students do the formula, a 7-step worked example, a spreadsheet fit with Δh **and** `em-task`, and in 65–75 min three checks, an argue task, the summary and the French corner. That is about 1,260 words of reading and four writing tasks. Make `em-task` optional or a fast-pairs task, give Apply 25 min, and move the French corner to the "running out of time" list.
3. `teacher.md` "Printing the worksheet": printing "the pages that contain it" from the page also prints the planning task and the start of the Evidence section. On A4 the worksheet runs over pages 10–14, "Group" and "Oil drops" are cut from their tables, and the cells are content-width. Make `docs/fy14/fotoni-worksheet.md` (or a PDF of it, linked from teacher.md) the primary route.
4. `teacher.md` lesson 1: Fotoni requires the double-slit video (7:25) and recommends the photoelectric one (5:30). Neither is in the timings. Put them in 20–40 min or set them as homework.
5. Worksheet, e/m station: prediction 2 has no observation prompt. Add the row "U kept the same, coil current increased → what happened to r?", in the same form as the photoelectric observation table.
6. `report-order`: each sentence starts with its part name (*Aim:*, *Method:* …), so the task is a copy of the list just read. Remove the labels, so that students sort by content and tense.

## Checked
The split is clear: lesson 1, the visit and lesson 2 are each mapped to page sections. Predictions lock on commit with no feedback, and each option has its own feedback. All six explain models stay closed until the student writes a sentence. Both numerics give their mistake feedback. The steps of the worked example open one at a time. Option lengths are within ±30 %. Every writing task has sentence starters. No console errors, no raw `$`, 360 px layout OK.

## Shared issues
- `templates/inquiry.js`: the pending text "Feedback appears when you have read the theory section" misleads in a lab unit. Allow a per-prediction pending text (here: "…after the visit, in *Theory summary*").
