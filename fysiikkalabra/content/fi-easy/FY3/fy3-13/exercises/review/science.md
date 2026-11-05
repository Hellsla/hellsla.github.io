VERDICT: PASS
CONTENT-HASH: fc8e9463ff0d07a5
Mode: full
Round: 2

## Blocking
(none)

## Fixed
- (none; no text edits were needed)

## Polish
- (none)

## Checked
- Scripted comparison of fy3-13-L2-08 against fi: table, answer, kind, choice order, correct flag and all numbers identical; formulas and units kept; decimal comma in text.
- Recomputed: 13.5 kPa >> 1.0 kPa, 0.8 kPa overlaps, ~62 kPa at -100 degC is an extrapolation of 120 degC; physics same as fi.
- NOTES.md section 12: extrapolointi explained in the feedback inline ("eli suoran jatkaminen mittausalueen ulkopuolelle"); no step dropped.
- check_i18n.py: nothing for fy3-13; build.py fy3-13 succeeds (see report).
