VERDICT: FAIL
CONTENT-HASH: 2652c350745c0908
Mode: delta
Round: 2

## Blocking
- [Major] data-table captions in L2-05, L2-06, L3-04, L3-05 (390 px) — the caption is one unwrapped line wider than the phone, so the closing "(example data)" / "(esimerkkiaineisto)" label is cut off (measured caption widths against about 330 px of space: "Ilman paine hitaassa ja nopeassa puristuksessa (esimerkkiaineisto)" is 469 px wide). It is the label that marks the data as example data, so a reader may take it for a real measurement. The same defect was in my round-1 finding; the round-1 fix reached only L2-08, and the cause is the shared template, not the wording — let the caption wrap (white-space: normal on the data table caption in templates/CSS), which fixes every chapter at once; shortening each caption is the alternative. May wait only if the template fix is scheduled before publication.

## Polish
- [Minor] L2-08 solution (fy3-13) / graph tick labels (fy3-9) — small items from round 1 (en-dash line break in "114.5–116.5 kPa"; small tick labels of the pick-* graphs at 390 px) remain optional.

## Checked
- Own 390 px renders of every exercise task with solutions open: fi-easy L2-08 and caption widths of all tasks; caption widths of every data table in the four pages measured by script.
- Round-2 re-check (fi-easy figures.json changed): L2-08 graphs and aria-labels unchanged and correct.
- Maths (fractions, aligned substitutions, units upright, decimal comma) clean in the opened tasks; no other blocking item seen. Sheets 1, 4, 5 of the full en sets were not opened.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
