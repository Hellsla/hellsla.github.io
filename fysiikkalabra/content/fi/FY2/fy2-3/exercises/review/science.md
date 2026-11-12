VERDICT: PASS
CONTENT-HASH: eeada8a6d64780eb
SCOPE: delta added-exercise from 2d22792f6d7cc426 base 611fb7d5c174
Mode: delta
Round: 1

## Blocking

## Polish
- exercises.json fy2-3-L1-09 text / solutions.md L1-09 Annettu — the symbol "hp" usually means mechanical horsepower (about 745,7 W); 735,5 W is the metric horsepower (hv, PS). Both values are inside the 4 % tolerance (6,71 MJ vs 6,62 MJ), so nothing breaks (C). If you like, name the metric horsepower ("hevosvoima, hv") or note that the two values differ.
- exercises.json fy2-3-L1-09 text — the rated power of an engine is its output power, so "Kuinka paljon energiaa moottori muuntaa" really means the mechanical energy it gives. The fuel's chemical energy is several times larger. To leave no doubt, write "… muuntaa liike-energiaksi (mekaaniseksi energiaksi)".
- Earlier items outside this delta (L2-08 stove powers and wording, L1-08, L3-04 hydro MW, the plan's stair task) are still open.

## Checked
- Hash eeada8a6d64780eb at the start and the end. I judged only the added L1-09 and L1-10.
- L1-09 recomputed: P = 5,0 · 735,5 W = 3677,5 W, Δt = 1800 s, ΔE = PΔt = 6,6195 MJ, the same as answers.py; the stated 6,6 MJ is 0,3 % away.
- L1-09 solution: ΔE = PΔt is solved from P = ΔE/Δt before substitution. The conversions (hp → W, min → s, J → MJ) are shown, two significant figures follow the data, and the checks (≈ 6,7 MJ, ≈ 1,8 kWh) are right. The lookup is in the text and the hint in `hints`.
- L1-09 scope: P = ΔE/Δt is the lesson's formula, used under the task's stated condition "tasaisesti". A 3,7 kW outboard motor is realistic.
- L1-10 recomputed: line B passes (0; 0), (40 s; 20 kJ) and (80 s; 40 kJ), so P = 40 000 J : 80 s = 500 W, the same as answers.py. A 2 % tolerance fits an exact grid reading.
- L1-10 figure: the drawing (ax.line to (80, 40)) and its description agree. B is the gentler line, the points fall on grid crossings, and no power or slope triangle gives the answer away.
- L1-10 solution: the slope gives the power (the lesson's statement), and the second point is a real check (also 500 W). The comparison with A (1500 W, as in L1-04) agrees.
- L1-10 uses the same figure as L1-04 but reads the other line, so it does not repeat that task.
