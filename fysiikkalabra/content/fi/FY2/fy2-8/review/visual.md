VERDICT: PASS
CONTENT-HASH: 4b1233005b94d34d

## Blocking
(none)

## Polish
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `\text{C} + \text{O}_2 \rightarrow \text{CO}_2`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.

## Checked
- delta review of 2c31ff041: Ennusta feedback (correct option) and the self-assessment criterion with $-18\,{}^\circ\text{C}$ / $+15\,{}^\circ\text{C}$ / $33\,\text{K}$; diff read. `screenshot.py fy2-8 --if-stale` (fresh captures).
- Own 390 px element captures of each changed block opened (scratchpad caps/fi-fy2-8-*-390.png): text wraps cleanly, KaTeX renders, no clipping, no horizontal scroll. Measured every inline .katex (getClientRects().length) at 360, 390 and 1280 px, all boxes open and all feedback shown, after `build.py fy2-8`: no formula in a changed passage breaks onto two lines.
- Earlier: batch delta review: greenhouse-effect paragraph, misconception box and summary bullet with $-18\,{}^\circ\text{C}$ (radiation-balance wording); built page and scripts/screenshot.py fy2-8 (captures current), changed passages opened at 390 px (e-390-0, e-390-1): clean wrapping, KaTeX renders, no inline formula wraps, no clipping, no horizontal scroll. Diff read; the rest of the lesson unchanged.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
