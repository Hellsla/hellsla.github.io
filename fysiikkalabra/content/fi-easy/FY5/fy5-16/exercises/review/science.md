VERDICT: PASS
CONTENT-HASH: d8c91c2175bb496c
SCOPE: delta added-exercise from d2b1980c7da012c4 base 81db4a6fd727

## Blocking
(none)

## Polish
- none.

## Checked
- Delta round 2, fi-easy: added fy5-16-L1-09 and L2-09 only.
- Round 1 blocking item fixed: solutions.md:246 and :257 now say "alueella, jossa on kuulovaurion vaara", the same as the passed Finnish and the figure ("pitkä altistus ... vaurioittaa kuuloa").
- Compared by script with the passed Finnish set: answer, unit, tolerance, figure identical; same numbers in text and solution.
- Recomputed: t = 8 h / 2^((L − 85 dB)/3 dB): 90 dB -> 2,52 h; 105 dB -> 480 min / 101,6 = 4,72 min. answers.py agrees; tolerance 2 % covers 2,5 h and 4,7 min.
- Figure fy5-16/scale-tehtava: levels written at the markers (90, 105 dB) match the tasks; description matches.
- Equal-energy 3 dB rule and rounding to two figures justified as in the Finnish; reasonableness checks correct.
- Hash same at start and end.
