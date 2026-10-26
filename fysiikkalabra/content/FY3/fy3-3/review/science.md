VERDICT: PASS
CONTENT-HASH: 824fae33df16ef17

## Blocking

## Polish
- exercises.json:82 — a bicycle tyre's "paine 300 kPa" is in everyday use the gauge (over)pressure, and p ∝ T holds only for the absolute pressure; the answer 321 kPa is right for absolute pressure — write "renkaan ilman (absoluuttinen) paine" or use a generic sealed container.

## Checked
- T = θ + 273,15, ΔT = Δθ, 0 K = −273,15 °C with "liike-energia pienimmillään" (not "zero"); p ∝ T at constant V and n stated with its conditions; micro-model (more frequent vs harder collisions) correct; all inside FY3 "termodynaaminen systeemi, tilanmuuttujat, lämpötila".
- Worked example: table matches an ideal gas (100 kPa at 0 °C → 107,3 / 114,6 / 122,0 / 129,3 / 136,6); k = 0,37 kPa/°C, θ = −p₀/k ≈ −270 °C, solved symbolically before substitution.
- Figures: kelvin scale to scale (1,20 px/K, 100 K = 120 px); extrapolation graph data points match the table to ±0,5 px, dashed line reaches p = 0 at −270 °C, y axis at −300 °C as the caption says; micro-model figure labelled schematic.
- answers.py recomputed in one script: all 12 match; exercise data are physically consistent (L2-03 ideal-gas check 137,2 and 86,7 kPa).
- solutions.md: conversions and proportions set up symbolically first; distractor values (36 °C, 10 °C) right.
- Simulation: v ∝ √T so mean KE ∝ T; pressure from wall impulses per wall length averaged over both axes, which removes the fixed-direction anisotropy exactly; effective box PX·V × (h − 2R) matches the reference. A Python port of the step gives 104/50/194/54/202 vs theory 100/50/200/50/200 — statistical scatter only. Limits (2D, no particle collisions, one speed) stated in the model box.
- exp-1 locks V, varies T (vRel, pRel, pTheory in simState); exp-2 locks T, varies V; slider ranges reach 150–600 K and 0,5–2,0 dm³.
- Predictions: 300 → 600 K doubles p, speed ×1,41 and 1,41² ≈ 2; halving V doubles p with vRel = 1,00; 327/27 ≈ 12 distractor explained.
- virhe 128 kPa (×1,068), siirto 122 kPa with mistakes 404 and 83,8; check-2 −273 °C with mistakes 0 and −123; nitrogen −196 °C.
- Exit ticket: 3,5 % rise, −273 °C.
