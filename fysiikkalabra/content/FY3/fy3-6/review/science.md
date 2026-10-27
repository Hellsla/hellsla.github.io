VERDICT: FAIL
CONTENT-HASH: f1c139c10781325d

## Blocking
- solutions.md:38 (L1-04; data exercises.json:30) — "kaksi merkitsevää numeroa, koska lämpötilat on annettu kokonaisina asteina" is wrong: 38 °C − 31 °C = 7 K has one significant figure. The worked example argues correctly that ΔT = 4,5 K limits the figures. By that rule the answer is −4·10¹ MJ, outside the tolerance. — Give 38,0 °C → 31,0 °C (ΔT = 7,0 K) and justify the two figures by ΔT = 7,0 K. The answer −35 MJ is unchanged.
- inquiry.json:292 (siirto solution; prompt :272) — "kaksi merkitsevää numeroa kuten massassa 80 kg" ignores that 38 − 30 = 8 K has one figure. `answer` 29.1 also disagrees with the stated 29 kg. — Give 30,0 / 38,0 / 60,0 °C and 80,0 kg, and answer 29,1 kg with three figures (or two figures justified by 8,0 K).

## Polish
- solutions.md:49 (L1-05) — "sama vesimäärä olisi vaatinut…": liquid water cannot be between −22 °C and −4 °C. — Say "the same ΔT for 0,50 kg of liquid water".
- solutions.md L2-01, L2-04 Muunnokset — "vain lämpötilaeroja" fits the balance equation, not the substituted weighted mean. — Add that the weights sum to the denominator, so a shift of scale carries through.

## Checked
- 12 exercises recomputed in one script: all match answers.py and exercises.json within tolerance. Other rounding justifications follow from the data.
- Every solution states principles with valid reasons (no phase change; isolated system; shared equilibrium T, so the stones stop at 40 °C), solves symbols first and converts correctly (kW→W, MJ→J, g cancels, ΔT °C = K). Reasonableness checks are real.
- Worked example: 5656,5 J and 374,6 → 3,7·10² J/(kg·K). The 24,6 °C → 383 sensitivity, lossless copper 24,6 °C and 1257 vs 75 J/K are correct.
- inquiry: ennuste-1 (26,8 / 44,0 °C, 8,5 / 30,2 kJ), ennuste-2 (40,0 / 55,0 / 63,1 °C), virhe (6,6 vs 30,0 °C), siirto 29,09 kg with mistakes 220 / 21,3, tarkistus-2 890,6 with mistakes 768 / 501, tarkistus-1 4500 vs 838 J/K.
- Lesson (T derivation, 35 °C, ratio 9,3) and exit ticket (419 kJ, ≈ 9×, 65 °C).
- Figures: water-sand rise ratio 5,25 vs c ratio 5,24; c-bars at 0,0933 px per J/(kg·K) throughout.
- Sim: Teq and Q follow the lesson's formula, and the equal-τ relaxation conserves energy. koe-1 and koe-2 isolate their varied parameter, and simState carries Teq and CB.
