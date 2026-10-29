VERDICT: PASS
CONTENT-HASH: 4c9468244fe46189

## Blocking
(none)

## Polish
- solutions.md fy2-7-L1-02 "Vastaus" — says "noin 32 MWh" while exercises.json/answers.py hold 32,4 (tolerance 3 %); state "32,4 MWh, noin 32 MWh".
- exercises.json fy2-7-L3-03 — "tasaisesti 150 kW" is stated, but a real network's loss varies with the season; the word "esimerkkitilanne" would mark it as an invented case, as the other tasks do.

## Checked
- Hash at start and end 4c9468244fe46189.
- Recomputed all 12 answers with own formulas in one script: 480; 32,4; 96,0; 120; 60; 150; 1500; 10,96 -> 11; 1200; 21,04 -> 21; 13,0; 65,7 -> 66. All match exercises.json and answers.py.
- Loss share always taken of the energy/power sent; L2 tasks divide by η, not multiply; wrong-base remarks in solutions correct (120 MWh, 1152 kWh).
- Units and conversions (GWh, TWh, kWh -> MWh, 8760 h) right; rounding reasons match the limiting datum.
- L1-02 reads 9 % off the Sankey figure, which carries that number and is to scale.
- Scope: only E_häviö, η, P = E : t; no later-course physics. Solutions complete and symbolic first; reasonableness checks are real checks.
