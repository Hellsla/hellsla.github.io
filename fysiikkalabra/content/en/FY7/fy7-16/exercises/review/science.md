VERDICT: PASS
CONTENT-HASH: adf32c4933691232

## Blocking

## Polish
- solutions.md fy7-16-L2-10 — the figure's curve is drawn with a = 0.30 dB/km (halving at 10.03 km), which gives 0.79 % at 70 km. The solution reads 10 km and gives 0.78 %. Both are inside the 5 % tolerance, so this is fine — optional: say "about 0.8 %" in the reasonableness check.
- solutions.md fy7-16-L3-02 Reasonableness — "the result is an upper limit" holds only inside the stated model (B₀ given at the base). In a steel base the ferromagnetism raises the heating, as L3-05 c) says — optional: write "an upper limit for this loop model".

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas (dB attenuation, P = RI², Φ = BA, e₀ = N·2πf·Φ₀, P = e₀²/(2R), Q = cmΔT, t = nL/c, interpolation, least-squares line through the origin). All match answers.py and the answer values.
- Figure charger-points: I recomputed the loop-flux model. The 3 mm panel gives 6 lines and the 6 mm panel gives 4, with a model flux ratio of 0.669 (2.81 V). This matches L2-09's 2.8 V. The description says lines are drawn at equal flux steps but does not give the count.
- Figure graph-curve: 100·10^(−0.030 L) puts the halving at 10 km and 6.3 % at 40 km. The task data and the solution agree with it, and the 70 km value is extrapolated by calculation, as the solution says.
- L2-08: exactly one correct option (11.8 ms). Each distractor's unit-error feedback gives exactly its value (11.8 µs, 1.18 ms, 11.8 s).
- L1-06: exactly one correct option, and each distractor's feedback gives the right physics (glass does not block the field; Lenz's law gives a direction and does not cancel currents).
- L3-01: 1172/111.1 = 10.55 → 11 sections → 10 amplifiers. The rounding reason and the task's assumptions (equal sections, amplifiers between them) are stated.
- L3-04: the fluxes 0.377…0.0384 µWb, Φ_min = 0.1061 µWb → 13.3 mm, and 15.0 mm at 130 kHz. The suggestion of more turns is right.
- L3-05: the powers 2.59, 2.07 and 1.29 kW and f_C = 30 kHz·√2 are right. The model's limits (self-field, aluminium and copper bases, steel) are stated correctly.
- L2-03 states that Q = cmΔT needs the water to stay liquid, and L1-03 and L3-02 say the energy changes into internal energy, as the guardrails require. Units, magnitudes and significant figures (2.46 kWh with three, the rest with two) are right.
- Scope: induction, eddy currents, alternating current and its effective values, and fibre attenuation in dB, which is defined in the glossary. All of this is FY7 applied content with no later-course physics.
