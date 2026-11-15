VERDICT: PASS
CONTENT-HASH: 6fc6fb8caaf31946
Review of the recognition chart (queue 9c) and the term change against the version passed at e8a6f31d617c0812; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- A: figure header says "mistä tunnistan lain?" but this unit's chart gives methods, and its aria-label says "menetelmää"; use "mitä menetelmää käytän?" (or keep "lain" in the figure and aria alike).
- B: aria-labels contain double spaces at line joins (harmless to screen readers).

## Checked
- Chart PNGs at 360 px (all units) and 1280 px (mittaaminen): no clipped, overlapping or cramped label; white on #1a4d2e legible; pill style and spacing identical across units; KaTeX subscripts, upright names, \overline vectors render correctly.
- Rows checked: toistettu mittaus, virhe, karkea, systemaattinen, suora, kulmakerroin, Δk (ääriviivat), s vs t². 
- ARIA_KARTTA (Finnish, in figures.py and unit.md) read against every row: same rows, same results, complete, right language.
- Diff of the remaining lines (term change, teacher.md/unit text, figure code): no regressions found.
