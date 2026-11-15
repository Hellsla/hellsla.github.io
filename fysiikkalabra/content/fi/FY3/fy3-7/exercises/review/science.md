VERDICT: PASS
CONTENT-HASH: b0becb0dcbed361b

## Blocking

## Polish
- exercises.json:41 (fy3-7-L1-05) and exercises.json:303 (fy3-7-L2-09) — the stored answers are 333 and 2083,3, but the solutions' Vastaus lines give two significant figures ($3{,}3 \cdot 10^{2}$, $2{,}1 \cdot 10^{3}$). The tolerances accept both. Consider making the shown answer and the Vastaus agree.

## Checked
- I recomputed all 20 numeric answers in one script with my own formulas. Every one lies within its tolerance.
  - L2-05: I extrapolated the plateau edges independently (17,5 s and 156,7 s), which gives 334 kJ/kg.
  - L3-04: P = 11,98 W, solidification from 3,24 to 30,9 min, Q = 19,9 kJ, s ≈ 200 kJ/kg. These are realistic for stearic acid (melting point about 69 °C).
- L2-05 data is internally consistent. The ice warming takes 10,5 kJ by both P t and c m ΔT, and the water rise of 0,575 K/s equals P/(c m). The figure melting-curve matches 200 kJ / 0,60 kg, c(ice) 2083 and the slope of the water part.
- L3-03: the two-power method cancels the loss of about 60 W. The data reproduce 90,0 g at 400 W, and the single-run values (2,45 and 2,67 MJ/kg) are right and too large for the stated reason.
- Guardrails:
  - Constant temperature during a change of state is tied to constant pressure (L1-06 feedback, L2-06).
  - The microscopic wording of L1-06 follows the guardrail text.
  - Freezing and condensation release energy (L1-03, L1-04, L3-05).
  - L3-01 checks that all the ice melts (36,7 kJ > 20,0 kJ).
- L2-07: interpolating between 50 and 70 kPa gives 85,65 °C, so the drop is 14,4 K. The true value is about 85,9 °C, so the ±4 % tolerance is appropriate.
- L3-05: 23,5 g of steam against 0,386 kg of water; 94 % of the steam's energy comes from condensation. The burn reasoning is right.
- L1-09: the ethanol value r = 840 kJ/kg is given with a correct caveat about the temperature.
- L2-08 order: 84 < 167 < 201 < 226 kJ. L1-06 and L1-07 have exactly one correct option each, and every distractor's feedback is right.
- Every solution states its assumptions in the task's terms, is symbolic first and justifies its rounding. Its checks are real.
