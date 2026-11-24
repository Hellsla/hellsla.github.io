VERDICT: PASS
CONTENT-HASH: d8f764e465cf7fc8

## Blocking

## Polish
- lesson.md:230, inquiry.json `epavarmuus` — the steepest line printed with rounded intercept $100{,}1$ kPa gives $103{,}97$ kPa at $10\,{}^\circ\text{C}$, 0,03 kPa below the bar end it is said to touch (exact line $100{,}13 + 0{,}3867\theta$ touches it). This does not change any result (−258,7 vs −259,0 °C; $\Delta\theta_0$ 18,08 vs 18,11 °C, both 18). Optional: write "noin" or give $100{,}13$.
- lesson.md:134 — caption: the fog is water vapour of the air that condenses in the cold nitrogen gas. "kylmän typpihöyryn ympärille tiivistyneitä" is acceptable, but "ilman vesihöyrystä kylmässä typpihöyryssä tiivistyneitä vesipisaroita" would be more exact.

## Checked
- All numbers recomputed in one script from the task data: worked example −276,02 °C, extreme lines −258,66 / −294,81 °C, $\Delta\theta_0$ = 18,08 °C; suora −275,8 (mistakes −296, 276); siirto −276,9 (−307); tarkistus-2 −282,9 (−298); Etsi virhe 40 − 316,1 = −276,1 °C; kertaus 313/293 = 1,068; exit 0,36 kPa/°C and −282…−258 °C. lesson-answers.py agrees.
- Least-squares fit of the data gives $k = 0{,}3667$ kPa/°C and $p_0 = 101{,}26$ kPa (θ₀ = −276,2 °C). Points A and B and (0; 101,3) lie on it. Every residual is under 0,6 kPa, so the correct option in `aineisto` is true.
- Steepest (10/85 °C bar ends) and shallowest (25/100 °C) lines pass through every ±1 kPa bar and really are the extremes (tried other pivot pairs). s2 = 98,9 + 0,42θ misses exactly the bars at 10, 70, 85 and 100 °C, as the feedback says.
- Figure pixels match the stated data. In fig 8, θ₀ is at −276,1 °C, the extremes at −259,0 and −295,2 °C, and the points match the table. In the zoomed figures, the best line, A, B, s1, s2 and the shallowest line all match their equations. "Mittakaavassa" holds.
- New or changed pictures: hero (ice water, room-temperature bath with bottle and gauge, boiling water) and thermometer schematic ($\theta$, $p$, $Q$, $V$ = vakio) agree with the text and alt texts; the scale disclaimer is stated.
- Model conditions are stated: closed rigid vessel, thin gas (summary), linear only over the measured range, the real gas liquefies before absolute zero, and the extrapolation is an assumption. Absolute zero is called "pienimmillään", not "motion stops" (guardrail).
- Uncertainty terms follow the guardrails: estimate, not a guaranteed limit; "todennäköisesti"; manufacturer's error limit kept separate; no point removed without a reason; the fit need not pass through every point.
- Predictions: exactly one correct option in each, and each distractor's feedback names the actual reason it is wrong (Celsius zero, curving data, the relative uncertainty is not kept). The ±18 °C answer is consistent with the computed uncertainty.
- Significant figures: the 3-figure and whole-degree reasoning is consistent; Δθ₀ = 18 °C because the difference 36 °C has two figures.
- Scope: FY3 temperature, gas state changes and experimental extrapolation; nothing beyond FY3.
