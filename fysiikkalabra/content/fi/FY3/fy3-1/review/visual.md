VERDICT: PASS
CONTENT-HASH: d748ffe438661103

## Blocking

## Polish
- [Minor] lesson.md, Paino (theory-1280-2) — the same paragraph still shows bare units in plain type, "(m/s²)" and "g yksikössä m/s²", next to KaTeX "$9{,}81\,\text{m/s}^2$", so two typefaces appear on one line. Step 4 of the worked example has the same mix. Fix: write the bare units as `$\text{m/s}^2$`. The table header can stay as it is.
- [Minor] sim-390, exp-exp-1-390 and exp-exp-2-390 — at phone width the canvas text is still about 6–9 px; the bar chart title, now fitted to the chart's width, is about the size of the tick numbers. The forcemeter scale still runs to 2500 N, so 98,1 N reads as almost "0". Fix: make the gauge scale follow the case.
- [Minor] force-extension figure (theory-1280-1, fig-5) — the solid line still runs past the last data point at 10 N and past the last gridline. Fix: dash the line after 10 N, or stop it there.
- [Minor] inquiry.json feedback — carried over from round 1: the written chains still divide with a slash, while the lesson uses a colon. Fix: use a colon in these chains as well.
- [Minor] Tarkista (choice) — carried over from round 1: a wrong selected answer has the same frame as a correct one. Fix: use a neutral style for the selected state.

## Checked
- Hash d748ffe438661103 at start and end; stamp.txt matches, captures current. Delta: sim.js bar-chart title only (8 px higher, width capped to the chart).
- exp-exp-1-390 and exp-exp-2-390 (each opened, chart cropped and zoomed 4×): the title "Sama massa, paino eri paikoissa" now sits on its own line above "G (N)", inside the canvas, right edge within the chart; "G (N)", the top tick "248" and the Jupiter label "248 N" are each clear of it and of each other. Legible at zoom, small at native size (see Polish).
- sim-390 (zoomed 4×): same layout, a little more room; nothing touches.
- sim-1280: title well above the chart, centred over the bars; axis, gridlines, value labels, planet names and legend intact.
- contact-3 (#25–#36: exp-2, top-1280, sim-1280, lab-1280-1, figures, theory, ennusta, tarkista): nothing else changed or broke.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
