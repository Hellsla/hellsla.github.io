VERDICT: PASS
CONTENT-HASH: eaf9669e846ed993

Re-review after the typesetting round (diff since the PASS: table headers $\theta$ and $p$ as maths in lesson.md and in the example task of inquiry.json; "95 kPa" as $95\,\text{kPa}$; learning goals rephrased).

## Blocking
- none
## Polish
- none
## Checked
- Changed items carry the same values and units: header symbols theta (°C) and p (kPa) match the formula section and figure; axis start 95 kPa unchanged.
- Recomputed the example data (7 points): least-squares slope 0,367 kPa/°C, p0 = 101,3 kPa, theta0 = -276 °C; matches the figure text and model answer.
- Two-point task: A(20,0; 108,6), B(90,0; 134,3) gives k = 0,367, theta0 = -275,8, answer -276 ok. Second task (30; 133,0), (90; 159,0) gives -276,9, answer -277 ok.
- Extreme lines: steepest 100,1 + 0,387 theta gives -258,7; shallowest 102,3 + 0,347 theta gives -294,8; half-range 18 °C; both touch the stated bar ends (10 and 85 °C; 100 °C). Result (-276 +/- 18) °C contains -273,15 °C; wording says estimate, not guaranteed limit.
- Scope and conditions (rigid vessel, constant n and V, extrapolation caveat) unchanged. LaTeX valid: \,, decimal {,}, units in \text.
- Learning goals still the same three goals, no change of physics.
