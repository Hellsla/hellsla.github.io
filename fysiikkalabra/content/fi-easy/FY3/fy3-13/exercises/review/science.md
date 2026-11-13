VERDICT: PASS
CONTENT-HASH: 595b3e4cd6e503dd
SCOPE: delta added-exercise from 4bbd51e0c6f48c2d base 89bcb63b7431
Mode: delta (added exercises fy3-13-L1-09, fy3-13-L2-09, fy3-13-L2-10)
Round: 1

## Blocking
(none)

## Polish
- solutions.md fy3-13-L2-09 / L2-10 — the accepted eye-fit ranges (−259 … −286 °C; 52–58 kPa) end just outside the ±5 % tolerance (−259,1 … −286,4 °C; 52,1–57,6 kPa). A fix: say −260 … −286 °C and 52–57 kPa, or widen the tolerance a little (and the same in the Finnish).

## Checked
- L1-09: T = θ + T₀ with T₀ = 273,15 K (MAFY); θ₀ = −273,15 °C; the reasoning (same degree size, shifted zero) is right; the large tolerance does no harm.
- L2-09: rigid closed vessel; line through (0 °C; 75 kPa) and (100 °C; 102,5 kPa), k = 0,275 kPa/°C, θ₀ = −272,7 °C; the middle points (82, 89, 96) lie on it within 0,4 kPa; the uncertainty statement (about 10 °C or more from about 1 kPa reading) is consistent with Δk/k ≈ 5 %.
- L2-10: linear model assumed outside the range in the task (condition stated, B satisfied); θ = −73,15 °C, p = 54,88 kPa; check p ∝ T gives 54,9 kPa.
- Figure extrapolation-points: to scale, axis to −150 °C, description lists the points and not θ₀.
- Solutions complete, symbolic first, conversions right.
- answers.py matches my recomputation (−273,15; −272,727; 54,884).
- Scripted comparison with the Finnish: answer, unit, tolerance, figure, lookup and all numbers identical.
- Hash the same at start and end.
