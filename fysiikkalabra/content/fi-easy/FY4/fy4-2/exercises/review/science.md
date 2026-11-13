VERDICT: PASS
CONTENT-HASH: 9b1085b913808538
SCOPE: delta added-exercise from c6b41b885c57e2a9 base 81db4a6fd727
Mode: delta (added MAFY task fy4-2-L1-09, Selkeä suomi against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Polish
- content/fi-easy/FY4/fy4-2/exercises/solutions.md:229 — "kolme merkitsevää numeroa kuten taulukon arvossa 24,79" while 24,79 has four figures (same wording in fi) — give the reason as three figures by house rule (data limited by the table value and h exact), in fi as well.

## Checked
- Script comparison with content/fi/FY4/fy4-2: same ids, levels, answer, unit, tolerance, lookup and every number in text, hints and solution of L1-09.
- Recomputed: free fall from rest, h = ½gt², t = √(2h/g) = √(40/24,79) = 1,270 s; answers.py gives 1,2703, exercises.json 1.2703.
- Model and conditions stated in the task (at rest, no air resistance); symbolic solution before substitution; Earth comparison 2,02 s and √2,5 ≈ 1,6 ratio are right.
- Tolerance 4 % covers table differences (24,8 vs 24,79) and rounding to 1,27 s.
- Hash unchanged at start and end.
