VERDICT: PASS
CONTENT-HASH: 5546f60acb4da541

## Blocking

## Polish
- lessons/FY6/fy6-4/figures.py:123 — the task-mixed figure (L3-01) draws a node dot at the top-right corner (R, T), where nothing branches. The only real junctions are (xa, T) and (R, ym). It is harmless to the physics, but the figure shows a third "branch point". Fix: drop `node(f, xa, ym)` and `node(f, R, T)`.

## Checked
- I recomputed all 12 answers in one script with my own formulas and compared them with answers.py: 670, 24, 1.50, 2.7, 110, 4.787→4.8, 35, 20, 1.32→1.3, 50, 4, 150. All agree, and each stored answer is within its tolerance (largest gap 1.5 % for L2-04, tolerance 0.03).
- Round-1 polish is done. L1-04 now names the measured lamp "ensimmäinen". L3-03 states that the data are taken as exact because of the small discriminant; I confirmed the sensitivity: Rr = 60.5 Ω gives 147 Ω.
- L3-01 "Kuvan lukeminen" now justifies the series connection by the whole battery current passing through R1. The figure gives every value needed, its topology is right, and the description does not give the answer away.
- answers.py: each line uses the right law (series sum, parallel reciprocal, Kirchhoff current sum, voltage split, Ohm's law in each part).
- L3-02: the ratio of 4 is derived symbolically. The task states constant resistance, and the powers are realistic (575 W and 2.3 kW).
- Every solution solves symbolically first, converts k → Ω and A → mA correctly, names the limiting datum, and makes a real reasonableness check.
- Notation matches the brief: R, R23, I = I1 + I2, and the colon for division in prose. Scope is "vastusten kytkennät".
