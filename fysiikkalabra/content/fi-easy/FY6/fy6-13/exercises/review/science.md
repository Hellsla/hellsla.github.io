VERDICT: PASS
CONTENT-HASH: 6a392abb385170f5
SCOPE: delta added-exercise from f05516e505a8af1a base 8f23aa7ae3bd

## Blocking
- none

## Polish
- exercises.json fy6-13-L2-08 — "toisen kondensaattorin" refers to another task's capacitor; on its own the task reads more clearly as "kondensaattorin" (the figure id ex-qu2 already keeps them apart).

## Checked
- fy6-13-L1-10 recomputed: C = ε₀ε_r A : d = 8,854 · 10⁻¹² F/m · 2,3 · 0,025 m² : 1,0 · 10⁻⁴ m = 5,09 nF; matches answers.py and exercises.json; a table giving ε_r = 2,25 yields 4,98 nF (−2,2 %), inside tolerance 0,05.
- L1-10 conditions: thin film filling the gap and plates large compared with d, as the brief's plate-capacitor formula requires; cm² and mm conversions right.
- fy6-13-L2-08 recomputed: C = 120 µC : 8 V = 15 µF, W = ½ · 15 µF · (7,0 V)² = 367,5 µJ; matches; rounded 370 µJ is +0,7 %, inside tolerance 0,02.
- Figure fy6-13/ex-qu2 (figures.py): straight line from the origin to (120 µC; 8 V) on 20 µC and 1 V gridlines; alt text gives the end point; no C or W written.
- L2-08 physics: (Q, U) line through the origin because C is constant; energy from C and the given 7,0 V; check ½QU = 367,5 µJ < QU right.
- Both solutions complete (principle, symbolic formula, conversions, substitution, rounding reason, check); no capacitor connections or exponential (scope notes kept).
- Content hash checked at start and end.
