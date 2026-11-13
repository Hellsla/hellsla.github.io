VERDICT: PASS
CONTENT-HASH: a1183f2bb759e378
SCOPE: delta added-exercise from ec42002a596881a5 base 81db4a6fd727

## Blocking

## Polish

## Checked
- L2-09 now matches the Finnish round-6 version: both vessels $2.00\,\textsf{l}$ as in L2-04, asked $n_\text{A}/n_\text{B}$; the earlier 1.66 l / 0.0500 mol inconsistency (my previous polish point) is gone.
- Recomputed: $100\,\text{kPa}/60\,\text{kPa} = 1.667$ at 400 K (200 K points give the same); answers.py 1.667, stored 1.67, unit "times", tolerance 0.03.
- Principle (rigid closed vessel, ideal gas, slope $p/T = nR/V$, equal $V$) and check (0.0602 and 0.0361 mol, ratio 1.67) are right.
- L1-09 unchanged: 3.047 MPa, answer 3.05 MPa.
- Script comparison with the Finnish exercises.json: same 23 ids, answers, tolerances and figures; numbers in every task text agree (differences only translated choice texts and sentence punctuation).
- Every answers.py value lies inside its tolerance.
- Hash same at start and end.
