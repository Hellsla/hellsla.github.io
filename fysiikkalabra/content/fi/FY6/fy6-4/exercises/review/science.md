VERDICT: PASS
CONTENT-HASH: 0bbb7ef633d3e151

## Blocking

## Polish
- exercises.json:153, :227, :329 (L2-05 102.1, L2-07 40.4, L3-05 1.32) vs solutions.md:150, :172, :194 (Vastaus 102 Ω, 40 Ω, 1,3 %) — answer field carries one digit more than the stated result; within tolerance, but set the field to the Vastaus value (102, 40, 1.3) as in the original tasks.
- L3-04 (exercises.json:288, solutions.md:182) — with R2 = R3 = 110 Ω the calculation cannot tell which branch is open; the R3 ammeter row (0,0 mA) gives it away, and part c repeats L3-01's mixed-circuit calculation while part b repeats L2-06. To match the plan's "todista laskulla": use unequal R2, R3 (e.g. 100 Ω and 150 Ω, adjusting 180 Ω) and drop the R3 ammeter row.
- L2-07 (exercises.json:220) — at 10,0 V the 40 Ω resistor dissipates 2,5 W and the 60 Ω 1,7 W; ordinary 0,25–0,6 W resistors would overheat and change R. Stop at 4–5 V or say "tehovastukset".
- L2-05 solutions.md:149 — the calculated value also carries the ±1,5 % of each single reading; one sentence that comparing to one error limit is the strict test would make the conclusion exact.
- L3-05 — E12 parts usually have ±5 % tolerance, larger than the 1,3 % vs 4,3 % difference; one line in Järkevyys noting that the comparison is between nominal values.

## Checked
- Hash 0bbb7ef633d3e151 at start and end; counts 8/7/5; tasks match docs/exercise-bank/FY6.md fy6-4.
- Recomputed in one script: L1-08 60 Ω; L2-05 series 1013 Ω (0,40 %), parallel 102,1 Ω (0,69 %); L2-06 198 Ω vs 100 Ω, R1 100 Ω, 3,02 + 5,98 = 9,00 V, one-branch model 30 mA; L2-07 ratios 24,10/24,10/24,29/24,02/24,15, mean 24,13 Ω, Rx 40,4 Ω; L3-04 125 Ω, faulty 180 Ω (49,8 mA ↔ 180,7 Ω), I3 36 mA; L3-05 all 42 pair-connections, best 560 ∥ 2700 = 463,8 Ω, 1,32 %, best series 490 Ω 4,26 %. All agree with exercises.json and answers.py.
- L1-06: four totals 33/300/150/67 Ω right, one correct option. L1-07: ideal battery stated, each lamp's current unchanged, feedback right.
- Unknown solved symbolically before substitution (1/Rx = 1/R − 1/R1); conversions mA ↔ A, kΩ right.
- L3-05 pruning argument (series only below 470 Ω, parallel only with smaller part above 470 Ω) is correct and complete.
- Batteries treated as ideal without stating it in L2-06/L3-04, consistent with the original L2-01 and the chapter level (C).
