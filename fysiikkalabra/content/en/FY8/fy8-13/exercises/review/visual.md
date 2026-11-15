VERDICT: FAIL
CONTENT-HASH: d0dbbc7ba907247a
SCOPE: delta reflow (long solution formulas set in aligned blocks)

## Blocking
- [Major] fy8-13-open-exercises-L3-1280-4.png, 13-19 (and the solution of the liver and stomach task, line 141) — the substitution row reads `0.12 \cdot 20 \cdot 0.10\,mGy + 1` and the next row `\cdot 0.50\,mGy`, the term `1 \cdot 0.50\,mGy` is split; the rows `+ 0.12 / \cdot 1.0\,mSv` do the same — a break inside a term is not at a meaningful boundary and the next row reads as a stray product — move the `+` to the start of the second row: `H_E &= 0.12 \cdot 20 \cdot 0.10\,mGy \\ &\quad + 1 \cdot 0.50\,mGy`

## Polish
(none)

## Checked
- Contact-sheet level triage skipped; opened open-exercise captures at 1280 px (fy8-1 L2-3, fy8-5 L2-5, fy8-7 1, fy8-13 L3-4, fy8-16 L2-6): aligned blocks, equals signs aligned, sentence marks inside the last row, no clipping, layout intact.
- No 390 px open-exercise capture exists in the packet (only stage-exercises-390); the other formulas of this lesson were checked from the source breaks, not from a capture.
- Hash re-run at the end: unchanged.

## Scores
illustrations 4 · typography 3 · Finnish 5 · accessibility 4
