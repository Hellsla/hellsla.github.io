VERDICT: PASS
CONTENT-HASH: 6b3c59a45cd6a20e

## Blocking
(none)

## Polish
- [Minor] worked example steps 3-5 (example-390-1/2) — formulas keep $qE = qvB_1$, $m = qB_2 r / v$ while the theory now writes $|q|$; step 1 says $|q| = q$, so it reads correctly — optionally use $|q|$ in the example too.
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `q = e = 1.602 \cdot 10^{-19}\,\text{C}` (worked example, Transfer; also at 1280 px), `v = E : B = 1.0 \cdot 10^{6}\,\text{m/s}`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.

## Checked
- Delta re-review: the diff only adds figures.json descriptions for the exercise option figures `pick-*`; the 18 existing entries are unchanged and no lesson figure uses the new keys.
- Fresh captures (`screenshot.py fy7-2 --lang en --if-stale`, 94 captures): opened fig-18-390 / fig-12-390 / fig-7-390 / fig-10-390 (lesson diagrams, graph, spectrometer): render cleanly, labels legible, descriptions still match what is drawn, no clipping or horizontal scroll.
- Earlier Minor items below the Polish heading still hold (pre-existing, outside this delta).

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
