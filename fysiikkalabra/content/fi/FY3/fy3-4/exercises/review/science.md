VERDICT: PASS
CONTENT-HASH: 1e4ae50abb983484

## Blocking
- none

## Polish
- solutions.md:190 (L3-04 Järkevyys) — "se koskee vain ylintä viidesosaa vesipatsaasta" is not exact: the middle layer (999,7 kg/m³, 10,0 m) also differs from 1000 kg/m³ and gives 3 of the 12 kg/m² deficit (the surface layer gives 9). — Write e.g. "Suurin poikkeama 0,18 % koskee vain ylintä viidesosaa vesipatsaasta, ja välikerroksessa poikkeama on vain 0,03 %, joten kokonaispaineen muutos on selvästi pienempi."
- exercises.json:76 (L1-07) — third plain ρgh task at level 1 (with L1-02, L1-05); acceptable, adds little.
- solutions.md:146, 160, 181, 196 (L2-05, L2-06, L3-04, L3-05) — Heading "Kuvaajan lukeminen" over a table reading; "Taulukon lukeminen" would be accurate. L2-05 is tagged `graph`, but no graph is drawn or asked; either ask the student to draw the (h, p) points and line, or drop the tag.
- solutions.md L3-05 Vastaus — rounding reason cites only 15,0/20,0 m; 5,0 m and 1,0 m have two figures. Say the width is exactly one metre.

## Checked
- All eight new answers were recomputed in one script with my own formulas, and they agree with answers.py: L1-07 394,4 kPa → 390 kPa; L2-05 p0 = 99,73 kPa (least squares 9,777 kPa/m, 99,75 kPa), ρ = 997 kg/m³; L2-06 2943 Pa; L2-07 Δh 14,5 cm → 1422 Pa, total 102 kPa; L3-04 196 082 vs 196 200 Pa → 0,118 kPa, depth error 1,2 cm vs 5,1 cm; L3-05 parts 122,6/367,9/613,1/858,4 kN, sum 1962 kN = whole-strip check, ratio 7,0.
- The tolerances accept the correctly rounded answers. The significant figures of L1-07, L2-06, L2-07 and L3-04 are justified.
- L1-06 and L1-08 MC: exactly one correct option, and every distractor's feedback says why it is wrong. L1-08's worked numbers (150 vs 199 kPa, ×1,3) are right.
- L2-07 manometer: the gas-side surface is lower, so the gas pressure is greater than p0. The sign and the reasoning are right.
- L3-04: the densities at 20/10/4 °C (998,2/999,7/1000,0) are realistic. The uncertainty comparison is done in both pressure and depth.
- L2-05 uses the guardrail fit sentence; L2-06 data within ±0,1 kPa of 2,94 kPa.
- Scope: everything stays inside p = F/A and p = p0 + ρgh; force is treated as a scalar. No duplicate of an existing task, and the levels fit 8/7/5 and the plan (diver data, paradox, U-tube, layered lake, dam).
- L3 1280 px screenshot renders cleanly; hash same at start and end.
