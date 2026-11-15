VERDICT: PASS
CONTENT-HASH: 191266ba7abd05ec
Mode: full (round 1; change: lead "Syventävä tehtävä." on L2-04 to L2-08 and L3-05)

## Blocking

## Polish
- content/fi-easy/FY7/fy7-15/exercises/exercises.json — Only six tasks have the "Syventävä tehtävä." lead. L1-02, L1-03, L1-04, L1-05, L1-07, L1-08, L1-10, L1-11, L2-01, L2-02, L2-03, L3-01, L3-02, L3-03 and L3-04 also use Malus's or Brewster's law, and the brief's note says "Tämän osion laskut ovat syventäviä". No physics is wrong, and the note ("tehtävät, jotka on merkitty syventäviksi") matches the chosen subset. The fi set has the same subset and the same Polish item, so this is the teacher's call: mark the rest, or keep the subset as it is.

## Checked
- Diff against origin/main: the six task texts get the lead and nothing else. No number, answer, unit or tolerance changed. The marking is the same as in content/fi.
- I recomputed all 22 numeric answers in one script with my own formulas: I/2, Malus cos²θ, Brewster atan(n₂/n₁), α₂ = 90° − α_B, and least-squares fits. All of them agree with exercises.json and answers.py within 0,5 %. L2-05 gives slope 313,9 lx (intercept 6,9 lx). L2-08 gives a line of 14,6 + 360,7·cos²θ lx and θ = 44,2°.
- L1-09: my own intensities are D 100, E 125, A 150, B 200 and C 240 W/m², so the order is D, E, A, B, C.
- L3-04: the model I₃ = (I₀/8) sin²2θ gives 0, 30, 90, 120, 90, 30 and 0 W/m². The table differs by a few W/m² both ways, which is realistic example data. The maximum is 1/8 = 12,5 %.
- L3-05: the Sun's height is 36,9° and the result is 7,14 W/m². The break-even tilt of 33,2° (cos²θ = 0,30 at θ = 56,8°) is right.
- L3-02: I checked the Brewster angle from inside the water (36,9°) against the critical angle (48,8°), and it is correctly below it.
- L1-06: exactly one option is correct. Every distractor's feedback is right, including the directions of the horizontally polarised glare and the vertical transmission axis.
- Scope: the core tasks L1-01 and L1-06 use only the qualitative model, which keeps the core path inside the scope note "polarisaatio kvalitatiivisesti".
- Figures: fit and graph-task. Their descriptions carry the same data and give no answer away.
- The hash is the same at the start and at the end.
