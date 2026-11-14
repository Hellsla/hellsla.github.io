VERDICT: PASS
CONTENT-HASH: 9da0b30d57e17342

## Blocking
None.

## Polish
1. answers.py docstring writes L = 10 dB · lg(I/I0); equivalent to the MAFY form the solutions use (code comment only).

## Checked
Full review (fi-easy: exercises.json, solutions.md, answers.py). The change: L2-09 answer 5.0 mW, tolerance 0.04 (4,8–5,2 mW), matches the solution's Vastaus 5,0 mW (2 s.f., r = 2,0 m read from the figure); answers.py gives 5,027 mW, inside; readings at the 4 m (74,0 dB) and 8 m (68,0 dB) points give 5,05 and 5,07 mW, also inside. Recomputed every answer with my own formulas: L1-01 2,0·10⁻³; L1-02 75,05 dB; L1-03 3,16·10⁻³; L1-04 2,55·10⁻⁴ W/m²; L1-05 20 dB; L1-08 120 dB; L1-09 2,51·10⁻⁵ W/m²; L2-01 86,46; L2-02 1,76; L2-03 72,96 dB; L2-04 3,98 → 4; L2-05 6,025 dB; L2-06 3,96 dB; L2-07 2,51; L2-08 10⁴; L3-01 84,63 dB; L3-02 15,8 m; L3-04 315 m (answer 320, tol 5 %); L3-05 44,6 m; every answer field within its tolerance of my values in fi, fi-easy and en. Solutions state the law first, solve symbolically, rounding reasons sound; choice keys (L1-06, L1-07, L2-08) and their feedback correct; L3-03 negative level and L2-06 reflection explanation correct.
