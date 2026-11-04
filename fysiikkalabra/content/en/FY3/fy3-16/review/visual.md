VERDICT: PASS
CONTENT-HASH: e7a0733ff5667593

## Blocking
(none)

## Polish
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `P = UA\Delta T = 0.90\,\text{W/K} \cdot 28\,\text{K} = 25\,\text{W}`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.
- [Minor] lesson.md U-value paragraph (untouched words of the edited line) — units in parentheses are plain text: (W/(m²·K)), (m²), (K) — write $\text{W/(m}^2\cdot\text{K)}$, $\text{m}^2$, $\text{K}$.

## Checked
- delta review of 2c31ff041: cooler-bag model sentence ($0\,{}^\circ\text{C}$ as a model assumption); diff read. `screenshot.py fy3-16 --lang en --if-stale` (fresh captures).
- Own 390 px element captures of each changed block opened (scratchpad caps/en-fy3-16-*-390.png): text wraps cleanly, KaTeX renders, no clipping, no horizontal scroll. Measured every inline .katex (getClientRects().length) at 360, 390 and 1280 px, all boxes open and all feedback shown, after `build.py fy3-16`: no formula in a changed passage breaks onto two lines.
- Earlier: batch delta review: opened the captures of the changed passages (theory-1280 / example-390), source diff read; no figure changed; text-only edits render cleanly, no clipping, no horizontal overflow, no inline formula wrapped. Worked-example area now LaTeX, checked in example-390-1.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
