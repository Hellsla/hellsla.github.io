VERDICT: PASS
CONTENT-HASH: 9a88d35a19ddea79

## Blocking
(none)

## Polish
- exercises.json:41 / solutions.md:49 (L1-05) — the solution now gives 3,3·10² kJ/kg (two figures, limited by 0,60 kg), while `answer` stays 333. The check range 323…343 still matches the tolerance, and L2-09 follows the same pattern (2083,3 against 2,1·10³), so this is not an error. If the shown answer should carry the solution's precision, use 330 with a range of 320…340.

## Checked
- Recomputed all 20 numeric answers with my own formulas in one script. They agree with answers.py and exercises.json: L1-05 200 kJ / 0,60 kg = 333; L2-02 278,85 kJ; L2-04 0,938 MJ; L3-01 9,68 °C (the ice all melts, 36,7 kJ > 20,0 kJ); L3-02 27,0 K; L3-03 2,264 MJ/kg with a loss of 60,4 W from both runs; L3-05 23,5 g and 0,386 kg of water (16×, 94 % from condensation).
- L2-05 data agree with the model. The ice slope 600/(0,25·2100) = 1,14 K/s and the water slope 0,573 K/s match the table, and the melt time s·m/P = 139 s matches 157 − 18 s. The explanation of 312 kJ/kg as too small is right.
- L3-04: the plateau at about 69 °C, P = 11,98 W, Δt = 27,7 min and Q = 19,9 kJ are right, giving s ≈ 199 kJ/kg, realistic for stearin. The constant emitted power is stated as an assumption.
- L2-07: the steam-table values and the midpoint interpolation give 85,65 °C, so ΔT = 14,35 K. The real value is about 85,9 °C, inside the stated ±4 %.
- Figure melting-curve: the last segment, 80 kJ / (0,60·4190) = 31,8 K, matches the drawn 31,9 °C. The first segment gives c ≈ 2083 J/(kg·K), and nothing names the melting part.
- L1-06 and L1-07: exactly one correct option each. The constant-pressure condition is stated, the microscopic model follows the guardrail wording (interaction energy, not broken bonds), and the distractor feedback is right.
- L1-09: ethanol r = 840 kJ/kg (MAFY), so Q = 4,2 kJ. The remark that r is greater at skin temperature is correct.
- The direction of energy in freezing and condensation is right. Units, significant figures and the rounding reasons are right.
- Hash the same at the start and the end.
