VERDICT: PASS
CONTENT-HASH: 5b44d9571400229b

## Blocking

## Polish
- lesson.md:211 — "Hajonta on sama asia kuin satunnaisvirheen suuruus" runs together two terms the guardrails keep apart: hajonta is the spread of the results, and random error is what causes it (C-level wording, no wrong numbers) — write "Hajonta kertoo satunnaisvirheen suuruudesta".
- lesson.md:267–273, inquiry.json `johtopaatos` model — the correction $x = x_\text{lukema} - \Delta x_\text{sys}$ assumes the error has the same size over the whole measured range (a zero offset). The definition at line 114 implies this, but a thermometer checked only in ice water shows the offset at $0\,{}^\circ\text{C}$ only — consider adding "kun virhe on koko mittausalueella sama (nollakohdan virhe)".
- lessons/FY1/fy1-3/lesson-answers.py:38 — `inq-ice-corrected` (62,3 °C → 60,8 °C) matches no number in the lesson or inquiry — delete it or add the task it belongs to.
- inquiry.json exp-1 feedback "noin $0{,}25\,\text{s}$" — the model gives 0,250 s at n = 5 but 0,260 s at n = 40. "noin" covers this; it could say "$0{,}25$–$0{,}26\,\text{s}$".

## Checked
- One script recomputed every number from the task data with my own formulas, independently of lesson-answers.py. It checked: worked example (sum 19,09 s, mean 3,1817 s, Δt 0,12 s, ε 3,77 % → 3,8 %, 5/6 inside the interval), Pysähdy 4,4 ± 0,2 s, karkea virhe (mean shift 0,19 s, Δt 0,09 → 0,62 s ≈ 7×), coin task (5,44 g and the mistakes 5,6 / 27,2 / 4,8 g), check-2 (2,08 % → 2 %, mistake 4,2 %), ice data (1,5 °C, 0,1 °C, 15×), exit ticket (19,9 g, Δm 0,1 g, 2 %). All are correct.
- Sim readings reproduced with JS-style rounding. The hook data = model readings 1–5. Exp-1: n = 1 gives an error of −0,22 s and n = 40 gives −0,0005 s. Exp-2: mean at n = 40 is 2,6995 s, so the error is 0,2995 s. Exp-3: 0,525/0,085 = 6,18. All claims in the predictions, feedback and model answers match.
- Numeric tolerances (relative): accepted answers rounded to the data's precision fall inside them. Every listed mistake value falls outside, so it can trigger.
- Experiments: each locks the other two parameters and varies one. `simState` holds `mean`, `puoli` and `vir`, and the slider steps reach every requested value.
- sim.js implements $t_i = T + \Delta t_\text{sys} + \Delta t_\text{sat} g_i$ (G: mean ≈ 0, sd 0,97). The Mallin oletukset box states the model, says the values are model values and notes that T is known only in the model.
- error-types figure is to scale (means 2,408 / 2,595 s, arrow 0,19 s). example-plot dots and bar (3,06–3,30 s) are to scale. Zero-scale 48,7 − 1,2 = 47,5 g.
- Definitions follow the guardrails: error vs uncertainty, resolution vs uncertainty (stopwatch 0,01 s vs about 0,2 s), half-range described as a cautious estimate for the mean, and outlier handling worded as the guardrails require.
- Each choice item has exactly one correct option, and every distractor's feedback explains why it is wrong.
- Scope is within FY1's central contents.
