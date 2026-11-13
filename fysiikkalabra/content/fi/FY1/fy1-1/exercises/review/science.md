VERDICT: PASS
CONTENT-HASH: 331a2d8c7ba45ff5
SCOPE: delta added-exercise from 67c7aa2652af10a6 base 81db4a6fd727

## Blocking
- none

## Polish
- content/fi/FY1/fy1-1/exercises/solutions.md:214 — "kolme merkitsevää numeroa kuten taulukon arvoissa": the table values 695 700 km and 6 378 km carry four figures, so this reason does not explain the three — say "kolme merkitsevää numeroa riittää suuruusvertailuun" or give 109,1.

## Checked
- fy1-1-L1-10 only (delta, added exercise); hash the same at start and end.
- Recomputed independently: k = 2r_A/(2r_M) = 695 700/6 378 = 109,08 (key 109.08); the shown 109 is 0,07 % from the key.
- MAFY values: Sun mean radius 695 700 km (IAU nominal) and Earth equatorial radius 6 378 km are right; the hint names the right table (Aurinkokunta).
- Physics: the d = 2r step is stated and the factor 2 cancels; the ratio formula is the lesson's own k = d_suurempi/d_pienempi; no units are left in k.
- Tolerance 0,04 covers other table editions (e.g. 6,96·10⁸ m gives 109,1).
- Reasonableness: 10⁵ km / 10³ km ≈ 10², which is a real check and agrees with L2-04 (109,4 from 1,39·10⁹ m / 1,27·10⁷ m).
- Scope: FY1 orders of magnitude, nothing beyond.
