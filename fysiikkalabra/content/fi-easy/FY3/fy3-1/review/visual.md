VERDICT: PASS
CONTENT-HASH: e3b9ca921e71f66f

## Blocking

## Polish
- [Minor] lesson.md l.214, l.292, table header l.216 — "(m/s²)" and "yksikössä m/s²" are plain text next to KaTeX $\text{m/s}^2$ in the same paragraph (theory-1280-2) — set them as $\text{m/s}^2$.
- [Minor] inquiry.json feedback ("Voimamittarin asteikko", Kuu numeric) — chains still divide with "/" ($5{,}6/1{,}6 \cdot 1{,}0\,\text{N}$, $12\,\text{N} / 1{,}62\,\text{m/s}^2$), while the lesson uses the colon — use ":".
- [Minor] exp-1/exp-2 "Alkutila" (carried) — "taivaankappale: Maa, massa $m$ = 10 kg" shows a plain "=" between the symbol and the value (exp-exp-1-390, lab-1280-1) — "taivaankappale Maa", with the quantity as one formula $m = 10\,\text{kg}$.
- [Minor] sim.js bar chart (sim-1280, lab-1280-1) — the axis title $G\ (\text{N})$ and the full-scale value $248$ are drawn noticeably smaller than the bar value labels; at 390 px the fitted chart title is about tick-label size. Readable; the same size as the other tick numbers would look more even.

## Checked
- Hash e3b9ca921e71f66f at start and end; stamp.txt matches, captures current. Delta: sim.js bar-chart title only (8 px higher, width capped to the chart).
- exp-exp-1-390 and exp-exp-2-390 (chart cropped and zoomed 4×): "Sama massa, paino eri paikoissa" sits on its own line above "G (N)", inside the canvas; "G (N)", the top tick "248" and the Jupiter "248 N" are clear of it and of each other. Bar labels, planet names and legend do not overlap.
- sim-390: same layout; nothing clips.
- sim-1280: title centred well above the bars; chart and readout "Palkkikaavion asteikko 0–248 N" intact.
- contact-1 (#1–#12: top, sim, figures 1–5, example, Pohdinta, Ennusta, Tutki with the narrow sim): nothing else changed or broke.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
