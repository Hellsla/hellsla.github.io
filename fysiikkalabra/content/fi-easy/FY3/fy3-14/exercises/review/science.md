VERDICT: PASS
CONTENT-HASH: 3fdffda8e884a03a
SCOPE: delta added-exercise from c966a0c1c917e65e base 81db4a6fd727

## Blocking
(none)

## Polish
- content/fi-easy/FY3/fy3-14/exercises/exercises.json (fy3-14-L2-09): "lisälämpöä veden pitäisi vielä luovuttaa" is a hypothetical. Water already at 0 °C cannot give more heat without freezing. "Kuinka paljon lisälämpöä tarvittaisiin vielä, jotta kaikki jää sulaisi?" says the same thing without that reading. Same in the Finnish.

## Checked
- L2-09 (new situation: the extra heat needed) works from the bars 25, 5 and 60 kJ. 5 ≤ 25 < 5 + 60 kJ, so the ice reaches 0 °C, only part of it melts, and the final temperature is 0 °C (the guardrail's boundary case, stated correctly). Q_lisä = 60 − (25 − 5) = 40 kJ, as in answers.py.
- The reasonableness check is right: 20/60 = 1/3 of the ice melts and 2/3 is left.
- 2 s.f. from the 5 kJ grid; tolerance 2 %.
- L1-09 (new situation: a 0 °C ice block of 80 g melts on a window sill): ice at the melting point, so Q = sm. With MAFY's s = 333 kJ/kg, Q = 26,64 kJ, so 27 kJ. The lesson's 334 kJ/kg stays inside the 4 % tolerance, and the solution says so.
- L1-09 check recomputed: 26,6 kJ / (4,19 kJ/(kg·K) · 0,25 kg) = 25 K.
- The figure energy-bars and its description give the three values and not the answer.
- The script compared fi-easy with the Finnish: answers, units, tolerances, figure ids and all numbers are identical.
- Hash the same at start and end.
