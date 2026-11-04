VERDICT: PASS
CONTENT-HASH: 7dc28f251828e30e
Round: 3
Mode: delta

## Blocking
(none)

## Fixed
- No change needed.

## Polish
- none

## Checked
- fy3-3-open-exercises-L2-1280-6 (L2-05): task text, table with theta_vert and theta_A, decimal comma shown as 0,0 and 1,4, unit K and solution start render correctly.
- No English left in the fi-easy captures opened; Finnish table headers (Mittaus, korva, otsa, suu) match the Finnish version.
- Line breaks of the shorter sentences read well; no overflow.

## Checked in round 2
- Delta (HEAD): split rows read well in source: each continuation "\\ &= result" aligns under the first "=" of its aligned block, the Finnish decimal comma / English point and unit spacing are unchanged. check_layout.py 360 px --site is OK for fy3-2 (the site still serves the previous version of the formulas, so this does not yet prove the new rows). No 360 px solution captures exist in review/shots (only 390 and 1280 shots), so the 360 px result is judged from the source: rows are now at most about one line of text at 360 px.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4

## Checked in round 3
- Delta (HEAD~3..HEAD, solutions.md display maths only): The corrected forehead temperature is now a single display formula, which fits a 360 px line better than the old split row; the aligned block above ends cleanly (the trailing space after the last row is harmless). check_layout.py fy3-3 --width 360 on freshly built preview: OK (fi, en, fi-easy), no formula overflow, only the existing wide-table scroll warning.
