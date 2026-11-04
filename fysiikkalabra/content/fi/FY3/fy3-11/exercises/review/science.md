VERDICT: FAIL
CONTENT-HASH: ffcb1851d948b740

## Blocking
- exercises.json:343, solutions.md:240, 242 (L3-05) — **A**: the data are impossible under the task's own assumption (all heat into the air). Air heated at constant p has W_k/Q = R/C_p = 2/7 ≈ 29 %, but the set gives and teaches 15 % ("loput 85 % jäi sisäenergiaksi"). With n ≈ 0,103 mol, W = 300 J means ΔT ≈ 350 K, while Q = 2000 J would mean ΔT ≈ 670 K. — Fix: make W/Q ≈ 0,29. For example P = 65,0 W and h 10,0 → 13,0 cm in 4,0 s (rows 10,0; 10,8; 11,5; 12,3; 13,0), which gives Q = 260 J, W_k = 75 J, ΔU = 185 J and 29 %. Update the answer, answers.py, the numbers in c) and Järkevyys.
- solutions.md:218 (L3-05) — **A**: "korkeus kasvaa tasaisesti, joten paineen vakioksi olettaminen sopii" is a wrong inference. A steady rise shows only a steady volume rate; the constant p comes from the light piston and the outside pressure. — Fix: "Paine on annettu vakioksi; tasainen nousu sopii vakiotehoiseen lämmitykseen."

## Polish
- solutions.md:218 — the header "Kuvaajan lukeminen" sits over a table. Use "Taulukon lukeminen".
- exercises.json:105 (L1-08) — `kind: reasoning` on a one-formula calculation.
- exercises.json:217 (L2-07) — tagged `experiment` for monitoring data. `data` is enough.
- exercises.json:290 (L3-04) — the plan asks why ε falls in frost. Add one sentence to c) or the model answer.
- docs/exercise-bank/FY3.md — the fy3-11 plan still lists a cycle pV graph (L2) and the Carnot limit (L3). Neither is in the set, and Carnot is rightly left out because the brief does not teach it. Update the plan.

## Checked
- New answers recomputed independently: L1-08 3,25; L2-05 31,4 % (21,2/28,9/31,4/29,8); L2-07 20,9 kWh; L3-04 2,74 (mean 2,88, saving 8,7 MWh); L3-05 1,70 kJ. All agree with answers.py.
- MC L1-06, L1-07, L2-06: exactly one correct option, the distractors are wrong and the feedback is correct and matches the brief.
- L2-07 and L3-04: ε falls with T_ulko, and the balances close.
- Scope: no Carnot, no C_p, no cycles beyond the brief.
- The significant-figure reasons are stated.
- No duplicates. Levels fit.
- The L3 capture at 1280 px renders the tables and equations cleanly.
