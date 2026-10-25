VERDICT: PASS
CONTENT-HASH: f34d5ca990f8a67f
## Blocking
(none)
## Polish
1. solutions.md:95 — "Häviöteho on noin 60 W" is computed from run 1 only. — Add that run 2 gives the same value, 400 W − 2,264 MJ/kg · 0,0900 kg / 600 s ≈ 60 W.
2. solutions.md:77 — The numerator is in J and the denominator in J/K, so the quotient is a temperature difference from 0 °C. — Optional: write "T − 0 °C = … ≈ 9,7 K, joten T ≈ 9,7 °C".
## Checked
- Hash stable. Lint 0/0. answers.py output matches. `check_layout.py fy3-7` OK at 360 px after the build.
- lesson.md:36, the SVG to scale for 1 kg at 0,155 px/kJ and 0,9 px/K. The exact x values are 79,8 / 131,5 / 196,5 / 546,8 / 559,2, against 80 / 132 / 197 / 548 / 560 drawn, so every point is within 1,2 px. y(−30 °C) = 197 and y(140 °C) = 44 are exact.
- lesson.md:31, the slopes: ice 2,7, water 1,385 and steam 3,0 px/px. The ratios 1,95 and 2,17 match 4190/2100 = 2,00 and 4190/2000 = 2,10, so "noin kaksi kertaa jyrkempiä" is true. The plateaus are 52 : 350 px, which is 334 : 2260.
- lesson.md:21–27, the constants table agrees with answers.py:6–7 and with sim.js:15.
- lesson.md:53–57, the example: 300 kJ / 0,128 kg = 2,344 MJ/kg, which is +3,7 %. The Δm notation is the same in the example (:53) and the summary (:67).
- lesson.md:10 and :60: 2260/334 = 6,77, 2260/419 = 5,39, and 334/4,19 = 79,7 K ≈ 80 K.
- L3-03, the algebra: subtracting (P₁ − P_h)t = rΔm₁ and (P₂ − P_h)t = rΔm₂ gives r = (P₁ − P₂)t/(Δm₁ − Δm₂) = 240 000 J / 0,106 kg = 2,264 MJ/kg. P_h = 60,38 W from both runs. Each single run gives 2,449 and 2,667 MJ/kg, both greater than r, because rΔm = (P − P_h)t < Pt.
- L3-01: T = 16 622,5 / 1717,9 = 9,676 °C. The check that all the ice melts holds: 36 662,5 J > 20 040 J. With 0 °C water instead of ice: 21,3 °C.
- L3-02: 648 800 / 24 000 = 27,03 K, and the share is 87 % / 13 %. Every factor has its unit.
- L1-01…05, L2-01…04: products, rearrangements, conversions and sanity figures are correct.
- Exit ticket: the q1 particle-model answer agrees with lesson.md:8, and the q3 formulas agree with :17 and :31.
