VERDICT: PASS
CONTENT-HASH: e590443b79e2e26e
SCOPE: delta added-exercise from 814ed3c8b96c2177 base 89bcb63b7431
Mode: delta (added exercises fy3-16-L1-09, fy3-16-L2-09, fy3-16-L2-10)
Round: 1

## Blocking
(none)

## Polish
- solutions.md fy3-16-L2-09 Kuvaajan lukeminen — "Kuvaaja on suora. Siksi teho on vakio." reads the cause backwards: the power is given as constant, and that (with constant c and small losses) is why the line is straight. A fix: "Teho on vakio, joten kuvaaja on suora" (also in the Finnish).

## Checked
- L1-09: water already at 100 °C, so Q = rm; MAFY r = 2260 kJ/kg, Q = 678 kJ, so 680 kJ; the comparison with heating 0–100 °C (126 kJ, more than five times) recomputed.
- L2-09: Pt = cmΔT with no losses as the task states; figure from (0 s; 20 °C) to (180 s; 60 °C), on grid crossings; c = 72 000 J / 80 kg·K = 900 J/(kg·K). The loss remark has the right direction (the true c is below the computed one).
- L2-10: figure melting-curve consistent with 0,60 kg ice: 2100 · 0,60 · 16 = 20,2 kJ and 334 · 0,60 = 200,4 kJ, so 220 kJ; after melting 80 kJ gives 31,8 K for water (drawn 31,9). t = 220 kJ / 25 W = 8800 s = 2,44 h; my value from the constants, 2,45 h, is inside the 3 % tolerance.
- Figure descriptions give the read points and not c or t.
- Solutions complete, symbolic first, conversions and rounding justified.
- answers.py matches my recomputation.
- Scripted comparison with the Finnish: answer, unit, tolerance, figure, lookup and all numbers identical.
- Hash the same at start and end.
