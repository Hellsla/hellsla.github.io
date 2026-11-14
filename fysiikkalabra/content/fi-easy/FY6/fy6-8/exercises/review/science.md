VERDICT: PASS
CONTENT-HASH: 8a4aaa9b86ce5839
SCOPE: delta added-exercise from 7090f26f691f0c78 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- none

## Checked
- fy6-8-L2-09 recomputed: R_s = (11 V − 7 V) : (250 A − 50 A) = 0,020 Ω; E = 11 V + 0,020 Ω · 50 A = 12 V; matches answers.py and exercises.json (unit Ω, tolerance 0,04).
- Model U = E − R_s I with R_s from the slope, not from one point's U : I — the solution says why (that would be the load's resistance); consistent with the brief's Kaava and its "two distant points on the line" rule.
- Figure fy6-8/ex-graph-car (figures.py): points 12 − 0,02 I at 50…250 A, line only over the data (no intercepts or slope written, so the answer is not given away); 50 A and 1 V gridlines put both read points on gridlines; alt text lists the same points.
- Magnitudes plausible for a lead-acid starter battery under cranking load (tens of mΩ, E 12 V); the task states the points are computed from a model, so no invented measured data.
- Solution complete: symbolic derivation by subtracting the two equations, no conversions, substitution, rounding reason, check with a third point and E.
- Content hash checked at start and end.
