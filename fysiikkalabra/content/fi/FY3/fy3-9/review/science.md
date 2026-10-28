VERDICT: PASS
CONTENT-HASH: 3edf45442c2b3963

## Blocking

## Polish
- inquiry.json (simulaatio, `model`): the gauge and readout show the gas's total pressure (100 kPa at the start), while lesson.md says to use total pressure, not the gauge's overpressure. Add one clause such as "mittari näyttää kaasun kokonaispaineen" so the two do not seem to contradict each other (carried over from round 2).
- lessons/FY3/fy3-9/sim.js:174: `p.textSize(ts(9))` is left over from the removed dial numbers and draws nothing. Delete it. Line 238: `fi()` is unused, and the duplicate "three significant figures" comment trails `tx`. Delete both.
- inquiry.json (johtopaatos, `model`): "mittausepätarkkuuden takia" is not one of the guardrail terms. Write "mittausepävarmuuden" or "satunnaisten mittausvirheiden" to match lesson.md ("mittausepävarmuuden rajoissa").
- lesson.md:342–347: in $T = \theta + 273{,}15\,\text{K}$, $\theta$ is a pure number added to a quantity. The text says so ("lukuarvona"), so this is fair (C). The form $T/\text{K} = \theta/{}^\circ\text{C} + 273{,}15$ would be cleaner.

## Checked
- I recomputed every number in one script with my own formulas, and all match: worked example 1,036 l (+29,5 %, pV 80,8 kPa·l); misconception 1,035 l (+3,5 %); kertaus 30 N (distractors 300 N, 0,030 N, 3,3·10⁸); pred-1 200 kPa, 5,00 J; pred-2 60,2 ml, 0,1706 ml/K, 110 ml; pred-3 200/100/50 kPa; γ = 1/293,15 K = 3,41·10⁻³; ruisku pV 5040 (5050), except 5430 at 30 ml (+7,7 %), expected 168 kPa; virhe 252,5 ≈ 250 kPa (student's 40,4); siirto 1,069 l, mistakes 2,10 and 0,00107, 71 %; check-c2 1,0999, 28 K/280,15 K; check-2 120 kPa (108, 0,12); exit ticket 160 kPa. lesson-answers.py agrees.
- Every correct option is right and is the only right one. Each distractor's feedback names the correct mechanism. In ruisku, heating (pV too large) is correctly told apart from a leak (pV too small).
- Conditions are stated where each law is used: a fixed amount of gas, isothermal, total pressure, a thin gas for V ∝ T and p ∝ T. The extrapolation to 0 K is called the model's prediction, because the gas condenses first.
- The micro model is right: with T constant the speed is constant, the hits per unit area double, and the hits are as hard as before. Heating in the isobaric and isochoric cases is "useammin ja kovempaa".
- Figures checked from their coordinates: boyle-graphs at pV = 2000 kPa·ml in both panels; absolute-zero with points at 253–373 K whose line runs through the origin (ratio 1,474 = 373/253); micro-boyle with heights 2 : 1 and 4 → 8 hit marks.
- Simulation, checked in a fresh Playwright render (isochoric 150 °C; isothermal 20 ml with 1/V): p = 144,3 kPa, p/T = 0,3411 kPa/K; p = 250 kPa, pV = 5000 kPa·ml. The needle stays under 300 kPa. The KaTeX canvas labels and axis ticks have the right values (0,01–0,05 1/ml; 0–160 kPa; 0–500 K). The reading above the gauge equals simState.p.
- The flash rate per wall length ∝ √T/V and the flash size ∝ speed, so the picture is consistent with p ∝ T/V. The 80-flash cap is not reached (about 54 at nopea, 20 ml).
- Experiments: exp-1 locks mode and θ and varies V. exp-2 locks the isobaric mode and varies θ. `constant` (J), p (Pa), Vgas (ml) and VperT (ml/K) are in the units the tables state.
- Scope: the lesson stays within "kaasujen tilanmuutokset" and the Boyle experiment. The lint gives no physics warnings.
