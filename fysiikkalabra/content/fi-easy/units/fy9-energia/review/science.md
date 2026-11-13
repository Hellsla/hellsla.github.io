VERDICT: PASS
CONTENT-HASH: db991bf31ee21542
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at ec7935cf8a9a834b.

## Blocking
(none)

## Polish
1. fy9-energia-s4 a) (wind): $k$ now names the capacity factor $0{,}30$, while the heating task fy9-energia-s3 uses $k$ for the slope. Separate tasks, so not a clash; $\varepsilon$ or $C_\text{f}$ would read more clearly.

## Checked
Every hunk of the fi-easy merge diff for this unit: the new symbolic steps (solving for the asked quantity before numbers) against the existing substitutions, answers and unit formula names/notation of #522; LaTeX balanced. Content hash recomputed with scripts/units.py (matches). Recomputed: point-slope $E = 93 + (-4{,}9)(-28 - 0) = 230{,}2\,\text{kWh}$; $T = (E_\text{muu} - E_0)/k = 16{,}5\,{}^\circ\text{C}$ (with $T_0 = 0$ the d-part's $E = E_0 + kT$ is the same line); wind $0{,}30 \cdot 2 \cdot 1{,}0\,\text{MW} \cdot 8760\,\text{h} = 5{,}3\,\text{GWh}$.
