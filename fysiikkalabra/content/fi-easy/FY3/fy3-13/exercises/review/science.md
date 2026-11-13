VERDICT: PASS
CONTENT-HASH: 5b2bbbf91992607b
SCOPE: delta added-exercise from 4bbd51e0c6f48c2d base 81db4a6fd727

## Blocking
- none

## Polish
1. content/fi-easy/FY3/fy3-13/exercises/solutions.md (fy3-13-L2-10, Periaate) — says "Pisteet ovat suoralla" while L2-09 now says "lähes suoralla" about the same figure; "lähes suoralla" here as well (the task's linearity assumption still carries the model).

## Checked
- Last round's Polish is fixed: the eye-fit ranges are now −260 … −286 °C (L2-09) and 53–57 kPa (L2-10). Both lie inside the ±5 % tolerance (own script: −259,1 … −286,4 °C; 52,14–57,63 kPa).
- L2-09: "lähes suoralla" in task and solution matches the figure. The middle points (82, 89, 96 kPa) are within 0,4 kPa of the line through (0 °C; 75 kPa) and (100 °C; 102,5 kPa), so this is not an exact fit (guardrail "Fits").
- L2-09 recomputed: k = 0,275 kPa/°C, θ₀ = θ₁ − p₁/k = −272,7 °C; answers.py −272,727 agrees. The uncertainty statement (about 10 °C or more) is consistent.
- L2-10 recomputed: θ = −73,15 °C, p = 75 + 0,275 · (−73,15) = 54,88 kPa; answers.py 54,884 agrees. The task states the condition that the model holds outside the measured range. The check against p ∝ T is independent.
- L1-09: θ₀ = −T₀ = −273,15 °C from MAFY 0 °C = 273,15 K; the reasoning (same degree size, shifted zero) is right.
- Figure fy3-3/extrapolation-points: gives every value needed, its description lists the same points, and neither gives θ₀ away.
- The other 21 exercises were not re-reviewed (unchanged, per the packet).
- Hash the same at start and end.
