VERDICT: PASS
CONTENT-HASH: 232a260c1ced7f13

## Blocking
(none)

## Polish
- lesson.md:304 — reversed battery: "smaller by the source voltages of two batteries" is right for identical cells (2E). With unequal cells it reads as "any two cells" — write "smaller by twice the source voltage of the reversed battery (2E for identical batteries)".
- lesson.md:174 — the potential graph goes through E first and then R_s. The model figure (line 136), going from the − terminal, has R_s first and then E. The physics is the same, but the two figures could use the same order.
- inquiry.json:116 — howto says the fitted line is "extended to the axes". For the new single cell, I_k = 8.0 A lies beyond the graph's 4 A edge, so the line stops at the edge. Say "towards the axes" or "to the edge of the graph".

## Checked
- One script recomputed every number from the task text with my own formulas and matched lesson-answers.py: experiments 1–3 (U and I at R = 1, 2, 4, 8 Ω), R_s from rounded readings = 0.2006 Ω, series 2.286 V, parallel 1.455 V, worked example 0.3586 Ω and 4.406 A, error task 0.667 A and 8.0 V, transfer 10.44 V, (U/E)² = 0.687, I_k = 1050 A, exit 5.0 A.
- Check-graph points: the least-squares fit gives exactly U = 9.00 V − 2.00 Ω·I, so the answer 2.0 Ω is right. The mistakes 4.0 Ω (U : I) and 6.0 Ω (E : I) are diagnosed correctly.
- The ui-graph is to scale: E = 1.50 V, I_k = 5.0 A, and the slope triangle runs from 1 A to 3 A with ΔU = 0.60 V.
- Model figure: polarity is right, and the current arrows point − to + inside the battery and + to − outside. Connections figure: 2E, 2R_s in series and E, R_s/2 in parallel.
- Predictions: exactly one correct option in each. Every distractor's feedback cites the right model values. In check 1, the "smaller source voltage" distractor really is wrong as the main cause: with a 5 Ω lamp the power is 0.39 W from the E drop alone vs 0.27 W with R_s as well.
- Experiments: each one locks everything except the varied parameter. Experiment 3 leaves the switch free for the open-circuit reading. simState has I and U, and the adapter has the keys paristo, kennot, kytkin and R; reset matches the initial values.
- sim.js implements I = E/(R+R_s) and U = E − R_s I, the series and parallel groups, glow per cell from R_s I_cell², and conventional current. The voltmeter sits across the terminals, ahead of the switch.
- The model's limits are stated in the Formula section and in the sim's model box (constant E and R_s, ideal meters, no measurement scatter). The extrapolation to I_k is flagged.
- Magnitudes: AA cell 0.2 Ω and 8 A, Li-ion cells tens of mΩ, 21700/18650 dimensions, a car battery at hundredths of an ohm and >1000 A. The cold-weather mechanism is right.
- Scope: accumulators, internal resistance and series/parallel cells are within FY6. The parallel-connection warning for unequal cells is correct.
