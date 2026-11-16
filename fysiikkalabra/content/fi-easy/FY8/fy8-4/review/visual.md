VERDICT: PASS
CONTENT-HASH: 6e18483831d8ad47

## Blocking
- none

## Polish
- [Minor] stage rows with a lone unit continuation row (e.g. "· 2,998 · 10^8 m/s" in fy8-4) could join the "=" column; existing layout, not a regression.

## Checked
- batch delta review, round 2: opened example-390-1 and stage-sovella-390-2 (lifted formulas with a following sentence, unit rows); the lifted formulas carry their closing mark inside the last row, no lone mark, rows aligned and unclipped. Not every capture of this lesson was opened; the rest is judged from the same shared build (mathlayout.with_punct).
