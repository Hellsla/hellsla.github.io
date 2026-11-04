VERDICT: PASS
CONTENT-HASH: 52803a892f6e90e0
Round: 2
Mode: delta

## Blocking
(none)

## Polish
- none

## Checked
- Opened captures fy3-2-open-exercises-1280-7 (L1-06/07 solutions), fy3-2-open-exercises-L2-1280-6 and fy3-2-open-exercises-L3-1280-5 of fi-easy: text, inline maths, display blocks and data tables render without overflow or clipping.
- Data tables (L2-05, L2-06, L3-04, L3-05) have captions and headers in plain Finnish (selkosuomi); unit symbols in math.
- Decimal comma rendered in the data tables and maths in fi-easy.
- Answer boxes show the right units (J, W, cm, kW, m/s); no Finnish remnants in the English captures.

## Checked in round 2
- Delta (HEAD): split rows read well in source: each continuation "\\ &= result" aligns under the first "=" of its aligned block, the Finnish decimal comma / English point and unit spacing are unchanged. check_layout.py 360 px --site is OK for fy3-2 (the site still serves the previous version of the formulas, so this does not yet prove the new rows). No 360 px solution captures exist in review/shots (only 390 and 1280 shots), so the 360 px result is judged from the source: rows are now at most about one line of text at 360 px.

## Scores
illustrations 4 · typography 5 · language 5 · accessibility 4
