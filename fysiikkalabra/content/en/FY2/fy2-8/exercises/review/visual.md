VERDICT: PASS
CONTENT-HASH: bfa242d0bb3d6d72
Mode: full
Round: 1

## Blocking
- none

## Polish
- none

## Checked
- en fy2-8-open-exercises-1280-6, -7, -8 (L1-06 greenhouse choices with feedback and solution, L1-07 climate vs weather, L1-08 input with kg unit and solution start): choices, feedback boxes, inline maths and the temperature values render correctly.
- fy2-8-open-exercises-L2-1280-5 (L2-05 table with caption, columns t (a) and c (ppm), ppm/a unit next to input) and fi-easy fy2-8-open-exercises-L3-1280-5 (L3-04 table, a) to c) bold questions, Answer/Solution blocks with maths): layout fits at phone width, no overflow, no leftover Finnish in en.
- Table headers short; units in column headers as in the Finnish. Remaining L2-06, L2-07, L3-05 follow the same components and were not found to differ from the Finnish text.

## Scores
illustrations 4 · typography 4 · Finnish (English) 4 · accessibility 4

## Follow-up (2026-11-04, teacher's edit of L1-06: exercises.json:69, solutions.md:125)
- Own Playwright check of the built preview, L1-06 answered (option 0) and the solution open: every inline formula of the two sentences ($+15\,{}^\circ\text{C}$, $-18\,{}^\circ\text{C}$, $33\,\text{K}$) lies on one line (one line box per `.katex-html`) at 390 px and at 360 px; scrollWidth = viewport width; no raw `$`. Captures retaken (`screenshot.py fy2-8 --lang <lang>`, 1280 px) and an own 390 px capture of L1-06 opened.
- Typography consistent with the lesson (thin space before units, upright C and K). English natural; "while" marks the contrast clearly.
- Scope: only these two sentences; the rest of this report stands from the earlier round.
