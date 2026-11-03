VERDICT: PASS
CONTENT-HASH: 98147d556de843b3

## Blocking
(none)

## Polish
- [Minor] sim-1280 — "Source separation d = 6.0 cm" wraps over two lines in the three-column control row (as the Finnish label does); shared layout, no action here.

## Checked
- Delta (coordinator fix): Prediction 1 reveal.pending now English, "Feedback opens when you read the section The principle of superposition in the Theory summary."; rebuilt preview/en/fy5-12.html shows it, and the section and stage it names exist on the page ("The principle of superposition" under Key idea, stage "Theory summary"). Nothing else changed. No Finnish left on the English page (built HTML searched for the old sentence: none).
- sim-390 and sim-1280 after the fixes: labels fit at 345 px; legend line now visible under the readout (it was 19 words and folded into an extra "Assumptions of the model and explanation" box; shortened to 14 words); canvas L = 8.0 cm with a decimal point.
- fig-4-390 (pulses): "while meeting" ran into the string line; figures.json now "meeting", figures regenerated, gap visible.
- fig-7-390 (constructive/destructive), theory-1280-1 and -3; fig-1, fig-5 (nodal line label), fig-6, top-390 and intro-1280 seen in contact-1.
- worked example (contact-1 #8–9, contact-2 #20–21): staged steps, aligned chains, decimal points, upright units.
- exp-koe-1-390-2: table headers (position of point P x, Δs (cm), Δs/λ, A_P (mm)) fit.
- contact-1…4 (open-exit, open-tarkista, exercises): no Finnish in figures, labels or subscripts; heading "Fourier analysis" renders without its {Fourier-analyysi} key.
- check_layout fy5-12 --width 345: OK for preview/en/fy5-12.

## Scores
illustrations 5 · typography 5 · Finnish (English) 4 · accessibility 4
