VERDICT: FAIL
CONTENT-HASH: a8679ac7293e5321

## Blocking
- [Major] fy5-16 exercises, solutions.md fy5-16-L3-01 Substitution (changed line) — at 390 px "Dose $= \left(\dfrac{4.0\,\text{h}}{4.0\,\text{h}} + \dfrac{4.0\,\text{h}}{16\,\text{h}}\right) \cdot 100\,\% = (1 + 0.25) \cdot 100\,\% = 125\,\%$" is one inline formula 496 px wide in a 304 px scroller (own capture): the view ends at "= (1 +", so the result 125 % is hidden — write it as a chain with a symbol on the left, e.g. "the dose $D = \dfrac{4.0\,\text{h}}{4.0\,\text{h}} + \dfrac{4.0\,\text{h}}{16\,\text{h}} = 1 + 0.25 = 1.25 = 125\,\%$", which mathlayout breaks into rows.

## Polish
- [Minor] solutions.md fy5-16-L2-05 Reading the table (untouched) — "$\Delta L_1 = … = 15.9\,\text{dB}$" and "$\Delta L_2 = … = 40.1\,\text{dB}$" overflow by about 15 px and clip the unit of the result at 390 px — give each its own chain (or shorten the lead-in) so mathlayout breaks it.

## Checked
- light delta review (teacher 2026-11-07), after fixes: exercise diff (L1-01, L2-01, L3 error task, feedback text, t_ref fractions); own 390 px scan of preview/en/fy5-16.html with every solution open: no inline formula wraps; three scrolling inline formulas, captured and opened (L3-01 dose line, L2-05 ΔL lines).
