VERDICT: PASS
CONTENT-HASH: bc9cdc28a007fde8
Review of the recognition chart (queue 9c) and the term change against the version passed at add641812b74c0f3; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- A: row 'kaarre tasaisella tiellä → kitka kaartaa, F_μ = mv²/r': in FY9 F_μ = μN now means liukukitka (voimat chart), while the unit's own text says the tyres do not slip (lepokitka). Show it as 'lepokitka kaartaa' (and F = mv²/r or F ≤ F_μ0) so the term and symbol do not contradict the changed friction terms. For science.
- B: ΣF = ma_n lacks \overline (voimat chart writes ΣF̄ = ma̅); consistent use would help.
- B: aria-labels contain double spaces at line joins (harmless to screen readers).

## Checked
- Chart PNGs at 360 px (all units) and 1280 px (mittaaminen): no clipped, overlapping or cramped label; white on #1a4d2e legible; pill style and spacing identical across units; KaTeX subscripts, upright names, \overline vectors render correctly.
- Rows checked: ΣM=0, a_n=v²/r, v=ωr, ΣF=ma_n, F_μ=mv²/r, gravitaatiolaki, mg=γMm/r², γMm/r²=mv²/r. 
- ARIA_KARTTA (Finnish, in figures.py and unit.md) read against every row: same rows, same results, complete, right language.
- Diff of the remaining lines (term change, teacher.md/unit text, figure code): no regressions found.
