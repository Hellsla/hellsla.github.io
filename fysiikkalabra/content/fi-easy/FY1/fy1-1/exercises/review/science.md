VERDICT: PASS
CONTENT-HASH: 975837ebd5d3d00b
SCOPE: delta added-exercise from 53e65cceaa271704 base 81db4a6fd727

## Blocking
- none

## Polish
- none

## Checked
- fy1-1-L1-10: MAFY values right (Sun mean radius 695 700 km, the IAU nominal value; Earth equatorial radius 6 378 km); k = d_A/d_M = r_A/r_M, the factor 2 cancels, stated in symbols before substitution.
- Recomputed independently: 695 700 / 6 378 = 109,08; answers.py and exercises.json agree; unit "kertaa" (dimensionless ratio) fine.
- Tolerance 0,04: an answer of 109 or 110 is accepted; three significant figures justified by the table values.
- Reasonableness check (10^5 km / 10^3 km ~ 10^2) is a real order-of-magnitude check, as the lesson teaches.
- Inside FY1 scope (ratio of sizes, powers of ten); notation k, d_suurempi/d_pienempi as in the brief.
- Same numbers, answer, unit and tolerance as the Finnish original (content/fi).
