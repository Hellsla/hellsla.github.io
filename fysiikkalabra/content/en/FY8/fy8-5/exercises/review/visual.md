VERDICT: FAIL
CONTENT-HASH: 462493f3cc212cb4
SCOPE: delta reflow (long solution formulas set in aligned blocks)

## Blocking
- [Major] solutions.md line 199 (interpolation) — the row ends after the fraction `\tfrac{90.0 - 72.3}{92.0 - 72.3}` and the next row opens with `\cdot 0.05`, so the product is cut in two — a break inside a term is not at a meaningful boundary and the next row reads as a stray product — keep the fraction and its factor together: break before `+ \tfrac{...}{...} \cdot 0.05\,\text{nm}`

## Polish
(none)

## Checked
- Contact-sheet level triage skipped; opened open-exercise captures at 1280 px (fy8-1 L2-3, fy8-5 L2-5, fy8-7 1, fy8-13 L3-4, fy8-16 L2-6): aligned blocks, equals signs aligned, sentence marks inside the last row, no clipping, layout intact.
- No 390 px open-exercise capture exists in the packet (only stage-exercises-390); the other formulas of this lesson were checked from the source breaks, not from a capture.
- Hash re-run at the end: unchanged.

## Scores
illustrations 4 · typography 3 · Finnish 5 · accessibility 4
