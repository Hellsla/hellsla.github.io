VERDICT: PASS
CONTENT-HASH: 9c0f11f51ee1c63c

## Blocking
- none

## Polish
- [Minor] exercises.json:259 — the formula block in the task text is centred at 1280 px while the blocks in the solutions are left-aligned; a template matter, no content change.

## Checked
- Delta (reflow). The packet's inventory has no phone-width capture of the opened exercise solutions, so own captures were made from preview/en/fy7-5.html (built after the content) with every exercise solution open at 390 and 1280 px: every solution step holding a display formula, opened at full size (sheets S5-390-1.png, S5-1280-1.png in the session scratchpad).
- Measured at both widths: no formula wider than its card, no page overflow, no KaTeX error, no raw LaTeX; no row starts inside a number, a power of ten or a unit.
- Task text of the find-the-error exercise (exercises.json:259): three aligned rows, the sentence continues below without stray punctuation.
- Trapezoid sum (solutions.md:201): breaks at + signs inside the bracket, readable at 390 px and joined to two rows at 1280 px.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
