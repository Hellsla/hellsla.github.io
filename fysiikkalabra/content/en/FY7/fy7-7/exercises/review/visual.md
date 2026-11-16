VERDICT: FAIL
CONTENT-HASH: 20765954e1e52615

## Blocking
- [Major] content/en/FY7/fy7-7/exercises/exercises.json:271 (fy7-7-L2-07, both widths) — the quotation now ends on a display block, so the closing `.”` is left alone on a line of its own under the formula — a stray punctuation line in a task statement that was clean before the reflow — let words follow the block, e.g. “… The current is $$…$$ in the bulb.”
- [Major] content/en/FY7/fy7-7/exercises/solutions.md:113 and :134 (390 px) — the row `&\cdot 100\,\% = 26.97\,\%` (and `= 2.44\,\%`) carries the relation in mid-row; the page aligns its `=`, so `·100 %` hangs left of the equals column and the row reads as an equation of its own, `·100 % = 26.97 %` — the relation must start a row — `&= \dfrac{…}{…} \cdot 100\,\% \\ &= 26.97\,\%` (the first row fits a phone card).

## Polish
- [Minor] solutions.md:132 — the same formula: `· 100 %` on its own row, left of the `=`, also at 1280 px; keep `\cdot 100\,\%` on the fraction row.
- [Minor] solutions.md:228 — “$2.0\,\text{mV}$ in the fast push …” reads as a fragment after the boxed value; acceptable.

## Checked
- Delta (reflow). The packet's inventory has no phone-width capture of the opened exercise solutions, so own captures were made from preview/en/fy7-7.html (built after the content) with every exercise solution open at 390 and 1280 px: every solution step holding a display formula, opened at full size (sheets S7-390-1.png, S7-1280-1.png in the session scratchpad).
- Measured at both widths: no formula wider than its card, no page overflow, no KaTeX error, no raw LaTeX; no row starts inside a number, a power of ten or a unit. One punctuation orphan found by scanning the built page: fy7-7-L2-07.
- Reflow: L1-01, L2-01, L2-02, L2-04, L2-06 and the task text of L2-07 at both widths.
- New exercise fy7-7-L2-08 in full at 390 px (N7-390-1/2.png) and 1280 px (N7-1280-1.png): source line (PhET link, reading date), parts a)–d), answer box, every solution step. Typography and English are sound; $e_\text{ka}$ follows the chapter's own notation.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 5
