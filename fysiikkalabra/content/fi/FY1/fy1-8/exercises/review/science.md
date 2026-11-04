VERDICT: PASS
CONTENT-HASH: 476992e005b0e229

Round 2: round 1 passed. The changed tasks (L1-06, L1-08, L2-05, L2-07, the rewritten L3-04 and L3-05) are checked against the whole set.

## Blocking
(none)

## Polish
- exercises.json:316 (L3-04): "Kuinka monta kertaa ... 0,15 s on keskiarvojen erotus?" can also be read as 0,27. The difference of 0,04 s has one significant figure, so the answer 4 falls outside the 2 % tolerance. Write "Kuinka moninkertainen ... on erotukseen verrattuna?" and use tolerance 0,07.
- solutions.md:168–169 (L3-04): a random error of 0,15 s per timing does not fit repeats that lie within ±0,04 s. A common reaction delay largely cancels in the difference. Add one sentence: the larger estimate is used as the cautious uncertainty, and "no difference can be shown" holds with either estimate.
- exercises.json:349 / solutions.md:178 (L3-05): the stem assumes the slowest container cools at the glass rate, but the Järkevyys says that it cools less. Make the two agree (for example "at least the glass rate", so that 10 min stays a lower bound).
- exercises.json:246 (L2-07): this is a by-eye line with tolerance 0,02 (0,294–0,306 m/s). A careful fit can give 0,29. Widen to 0,04.
- L3-04 reuses the L2-05 data and its overlap conclusion. Whether that is acceptable is pedagogy's call.

## Checked
- Round-1 Polish has been applied: L2-05 ends "onko eroa", L1-06 and L3-05 say "riippumaton (muutettava)", and the L1-08 stem is fixed.
- One script recomputed the changed answers: L2-05 3,12 s and 3,08 s, ±0,04 s, 100 %. L2-07: the table's least-squares slope is 0,2995 m/s (0,3005 m/s through the origin), the line points give 0,30 m/s, and 1/v = 3,33 s/m. L3-04 3,75, the difference being 1,3 % of the time. L3-05 2,0 K/min, then 20 K and 10 min; the per-minute drops 2,1/1,9/2,0/1,8 K are realistic. All match answers.py.
- L3-04: overlap is not taken as support, the hypothesis is not called proven, and no data are removed, as the guardrails require.
- L3-05: the controlled variables are physically justified, and 10 min is called a lower bound.
- L1-08 "Viiden mittauksen" agrees with its feedback. Levels fit, and there is no other duplicate.
