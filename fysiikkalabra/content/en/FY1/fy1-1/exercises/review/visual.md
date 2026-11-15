VERDICT: FAIL
CONTENT-HASH: c3ecfaae8afcabca

## Blocking
- [Major] content/en/FY1/fy1-1/exercises/exercises.json, task with the student's Voyager solution (captures 14, 15) — the chain of inline formulas inside the quotation is merged into two display blocks, and the sentence marks are left orphaned: a line starts with a lone `. The distance is` and `. So Voyager would be…` — lone punctuation and a broken quotation flow, reads unnaturally at 360 px — keep the quotation in one flow: write the two chains as inline formulas that wrap without being merged, or lift them as `$$…$$` directly followed by the full stop so the build moves the mark into the last row (`\text{.}`).

## Polish
- none

## Checked
delta review 5d reflow, round 1: opened the 360 px captures 02-15 (tiled into contact sheets, every capture of this part viewed); equals signs aligned, no row broken inside a number or unit, nothing clipped or scrolling, display formulas read naturally in their sentences.

## Scores
illustrations 5 · typography 3 · English 4 · accessibility 4
