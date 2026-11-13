VERDICT: PASS
CONTENT-HASH: 72145bfe95e4ffab
Mode: delta, round 1

## Blocking
- none

## Polish
- [Minor] fy1-2 unit table, 360 and 768 px: the packet has no 360 or 768 px captures, only 390 and 1280 px; those two widths rest on the 390 px stacked layout and check_layout.py. Not blocking.

## Checked
- fy1-2-theory-1280-2.png: the table has four short headers, all cells LaTeX with units, no wrapping problem except natural wraps in "Planeettojen radat" and "astronominen yksikkö"; sits right after its lead sentence.
- fy1-2-stage-selita-390-2.png and -3.png (390 px): the table becomes six stacked cards with a label on each row, readable, no horizontal overflow, nothing clipped. Text after the table intact.

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
