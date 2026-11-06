VERDICT: PASS
CONTENT-HASH: 733cd6c68e7ef781
Mode: delta
Round: 2

## Blocking
(none)

## Fixed
- (none; delta: only the L2-08 table caption was shortened to "Air pressure, sealed bottle (example data)"; no number, formula or answer changed)

## Polish
- (none)

## Checked
- Scripted comparison of fy3-13-L2-08 against fi: text, table cells, answer, kind, four choices, correct flag and order identical; every number (13.5, 0.8, 1.0 kPa, intervals 101.0-103.0, 101.8-103.8, 114.5-116.5, 62 kPa, -100 degC, 120 degC) equals fi; English decimal point throughout.
- Recomputed: 115.5-102.0 = 13.5 kPa (>10 x 1.0); 0.8 < 1.0 so intervals overlap; fitted slope ~0.34 kPa/degC gives ~62 kPa at -100 degC. Correct choice is the only valid conclusion.
- Physics: "cannot show" is not "no difference"; extrapolation is an estimate under a linearity assumption; sealed rigid bottle justifies rising p. Same as fi.
- check_i18n.py: nothing for fy3-13; build.py fy3-13 succeeds (see report).
- Caption shortened to fit 390 px: still describes the data (air pressure, sealed bottle); no physics change.
