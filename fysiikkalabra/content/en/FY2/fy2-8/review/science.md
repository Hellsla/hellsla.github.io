VERDICT: PASS
CONTENT-HASH: abcb7e503f0e1643

Follow-up review of the fix commit 2c31ff041 (delta from 072d395e58551111, whose full review is kept below). Changes: Prediction 1's correct-option feedback and tarkistus-3 criterion 2.

## Blocking

None.

## Polish
- inquiry.json:71 and :410: "raise(s) the temperature by about $33\,\text{K}$" — "the difference, about $33\,\text{K}$, …" or "in the simple model" would match (C).
- Lesson: "without it the water in the oceans would be frozen" right after the caveat; "would very likely be frozen" fits better (C).

## Checked
- Earlier blocking item 1 resolved: inquiry.json:63 now says "A simple radiative balance model of the Earth gives an effective radiating temperature of about $-18\,{}^\circ\text{C}$, while the mean surface temperature is about $+15\,{}^\circ\text{C}$. The difference, about $33\,\text{K}$, illustrates how much the greenhouse effect matters." Physically right ($T_\text{eff} \approx 255\,\text{K}$).
- Earlier blocking item 2 resolved: criterion 2 now asks exactly what the model answer (:501) says.
- Consistency: grep of "-18" in lesson.md and inquiry.json — Key idea (:136, with the clouds/ice caveat), misconception (:328), Summary (:331), sim model box (:112), koe-1 (:154), Prediction 1, tarkistus-3 — all use the model wording.
- Greenhouse mechanism, CO₂ 280 → 424 ppm (WMO 2025), < 0.5 ‰: correct. Sim temperatures (+14, +15, +16 settled, +17 at 560 ppm with ECS 3 K, likely 2.5–4) match IPCC AR6.
- IPCC AR5 WGIII Annex III medians and the biomass accounting note: correct.
- Recomputed: worked example $2.352\,\text{t} \to 2.4\,\text{t}$, wind $57.6\,\text{kg}$, ratio 41; coal/nuclear 68; data task $820\,\text{kg}$; error item $43.2\,\text{kg}$; transfer $49\,000\,\text{t}$ (mistakes 0.049, $4.9 \cdot 10^{10}$); wind $1200\,\text{t}$; trip $15.9\,\text{kg}$ (mistakes 13.2, 15 900); exit $120\,\text{g}$, ~70×. All agree with lesson-answers.py.
- Every choice has exactly one correct option; distractor feedback right.
- Hash at start and end: abcb7e503f0e1643.

## Shared issues
- Outside this hash: exercises/solutions.md:125 and exercises.json:69 keep "raises … from about $-18$ to about $+15\,{}^\circ\text{C}$"; align when the exercise set is next edited.
