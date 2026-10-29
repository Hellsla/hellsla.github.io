VERDICT: PASS
CONTENT-HASH: 2f5b71320a9d05a7

## Blocking
(none)

## Polish
- exercises.json fy2-3-L3-02 — the question also asks "suurempi vai pienempi ... ja miksi", which the numeric answer does not check and no data decides — keep as a reasoning prompt or give an example nominal sum.

## Checked
- Recomputed all 12 answers in one script: 2000 W, 40 J, 60 s, 1500 W, 3,0 kWh, 3,0 €, 54 000 J, 1200 W, 78,84 kWh, 15,18 €, 342,5 W, 102,2 km all agree with answers.py and exercises.json.
- Tolerances fit: 2 % covers the rounded 79, 15 and 340; 3 % covers 100 km.
- graph-ab: line A (40 s; 60 kJ) to (80 s; 120 kJ) gives 1500 W; B gives 500 W as in the solution; the figure does not give the answer away.
- Solutions complete, symbolic first, conversions right (kWh to J, min to s, W to kW); sig figs justified.
- L3-03 states that charging losses are ignored; no work, force or later-course physics used.
