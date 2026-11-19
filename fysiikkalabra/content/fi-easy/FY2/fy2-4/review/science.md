VERDICT: PASS
CONTENT-HASH: 1d22b92ccc00686b

## Blocking

## Polish
- None.

## Checked
- Delta review, round 2: inquiry.json ennuste-1 prompt (hint removed), ennuste-2 and koe-2 question no longer optional, koe-2 question prompt now asks the student to read P_a from the readout.
- ennuste-1 without the hint still has exactly one correct option (25 %, 15 kW useful, 45 kW losses at 60 kW); distractor feedback unchanged and right (60 % -> 24 kW losses recomputed).
- koe-2 prompt: the sim readout shows P_a (sim.js line 66 `tehot`, canvas label line 104); at the locked 40 W hehkulamppu, P_a = 0,05 * 40 W = 2,0 W, P_a : P_o = 5 %.
- koe-2 rows recomputed: t = 10 s gives E_o = 400 J, E_a = 20 J; t = 20 s gives 800 J, 40 J; E_a : E_o = 5 % on every row, so the single correct option (same ratio as the powers, energies grow) holds and the two distractors stay wrong for the stated reasons.
- "at least two rows at different times" isolates t as the varied parameter with laite and Po locked; simState gives Eo, Ea and Pa at those values.
- ennuste-2 now on the core path: its reveal (after koe-2, min 3) points to a non-optional experiment; feedback (time cancels at constant power; the model assumes constant η, so the argument is the calculation, not the sim) is correct.
- Hash identical at start and end.
