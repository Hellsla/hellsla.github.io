VERDICT: PASS
CONTENT-HASH: 6b0d9bd95acee718
SCOPE: delta added-exercise from b38642a6e641d4f2 base 81db4a6fd727

## Blocking
- none

## Polish
1. content/fi/FY3/fy3-13/exercises/solutions.md:271 (L2-10, Periaate) — the solution still says "Pisteet ovat suoralla". The task itself states the linearity assumption, so this is harmless, but "lähes suoralla" as in L2-09 would match the fits guardrail.
2. solutions.md:271 (L2-10, Kaava) — "$\theta = T - 273{,}15\,\text{K}$ (celsiusasteina)" mixes units. Better: $\theta = (T/\text{K} - 273{,}15)\,{}^\circ\text{C}$, or the brief's $T = \theta + T_0$ solved for θ.
3. exercises.json:115 (L1-09) — a tolerance of 0,04 (±11 °C) is loose for an exact defined value. 0,01 would fit a lookup. Harmless (carried over).

## Checked
- L1-09: θ₀ = −T₀ = −273,15 °C (MAFY: 0 °C = 273,15 K); answers.py gives −273,15, which matches. The Järkevyys check (no negative kelvin temperature) is correct.
- L2-09: from the end points (0 °C; 75 kPa) and (100 °C; 102,5 kPa), k = 0,275 kPa/°C and θ₀ = −272,7 °C; answers.py matches. The least-squares line over all five points gives −272,1 °C.
- L2-09 range: the stated hand-drawn range −260…−286 °C lies inside tolerance 0,05 (−259,1…−286,4 °C). Fixed since round 2.
- L2-09: task and Periaate now both say "lähes suoralla", in line with the fits guardrail. Fixed.
- L2-10: θ = −73,15 °C, p = 75 + 0,275·(−73,15) = 54,88 kPa; answers.py matches. The independent check p ∝ T gives 54,9 kPa, and the least-squares line gives 54,91 kPa.
- L2-10 range: the stated 53–57 kPa now lies inside tolerance 0,05 (52,1…57,6 kPa). Fixed.
- L2-10: the task states that the extrapolation is assumed linear outside the measured range, and that the axis is in °C while the asked temperature is in K. The conversion is shown.
- Closed rigid vessel (n and V constant) is stated in both tasks. Symbols follow the brief (k, θ₀ = θ₁ − p₁/k). Solutions are complete and solve symbolically first.
- Figure fy3-3/extrapolation-points gives the five points and the grid. The description gives the same information and no answer.
- Hash is identical at the start and the end.
