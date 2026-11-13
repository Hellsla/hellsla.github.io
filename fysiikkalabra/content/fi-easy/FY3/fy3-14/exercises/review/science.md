VERDICT: PASS
CONTENT-HASH: b2728409903da70a
SCOPE: delta added-exercise from c966a0c1c917e65e base 89bcb63b7431
Mode: delta (added exercises fy3-14-L1-09, fy3-14-L2-09)
Round: 1

## Blocking
(none)

## Polish
- None.

## Checked
- L1-09: ice already at 0 °C, so Q = sm; MAFY s = 333 kJ/kg, Q = 26,64 kJ, so 27 kJ; the 334 kJ/kg of the texts stays inside the 4 % tolerance and the solution says so; the check (warming 0,25 kg water by about 25 K) recomputed: 26,6/(4,19 · 0,25) = 25 K.
- L2-09: the boundary case is right: 5 kJ ≤ 25 kJ < 5 + 60 kJ, so the ice warms to 0 °C, part melts and the final temperature is 0 °C. Melted 20/334 = 59,9 g, total 179,6 g, left 119,8 g, so 120 g; tolerance 2 %.
- Figure energy-bars: bars end at 25, 5 and 60 kJ on the 5 kJ grid; the description gives the same values and not the answer.
- Solutions complete, symbolic first, units and rounding justified.
- answers.py matches my recomputation (26,64; 119,760).
- Scripted comparison with the Finnish: answer, unit, tolerance, figure, lookup and all numbers identical.
- Hash the same at start and end.
