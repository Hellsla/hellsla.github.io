VERDICT: PASS
CONTENT-HASH: 22507547242a4988
Review of the recognition chart (queue 9c) and the term change against the version passed at c744b5e13b28d510; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- B: pills on their own line vs beside the arrow vary between rows (by width only); acceptable, same pill style.
- B: aria-labels contain double spaces at line joins (harmless to screen readers).

## Checked
- Chart PNGs at 360 px (all units) and 1280 px (mittaaminen): no clipped, overlapping or cramped label; white on #1a4d2e legible; pill style and spacing identical across units; KaTeX subscripts, upright names, \overline vectors render correctly.
- Rows checked: all 8 rows; two-line pills (E_p0+E_k0=E_p+E_k, p_ennen=p_jälkeen, ...) sit right-aligned on their own line without clipping at 360 px. 
- ARIA_KARTTA (Finnish, in figures.py and unit.md) read against every row: same rows, same results, complete, right language.
- Diff of the remaining lines (term change, teacher.md/unit text, figure code): no regressions found.
