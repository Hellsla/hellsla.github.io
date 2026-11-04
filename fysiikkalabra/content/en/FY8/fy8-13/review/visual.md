VERDICT: PASS
CONTENT-HASH: 141c2ca7c9b3b1f4

## Blocking
(none)

## Polish
- [Minor] lesson.md weighted doses — the effective-dose sentence is long ("... not anyone's individual risk, and with it very different exposures ... can be compared") — split after "individual risk": "With it, very different exposures ... can be compared."
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `H_\text{E} = 0.12 \cdot 20 \cdot 0.50\,\text{mGy} = 1.2\,\text{mSv}`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.

## Checked
- delta review of 2c31ff041: exit-ticket answer (effective dose: small doses, average person); diff read. `screenshot.py fy8-13 --lang en --if-stale` (fresh captures).
- Own 390 px element captures of each changed block opened (scratchpad caps/en-fy8-13-*-390.png): text wraps cleanly, KaTeX renders, no clipping, no horizontal scroll. Measured every inline .katex (getClientRects().length) at 360, 390 and 1280 px, all boxes open and all feedback shown, after `build.py fy8-13`: no formula in a changed passage breaks onto two lines.
- Earlier: batch delta review: opened the captures of the changed passages (theory-1280 / example-390), source diff read; no figure changed; text-only edits render cleanly, no clipping, no horizontal overflow, no inline formula wrapped.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
