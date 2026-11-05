VERDICT: PASS
CONTENT-HASH: 9cfa5cdd244942ed
Mode: full (translation review against the reviewed Finnish set; new task fy1-5-L2-08)
Round 2

## Blocking
(none)

## Fixed
- "velocity" changed to "speed" for $v$ and the slope in L2-08 (exercises.json, solutions.md, figures.json caption of pick-vt): the English lesson calls $v$ speed throughout, and fi uses one word (nopeus).

## Polish
(none)

## Checked
- L2-08 compared with content/fi: same id, level, kinds, answer "C", exactly one correct option (pick-back); texts, feedback, solution numbers (6.0 m, 4.0 s, 1.0 m/s, 6.0 s, 10 s, 12 m) identical.
- Re-derived: return 6.0 m / 1.0 m/s = 6.0 s, arrival at 4.0 s + 6.0 s = 10 s; only graph C (6 m flat to 4 s, then down to 0 m at 10 s) fits; A rises to 12 m, B is (t, v), D is distance from 0 to 6 m.
- All four pick-* figure descriptions in figures.json translated and match the fi captions (points, grid 1 s / 2 m / 0.25 m/s); check_i18n.py: nothing for fy1-5; build.py fy1-5 succeeds.
