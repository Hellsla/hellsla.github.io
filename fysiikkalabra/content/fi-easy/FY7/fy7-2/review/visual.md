VERDICT: PASS
CONTENT-HASH: 95e436a1b8ea1958

## Blocking
(none)

## Polish
- [Minor] esimerkin vaiheet 3-5 — kaavoissa on yhä $q$, teoriassa $|q|$; vaihe 1 sanoo $|q| = q$, joten teksti toimii — halutessa $|q|$ myös esimerkkiin.
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `q = e = 1{,}602 \cdot 10^{-19}\,\text{C}` (worked example, Siirto), `2e = 3{,}204 \cdot 10^{-19}\,\text{C}`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.

## Checked
- delta review of 2c31ff041: Laskennan selitys box: $|q|vB$, $F_\text{m} = |q|vB$, $F_\text{s} = |q|E$; diff read. `screenshot.py fy7-2 --lang fi-easy --if-stale` (fresh captures).
- Own 390 px element captures of each changed block opened (scratchpad caps/fi-easy-fy7-2-*-390.png): text wraps cleanly, KaTeX renders, no clipping, no horizontal scroll. Measured every inline .katex (getClientRects().length) at 360, 390 and 1280 px, all boxes open and all feedback shown, after `build.py fy7-2`: no formula in a changed passage breaks onto two lines.
- Earlier: batch delta review: opened theory-1280-1..4, example-390-1..2 and open-exit-1280 (new |q| display blocks, inline formulas, summary bullets, exit-ticket answer and the example Given line render in KaTeX; no inline formula wraps onto two lines; no overflow); diffs of lesson.md, inquiry.json, exit-ticket.json read.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
