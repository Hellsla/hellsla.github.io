VERDICT: PASS
CONTENT-HASH: 9f01aec0f0034f76

## Blocking

## Polish
- lesson.md:35 — "ne osuvat seinämiin kaksi kertaa niin usein" says that the total hit rate doubles. In the halved volume the side walls get the same number of hits per second over half the area, so only the hits per unit area double (check-1's feedback says this correctly). — add "pinta-alaa kohti" (C-level wording, not an error in the picture).
- lesson.md:550 — In the summary, "Tilanmuutoksessa kaasun paine, tilavuus ja lämpötila muuttuvat" reads as if all three always change, but the next sentence keeps one constant. — Use the Ydinajatus wording: "muuttuu ainakin kaksi niistä".
- inquiry.json exp-1 — The experiment table shows pV in J and p in Pa, but the sim's own table under the canvas shows kPa and kPa·ml. The intro states the conversion, so this is consistent, but students see two unit systems side by side. — Optional: say in the intro that the sim's table uses kPa·ml.

## Checked
- One script recomputed every number: kertaus (2020 N, 5,05 MN), pred-1/2/3 (200 kPa, 5,00 J, 60,2 ml, 0,171 ml/K), the γ question (0,1706/50 = 3,41·10⁻³ = 1/293), ruisku (pV 5040/5050/5040/5430/5040, 168 kPa, +7,7 %), virhe (252,5 vs 40,4 kPa), siirto (1,069 l, mistakes 2,10 and 0,00107), check-c2 (1,0999), check-2 (120, mistakes 108 and 0,12), the worked example (1,036 → 1,0 l, ×1,29, pV 80,8), the misconception example (1,035 l), the exit ticket (160 kPa). All agree with lesson-answers.py.
- Figures are to scale: in boyle-graphs, pV = 2000 kPa·ml on the curve at 8 and 42 ml and on the line's slope (about 1996); in absolute-zero, both lines are proportional to T (ratio 1,474 = 373/253) with their extensions through 0 K; in micro-boyle, the gas heights are 2:1, the hit marks 4 vs 8, the arrows equally long.
- Every prediction, check and Etsi virhe has exactly one correct option, and each distractor's feedback names the real error (Celsius ratios, an inverted ratio, a leak vs heating, speed vs collision rate).
- Conditions are stated: a fixed amount of gas, isothermal for Boyle, a thin gas and kelvins for V∝T and p∝T, absolute rather than gauge pressure, and the extension as a model prediction (condensation).
- Sim: the state follows pV/T = const from 50 ml, 100 kPa and 293,15 K; particle speed ∝ √T and hit rate × size ∝ T/V illustrate p; the calc box and the model answer call the readings model values that do not prove the law.
- Experiments: exp-1 locks mode and Tc and varies Vml, with p and constant (J) in simState; exp-2 locks mode, varies Tc and reads T, Vgas and VperT through the adapter's get. The ranges fit the axes (72,2 ml < 80, 144 kPa < 160, 1/V ≤ 0,05).
- Mechanisms: fast compression heats the air, so the pressure is too high; the isobaric piston rises until the sparser gas balances the weight; the cabin-pressure explanation with the bag's slightly higher pressure when taut.
- Scope: FY3 kaasujen tilanmuutokset and Boylen laki; there is no ideal-gas equation with n or R, and no later-course physics.
- Significant figures and rounding are justified in the worked example, siirto and check-2.
