VERDICT: PASS
CONTENT-HASH: 2c9fdf155f72e6a3

## Blocking
(none)

## Polish
(none)

## Checked
- Compared fy2-1-L1-09 (fi-easy) with the reviewed Finnish: id, level, kind, answer key (1 T, 2 F, 3 T, 4 F, 5 T), unit, tolerance and the five true flags are identical.
- Task text keeps the same physics: 1 m drop from rest, isolated system of ball, floor and air, bounces lower each time, ball ends at rest.
- Feedback 1 names the right mechanism (mechanical energy to thermal energy in the collision and by air resistance); feedback 2-4 keep the same misconceptions and reasons; 5 keeps ball, floor and air.
- solutions.md L1-09: Principle E_initial = E_final for an isolated system, all energy forms incl. thermal; model answer 1, 3, 5 true and 2, 4 false, same as fi. No numbers, so no answers.py line needed.
- No decimal comma/point issue (only "1 m"); no formulas added or lost.
- check_i18n.py shows nothing for fy2-1; build.py fy2-1 succeeds. No translation edits were needed.
- Round 2 (commit 442c889ba): L2-05 Reasonableness sum check now split into 60 % + 17.5 % = 77.5 %, 15 % + 7.5 % = 22.5 %, total 100 %. Recomputed from 36.0/10.5/9.0/4.5 GJ of 60.0 GJ: 60, 17.5, 15, 7.5 %; correct, same as fi.
- Round 2: check_i18n.py shows nothing for fy2-1; build.py fy2-1 succeeds; hash unchanged at start and end of round.
