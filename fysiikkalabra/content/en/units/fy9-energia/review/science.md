VERDICT: PASS
CONTENT-HASH: e22d2e4b5a939769
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: s7 d states that the car that drove the furthest lost the largest share. The table supports this only among its three cars; if the chart of all 24 cars shows a larger deviation for another car, write "one of the largest shares".
- C: s7 c, the density argument could say in one clause that the mass per volume grows in the same ratio as n/V.

## Checked
- Every item 18 hunk (unit.md, inquiry.json, figures.json, solutions.md, tasks.json): "internal energy / transferred to the surroundings as heat" is carried out correctly and agrees with the numbers around it (67.5 kJ - 54 kJ = 13.5 kJ; 289 - 216 = 73 MWh). Fridge share 1.08 kWh : 1.54 kWh = 70 %, the corrected sentence is right.
- s7 recomputed with my own formulas: a -28.9 %, -42.9 %, -45.8 %, mean 39.2 %, wrong denominator 41 %; b 16.67 kWh, 279 km, 26.88 kWh, factor 1.61, 600 N, wrong method 23 kWh; c temperature differences 27 K and 52 K (ratio 1.93), 15 kWh = a fifth of 75 kWh, density +15.8 % at -20 C against +20 C. All agree with tasks.json, the solution and answers.py (practice.py check OK).
- Physics of c (heat transfer, P = UI, RI^2 and terminal voltage, W = Fs), the confounding argument of d and the experiment design of e are right and within FY1-FY8; rubric points add up to each part's points (3, 4, 4, 2, 2) and every criterion asks only what the task gives.
- Hash the same at the start and the end.
