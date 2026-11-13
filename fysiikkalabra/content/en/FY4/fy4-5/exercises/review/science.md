VERDICT: PASS
CONTENT-HASH: 0e0928bdaf93292f
SCOPE: delta added-exercise from 0856c4022f143716 base 7db0992d648a
## Blocking

## Polish
- content/en/FY4/fy4-5/exercises/solutions.md fy4-5-L2-08 Answer — "53° above the horizontal" in a top view where every force is horizontal; same as the passed Finnish ("vaakasuunnasta ylöspäin") — consider "53° from the x axis towards +y" in both languages.

## Checked
- L2-08: frictionless horizontal ice, vertical forces cancel (stated); ΣF_x = 10 N − 4.0 N = 6.0 N, ΣF_y = 12 N − 4.0 N = 8.0 N, ΣF = 10 N, a = 10 N / 2.5 kg = 4.0 m/s² (recomputed).
- Figure ruutu-vinot: scale 14 px/N = 28 px per 2.0 N square, F_1 (10;12) N = 5;6 squares, F_2 (−4;−4) N = 2;2 squares, scale bar 2 squares = 4.0 N; description matches; no net force drawn.
- voimakuvio spec: |F_1| = 15.62 N at 50.19°, |F_2| = 5.657 N at 225°, a at 53.13° all consistent with the components; force-diagram checklist: only interactions on the puck, no velocity as a force, nothing double-counted.
- answers.py line equals my value and exercises.json.
- en vs fi: answer, unit, tolerance, figure id, fbd skill and every number of text and solution identical.
