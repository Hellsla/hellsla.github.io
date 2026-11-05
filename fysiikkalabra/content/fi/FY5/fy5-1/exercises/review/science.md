VERDICT: PASS
CONTENT-HASH: ca55abf18de305a6

## Blocking

## Polish
- exercises.json:77 (L1-07) — the new "(naru on oven reunan suuntainen …)" is ambiguous, because a door has both vertical and horizontal edges. The physics is right either way: a pull in the door's plane toward the hinges has zero moment about the hinge axis. "vaakasuora, oven tason suuntainen" would be clearer.
- exercises.json:146 (L2-05) — the plan's (1/r, F) graph is still done as products Fr; acceptable.

## Checked
- Round 1 Blocking fixed: L3-04 now states that the crank and chainring turn steadily, so the pedal moment and the chain moment about the crank axle are equal and opposite; the Periaate cites it. Numbers unchanged and recomputed: 787,5 N; 70,875 / 47,25 / 31,5 Nm. The added speed trade-off for the large sprocket is correct.
- L2-07 now rounds to 22 Nm (two significant figures from 90 N); answer 21,6 with tolerance 0,02 accepts it.
- L1-07 options reordered only; still exactly one correct option, and the feedback is unchanged and right.
- answers.py unchanged; all 8 new answers recomputed in round 1 (−9,0; 25; 0,118; 21,6; 70,9; 166) still match the task data.
- Scope: now inside fy5-1 (moment, arm, sign, oblique force); no duplicates; levels and plan +3/+3/+2 fit.
