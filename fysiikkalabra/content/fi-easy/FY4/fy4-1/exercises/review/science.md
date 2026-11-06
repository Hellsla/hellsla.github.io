VERDICT: PASS
CONTENT-HASH: d0bb3ff4b5264b29

## Blocking

## Polish
- None.

## Fixed
- No text change needed in this translation.

## Checked
- New task fy4-1-L1-09 (graph choice: x0 = 6.0 m, v = -1.0 m/s, x(4.0 s) = 2.0 m; options A-D with figures pick-rising/origin/falling/flat) compared with the reviewed Finnish: same id, level, kind, answer, tolerance, correct flags, choice and reason order, every number and formula.
- Recomputed the physics: x = 6.0 + (-1.0)(4.0) = 2.0 m; A grows, B starts at origin, D horizontal at -1 m, C only correct.
- solutions.md block matches the Finnish step by step (same equations and numbers).
- figures.json: all four pick-* descriptions give the same axes (t 0-5 s, x -6...12 m) and endpoints as the Finnish (6->10, 0->-4, 6->2, -1 flat) and match figures.py; none names the answer
- check_i18n shows nothing for fy4-1; build.py fy4-1 succeeds.
