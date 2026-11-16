VERDICT: PASS
CONTENT-HASH: 000b72e7ae8c6d61
Round 2: delta against the version round 1 reviewed (fix round 1).
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- (none)

## Checked
- s7 d task text (round-1 Blocking): the part now asks for the estimate of electrical energy with the efficiency of a thermal power plant, so the third rubric criterion asks only what the task asks, and the given "about a third" is enough to solve it. Solution "Find" updated to match. Recomputed: 3.15 MJ : 300 MJ = 1.05 %, 2.05 MJ : 300 MJ = 0.68 %, 3.15 MJ : 3 = 1.05 MJ = 0.35 % of 300 MJ. Points 1 + 1 + 1 = 3.
- s7 c answer: the reason for two significant figures is now the temperature difference 80 K, which is the right reason (the task gives 20 C; 3.15 MJ and 4.19 kJ/(kg K) have three). 3.15e6 J : (4190 J/(kg K) * 80 K) = 9.40 kg; the three-figure answer is still accepted under "Hyväksytään myös".
- s7 e first criterion: one fitting reason is enough; both examples are correct and in the solution.
- Task text: the three data rows are now full sentences under "Further information"; values unchanged (4.19 kJ/(kg K), 300 MJ, a third).
- practice.py check OK (7 tasks, 110 points). Hash the same at the start and the end.
