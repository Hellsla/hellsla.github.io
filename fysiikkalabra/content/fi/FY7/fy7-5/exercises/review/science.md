VERDICT: PASS
CONTENT-HASH: 5cd62b0183fa3d77

## Blocking
- none

## Polish
- solutions.md fy7-5-L3-05 Periaate — writes eΔt = −NΔΦ while the task's first pulse is positive as the flux grows; add "etumerkki riippuu käämin kytkennästä, joten lasketaan itseisarvoja" so the sign does not look contradictory (same in L3-03 if wished).
- exercises.json fy7-5-L3-05 — the example data's peak ratio 2,16 : 1,77 ≈ 1,22 with ~20 ms between peaks implies a speed of about 0,9 m/s at the coil (Δv = gΔt ≈ 0,2 m/s), i.e. a drop of only ~4 cm, which sits awkwardly with "magneetti on kaukana käämistä"; a smaller ratio (~1,1) fits a drop of 15–20 cm. The explanation and the area result are unaffected.

## Checked
- Hash 5cd62b0183fa3d77 (--exercises) at start and end.
- All answers recomputed in one script with own formulas: L1-01 5,04→5,0 mWb; L1-02 3,0 V; L1-03 0,20 V; L1-04 0,36 mWb; L1-05 0,50 m/s; L1-07 2,25→2,3 V (tolerance 3 % covers both roundings); L1-08 0,060 T; L1-09 order C 0 < D 0,60 < A 1,2 < E 2,0 < B 3,0 V; L2-01 48 mV; L2-02 2,0 V; L2-03 0,30 A; L2-04 75 mV; L2-05 1,452 V; L2-06 least squares 0,1498 T, ratios 29–31 mV/(m/s); L2-08 4,0 V; L3-01 4,23 mV; L3-02 50 µT (ΔΦ = 2BA); L3-03 0,060 mWb; L3-04 a = 1,64 m/s², s = 1,18 m; L3-05 areas 0,01946 and −0,01968 V·s → 0,0778 and 0,0787 mWb. answers.py implements the same physics.
- Task figures flux-task and flux-task-2 (figures.py) hold the values the solutions read; L2-08 asks only 0–0,40 s where the graph is straight.
- L3-01: only the vertical component gives an axle-directed force; reasoning correct.
- L2-07, L1-06: exactly one correct option; distractor feedback correct (open-circuit rod still has e = vBl; current is consequence, not cause).
- Solutions symbolic first, conversions right, significant figures justified by the limiting datum, reasonableness checks real (flux-sweep cross-checks, field magnitudes).
- Scope: Φ, induction law, vBl, Ohm's law and uniform acceleration from earlier courses; no self-induction.
