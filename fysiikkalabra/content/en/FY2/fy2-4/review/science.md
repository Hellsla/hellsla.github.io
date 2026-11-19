VERDICT: PASS
CONTENT-HASH: c7b1782d5249a6cd

## Blocking
(none)

## Polish
(none)

## Checked
- delta review, round 2: inquiry.json diff only (ennuste-1 prompt, ennuste-2 and koe-2 question no longer optional).
- ennuste-1: removing the incandescent-lamp hint leaves the question self-contained; exactly one correct option (25 %), distractor feedback unchanged and right (60 % gives 24 kW losses; 15 kW useful, 45 kW losses).
- ennuste-2 made core: correct option (efficiency unchanged at constant power) and both distractors' feedback still right; reveal after koe-2 with min 3 is consistent with the experiment.
- koe-2 new prompt: the student now reads P_a from the readout instead of being told it; sim.js shows P_a in the readout text (tehot) and on the canvas, and simState holds Pa, Eo, Ea.
- Recomputed for the locked setup (lamp, eta 0.05, P_o = 40 W): P_a = 2.0 W, P_a : P_o = 5 %; t = 10, 20, 30 s give E_o = 400, 800, 1200 J and E_a = 20, 40, 60 J, ratio 5 % on every row; correct option and the "t = 10 s and t = 20 s" feedback agree.
- "at least two rows with different times" matches min 3 rows with t varied and P_o locked: the setup isolates t.
- koe-1 numbers unchanged context: 0.75 * 600 000 J = 450 000 J, 75 % losses, 25 % efficiency.
