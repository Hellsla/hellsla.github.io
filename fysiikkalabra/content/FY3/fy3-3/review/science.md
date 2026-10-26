VERDICT: PASS
CONTENT-HASH: 4e7f29e160d08f99

## Blocking

## Polish
- lesson.md:8 — "Kun tilavuus pienenee … yksittäinen törmäys ei muutu kovemmaksi" leaves out the condition that the temperature stays the same (when a gas is compressed quickly it warms up) — add "ja lämpötila pysyy samana", as the next sentence does for volume.
- inquiry.json:134 (simulaatio.calc) — a single reading of the measured pressure varies a lot. In a port of the sim with seed 7, 1.5 s window, 20 s run, the measured value ranged 40–61 against a theory value of 50 at 150 K, and 180–219 against 200 at 600 K; the time averages match the theory to 1 %. — say "vaihtelee jopa ±20 %" or tell the student to read it a few times and average, so that a reading of 40 at 150 K is not taken as evidence against p ∝ T.
- inquiry.json:287 (siirto.solution, Järkevyys) — "Siksi kuumana suljettu purkki…" describes the reverse process (sealed hot, then cooled), not the one in the task. The physics is right, but "Siksi" makes it sound like it follows from this task — write "Samasta syystä…".

## Checked
- All 12 exercise answers recomputed with my own formulas; answers.py, exercises.json and my values agree within tolerance (e.g. L2-04 3.996, L3-02 127.05 °C, L3-03 −126.6 °C).
- Solutions: each unknown is solved symbolically before substitution. The wrong-scale counterexamples (36 °C, 10 °C, 35/15) are correct.
- Worked example: the table fits p = 100·T/273.15 to within 0.4 kPa; k = 0.37 kPa/°C and θ₀ ≈ −270 °C are right; the limit of the model (real gases liquefy first) is stated.
- Figures: the extrapolation SVG has a consistent scale (1.25 px/°C, 1.5 px/kPa, axis at −300 °C, data points correct). The Kelvin scale figure, which says it is to scale, is: 351 px for 273.15 K and 129 px for 100 K, both ≈1.29 px/K.
- sim.js: the 2D wall-momentum pressure, using the effective box (W−2R)·(H−2R), gives exactly pRel = 100·(T/300)/V on average. Ported to Python and run at 5 states: mean within 0.5 % of the theory value. vRel = √(T/300). Simplifications (2D, no collisions between particles, one speed for all) are stated in `model`.
- exp-1 locks V, exp-2 locks T. Initial states and example values (150/300/600 K; 2.0/1.0 dm³) are within slider range. simState provides theta, vRel, pRel and pTheory.
- Predictions: pred-1 600.15/300.15 = 2.00 and 1.41² ≈ 2; pred-2 vRel stays at 1.00 and wall hits per unit length double; pred-3 correct option and all feedback right.
- virhe 128.2 kPa (+7 %); siirto 121.7 kPa, with mistake values 404 and 83.8 matching the errors they diagnose; check-2 −273 °C, with the −123 °C feedback (150 °C further down) right.
- Misconception and exit ticket: 293/283 = 1.035. The absolute zero wording ("pienimmillään", not zero) is physically careful. N₂ boils at −196 °C, the cosmic background is 2.7 K and the Moon's −173/127 °C are realistic.
- Scope: T = θ + 273.15 and p ∝ T (V, n constant) are within FY3 "lämpötila" and "kaasujen tilanmuutokset". Pressure is only defined, and later lessons are referred to.
- Hash is the same at the start and the end.
