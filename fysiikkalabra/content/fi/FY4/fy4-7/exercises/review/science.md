VERDICT: PASS
CONTENT-HASH: b2ac4ac61efac0df
SCOPE: delta added-exercise from 36a9f0fc1bd88cd4 base 81db4a6fd727

## Blocking

## Polish
- lessons/FY4/fy4-7/figures.py (pallo_ek) — the axis runs to 6,5 m/s, but the description says "nollasta 6 metriin sekunnissa". The difference is harmless.

## Checked
- L2-08 (fy4-7/pallo-ek): the curve is E_k = 0,25 v², which is a 0,50 kg ball, and the mass is not shown. It passes (2; 1) and (6; 9) on 1 J grid lines, so ΔE_k = 9,0 J − 1,0 J = 8,0 J can be read to within 5 %. The check (three times the speed gives nine times the energy) uses the chapter's own v² rule.
- L2-09 (fy4-7/ep-kuvaaja): the line is E_p = 2,0 · 9,81 · h with the floor as zero level, as stated. At 2,0 m it is 39,2 J, 0,8 J under the 40 J grid line. A reading of 39 J or 40 J gives 1,99 kg or 2,04 kg, both inside 5 %. Solved m = E_p/(gh) first. The slope check mg ≈ 19,6 N is a real one.
- Neither task repeats an existing task: no other exercise uses these figures. L2-07 fits E_k from a table, and L2-08 reads ΔE_k directly.
- The descriptions give the points' values but no mass, so they hold the same information as the picture and do not give the answers away.
- Notation E_k, E_p, h, v and m as in the chapter. The zero level is named in L2-09.
- Recomputed in one script (my formulas beside python -I answers.py): 8,0 J and 2,00 kg. Both agree with exercises.json.
- Hash b2ac4ac61efac0df at the start and at the end.
