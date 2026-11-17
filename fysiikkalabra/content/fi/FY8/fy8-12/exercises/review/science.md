VERDICT: PASS
CONTENT-HASH: 0e64d48ba9795111
SCOPE: delta added-exercise from 844ef976147dad75 base 5b3ca4f81c77

## Blocking

## Polish
- exercises/exercises.json:332 (fy8-12-L2-09) — the task ends "Anna vastaus pulsseina minuutissa", while the answer field now shows $\tfrac{1}{\text{min}}$. The two are physically the same because a pulse count has no dimension, so this is not an error. For consistency with L1-07 (line 77, "Anna vastaus yksikössä $\tfrac{1}{\text{min}}$"), the sentence could say the same. This is optional.

## Checked
- Hash 0e64d48ba9795111 at the start and the end. Judged the one-line diff in its context (exercises.json:329–341).
- A count rate is a number of events per unit time, so 1/min is a correct SI-style unit for a net pulse rate. It matches the unit already used for the count rate in L1-07 (line 80).
- I recomputed the answer myself: $R = 800 \cdot (1/2)^{30/12} = 141{,}42$ per minute. answers.py line 44 gives the same value, and the stored answer 141,4 agrees.
- Tolerance 0,02 accepts about 138,6–144,2. That covers 141 and also 140, the two-figure rounding the answers.py comment names.
- Nothing in L3-07 or in the figure `fy8-12/tuntematon` changed since round 2.
