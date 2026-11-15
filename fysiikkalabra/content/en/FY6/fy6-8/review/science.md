VERDICT: PASS
CONTENT-HASH: 232a260c1ced7f13

## Blocking
(none)

## Polish
- lesson.md:304 — reversed battery: "smaller by the source voltages of two batteries" is right for identical cells (2E). With unequal cells it reads as "any two cells" — write "smaller by twice the source voltage of the reversed battery (2E for identical batteries)".
- lesson.md:174 — the potential graph goes through E first and then R_s. The model figure (line 136), going from the − terminal, has R_s first and then E. The physics is the same, but the two figures could use the same order.
- inquiry.json:116 — howto says the fitted line is "extended to the axes". For the new single cell, I_k = 8.0 A lies beyond the graph's 4 A edge, so the line stops at the edge. Say "towards the axes" or "to the edge of the graph".

## Checked
- One script recomputed every number from the task text and matched lesson-answers.py (experiments 1–3, R_s = 0.2006 Ω, 2.286 V and 1.455 V, worked example 0.359 Ω and 4.41 A, error task, transfer 10.44 V, exit 5.0 A).
- Check-graph: the least-squares fit is exactly U = 9.00 V − 2.00 Ω·I. The mistakes 4.0 Ω and 6.0 Ω are diagnosed correctly.
- The ui-graph is to scale (1.50 V, 5.0 A, ΔU = 0.60 V over 2.0 A).
- Model and connections figures: polarity, current arrows, 2E/2R_s and E/R_s/2 are all right.
- Every choice item has exactly one correct option, and the feedback cites the right model values. In check 1, the "smaller E" distractor really is wrong (5 Ω lamp: 0.39 W from the E drop alone vs 0.27 W).
- Each experiment isolates its varied parameter; experiment 3 leaves the switch free on purpose. simState gives I and U, and the adapter keys and reset match.
- sim.js implements the lesson's model, the cell groups, the glow per cell and conventional current. The voltmeter is across the terminals.
- The model's limits are stated in the Formula section and the sim box, and the extrapolation to I_k is flagged.
- Magnitudes (AA, Li-ion, car battery) and the cold-weather mechanism are right.
- Scope is within FY6.
