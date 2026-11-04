VERDICT: PASS
CONTENT-HASH: 208276c111678272

## Blocking
(none)

## Polish
- [Minor] solutions.md — L1-02 now writes $|q|vB = \dfrac{mv^2}{r}$, $r = \dfrac{mv}{|q|B}$ but other magnetic-force solutions (L1-01, the proton period, the selector) still use $q$ while the lesson uses $|q|$ — notation consistency only (for science: whether they should follow).
- [Minor] solutions.md (untouched) — `m_\alpha = 6{,}645 \cdot 10^{-27}\,\text{kg}` (L3-03) breaks at 360, 390 and 1280 px, `m = 1{,}673 \cdot 10^{-27}\,\text{kg}` (L2-04) at 360 px — brace each as one group `${...}$`, as in L1-02.
- [Minor] solutions.md — long substitution chains (L1-01, L1-05, L2-02) shown as eq-chain rows still break inside a row at 360/390 px (by design of mathlayout.py); if the teacher's never-wrap rule covers chain rows too, split them at meaningful boundaries.

## Checked
- Follow-up of the FAIL on L1-02 Annettu: `${|q| = e = …\,\text{C}}$` is now braced. `build.py fy7-2` (exercises from the working tree), then every inline .katex measured with getClientRects().length at 360, 390 and 1280 px, every level and solution open: the formula is ONE line at all three widths (also in fi, en and fi-easy). Captures opened: own element captures of the Annettu paragraph at 360, 390 and 1280 px (scratchpad caps/fi-easy-fy7-2-*): `|q| = e = 1,602 · 10⁻¹⁹ C,` stays together with its comma; no clipping, no overflow.
- `screenshot.py fy7-2 --lang fi-easy --if-stale`: fresh captures; diff of solutions.md read (only the braces changed).
- Earlier: Delta: diff of solutions.md read (L1-02 Given/Formula with $|q|$, two chapter names). / Opened open-exercises-1280-1 and -2 (2-1 and 2-2 solutions, every block open): $|q|$ renders in KaTeX, rows aligned, nothing clipped, no overflow; no exercise text or figure changed.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
