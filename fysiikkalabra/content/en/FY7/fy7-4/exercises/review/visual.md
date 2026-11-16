VERDICT: PASS
CONTENT-HASH: 5666845b183f76d2

## Blocking
- none

## Polish
- [Minor] solutions.md:100 — at 1280 px `= 0.074 T.` keeps its own row although the line has room; harmless.

## Checked
- Delta (queue 5d reflow), round 2. The packet's inventory has no phone capture of the opened solutions, so own captures were made from preview/en/fy7-4.html (rebuilt with build.py) with every solution open at 360, 390 and 1280 px; the 390 and 1280 px sheets of every solution step and task text the diff touches were read at full size (S-Efy7-4-390-*.png, S-Efy7-4-1280-*.png in the session scratchpad).
- Measured at all three widths over the whole exercise section: no formula wider than its card or scrolling in its box (so nothing of docs/clipped-formulas.tsv clips on this page in these captures), no page overflow, no KaTeX error, no raw LaTeX, no lone punctuation line.
- Source against main: the same tokens in the same order outside any new exercise; every new row starts with a relation, a sign or between whole quantities; the older aligned blocks are unchanged.
- 390 and 1280 px: the conversions, the checks (lines 29, 100, 128, 220), the L3 substitution `F = … / · sin 74° / = …`, the numerator and force rows of the two-wire task. Line 220 now breaks before the colon (`0.225 N` / `: (6.0 A · 0.25 m · sin 30°)`), the bracket whole. The quoted student calculation is inline and wraps inside its card.
- Hash identical at the end.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
