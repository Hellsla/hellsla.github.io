VERDICT: FAIL
CONTENT-HASH: b5ff0600214c4eda

## Blocking
- [Major] fy4-15-L2-08 solution, Mallivastaus first line "v = 36 km/h = 36 000 m / 3600 s = 10 m/s" — at 390 px the inline chain is 306 px in a 304 px container and the end of the result, "10 m/s", is clipped (the final s is cut; measured scrollWidth 311 > 304) — the converted speed is the key step of the task — put the conversion in the aligned block: v = 36 km/h on one row, "= 36 000 m / 3600 s" and "= 10 m/s" on the next rows (the block already holds A and P chains in 290 px).

## Polish
- [Minor] fy4-15-L2-08 choices — the options are in ascending order of size except that the correct 2 MW stands first when rendered; fine, but the "Oikein" feedback gives the whole formula, which is acceptable here (one stage).
- [Minor] fy4-15-L2-08 solution — the final paragraph is long (about 110 words in one block); split after "…noin 90 MW." for phone reading.
- [Minor] fy4-15-L2-08 solution — "noin 47 kertaa liian suuri" and the 36^3 : 10^3 comparison are fine; the unit stack kg/m^3 in the block repeats the earlier stacked-unit style (carried polish).

## Checked
- Opened (own script vr4_task390.py, 390 px viewport, feedback of both questions and solution open, overflow measured): 12-16 (L2-08) in full, both states; the other three tasks of the diff do not exist (only this one added).
- Distractors catch the warned mistakes (v instead of v^3, v^2, km/h not converted); no correct-by-form cue (units and magnitudes only).
- Overflow measured at 390 px: page width 390; only the clipped line above.
- Text only: solutions.md diff.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
