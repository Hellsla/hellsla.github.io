VERDICT: PASS
CONTENT-HASH: f349123e5b25e48b

## Blocking

## Polish
- [Minor] lesson.md, Paino (theory-1280-2) — the same paragraph still shows bare units in plain type, "(m/s²)" and "g yksikössä m/s²", next to KaTeX "$9{,}81\,\text{m/s}^2$", so two typefaces appear on one line. Step 4 of the worked example has the same mix. Fix: write the bare units as `$\text{m/s}^2$`. The table header can stay as it is.
- [Minor] sim-390, exp-exp-1-390 and exp-exp-2-390 — at phone width the canvas text is still about 6–9 px. The forcemeter scale still runs to 2500 N, so 98,1 N reads as almost "0". Fix: make the gauge scale follow the case.
- [Minor] force-extension figure (theory-1280-1, fig-5) — the solid line still runs past the last data point at 10 N and past the last gridline. Fix: dash the line after 10 N, or stop it there.
- [Minor] inquiry.json feedback — carried over from round 1: the written chains still divide with a slash, while the lesson uses a colon. Fix: use a colon in these chains as well.
- [Minor] Tarkista (choice) — carried over from round 1: a wrong selected answer has the same frame as a correct one. Fix: use a neutral style for the selected state.

## Checked
- The hash is f349123e5b25e48b at the start and at the end. stamp.txt matches it, so the captures are current.
- Round-1 Blocking item, theory-1280-2: the sentence now renders as one formula, "sillä $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$", with KaTeX spacing. Resolved.
- exp-exp-1-390 and exp-exp-2-390 (each opened, plus a 3× crop of the chart): the old scale caption is gone. "248" sits on the top tick of the axis, "G (N)" sits above the axis under the chart title, and the "248 N" label sits over the Jupiter bar. Nothing collides, and the labels can be read at that size. The readout line "Palkkikaavion asteikko 0–248 N on tämän massan paino Jupiterissa" explains the scale.
- sim-390 and sim-1280: the chart has the same layout and has plenty of room. The bar labels, planet names and legend are all clear.
- I also opened theory-1280-1 (figures 2 and 5), the G(m) graph in theory-1280-2, example-390-2 and contact-1 (top-390, hero image, figures, worked example, the Ennusta and Tutki stages). Nothing else broke.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
