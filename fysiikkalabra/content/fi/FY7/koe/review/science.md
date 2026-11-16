VERDICT: PASS
CONTENT-HASH: 478eb4d6fd5b3eb1

## Blocking
None.

## Polish
- fy7-k4 c: tasks.json `answer` N = 2788.0 (answers.py uses the unrounded U₁ = 12,374 V), while the substitution now shows 2789 (from the rounded 12,37 V). Both are correct for their inputs and well inside the 3 % tolerance; the answer 2790 follows from either. No change needed.

## Checked
- Delta review from 6d4426affade3fc5; only the diff (solutions.md k4 c, k5 b, k6 d; tasks.json k6 d conclusion criterion) was judged. Unchanged content was not re-reviewed.
- k4 c: recomputed 150 · 230 V / 12,37 V = 2789,0, so "= 2789" is right for the numbers shown; answers.py gives 2788,02 with U₁ = 17,5 V/√2 = 12,374 V. Vastaus "noin 2790" and the criterion "N₂ ≈ 2790" still agree. I₂ = 0,200 A and I₁ = 3,72 A are unchanged and correct.
- k5 b: the mean written with \dfrac is (3,327 + 3,347 + 3,321)/3 = 3,332 µm → 3,33 µm; answers.py mean 3,3315 µm. The number is unchanged; only the typesetting changed.
- k6 d: payback 3,0 M€ / 334 175 €/a = 8,98 a (answers.py fy7-k6-c-pay); with the two transformers' 120 kW losses 3,0 M€ / 310 175 €/a = 9,67 a (answers.py k6-tr). "noin 9–10 vuodessa" covers both cases and agrees with the c part (9,0 a) and its Järkevyys note (9,7 a). The model answer and the rubric criterion now say the same. This also partly answers the earlier polish point that the payback is longer than 9 a with real losses.
- Hash confirmed 478eb4d6fd5b3eb1 with `python3 scripts/practice.py hash FY7/koe` at start and end.
