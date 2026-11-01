VERDICT: FAIL
CONTENT-HASH: 50ba844bc762df91

## Blocking
1. [Major] `unit.md` figure `em`, `figures.py` `emtube()` (captures `stage-tutki-390-1`, `stage-tutki-1280-1`). The upper-right field marker ⊙ at (328, 108) sits on the arrowhead of $\overline{v}$ (308, 105). The $\overline{v}$ label (foreignObject x 320, y 102) is drawn over that marker, so at both widths the velocity label cannot be read. This is the only figure that shows the three vectors, so it matters. Fix: move that ⊙ to about (290, 62), clear of the arrow, the label and the beam, and regenerate.
2. [Major] `docs/fy14/fotoni-worksheet.md`, *Useful equations*. "Repeated readings: mean ± half of the range (largest − smallest)/2" says the half twice, so it can be read as range/4. The unit page says the half range is right. Fix: "Repeated readings: mean ± (largest − smallest)/2, that is, half of the range."
3. [Major] `teacher.md` *Printing the worksheet*. I printed the page to A4 (Chromium, print media). The worksheet starts in the middle of page 11, after the plan's model answer, and ends on page 14 next to the word bank. The tables keep their narrow screen width: the spectra and filament tables use about half the page, and the Group table about a third. The cells are too small to write in by hand. There is also no section to "open". The claim "prints cleanly on A4" is therefore wrong. Fix: tell teachers to print `docs/fy14/fotoni-worksheet.md`, or its PDF export, as the worksheet, and keep the page section for reading on screen. See shared issue 1.

## Polish
1. [Minor] Worked example, step 1 and step 7 (390). "$6.626 \cdot$ / $10^{-34}$" and "$6.1\text{–}6.7 \cdot$ / $10^{-34}$" break after the dot. Wrap each in braces and write the range as ${(6.1\ \text{to}\ 6.7) \cdot 10^{-34}\ \text{J} \cdot \text{s}}$.
2. [Minor] The `own-data` and `report-write` model answers, and the `report-order` item *Analysis*, break "$h = (6.4 \pm$ / $0.3)$" at 390. Use `{…}` braces as elsewhere.
3. [Minor] Formula section, *percentage difference*. "$\cdot 100\ \%$" goes on its own line even at 1280, where the expression fits on one line. Use ${\text{difference} = \dfrac{x - x_\text{acc}}{x_\text{acc}} \cdot 100\ \%}$ on one display line.
4. [Minor] Worksheet: the page and the md file differ. The md file has 5 position rows, a "Counts at different positions" heading and space under the magnet question. The page has 4 rows and no space. The oil-drop station has no research question in either. Align them.
5. [Minor] `teacher.md`, *Fast pairs*: "B²r²" in Unicode, while the rest of the teacher notes use LaTeX. Write $2U$ against $B^2r^2$.

## Checked
- All 85 captures were rebuilt and recaptured for this hash (page 6c9b02ec). I triaged them on contact sheets 1–8 and opened top-390, intro-1280, stage-tutki-390-1/5/6/7/8, tutki-1280-1, sovella-390-1/2, fx-5-390 and the teacher captures.
- `em` was zoomed at 390 and 1280. The force direction is correct (−e·v×B points to the centre).
- I measured the rendered label sizes. `em` is 23.9 px at 390 and 40.5 px at 1280; `fit` is 15.9 px at 390 and 23.2 px at 1280. `hero` has no text.
- I opened the worked example with all 7 steps at 390 and 1280. I also opened all six explain models after typing an answer, and the e/m and slit solutions.
- The page has no console errors, no `.katex-error` and no horizontal overflow at 390 or 1280.
- I printed the page to A4 (pages 11–14) and read the worksheet md file in full. The French respellings are consistent (ẽ õ ã nasal, ö, y).
- The hash was unchanged at the end.

## Scores
illustrations 3 · typography 4 · English 4 · accessibility 4

## Shared issues
1. `templates/site.css` `@media print`. Tables keep their screen width, and empty rows are short. Add `table{width:100%} td{height:1.1cm}` for print, and a `break-before:page` hook for a worksheet section.
2. `scripts/inquiry.py`. The criteria box links to `#exercises`, which a unit without exercises does not have (the developer reported this already).
