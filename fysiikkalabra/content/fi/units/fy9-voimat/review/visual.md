VERDICT: PASS
CONTENT-HASH: 8fd79cadff819b5c
Review of the recognition chart (queue 9c) and the term change against the version passed at 8fb4b213f8bfbe4b; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- B: 'ΣF_i = m_i a_i' (row 4) has no \overline although rows 1-2 use vector form; as component/magnitude form it is acceptable, but a reader may wonder.
- B: aria-labels contain double spaces at line joins (harmless to screen readers).

## Checked
- Chart PNGs at 360 px (all units) and 1280 px (mittaaminen): no clipped, overlapping or cramped label; white on #1a4d2e legible; pill style and spacing identical across units; KaTeX subscripts, upright names, \overline vectors render correctly.
- Rows checked: all 9 rows incl. friction rows (liukukitka F_μ=μN, lepokitka F≤F_μ0, täysin kehittynyt lepokitka eli lähtökitka F_μ0=μ0 N); the wrapped 'eli lähtökitka' line at 360 px is legible. Changed terms liikekitka→liukukitka checked in the diff (inquiry, tasks, solutions): consistent, no leftover 'liikekitka'. 
- ARIA_KARTTA (Finnish, in figures.py and unit.md) read against every row: same rows, same results, complete, right language.
- Diff of the remaining lines (term change, teacher.md/unit text, figure code): no regressions found.
