VERDICT: PASS
CONTENT-HASH: 28edfef6c272a14b

## Blocking
(none) The three earlier blocking findings are resolved:
- **e/m figure.** The field marker moved to (290, 62) and $\overline{B}$ now sits beside it. At 390 and 1280, $\overline{v}$ and its arrowhead are clear.
- **Worksheet md.** The repeated-readings line now reads "Δx of one reading ≈ (largest − smallest)/2, that is, half of the range". The page says the same.
- **Printing.** `teacher.md` now sends teachers to `docs/fy14/fotoni-worksheet.md` for printing. It says the page section is for the screen and that its tables print narrow.

## Polish
1. [Minor] The Lesson 2 fold (`inquiry.json`, `theory-main`) says "after the visit" three times: the tag "Lesson 2: after visit", the summary "After the visit: open in lesson 2" and the heading "After the visit: what the stations show". The tag also lacks an article. Fix: tag "Lesson 2"; summary "After the visit: what the stations show".
2. [Minor] Page worksheet: the first column of the new e/m observation table wraps to two lines at 390. That is acceptable. On paper, the md file is the reference.
3. [Minor] The `em` sketch is 608 px wide at 1280, large for a simple diagram. It could be capped at about 420 px. Optional.

## Checked
- All captures were rebuilt for this hash (page a9ac09c5, after 903608be). I triaged them on the contact sheets and opened tutki-390-1 and tutki-1280-1 (the `em` figure, zoomed) and selita-390-1 (the fold opened).
- I also opened sovella-390-1 (the percentage difference is now on one display line) and ws-390, the worksheet section with the new observation table and the position-count heading.
- I captured the Lesson 2 fold closed next to an Optional box at 390 and 1280. The solid tag and the green frame set it clearly apart from the dashed Optional boxes.
- Worked example: all 7 steps at 390 and 1280. Steps 1 and 7 no longer break inside $6.626 \cdot 10^{-34}$ or $(6.1\ \text{to}\ 6.7) \cdot 10^{-34}$.
- Model answers: all six opened after typing an answer. `own-data` and `report-write` keep $(6.4 \pm 0.3) \cdot 10^{-34}\ \text{J} \cdot \text{s}$ on one line.
- The e/m and slit solutions are open.
- Label sizes: `em` 23.9 px at 390 and 40.5 px at 1280; `fit` 15.9 px at 390 and 23.2 px at 1280. `hero` has no text.
- The page has no console errors, no `.katex-error` and no horizontal overflow at 390 or 1280.
- I read `docs/fy14/fotoni-worksheet.md` in full: the oil-drop research question and the beam observations are now there. `teacher.md` printing and timings read well.
- The hash was unchanged at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Shared issues
1. `templates/site.css` `@media print`: when a page is printed, its tables keep their screen width and empty rows are short. This no longer blocks this unit, because printing goes through the md file.
2. `scripts/inquiry.py`: the criteria box links to `#exercises`, which a unit without exercises does not have.
