VERDICT: PASS
CONTENT-HASH: aa44f962e1cff333
Mode: delta (fi-easy translation review of the new task fy1-4-L2-08 against the reviewed Finnish set, NOTES.md §12)
Round 2

## Blocking
(none)

## Fixed
(none needed)

## Polish
(none)

## Checked
- L2-08 compared with content/fi: id, level, kind (error), answer string, tolerance, correct flag (Line/Rivi 3 only), all five choices and every number (2.0/10.0 min, 5.0/17.0 l, 12.0 l, 12.0 min, 1.0 l/min) identical; decimal point/comma only.
- Recomputed: dV = 12.0 l, true dt = 8.0 min (the 12.0 min on line 3 is the planted error), k = 12.0/8.0 = 1.5 l/min; check 1.5*8.0 = 12.0 l, 1.0*8.0 = 8.0 l. Matches the solution.
- Each distractor feedback is physically right: lines 1, 2 and 4 are correct (line 4 only inherits the wrong dt); "no error" is refuted with k = 1.5 l/min.
- solutions.md L2-08 has the same Find/Principle/Model answer sections and the same physics as Finnish.
- check_i18n.py: nothing for fy1-4; build.py fy1-4 succeeds.
