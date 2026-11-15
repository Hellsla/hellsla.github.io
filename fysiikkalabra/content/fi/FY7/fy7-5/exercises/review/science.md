VERDICT: PASS
CONTENT-HASH: 5cd62b0183fa3d77

## Blocking

## Polish
- docs/figures/catalog.json:927–928 — the catalog descriptions of `fy7-5/flux-task` and `fy7-5/flux-task-2` still say "millivebereinä", while figures.py now says "milliwebereinä" (the packet's figure list was built from the catalog) — regenerate the catalog (figcat) so that the description the figure gets matches figures.py. This file is outside the exercise set, so it does not block.

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas (Φ = BA, |e| = N|ΔΦ|/Δt, e = vBl, I = e/R, NBlv, 2BA for the flip coil, triangle and trapezoid areas, fits through the origin). They agree with answers.py and exercises.json, and every rounded answer is within its tolerance (largest gaps: L1-07 2.2 % against 3 %, L3-04 2.7 % against 4 %).
- L1-09 ordering: C 0, D 0.60, A 1.2, E 2.0, B 3.0 V. It is correct, and the two wrong lines of reasoning in the model answer move the situations as it says.
- L1-06, L2-07: each has exactly one correct option, every distractor is really wrong, and each feedback gives the right reason. In L2-07, v ∥ B gives no force on the electrons and no change in flux.
- L2-05: interval ΔΦ values recomputed; the steepest is 0.40–0.50 s, 1.21 mWb → 1.45 V. Three significant figures is justified by the table.
- L2-06, L3-04: the ratios e/v and e/t fall in the ranges stated. A free fit gives an intercept ≈ 0, which supports the line through the origin (t counted from rest, e = aBl·t). s = ½at² = 1.18 m.
- L3-05: trapezoid areas 0.01946 and −0.01968 V·s → 0.078 and 0.079 mWb. The explanation of the sign and the narrower, taller second pulse is consistent with the data (peak 2.16 vs 1.77 V).
- L3-01: correct argument that only the vertical component of B gives a force along the axle (v × B_h is vertical). 4.23 mV → 4.2 mV.
- L3-02: ΔΦ = 2BA for a half turn, B = 50 µT, a realistic value for Finland. L3-03: the task states that the flux is zero at the start and largest at the end of the pulse.
- Figures: the flux-task and flux-task-2 polylines give every value the solutions read (4.0 mWb over 0.20/0.10 s; 5.0 → −3.0 mWb over 0.40 s). Neither shows a voltage. The alt text in figures.py matches the drawing.
- Scope and notation: induction, e = vBl and the flux graph, as in the brief. There is no self-induction, and Lenz's law is deferred to its own chapter. Every solution solves symbolically before substituting. The fixes in this round (weber, tesloina) changed no physics. A grep finds no "veber" or "teslaina" left in the exercise set, answers.py or figures.py.
