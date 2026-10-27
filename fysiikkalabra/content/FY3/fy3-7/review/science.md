VERDICT: FAIL
CONTENT-HASH: d591ace02c4d2860

## Blocking
- solutions.md:49 (L1-05) — the rounding reason is false: 19 kJ has two figures, not three. 167 kJ is right because both readings are to the nearest kJ, so their difference is too (NOTES §2) — fix: "Molemmat lukemat ovat kilojoulen tarkkuudella, joten erotuskin on: 167 kJ, kolme merkitsevää numeroa."
- solutions.md:50 (L1-05) — the check says "yli yhdeksän kertaa", but 167 kJ / 18,9 kJ = 8,8 — fix: "lähes yhdeksän kertaa".

## Polish
- solutions.md:119 (L3-03) — the rounding reason should name the difference that limits the result: 196 g − 90,0 g = 106 g, which is to the gram and has three figures.
- solutions.md:29 (L1-03) — 4,5 cm of water frozen in one night means about 350 W/m² for 12 h. That is generous for a check. Fix: about 20 kg/m², or "pakkasviikon aikana".
- inquiry.json:301 (siirto) — the answer field is 188, but the solution says "190 W (tarkemmin 188 W)". Fix: state one value.

## Checked
- answers.py and an independent recomputation agree on all 12 exercises, and on siirto (188,3 W), check-2 (0,597 kg) and the example (2,34 MJ/kg, +3,7 %, 133 g). The `mistakes` values are right: 27,8 W, 11 300 W, 0,677 kg and 4,04 kg.
- Every stated principle applies, and its reason is right. In L3-03 the loss power cancels when the equations are subtracted (P_h = 60,4 W from both runs).
- The conversions are right: g→kg, kJ→J, min→s, h→s and MJ. ΔT has the same value in K and in °C.
- The rounding in check-2 rightly uses the difference 15,0 min.
- The reasonableness numbers are right: 2,7 kg, 54 K, 3,9 cm, 24 %, 87 %, 540 K, 21 °C/11,7 K, 0,54 kg, and 2,5 kJ/×9,6.
- In lesson.md the ratios are right: r/s = 6,8, r/(c·100 K) = 5,4, and s equals the heat to warm water from 0 to 80 °C. The slopes of the heating curve are ≈ 2 : 1 : 2, plateaus marked not to scale. The phase diagram's melting line leans left.
- The sim implements the piecewise model and states its pressure, piston and loss assumptions.
- exp-1 locks m and exp-2 locks P. simState carries tMelt and tBoil. The numbers in pred-1 and pred-2 match the model (1130/565 s; 83,5/565 s and 167/1130 s).
- pr-lampo, virhe, check-1, check-3 and the exit ticket are right.
