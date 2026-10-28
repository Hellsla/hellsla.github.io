VERDICT: PASS
CONTENT-HASH: a8c5706f60d4138d

## Blocking

## Polish
- inquiry.json pred-2, last option's feedback — "koska hiukkaset palaavat seinälle nopeammin" can be read as "move faster", which contradicts the correct option (speed unchanged at constant T) — write "palaavat seinälle useammin / lyhyemmässä ajassa".
- inquiry.json check-1 correct option — "verrannollinen kelvinlämpötilaan $273\,\text{K}$" reads oddly; "verrannollinen kelvinlämpötilaan, joka on $273\,\text{K}$" is clearer.
- lesson.md Esimerkki, Tulos — "−270 °C, kaksi merkitsevää numeroa" is fine; the intermediate "−270,27 °C" could carry "≈" to avoid implied precision.

## Checked
- Definitions: system/surroundings/closed system, state variables, temperature as mean (translational) kinetic energy for a dilute gas with "Mallin rajat" for liquids/solids, temperature ≠ internal energy (ice/water at 0 °C), absolute zero = lowest energy, motion does not stop — all guardrail wording.
- p ∝ T stated with its conditions (constant V and amount, dilute gas far from condensing) in theory, summary, solutions; extrapolation's limit (real gases liquefy) stated.
- Recomputed in one script: Esimerkki data vs 100·T/273,15 kPa (107,3/114,6/122,0/129,3/136,6), k = 0,37 kPa/°C, θ₀ = −270 °C, check 136,6 kPa; virhe 128 kPa; siirto 121,7 → 122 kPa and mistakes 404 / 83,8; check-2 −273 °C; 293/283 = 1,035; √2 = 1,41.
- Figures to scale: kelvin-scale 1,20 px/K (0, 273,15, 373,15 K ticks), extrapolation graph axes and the six points and the −270 °C intercept verified from coordinates.
- sim.js: 2D ideal particles, v ∝ √T, pressure measured from wall momentum per time per wall length over both axes, reference N·v²/(2·A) correct, so p ∝ T/V emerges; model box states 2D, no particle–particle collisions, equal speeds.
- exp-1 locks V = 1,0 and varies T (simState gives theta, vRel, pRel, pTheory); exp-2 locks T and varies V; the predictions' numbers (100 → 200, 50 → 100, 1,41) match pTheory and vRel.
- Exactly one correct option in pr-pumppu, pred-1, pred-2, pred-3, virhe, check-1; distractor feedback correct (Celsius ratio, heat-as-substance, particle expansion, nitrogen at −196 °C).
- Worked example: seven stages, symbolic θ₀ = −p₀/k first, no conversion needed justified, real independent check.
- Exit ticket and check-3 model agree with theory (3,5 %, −273,15 °C, lowest energy).
