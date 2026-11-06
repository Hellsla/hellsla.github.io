VERDICT: PASS
CONTENT-HASH: 36f1e76b61ba6c02

## Blocking
(none)

## Polish
- [Minor] esimerkin vaiheet 3-5 — kaavoissa on yhä $q$, teoriassa $|q|$; vaihe 1 sanoo $|q| = q$, joten teksti toimii — halutessa $|q|$ myös esimerkkiin.
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `q = e = 1{,}602 \cdot 10^{-19}\,\text{C}` (worked example, Siirto), `2e = 3{,}204 \cdot 10^{-19}\,\text{C}`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.

## Checked
- Delta re-review: the diff only adds figures.json descriptions for the exercise option figures `pick-*`; the 18 existing entries are unchanged and no lesson figure uses the new keys.
- Fresh captures (`screenshot.py fy7-2 --lang fi-easy --if-stale`, 94 captures): opened fig-18-390 / fig-12-390 / fig-7-390 / fig-10-390 (lesson diagrams, graph, spectrometer): render cleanly, labels legible, descriptions still match what is drawn, no clipping or horizontal scroll.
- Earlier Minor items below the Polish heading still hold (pre-existing, outside this delta).

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
