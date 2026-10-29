VERDICT: PASS
CONTENT-HASH: 52d1d3417776fda8

## Blocking

## Polish
- solutions.md L2-03 — Vastaus gives 0,23 kWh while answers.py and exercises.json hold 0,228; inside the 2 % tolerance, but state "0,228 kWh, eli 0,23 kWh" so they agree.
- exercises.json L1-02 — same data as the lesson's Etsi virhe item; physics right.

## Checked
- All 12 answers recomputed in one script with own formulas: 85, 30, 3,0, 2000, 4,0, 96, 54, 0,228, 45, 1,5, 2083,3, 180: all agree with answers.py and exercises.json.
- Units and conversions (kW, min, h, kWh, MJ) right; units and tolerances fit the 2-s.f. data.
- Each solution is symbolic first, states the principle, and has a real reasonableness check.
- L2-04 and L3-02 use P_o = P_a/eta and E_a = P_a t correctly (steady power stated by device running).
- L3-03 figure: grid 20 px, input 160 px = 8 squares, useful 2, loss 6, aligned to the grid; 180 J follows; figure gives only E_o, no answer disclosed.
- Notation matches the lesson (E_o, E_a, E_h, P_o, P_a, P_h, eta); no FY3 content.
