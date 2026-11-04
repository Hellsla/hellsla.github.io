VERDICT: PASS
CONTENT-HASH: 981a7d725fe69627

## Blocking
(none)

## Polish
- [Minor] solutions.md — earlier note: other untouched inline formulas break; measured now, in the exercises only `m_\alpha = 6{,}645 \cdot 10^{-27}\,\text{kg}` (L3-03, at 360, 390 and 1280 px) and `m = 1{,}673 \cdot 10^{-27}\,\text{kg}` (L2-04, 360 px) — brace them the same way, `${m_\alpha = 6{,}645 \cdot 10^{-27}\,\text{kg}}$`. (`q = e = …`, `2e = …`, `1\,\text{u} = …` break in the lesson text, see review/visual.md.)
- [Minor] solutions.md — long substitution chains (L1-01, L1-05, L2-02) shown as eq-chain rows still break inside a row at 360/390 px (by design of mathlayout.py); if the teacher's never-wrap rule covers chain rows too, split them at meaningful boundaries.

## Checked
- Follow-up of the FAIL on L1-02 Annettu: `${|q| = e = …\,\text{C}}$` is now braced. `build.py fy7-2` (exercises from the working tree), then every inline .katex measured with getClientRects().length at 360, 390 and 1280 px, every level and solution open: the formula is ONE line at all three widths (also in fi, en and fi-easy). Captures opened: own element captures of the Annettu paragraph at 360, 390 and 1280 px (scratchpad caps/fi-fy7-2-*): `|q| = e = 1,602 · 10⁻¹⁹ C,` stays together with its comma; no clipping, no overflow.
- `screenshot.py fy7-2 --if-stale`: fresh captures; diff of solutions.md read (only the braces changed).
- Earlier: Delta: changed lines of L1-02 (Annettu, Kaava `|q|vB = \dfrac{mv^2}{r}`, `r = \dfrac{mv}{|q|B}` at 390 px, capture ex-390-0: fractions and bars read correctly) and the chapter-reference edits in L2-03 and L3-02 (plain italic text, no layout effect). Measured every inline formula of the built page at 360, 390 and 1280 px for line breaks; only the L1-02 Annettu line is new.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
