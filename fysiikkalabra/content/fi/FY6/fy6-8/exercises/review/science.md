VERDICT: PASS
CONTENT-HASH: af384e5fbc815b56
SCOPE: delta added-exercise from fe154ae5f2ac3508 base 8f23aa7ae3bd

## Blocking

## Polish
- content/fi/FY6/fy6-8/exercises/solutions.md (fy6-8-L2-09, Vastaus) — "kaksi merkitsevää numeroa, koska arvot luetaan ruudukolta" is thin: say that the read points lie exactly on gridline crossings, which justifies 0,020 Ω.

## Checked
- Hash af384e5fbc815b56 at start and end; delta round 2: only fy6-8-L2-09 judged.
- Round-1 blocking item resolved: the task now says "(mallista lasketut pisteet)" and the figure's alt text "Mallista lasketut pisteet ovat …", matching figures.py, which draws the points exactly from U = 12 V − 0,020 Ω · I.
- Figure generator: points (50; 11), (100; 10), (150; 9), (200; 8), (250; 7) on the line drawn over the data only (no E or I_k shown); gridlines 50 A and 1 V; alt text gives the same points.
- Model U = E − R_s I, slope −R_s; the solution derives R_s = (U₁ − U₂) : (I₂ − I₁) before numbers and warns that one point's U : I is the load resistance.
- Recomputed: R_s = 4 V : 200 A = 0,020 Ω; answers.py agrees; unit Ω and tolerance 4 % fit.
- Magnitudes realistic (E = 12 V, 20 mΩ, 7 V at 250 A); check with the third point and E = 12 V is a real check.
