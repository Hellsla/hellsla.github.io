VERDICT: PASS
CONTENT-HASH: feeb2becb9e04fe2
Mode: delta (new task L2-08, translation against reviewed fi)
Round 2

## Blocking
(none)

## Fixed
(none needed)

## Polish
(none)

## Checked
- L2-08 ids, kinds, order (B, D, A, C), answer string, unit, tolerance identical to fi; values and units in the text identical (decimal point/comma only).
- Recomputed: A 2.7, B 0.90, C 9.0, D 1.2 g/cm3; conversions 0.36 kg = 360 g, 0.40 dm3 = 400 cm3, 4.5 kg = 4500 g, 100 ml = 100 cm3; order correct.
- Solution: same steps and remarks as fi (B floats, mass order differs, two significant figures).
- check_i18n.py: nothing for fy1-7; build.py fy1-7 succeeds.
