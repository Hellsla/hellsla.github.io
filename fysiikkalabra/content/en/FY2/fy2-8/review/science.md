VERDICT: FAIL
CONTENT-HASH: 072d395e58551111

## Blocking
- inquiry.json:63 (Prediction 1, correct option's feedback) — **B / consistency**: "Without the natural greenhouse effect the mean temperature would be about $-18\,{}^\circ\text{C}$ instead of the real $+15\,{}^\circ\text{C}$" states as fact the counterfactual surface temperature that the lesson now explicitly says not to read from the model ("should not be read as an exact prediction of the surface temperature if the greenhouse gases were removed, because clouds and ice cover … would change too"). Fix: "A simple radiative balance model gives the Earth an effective radiating temperature of about $-18\,{}^\circ\text{C}$, about $33\,\text{K}$ below the real mean surface temperature $+15\,{}^\circ\text{C}$; the real change would also depend on clouds and ice."
- inquiry.json:497 (tarkistus-3, criterion 2) — **B**, same point in a rubric: "the natural effect raises the mean temperature from about $-18\,{}^\circ\text{C}$ to about $+15\,{}^\circ\text{C}$". The model answer already says it correctly ("the roughly $-18\,{}^\circ\text{C}$ given by the radiative balance model"). Fix: "I mentioned that a simple radiative balance model gives about $-18\,{}^\circ\text{C}$, while the mean surface temperature is about $+15\,{}^\circ\text{C}$."

## Polish
- inquiry.json:71 and :410: "raise(s) the temperature by about $33\,\text{K}$" — add "in the simple model" for the same reason (C as it stands).
- Lesson: "without it the water in the oceans would be frozen" is a firm counterfactual right after the caveat; "would very likely be frozen" fits it better.

## Checked
- Full review: Key idea, Common misconception and Summary now give $-18\,{}^\circ\text{C}$ as the effective radiating temperature of a simple radiative balance model with the caveat; the sim's model box and koe-1 feedback say the same.
- Greenhouse mechanism (sunlight mostly through, thermal radiation absorbed and re-emitted in all directions, N₂/O₂ hardly absorb), CO₂ 280 → 424 ppm (WMO 2025), < 0.5 ‰: correct. Sim temperatures (+14, +15 measured, +16 settled, +17 at 560 ppm with ECS 3 K, likely 2.5–4) match IPCC AR6.
- IPCC AR5 WGIII Annex III medians (820, 490, 230, 41–48, 24, 12, 11–12) and the biomass accounting note: correct.
- Recomputed in one script: worked example $2.352\,\text{t} \to 2.4\,\text{t}$, wind $57.6\,\text{kg}$, ratio 41; coal/nuclear 68; data task $820\,\text{kg}$; error item $43.2\,\text{kg}$; transfer $49\,000\,\text{t}$ (mistakes 0.049, $4.9 \cdot 10^{10}$); wind model answer $1200\,\text{t}$; trip $15.9\,\text{kg} \to 16\,\text{kg}$ (mistakes 13.2, 15 900), $2.2\,\text{kg/l}$; exit $120\,\text{g}$, ~70×. All agree with lesson-answers.py.
- Every choice has exactly one correct option; distractor feedback right. Hydrogen burns to water; fossil vs biomass carbon timing correct.
- Hash at start and end: 072d395e58551111.
