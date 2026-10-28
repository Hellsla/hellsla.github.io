VERDICT: FAIL
CONTENT-HASH: 59f4726db9209370

## Blocking
- inquiry.json pred-3 / exp-1 — pred-3 (Bea vs Cem: asymmetric vs symmetric vibration) is revealed after exp-1, but the sim draws symmetric vibration and sets the spacing from the formula (the model text says so). What the student sees matches Cem's option, which the feedback then calls wrong; exp-1 cannot refute the prediction it is meant to test (only Aino's "particles grow" is testable). Fix: reveal pred-3 after the theory stage (reflect) instead of exp-1, and take "ja 3" out of exp-1's intro; or draw the vibration asymmetrically (longer swing away from the neighbour).

## Polish
- sim.js canvas (390 px) — KaTeX labels are legible but small: graph tick numbers and "mikromalli"/"katkoviiva" are about 7-8 px when the canvas scales to 366 px (exp captures); readable at 1280. Enlarge the tick and caption font in the narrow layout, or drop the second caption line.
- sim canvas — the four thin graph lines differ only by colour and are not named; the key is a sentence in Käyttöohje. Label each line at its right end ($\alpha$ or the material name) so colour is not the only carrier.
- sim readout — the line "Kuvaajan ΔL-akseli −20–30 mm, kun L₀ = 10 m." is housekeeping, not a quantity; remove it from the visible readout (move to Käyttöohje). The five remaining lines wrap to eight at 390 px.
- lesson.md figures — fig 1 (hiukkasrivi) shows symmetric arrows, the one thing the text says is not the cause; add a longer arrow away from the neighbour. Fig 3 (sauva) comes after both tables instead of right after the ΔL paragraph.
- Finnish — "pyrkisi valumaan yli" (L3-03) and "Muutos on pieni mutta voimakas" read slightly awkward; consider "valuisi yli" and "Muutos on pieni, mutta voima on suuri".

## Checked
- Sim captures 390 and 1280 px: no overlaps or clipping; all canvas labels and the readout are KaTeX, upright units with thin space, consistent with the controls.
- Legacy notes now behind Käyttöohje and Mallin oletukset; lead text under 30 words.
- Wide layout: sim beside the experiments, locked controls greyed with "(vakio)", table headers clear.
- Learning path: hook, retrieval of ΔT in K, predictions 1 and 2 refutable by exp-1 and exp-2, theory, reflect, example, error-spot, transfer, three checks; one-lesson workload.
- Predictions: wrong options repair a named misconception; feedback quotes model values.
- Worked example: four staged steps, symbolic first, units checked; does not repeat any exercise.
- Exercises: 5/4/3, levels fit, solutions symbolic first; exit ticket tests the core idea.
- Scope: stays within lämpölaajeneminen and the micro-model; gas detail deferred to a named chapter.
