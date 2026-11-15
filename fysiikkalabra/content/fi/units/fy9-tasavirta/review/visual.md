VERDICT: PASS
CONTENT-HASH: ed63c3e5b1928717
Review of the recognition chart (queue 9c) and the term change against the version passed at f131fb403db2206f; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- B: 1/R_kok = Σ1/R pill is the widest in the chart and nearly fills the row; not clipped.
- B: aria-labels contain double spaces at line joins (harmless to screen readers).

## Checked
- Chart PNGs at 360 px (all units) and 1280 px (mittaaminen): no clipped, overlapping or cramped label; white on #1a4d2e legible; pill style and spacing identical across units; KaTeX subscripts, upright names, \overline vectors render correctly.
- Rows checked: I=ΔQ/Δt, U=RI, R=ρℓ/A, R_kok=ΣR, 1/R_kok=Σ1/R, ΣI_t=ΣI_l, ΣΔV=0, P=UI, U=E−R_sI. 
- ARIA_KARTTA (Finnish, in figures.py and unit.md) read against every row: same rows, same results, complete, right language.
- Diff of the remaining lines (term change, teacher.md/unit text, figure code): no regressions found.
