VERDICT: FAIL
CONTENT-HASH: 0db84c5b62470dbd

## Blocking
- [Major] fy3-12-L2-06 (task text, 390 and 1280 px) — the display formula of the student's solution (P = UAΔT, three rows) is followed by `.”`, which stands alone on the next row, left of an empty line — the very defect of the reflow rule (punctuation alone after a display formula) and it looks like a stray mark — move the closing into the formula (`= 9.6\,\text{W}\,.”` inside the aligned block) or set the student's chain inline: `$P = UA\Delta T = 1.0 \cdot 1.6 \cdot 6\,\text{W} = 9.6\,\text{W}$.”`.

## Polish
None.

## Checked
- Own 390 px and 1280 px captures of the built page with every exercise solution open (the packet's shots hold 1280 px only): every display formula in text context (about 10 per set, stitched sheets) and a DOM check of clipping, horizontal overflow and lone punctuation after a display formula in all exercises; plus the packet captures open-exercises-L*-1280.
- Changed formulas: equals signs in one column, continuation rows start with an operator, wide screens join the rows, no clipping at 390 or 1280 px, no row breaking inside a number or unit; trailing punctuation sits inside the formula in solutions.
- Hash run at start and end: unchanged.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
