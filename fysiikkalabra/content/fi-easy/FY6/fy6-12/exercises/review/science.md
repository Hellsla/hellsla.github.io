VERDICT: PASS
CONTENT-HASH: d29240691e2c2f1f
SCOPE: delta added-exercise from 5d9a1e2a7804d5aa base 8f23aa7ae3bd

## Blocking
- none

## Polish
- none

## Checked
- fy6-12-L2-09 recomputed: V(1,0 cm) = 50 V, V(5,0 cm) = 250 V, U = 200 V; v = √(2eU/m) = 8,387 · 10⁶ m/s; matches answers.py and exercises.json (unit m/s, tolerance 0,02; rounded 8,4 · 10⁶ is +0,2 %).
- Physics: an electron from rest moves towards higher potential, its E_p falls by eU and E_k rises as much; only the electric force works (stated in the task); 2,8 % of c, so ½mv² holds — consistent with the brief's Kaava and worked example.
- Figure fy6-12/ex-vgraph (figures.py): straight line from (0; 0 V) to (5,0 cm; 250 V) on 1 cm and 50 V gridlines, so both needed potentials sit on gridlines; alt text gives the line's ends, from which the reader gets the same values; no answer marked.
- Distinct from the worked example (potential difference read from a graph and a start point inside the gap).
- Solution complete (given, principle, symbolic v, units, substitution, rounding reason, check against c and the 3,0 kV example).
- Content hash checked at start and end.
