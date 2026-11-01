VERDICT: PASS
CONTENT-HASH: 610363548f8ddbac

## Blocking

## Polish
- [Minor] lesson.md l.214, l.292, table header l.216 — "(m/s²)" and "yksikössä m/s²" are plain text next to KaTeX $\text{m/s}^2$ in the same paragraph (theory-1280-2) — set them as $\text{m/s}^2$.
- [Minor] inquiry.json feedback ("Voimamittarin asteikko", Kuu numeric) — chains still divide with "/" ($5{,}6/1{,}6 \cdot 1{,}0\,\text{N}$, $12\,\text{N} / 1{,}62\,\text{m/s}^2$), while the lesson uses the colon — use ":".
- [Minor] exp-1/exp-2 "Alkutila" (carried) — "taivaankappale: Maa, massa $m$ = 10 kg" shows a plain "=" between the symbol and the value (exp-exp-1-390, lab-1280-1) — "taivaankappale Maa", with the quantity as one formula $m = 10\,\text{kg}$.
- [Minor] sim.js bar chart at 1280 px in the lab column (lab-1280-1) — the axis title $G\ (\text{N})$ and the full-scale value $248$ are drawn noticeably smaller than the bar value labels. They are readable, but the same size as the other tick numbers would look more even.

## Checked
- Major 1 resolved: exp-exp-1-390 and exp-exp-2-390, zoomed. The caption is gone. The full-scale line carries $248$ at the axis, $G\ (\text{N})$ sits above the axis, and the Jupiter label "$248\,\text{N}$" stands clear of both. The bar labels, planet names and legend do not overlap.
- Major 2 resolved: lesson.md l.214 now reads "$1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$" as one formula and renders cleanly in theory-1280-2.
- Chart at sim-390, sim-1280 and lab-1280-1 (narrow column): the gridlines at 50–200, the 248 top line and the readout "Palkkikaavion asteikko $0\text{–}248\,\text{N}$" (KaTeX) agree. The bars are honest relative to the scale.
- The layout survived: contact-1 to contact-3 (top, intro, figures 1–5 and fig-row, example, stages, tarkista, exercises, exit, lab-1280). There is no clipping or overflow, and the rest of the page is unchanged from round 1.
- fi-easy register: the short plain sentences in the cards and theory hold, and the readout sentence is one simple clause.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
