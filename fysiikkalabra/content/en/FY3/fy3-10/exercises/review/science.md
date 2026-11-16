VERDICT: PASS
CONTENT-HASH: 1d1d07f24a542ddf

## Blocking

## Polish
- lessons/FY3/fy3-10/answers.py:45 — the L1-07 comment ends "-> 2,31 l", but exercises.json and the solution give 2.3 l (two significant figures, limited by 98 kPa). Cosmetic: change the comment to "-> 2,3 l".

## Checked
- I recomputed all 22 numeric answers in one script with my own formulas (pV = nRT, the combined gas law, n = m/M, N = nN_A, and my own least-squares fit for L2-06). All match answers.py and exercises.json within tolerance.
- L2-06: my own least-squares fit gives k = 0.408 cm³/K and intercept 1.1 cm³, so n = 4.96 mmol. The slope is taken from points on the line, not raw points, as the guardrail requires. The reason the line passes through the origin is stated.
- L2-07: pV is 244 (A) against about 305 (B) kPa·l on every row, so B is the only correct option. Each distractor's feedback is right.
- L1-06, L1-08 and L2-08: exactly one option is correct in each. The feedback is physically right, including the Celsius-substitution distractor ("result too large").
- L3-03: the gauge-pressure difference cancels atmospheric pressure. Δm = 0.72 kg, and the 27 % / 30 % comparison is right.
- L3-04: n₁ = 12.29, n₂ = 9.00 and n₃ = 5.32 mol, giving 27.9 g. Balloons: 15.9 + 17.8 = 33.7, with 21.7 left. The cold-gas argument against using the pressure difference (25 g) is correct.
- L3-05: n = 105.4 mol, V₁₀ = 7.38 m³, V₁₅ = 15.69 m³ and h ≈ 12.8 km. "The real limit is slightly higher" is correct, because V(h) is convex (pressure falls exponentially above 11 km). The ICAO values are right.
- L2-03: 828 K = 555 °C is plausible for a compression ratio of 16.7. L2-01: 180 bar, and the remark that a real gas deviates by a few per cent at this pressure is fair.
- `fy3-10/pt-suorat`: the grid points (200; 50/30) and (400; 100/60) give Δn = 0.024 mol and a ratio of 1.67. The description matches the drawing and gives no amounts of substance.
- Ideal-gas assumptions are stated wherever high pressure is involved (L1-09, L2-01, L2-04, L3-04). Absolute pressure is used in pV = nRT throughout.
