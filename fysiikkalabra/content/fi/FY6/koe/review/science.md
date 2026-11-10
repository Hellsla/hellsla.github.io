VERDICT: PASS
CONTENT-HASH: b5bb5b56528e46c5

## Blocking

## Polish

## Checked
- Delta: the fy6-k4 d answer now keeps the power (1,9 kW) apart from the energy given to the ions in one second (1,9 kJ), and states the rate 1,9 kJ/s = 1,9 kW. The units are right. The earlier "sama 1,9 kJ" next to a power is resolved.
- Recomputed: P = UI = 1100 V · 1,76 A = 1936 W. N = I/e = 1,099·10¹⁹ s⁻¹. N·eU = N·½mv² = 1936 J/s. These match answers.py (fy6-k4-d 1936, tol 0,02). Rounding to two significant figures (1,9 kW) is justified by I and U, and 1936 rounds to 1,9.
- Reason "every ion leaving the grids gets eU" and the Järkevyys identity N·eU = (I/e)·eU = UI: right.
- Rubric d: "liike-energian sekunnissa ≈ 1,9 kJ ja toteaa sen samaksi" now matches the answer's wording. Points 1 + 1 + 1 = 3 as stated. practice.py check OK.
- The rest is unchanged since the last PASS (75644e4be115aed6).
- Hash identical at start and end.
