VERDICT: PASS
CONTENT-HASH: 1ecf085acd3d008f
SCOPE: delta added-exercise from 5338796927c96918 base 81db4a6fd727
## Blocking

## Polish

## Checked
- L1-09 (final fix): locked wheels sliding, so the sliding coefficient (liukukitkakerroin, teacher's choice) is the right one; level road, no air resistance stated; a = μg = 0,8 · 9,81 = 7,85 m/s², s = (22,22 m/s)²/(2 · 7,85 m/s²) = 31,46 m → ≈ 31 m (recomputed); exercises.json 31.46 equals fi and answers.py.
- L1-09 range: μ = 0,8 is the table range's upper end, giving the shorter extreme; μ = 0,5 gives 50,3 m ≈ 50 m, so the stated "longer at the lower end" is right; comparison with ABS on dry asphalt (μ ≈ 0,9, brief's 0,92) consistent. Tolerance 5 % accepts 31 m and 30 m.
- L2-09: rectangle 20 m/s · 1,0 s + triangle ½ · 20 m/s · 2,5 s = 45 m (recomputed from figures.py); deceleration 8,0 m/s² plausible; 70 m upper bound check right.
- L3-06: Δv = 15 m/s, Δt_A = 0,060 s, Δt_B = 0,150 s; F_A = 17,5 kN, F_B = 7,0 kN, difference 10,5 kN (recomputed); linear v(t) justifies constant force; ratio 2,5 = inverse time ratio.
- Both figures give the needed values (0,150 s halfway between 0,14 and 0,16 gridlines, also in the description) and show no answer.
- All 24 tasks: answer, unit, tolerance, figure, data and correct options equal the Finnish set; answers.py agrees.
- Hash unchanged at start and end.
