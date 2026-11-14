VERDICT: PASS
CONTENT-HASH: fc973652ab241b0a
SCOPE: delta added-exercise from 053cb480bab0df62 base 8f23aa7ae3bd

## Blocking

## Polish

## Checked
- Delta round 2, fi-easy: added fy5-4-L2-09 and fy5-4-L3-06 only (new figures kuvaaja-a, kuvaaja-b).
- Compared by script with the passed Finnish set: answer, unit, tolerance, figure, level identical; every number in task text and solution the same in fi and fi-easy.
- Recomputed independently: L2-09 r = v²/a_n = 225/3,0 = 75 m; L3-06 μ0 = F/(mg) = 8000/(1200 · 9,81) = 0,6796 -> 0,68. answers.py agrees; 2 % tolerance fits two significant figures.
- Figures: kuvaaja-a plots v²/75 and passes (15; 3,0); kuvaaja-b plots 1,2v²/60 kN = mv²/r for 1200 kg, r = 60 m, and passes (20; 8,0). The marked points lie on the curves; the radius is not stated, so neither figure gives the answer away; the descriptions give the same values.
- Physics: uniform circular motion on a level curve, friction the only horizontal force, N = mg stated, limiting case F = μ0 N. Matches the brief's worked example; symbolic first; rounding reason is the 2-figure reading.
- Reasonableness checks are real checks (second point 10 m/s -> 1,33 m/s²; mg ≈ 12 kN).
- Hash same at start and end.
