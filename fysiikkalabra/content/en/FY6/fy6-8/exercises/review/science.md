VERDICT: PASS
CONTENT-HASH: a65b3da0c07dac65
SCOPE: delta added-exercise from abbe309450785620 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- none

## Checked
- fy6-8-L2-09 recomputed: R_s = (11 V − 7 V) : (250 A − 50 A) = 0.020 Ω; answers.py and exercises.json agree; unit Ω, tolerance 0.04.
- Figure fy6-8/ex-graph-car (figures.py): points U = 12 − 0.02 I at 50…250 A give 11, 10, 9, 8, 7 V, all on the 50 A / 1 V gridlines; the line is drawn only over the data, so neither E nor I_k nor the slope is given away; the description lists the same points.
- Model U = E − R_s I is the lesson's model (answers.py header); the solution derives R_s from two points by subtracting the equations, symbolically before numbers, and says why U : I at one point is the load resistance, not R_s.
- The task says the points are calculated from a model, so no invented data is presented as measured (guardrail: say whether data are measured, simulated or calculated).
- Magnitudes: E = 12 V and R_s = 20 mΩ are realistic for a car starter battery; currents of hundreds of amperes fit the starter motor.
- Reasonableness checks are real: a third point (150 A; 9 V) gives the same slope; E = 11 V + 0.020 Ω · 50 A = 12 V.
- Inside FY6 central contents (batteries; internal resistance of a source, the experimental work named in LOPS).
- Recomputed in one script together with fy6-1, -2, -3, -4, -6, -7; content hash checked at start and end.
