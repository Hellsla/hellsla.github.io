VERDICT: PASS
CONTENT-HASH: 77dfaf74f9ed879e

## Blocking
- none

## Polish
- [Minor] stage rows with a lone unit continuation row (e.g. "· 2,998 · 10^8 m/s" in fy8-4) could join the "=" column; existing layout, not a regression.

## Checked
- batch delta review, round 2: opened stage-sovella-390-1 and stage-selita-390-5 (lifted formulas); the lifted formulas carry their closing mark inside the last row, no lone mark, rows aligned and unclipped. Not every capture of this lesson was opened; the rest is judged from the same shared build (mathlayout.with_punct).
