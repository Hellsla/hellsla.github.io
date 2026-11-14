VERDICT: PASS
CONTENT-HASH: 0cb6ba559dd03245

## Blocking

## Polish
- lessons/FY5/fy5-9/answers.py — docstring says Mars g = 3,71 m/s² while L1-09 uses MAFY's 3,72 m/s²; both are right for their tasks (L2-04 gives its own value), a comment would avoid confusion. Optional.

## Checked
- Delta round 2, fi-easy: added fy5-9-L1-09 (MAFY Mars pendulum), L1-10 (energy from x(t)), L2-09 (maximum speed from x(t)).
- Compared by script with the passed Finnish set: answer, unit, tolerance, figure, lookup, level identical; every number in task text and solution the same in fi and fi-easy.
- Recomputed independently: L1-09 T = 2π√(1,00/3,72) = 3,258 s -> 3,26; L1-10 E = ½ · 120 · 0,030² = 0,054 J; L2-09 v_max = 2πA/T = 2π · 0,030/0,40 = 0,471 -> 0,47 m/s. answers.py agrees; tolerances fit.
- Figure kuvaaja-k: 3cos(2πt/0,40) cm, maxima at 0; 0,40; 0,80 s, minima at 0,20; 0,60 s, A = 3,0 cm, as the solutions read; no k shown, so L2-09 rightly uses 2π/T = √(k/m).
- Conditions stated: small swings for the pendulum, frictionless oscillation for energy conservation.
- Reasonableness checks real: Earth pendulum 2,01 s and ratio 1,62; v_max = (π/2) · mean speed 0,30 m/s.
- No SCOPE line in the packet, so none written.
- Hash same at start and end.
