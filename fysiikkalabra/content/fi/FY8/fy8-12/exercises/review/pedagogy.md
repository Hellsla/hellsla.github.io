VERDICT: PASS
CONTENT-HASH: 15261a26498e83ce
SCOPE: delta added-exercise from 844ef976147dad75 base 5b3ca4f81c77

## Blocking

## Polish

- solutions.md (L2-09) writes the rate as `pulssia/min` while the `unit` field is now `min⁻¹` (L1-07 and L2-03 use `min^{-1}`). Optional: use `\text{min}^{-1}` in the L2-09 solution.
- L2-09 and L3-07 share the figure fy8-12/tuntematon and the read-d1/2 step; L3-07 adds extrapolation and a safety decision, so the level difference is real. Optional: a second graph for L3.

## Checked

- Diff since the passed version: L1-07 text and unit and L2-09 unit changed from 1/min to min⁻¹; answers 1530 and 141,4 unchanged and consistent with the solutions; notation matches the other count-rate exercises.
- solutions.md diff is blank-line reflow only; all stages remain, symbolic before numeric, reasonableness checks intact.
- Earlier checks still stand: L3-07 uses 1/50 (not the worked example's 1/20), answer 68 mm rounded up for "at most", conclusion consistent; L2-09 answer 141,4 = 800*2^-2,5; figure description gives no answer; set mix of levels and kinds fits the plan.
- Hash unchanged at start and end (15261a26498e83ce).
