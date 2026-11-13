VERDICT: PASS
CONTENT-HASH: b0821156ba49dd4c
SCOPE: delta added-exercise from 4f903b6a27cc71f7 base 81db4a6fd727

## Blocking
(none)

## Polish
- none

## Checked
- fy3-1-L1-10: G = m g_Mars = 85.0 kg * 3.72 m/s^2 = 316.2 N, answer 316 N in three figures; answers.py line agrees; the MAFY Mars value (3.72) differs from the 3.71 used elsewhere in the set by 0.3 %, well inside the 4 % tolerance, and the solution says tables differ.
- fy3-1-L1-10 solution: weight as the Mars-astronaut interaction, mass unchanged, reasonableness 0.38 * 834 N = 317 N is a real check.
- fy3-1-L2-08: figure weight-points has (2;10) ... (10;50) on a 2 kg / 10 N grid, so g = 5.0 m/s^2 and G = 12 kg * 5.0 m/s^2 = 60 N; extrapolation to 12 kg justified by G = m g (line through the origin has a physical reason); tolerance 3 % fits reading by eye.
- Figure description gives every point and does not state g or the answer.
- Scripted comparison with the Finnish exercises.json: same ids, answers, units, tolerances, figures and every number in the task texts for all 23 exercises.
- Recomputed all answers.py values in one run against exercises.json: every answer within its tolerance.
- FY3 scope kept (G = m g only, no Newton's laws).
- Hash identical at start and end.
