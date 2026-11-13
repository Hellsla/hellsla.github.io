VERDICT: FAIL
CONTENT-HASH: fd34db779eea2d90

## Blocking
- [Major] guide.md, Tuloksen epävarmuus step 2 (page-390-3) — at 390 px the calculation lines are clipped at the right edge: "Δk = (4,21 − 3,89) s²/m : 2 = 0,16 s…" and "Δg ≈ 0,040 · 9,748 m/s² ≈ 0,39 m/s…" lose their last characters (unit and exponent), and these lines carry the result. A result cut off on a phone breaks the "nothing clipped" rule. At 1280 px they fit. — Fix: the shared mathlayout should break these chains inside list items (rows wrapping after an operator); if it does not, report it as a shared-component bug. Do not hand-split the chain.

## Polish
- [Minor] fig-1 (lines) — at 390 px the labels $k_\text{max}$, $k_\text{min}$ and $k$ are about 9–10 px, and the two dashed lines nearly coincide with the fitted line. A larger tilt difference and larger labels would help the point read.
- [Minor] fig-2-390 capture is a 28×28 empty image — a stray element after the figure? Check that there is no empty figure or unlabelled box.
- [Minor] guide.md step 2 "ohjelman m:n" — the plain m is a symbol in text; write $m$:n.
- [Minor] Step 2 of Tuloksen epävarmuus is one dense paragraph of five formulas; consider a separate line for each step (still one chain per step).

## Checked
- Opened: fig-1-390, page-390-1/2/3, page-1280-2, top-1280. Not opened separately: contact sheets, page-390-4/5, page-1280-1/3/4, top-390, fig-2-390 (judged from its 28×28 size in the inventory).
- The 1280 px layout, headings, the formula and the links read well. The decimal comma, \cdot, the colon for division and the units in LaTeX are consistent.

## Scores
illustrations 3 · typography 3 · Finnish 4 · accessibility 3
