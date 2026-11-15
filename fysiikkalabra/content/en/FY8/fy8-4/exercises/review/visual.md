VERDICT: FAIL
CONTENT-HASH: 073e9ceab48f9389
SCOPE: delta reflow (long solution formulas set in aligned blocks)

## Blocking
- [Major] solutions.md line 282 (the fy8-4 solution with the sum of squares) — the row break falls inside the product `9.319 \cdot 8.863` in a parenthesis: `... + 9.319` ends one row and `\cdot 8.863)` starts the next — a break inside a term is not at a meaningful boundary and the next row reads as a stray product — break before a `+` or a `-`, never between the factors of a term: put `+ 9.319 \cdot 8.863)` on the second row

## Polish
(none)

## Checked
- Contact-sheet level triage skipped; opened open-exercise captures at 1280 px (fy8-1 L2-3, fy8-5 L2-5, fy8-7 1, fy8-13 L3-4, fy8-16 L2-6): aligned blocks, equals signs aligned, sentence marks inside the last row, no clipping, layout intact.
- No 390 px open-exercise capture exists in the packet (only stage-exercises-390); the other formulas of this lesson were checked from the source breaks, not from a capture.
- Hash re-run at the end: unchanged.

## Scores
illustrations 4 · typography 3 · Finnish 5 · accessibility 4
