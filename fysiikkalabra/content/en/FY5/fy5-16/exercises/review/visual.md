VERDICT: PASS
CONTENT-HASH: 5575f15b7bd4bcfd

## Blocking
(none)

## Polish
- [Minor] solutions.md fy5-16-L2-05 Reading the table (untouched) — "$\Delta L_1 = … = 15.9\,\text{dB}$" and "$\Delta L_2 = … = 40.1\,\text{dB}$" overflow by about 15 px and clip the unit of the result at 390 px — give each its own chain (or shorten the lead-in) so mathlayout breaks it.
- [Minor] solutions.md fy5-16-L3-01 Formula — the Formula line still writes "dose $= (\dots) \cdot 100\,\%$" while the Substitution now introduces $D$ without the factor $100\,\%$ — name it $D$ in the Formula too, e.g. "dose $D = \dfrac{t_1}{t_{\text{ref},1}} + \dfrac{t_2}{t_{\text{ref},2}}$, as a percentage".

## Checked
- light delta review (teacher 2026-11-07), after fixes 2: own 390 px (2×) capture of fy5-16-L3-01 Substitution with every box open in preview/en/fy5-16.html — "The dose" then an aligned chain D = 4.0 h/4.0 h + 4.0 h/16 h = 1 + 0.25 = 1.25 = 125 %, fully visible, no scroller, result in view; no inline formula in L3-01 wider than the column; page scrollWidth 390.
