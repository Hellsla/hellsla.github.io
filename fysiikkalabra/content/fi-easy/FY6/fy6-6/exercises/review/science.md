VERDICT: PASS
CONTENT-HASH: d41d82457f2f3aac
SCOPE: delta added-exercise from bd18cf01612b6d99 base c7f5e91173b0

## Blocking
- none

## Polish
- solutions.md fy6-6-L2-09 Vastaus — "kolme merkitsevää numeroa" rests on exact gridline readings while the task's time 12 min has two figures; either keep with that reason or give $7{,}8 \cdot 10^{2}\,\text{kJ}$ (both inside the tolerance).

## Checked
- fy6-6-L2-09 recomputed: E = 2000 W · 180 s + 1000 W · 300 s + 500 W · 240 s = 360 + 300 + 120 = 780 kJ; matches answers.py and exercises.json (unit kJ, tolerance 0,02).
- Model: E = Pt per constant-power step, summed (area under the (t, P) graph); a hob plate is resistive, so all the electrical energy becoming internal energy is right.
- Figure fy6-6/ex-pt (figures.py): steps 2000 W 0–3 min, 1000 W 3–8 min, 500 W 8–12 min, 500 W and 1 min gridlines, so every value is read on a gridline; alt text gives the same; no energy shown.
- Solution complete: principle, symbolic sum, min → s conversions, substitution, check by mean power 1,08 kW between 0,5 and 2,0 kW.
- Content hash checked at start and end.
