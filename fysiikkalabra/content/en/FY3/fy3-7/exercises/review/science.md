VERDICT: PASS
CONTENT-HASH: afd036d994463efc

## Blocking

## Polish
- content/en/FY3/fy3-7/exercises/solutions.md:145 — the L1-07 model answer uses r = 2260 kJ/kg (the value at 100 °C) for sweat evaporating at skin temperature. There r is about 2.4 kJ/g. "about 2.3–2.4 kJ" or "at least 2.26 kJ" would match the remark in the L1-09 solution that the latent heat is larger at lower temperature.

## Checked
- I recomputed all 21 numeric answers in one script with my own formulas: Q = sm, Q = rm, Q = cmΔT, the energy balances and the slope extrapolations. All match answers.py and exercises.json within tolerance. For L3-04 my value is 19.87 kJ against 19.91 kJ, which is inside 8 %.
- L2-05: the table is consistent with the physics. 1.14 K/s gives c_ice = 2100 J/(kg·K). 0.573 K/s gives c_water. The plateau runs 17.5 → 156.7 s, giving s ≈ 334 kJ/kg. The solution's warning about the 20 s and 150 s rows is correct.
- L3-04: stearin. P = 11.98 W, the plateau runs 3.24 → 30.89 min, Q ≈ 20 kJ and s ≈ 200 kJ/kg, which is a realistic value for stearin. The constant power to the surroundings is stated in the task.
- L3-01: the solution checks the boundary case explicitly: 36.7 kJ is available and 20.0 kJ is needed, so all the ice melts. T = 9.7 °C, and the comparison with 0 °C water (21 °C) is right.
- L3-03: the two-power difference cancels the loss. r = 2.26 MJ/kg, the single runs give 2.45 and 2.67 MJ/kg (too large), and the loss power is about 60 W.
- L3-05: m_s = 23.5 g against m_w = 0.386 kg. About 94 % of the steam's energy is released in condensation, and the burn explanation is correct.
- L2-07: linear interpolation gives 85.65 °C (the steam-table value is about 85.9 °C), and the 4 % tolerance covers it. The explanation in b) is correct.
- L1-06 and L1-07: exactly one option is correct in each. The feedback states the constant-pressure, pure-substance condition and uses the guardrail wording about interaction energy.
- L2-06 is a correct error analysis: at constant pressure, boiling water does not exceed its boiling point. m = 0.40 kg.
- `fy3-7/melting-curve`: the grid points (0; −16), (20; 0) and (220; 0) give s = 333 kJ/kg and c_ice = 2083 J/(kg·K). The slope after melting gives c_water ≈ 4180 J/(kg·K). The description and the figure agree, and the figure does not give the answer away.
