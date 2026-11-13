VERDICT: PASS
CONTENT-HASH: 736f5d8b8a59c6e2
SCOPE: delta added-exercise from 36a9f0fc1bd88cd4 base 81db4a6fd727

## Blocking

## Polish

## Checked
- The round-1 polish is fixed. The pallo_ek description now says "nollasta 6,5 metriin sekunnissa", matching the axis x = (0, 6.5) in figures.py. The description still gives the same points as the picture and no mass.
- L2-08: the curve is E_k = 0,25 v². ΔE_k = 9,0 J − 1,0 J = 8,0 J, read at grid crossings (tolerance 0,05). The check (three times the speed gives nine times the energy) is a real one.
- L2-09: E_p = 2,0 · 9,81 · h, with the floor as the zero level as stated. A reading of 39 J or 40 J at 2,0 m gives 1,99 kg or 2,04 kg, inside 5 %. m = E_p/(gh) is solved in symbols first.
- Recomputed in one script (my formulas beside python -I answers.py): 8,0 J and 2,00 kg, both agreeing with exercises.json.
- Hash 736f5d8b8a59c6e2 at the start and at the end.
