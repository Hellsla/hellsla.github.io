VERDICT: FAIL
CONTENT-HASH: 2040e0e2c0e5a3c7
Mode: delta, round 1

## Blocking
[Major] fy4-10-L2-07 task text — the student's calculation `v' = (0.60 · 0.80 + 0.20 · (−0.40)) / (0.60 + 0.20) m/s = 0.` is one inline chain 420 px wide that is not split into rows and runs past the card edge: the result `0.70 m/s`, which the task asks to find the error behind, is cut off, and the page gets a horizontal scroll (scrollWidth 426 at 390 px) — essential information clipped — set the student's chain so the layout can wrap it (display `aligned`, or break after the fraction: `v' = \dfrac{…}{…}\,\text{m/s}` then `= 0{,}70\,\text{m/s}` as a second line).
- [Major] fy4-10-L2-05 solution (Substitution, parts a) — the inline chains `0.80 · 0.37 kg·m/s = 0.296 kg·m/s` and `(0.125 + 0.174) kg·m/s = 0.299 kg·m/s` are 350–400 px wide and are cut off at the card edge (the end of `0.296 kg·m/s` and `0.299 kg·m/s` is missing); not in fi-easy — unreadable result lines — shorten (drop the thin spaces' units in the middle step) or put each step on its own row.
(Both items are in text untouched by the delta, found while measuring; the new L2-08 is clean. They may only wait if the teacher accepts that the earlier PASS missed them.)

## Polish
- [Minor] fy4-10-L2-02 / L2-06 solutions — long chains (about 360 px) scroll inside `.eq-chain`; acceptable by design, but CI KaTeX is about 20 px wider, so check the rows still read.
- [Minor] fy4-10-L2-08 task — the student's four lines are plain paragraphs; fine, but line 4's fraction makes the line tall; no change needed.

## Checked
Rendered at 390 px with every hint, feedback and solution open (own scratch script): page scrollWidth, clipped elements and inline KaTeX chains over 280 px measured; no KaTeX errors.
- fy4-10-L2-08 (new, solutions.md): task, five options with feedback, solution; no overflow, units upright, `\cdot` used, solution order principle → formula → substitution → result → check is clear.
- fy4-10-L2-05, L2-07 opened at readable size (findings above). No figures in the delta.

## Scores
illustrations 4 · typography 3 · Finnish (English) 5 · accessibility 3
