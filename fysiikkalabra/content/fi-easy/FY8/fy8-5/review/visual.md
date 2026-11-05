VERDICT: PASS
CONTENT-HASH: ae78867bcf7d5485

## Blocking
(none)

## Polish
- [Minor] whole page (pre-existing, outside this delta) — other inline formulas still break at 390 px, e.g. `1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}`; templates/lesson.html glues only pieces of at most 14 characters, so a longer formula can break (teacher's rule: never) — brace each as one group `${...}$`, as done in fy7-2 L1-02, or show it as a display row.

## Checked
- delta review of 2c31ff041: learning goal 2 (orbital as a quantum state, its picture as a region); diff read. `screenshot.py fy8-5 --lang fi-easy` fails because build.py exits on the en inquiry.json (see en report); the fi-easy page was built in a scratch root with only the en goal shortened and captured with `--no-build`.
- Own 390 px element captures of each changed block opened (scratchpad caps/fi-easy-fy8-5-*-390.png): text wraps cleanly, KaTeX renders, no clipping, no horizontal scroll. Measured every inline .katex (getClientRects().length) at 360, 390 and 1280 px, all boxes open and all feedback shown, after `build.py fy8-5`: no formula in a changed passage breaks onto two lines.
- Earlier: batch delta review: opened the captures of the changed passages (theory-1280 / example-390), source diff read; no figure changed; text-only edits render cleanly, no clipping, no horizontal overflow, no inline formula wrapped.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
