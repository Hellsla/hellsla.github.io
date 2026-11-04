VERDICT: FAIL
CONTENT-HASH: 356ba65090c8758b

## Blocking
- solutions.md:109 (fy6-15-L3-02) and solutions.md:39 (L1-04) — B: rubber shoes are called "tämän suojan", and 2,3 mA and 4,6 mA are presented with no condition. This holds only for intact, dry soles, a dry floor and a single contact to earth; a hand on a tap or an earthed appliance bypasses the shoes — fix: add one sentence saying so, and that shoes are no protection to rely on.

## Polish
- solutions.md:29 (L1-03) — "Kymmenen kertaa jännite on 2300 V" compares volts with ohms. Say that the resistance is ten times the voltage's numerical value.
- lessons/FY6/fy6-15/figures.py:366 — "(4 m; 300 V)" is called a grid intersection, but the grid is 200 V.
- exercises.json:66 (L2-03) — only the solution says that 3,0 cm is a uniform-field lower bound and that real distances are metres. Add "laskennallinen alaraja" to the task text.
- solutions.md L3-03 — a foot-to-foot path carries little current through the heart. Add that a fall can put the heart in the current path.

## Checked
- All twelve answers were recomputed with my own formulas and match answers.py: 8,70 A; 2300 W; 100 mA; 4,6 mA; 51,2 W; 480 W; 22,7 W; 3,0 cm; 15 V; 4,84; 2,27 mA; 50 mA.
- L2-03: 90 kV is the peak phase-to-earth voltage of a 110 kV line, and the solution states the uniform-field condition.
- L3-03: the figure model V = 1200 V·m / r gives 600 V and 400 V on gridlines, and the 4–5 m difference is 60 V.
- L3-01 reinforces the rule against fitting a larger fuse, and its (22 : 10)² ratio is correct.
- L2-01, L2-02 and L1-05: the remainder, the cord-drop assumption (2,6 V) and the coiled-cord warning are correct.
- Every solution is solved symbolically first, and its rounding follows the limiting datum.
