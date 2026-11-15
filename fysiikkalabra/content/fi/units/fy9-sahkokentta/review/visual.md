VERDICT: PASS
CONTENT-HASH: b06b70d01d7351bf
Review of the recognition chart (queue 9c) and the term change against the version passed at 31c49fc33ef52617; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- B: the first pill F_E = kQ1Q2/r² fills its box almost edge to edge at 360 px (tight but not clipped); the symbol E means field strength in row 2 and energy in row 7 within one chart (MAFY usage, a reader may pause).
- B: aria-labels contain double spaces at line joins (harmless to screen readers).

## Checked
- Chart PNGs at 360 px (all units) and 1280 px (mittaaminen): no clipped, overlapping or cramped label; white on #1a4d2e legible; pill style and spacing identical across units; KaTeX subscripts, upright names, \overline vectors render correctly.
- Rows checked: Coulomb, E=F_E/Q, U=Ed, QU=½mv², Q=CU, C=ε0εr A/d, E=½CU², ΣΔV=0. 
- ARIA_KARTTA (Finnish, in figures.py and unit.md) read against every row: same rows, same results, complete, right language.
- Diff of the remaining lines (term change, teacher.md/unit text, figure code): no regressions found.
