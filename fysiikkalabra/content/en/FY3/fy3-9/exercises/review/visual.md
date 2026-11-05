VERDICT: FAIL
CONTENT-HASH: 63d133ef967c9f45
Mode: full
Round: 2

## Blocking
- [Major] data-table captions in L2-05, L2-06, L3-04, L3-05 (390 px) — the caption is one unwrapped line wider than the phone, so the closing "(example data)" / "(esimerkkiaineisto)" label is cut off (measured caption widths against about 330 px of space: "Air pressure in vessel A and volume in vessel B (example data)" is 432 px wide, the longest 485 px). It is the label that marks the data as example data, so a reader may take it for a real measurement. The same defect was in my round-1 finding; the round-1 fix reached only L2-08, and the cause is the shared template, not the wording — let the caption wrap (white-space: normal on the data table caption in templates/CSS), which fixes every chapter at once; shortening each caption is the alternative. May wait only if the template fix is scheduled before publication.

## Polish
- [Minor] L2-08 solution (fy3-13) / graph tick labels (fy3-9) — small items from round 1 (en-dash line break in "114.5–116.5 kPa"; small tick labels of the pick-* graphs at 390 px) remain optional.

## Checked
- Own 390 px renders of every exercise task with solutions open: en 9 and 13, contact sheets 0, 2 (fy3-9) and 0, 3 (fy3-13), L2-08 individually; caption widths of every data table in the four pages measured by script.
- Round-1 Major fixed: the four pick-* graphs now have English aria-labels (read from the rebuilt page), and the L2-08 caption fits.
- Maths (fractions, aligned substitutions, units upright, decimal point) clean in the opened tasks; no other blocking item seen. Sheets 1, 4, 5 of the full en sets were not opened.

## Scores
illustrations 4 · typography 4 · Finnish (English) 4 · accessibility 4
