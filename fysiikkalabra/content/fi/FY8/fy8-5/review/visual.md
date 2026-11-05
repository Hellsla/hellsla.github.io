VERDICT: PASS
CONTENT-HASH: 8c4a1518d4ca3b47

## Blocking
(none)

## Polish
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.

## Checked
- delta review of 2c31ff041: learning goal 2 (orbital as a quantum state, its picture as a region); diff read. `screenshot.py fy8-5` fails because build.py exits on the en inquiry.json (see en report); the fi page was built before the abort and contains the new goal, so captures were taken with `--no-build`; intro-1280 opened.
- Own 390 px element captures of each changed block opened (scratchpad caps/fi-fy8-5-*-390.png): text wraps cleanly, KaTeX renders, no clipping, no horizontal scroll. Measured every inline .katex (getClientRects().length) at 360, 390 and 1280 px, all boxes open and all feedback shown, after `build.py fy8-5`: no formula in a changed passage breaks onto two lines.
- Earlier: batch delta review: heading "Orbitaali kuvaa elektronin kvanttitilaa", paragraph and summary bullet; built page and scripts/screenshot.py fy8-5 (captures current), changed passages opened at 390 px (b-390-0, b-390-1): clean wrapping, KaTeX renders, no inline formula wraps, no clipping, no horizontal scroll. Diff read; the rest of the lesson unchanged.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
