VERDICT: PASS
CONTENT-HASH: 3ddcea2954d318b6
SCOPE: delta added-exercise from f6987a85f62564f9 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- exercises/solutions.md fy6-7-L2-08 Answer — "the values are read from the grid lines of 0.4 kW": the cooling power 0.2 kW lies halfway between two gridlines, not on one. Could say "0.2 kW lies halfway between gridlines". A misreading of ±0.1 kW changes the cost by only 2 %, inside the 0.03 tolerance, so the answer is safe.

## Checked
- fy6-7-L1-10 recomputed: E = Pt = 1.5 kW · 2.0 h = 3.0 kWh; 3.0 · 3.6 MJ = 10.8 MJ; the stated 11 MJ is 1.9 % off, inside tolerance 0.04; 1 kWh = 3.6 · 10⁶ J is exact (1000 W · 3600 s).
- fy6-7-L2-08 recomputed: E = 2.4 kW · 0.5 h + 1.2 kW · 1.0 h + 0.2 kW · 0.5 h = 2.5 kWh; K = 0.18 €/kWh · 2.5 kWh = 0.45 €; answers.py and exercises.json agree; unit €, tolerance 0.03.
- Figure fy6-7/dryer (figures.py): steps 2.4 kW (0–0.5 h), 1.2 kW (0.5–1.5 h), 0.2 kW (1.5–2.0 h), then 0; gridlines 0.4 kW and 0.25 h; no energy or cost shown; description carries the same values.
- Realistic magnitudes: a 2.4 kW heating stage and 2.5 kWh per program are typical for a tumble dryer; 18 c/kWh a plausible price.
- Both solutions: E = Pt with the condition "power constant" stated, the energy as rectangle areas, the price conversion c → €, symbolic formulas before substitution, rounding stated, real reasonableness checks (average power 1.25 kW; 3 · 4 MJ upper bound).
- Inside FY6 central contents (electric power; household energy builds on FY2 kWh).
- Content hash checked at start and end.
