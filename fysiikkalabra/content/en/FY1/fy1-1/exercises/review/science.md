VERDICT: PASS
CONTENT-HASH: 486bd3822684574e
SCOPE: delta added-exercise from 80a20c797b439941 base 81db4a6fd727

## Blocking
- none

## Polish
- exercises/solutions.md fy1-1-L1-10 — the Answer says "three significant figures as in the table values", but the table radii have six and four figures — give the real reason (a size comparison needs no more than three figures; four, 109.1, would follow from the 6 378 km datum).

## Checked
- Added task fy1-1-L1-10 only (delta, added exercise); hash recomputed at start and end.
- Table values: Sun mean radius 695 700 km (IAU nominal), Earth equatorial radius 6 378 km; correct.
- k = d_A/d_M = r_A/r_M, the factor 2 cancels, solved symbolically before substitution; units cancel.
- Independent recompute 109.078 = answers.py 109.08; the shown 109 lies 0.07 % from it, within the 4 % tolerance.
- Unit "times" fits a ratio; reasonableness check by orders of magnitude (10^5/10^3) is a real check.
- Inside FY1 scope (powers of ten, size comparison); en numbers identical to the Finnish original.
