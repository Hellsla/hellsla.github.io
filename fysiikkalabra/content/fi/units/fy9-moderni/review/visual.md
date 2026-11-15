VERDICT: PASS
CONTENT-HASH: 84c1d79c5900ea6f
Review of the recognition chart (queue 9c) and the term change against the version passed at dc13071f6130e116; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- B: in 'Ḣ ∝ 1/r²' the dot over H and the subscripts (E_y, E_a, w_R) render upright and clear at 360 px; no change needed. Optional: the pill 'N = N_0 e^{−λt}' is the only one with an exponent-only subscript clash with N_0 - fine.
- B: aria-labels contain double spaces at line joins (harmless to screen readers).

## Checked
- Chart PNGs at 360 px (all units) and 1280 px (mittaaminen): no clipped, overlapping or cramped label; white on #1a4d2e legible; pill style and spacing identical across units; KaTeX subscripts, upright names, \overline vectors render correctly.
- Rows checked: E=hf, hf=W+E_k, hf=E_y−E_a, hajoamislaki, A=λN, E=Δmc², H=w_R D, Ḣ∝1/r², I=I0 e^{−μx}. 
- ARIA_KARTTA (Finnish, in figures.py and unit.md) read against every row: same rows, same results, complete, right language.
- Diff of the remaining lines (term change, teacher.md/unit text, figure code): no regressions found.
