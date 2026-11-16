VERDICT: PASS
CONTENT-HASH: 89a997b1d45fdf7c

## Blocking
- none

## Polish
- [Minor] exercises.json (find-the-error task) — in the split inline chain `e = vBl` `= 2.0 m/s · 0.50 T · 0.30 m` `= 0.30 V` the pieces that begin with `=` have no relation space on their left (`vBl= 2.0 m/s`, `0.30 m= 0.30 V` at 1280 px); readable, `${} = …$` would even it out.
- [Minor] solutions.md:256 (untouched, as on main) — the leading minus of `− 8.0 mWb : 0.40 s` is spaced like a subtraction; `{-}8.0` would set it as a sign.

## Checked
- Delta (queue 5d reflow), round 2. The packet's inventory has no phone capture of the opened solutions, so own captures were made from preview/en/fy7-5.html (rebuilt with build.py) with every solution open at 360, 390 and 1280 px; the 390 and 1280 px sheets of every solution step and task text the diff touches were read at full size (S-Efy7-5-390-*.png, S-Efy7-5-1280-*.png in the session scratchpad).
- Measured at all three widths over the whole exercise section: no formula wider than its card or scrolling in its box (so nothing of docs/clipped-formulas.tsv clips on this page in these captures), no page overflow, no KaTeX error, no raw LaTeX, no lone punctuation line.
- Source against main: the same tokens in the same order outside any new exercise; every new row starts with a relation, a sign or between whole quantities; the older aligned blocks are unchanged.
- 390 and 1280 px: the checks of lines 39, 70, 132, 179, 254; the trapezoid sum (201) broken at its plus signs inside the bracket, three rows on a phone and two at 1280 px; the find-the-error task text, inline again, wrapping at the relations with no stray punctuation.
- Hash identical at the end.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
