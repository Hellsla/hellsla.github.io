VERDICT: PASS
CONTENT-HASH: 2e9af2ebebcd6069
SCOPE: delta added-exercise from 77b4b5a62a82d3a0 base 89bcb63b7431

## Blocking

## Polish
- exercises/solutions.md (fy3-8-L1-09, Järkevyys) — the expansion gap explains a jointed track; a modern welded rail is held in place and takes the change as stress instead. Optional: "jatkettavien kiskojen väliin". C, not an error.
- exercises/exercises.json (fy3-8-L2-09) — a student who reads the temperature straight off the line at 2,0 mm may say 55 °C, at the edge of the tolerance 0,03 (51,7–54,9 °C); the slope method the solution shows gives 53,3 °C exactly. Optional: tolerance 0,04.

## Checked
- MAFY value verified on mafytaulukot.fi (*Pituuden lämpölaajenemiskertoimia*, 25 °C): teräs $12 \cdot 10^{-6}\,\text{1/K}$, as the solution uses.
- L1-09 recomputed: $\Delta L = \alpha L_0 \Delta T = 12 \cdot 10^{-6} \cdot 25 \cdot 50 = 0{,}015\,\text{m} = 15\,\text{mm}$; answers.py agrees. ΔT 50 K within the ~100 K range where the brief says the linear model holds.
- L1-09 solution: formula symbolic, m → mm, two figures from 25 m and 50 K, check (1,2 mm per m per 100 K) real.
- L2-09 recomputed from the figure code: (20 °C; 0 mm) and (70 °C; 3,0 mm) on grid crossings (10 °C, 0,5 mm), $k = 0{,}060\,\text{mm/K}$, $\Delta T = 33{,}3\,\text{K}$, $T = 53{,}3\,{}^\circ\text{C}$; answers.py agrees.
- L2-09 physics: $\Delta L \propto \Delta T$ from the brief's $\Delta L = \alpha L_0 \Delta T$; K and °C differences handled correctly; interpolation stays inside the measured range.
- Figure description lists end points only, not the answer or α.
- Rest of the set unchanged since PASS; hash same at start and end.
