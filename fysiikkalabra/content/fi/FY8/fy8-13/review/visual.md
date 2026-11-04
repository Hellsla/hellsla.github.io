VERDICT: PASS
CONTENT-HASH: e173669c713bd9b1

## Blocking
(none)

## Polish
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `H_\text{E} = w_{\text{T}1} H_{\text{T}1} + w_{\text{T}2} H_{\text{T}2}`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.

## Checked
- delta review of 2c31ff041: exit-ticket answer (effective dose: small doses, average person); diff read. `screenshot.py fy8-13 --if-stale` (fresh captures).
- Own 390 px element captures of each changed block opened (scratchpad caps/fi-fy8-13-*-390.png): text wraps cleanly, KaTeX renders, no clipping, no horizontal scroll. Measured every inline .katex (getClientRects().length) at 360, 390 and 1280 px, all boxes open and all feedback shown, after `build.py fy8-13`: no formula in a changed passage breaks onto two lines.
- Earlier: batch delta review: effective-dose paragraph, reasonableness line, misconception box; built page and scripts/screenshot.py fy8-13 (captures current), changed passages opened at 390 px (m-390-0): clean wrapping, KaTeX renders, no inline formula wraps, no clipping, no horizontal scroll. Diff read; the rest of the lesson unchanged.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
