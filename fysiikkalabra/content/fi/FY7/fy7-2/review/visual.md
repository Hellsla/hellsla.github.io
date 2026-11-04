VERDICT: PASS
CONTENT-HASH: 60566c60301b819d

## Blocking
(none)

## Polish
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `q = e = 1{,}602 \cdot 10^{-19}\,\text{C}` (worked example, Siirto; also at 1280 px), `v = E : B = 1{,}0 \cdot 10^{6}\,\text{m/s}`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.

## Checked
- delta review of 2c31ff041: Laskennan selitys box: $|q|vB$, $F_\text{m} = |q|vB$, $F_\text{s} = |q|E$; diff read. `screenshot.py fy7-2 --if-stale` (fresh captures).
- Own 390 px element captures of each changed block opened (scratchpad caps/fi-fy7-2-*-390.png): text wraps cleanly, KaTeX renders, no clipping, no horizontal scroll. Measured every inline .katex (getClientRects().length) at 360, 390 and 1280 px, all boxes open and all feedback shown, after `build.py fy7-2`: no formula in a changed passage breaks onto two lines.
- Earlier: batch delta review: all $|q|$ formulas of the lesson (sähköinen voima, $W = |q|U$, $F_\text{m} = |q|vB \sin\alpha$, $r = mv : (|q|B)$ inline and in displays, the nopeusvalitsin display $|q|E = |q|vB$, massaspektrometri $m = |q| B_2 r / v$, summary bullets). Built page at 360, 390 and 1280 px with every box open: all 23 inline formulas containing $|q|$ stay on one line in the lesson text (the one that wraps is in the exercise solutions, see exercises/review/visual.md); captures q-390-1 to q-390-3 opened: the bars read as absolute value, $\overline{F}_\text{s} = q\overline{E}$ vector set correctly, the aligned display is centred. No clipping, no horizontal scroll.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
