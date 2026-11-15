VERDICT: PASS
CONTENT-HASH: 60d4680b6d8d1544

## Blocking
- none

## Polish
- [Minor] stage rows with a lone unit continuation row (e.g. "· 2,998 · 10^8 m/s" in fy8-4) could join the "=" column; existing layout, not a regression.

## Checked
- batch delta review, round 2: opened example-390-1 and open-exercises-L2-1280-3 (open solution with display formulas); the lifted formulas carry their closing mark inside the last row, no lone mark, rows aligned and unclipped. Not every capture of this lesson was opened; the rest is judged from the same shared build (mathlayout.with_punct).
