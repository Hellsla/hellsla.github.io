VERDICT: PASS
CONTENT-HASH: 6fabd323295174cf
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- exercises.json L2-06 b: 'How many times the wavelength is the gap' -> 'How many times as wide as the wavelength is the gap'.
- exercises.json L3-05 b: 'How many times the wavelength of FM radio is the width of the mountain?' -> '... as large as the wavelength of FM radio ...'.
- exercises.json L3-04: 'A fisher' -> 'An angler'.
- solutions.md L2-06 and L3-05 answers: 'times the wavelength in width' and 'times the width of the wavelength of FM' reworded to 'times as wide as the wavelength'. Numbers and formulas untouched.

## Polish
- none left.

## Checked
- 8 new exercises (L1-06..08, L2-05..07, L3-04..05) against fi: ids, answers, units, tolerances, correct flags, choice order and feedback, data table cells, every number in exercises.json and solutions.md identical (math tokens compared programmatically; en decimal point, fi-easy comma as fi).
- Recomputed: 48 ms; 342.86 -> 343 m/s; lambda 1.8 cm, b/lambda 8.0; 32 deg; depths 40.0, 44.4, 52.5, 66.6, 71.8, 62.9 m and slope 35.1 deg; lambda 333 m, 3.00 m, 0.500 m and b/lambda 200.
- L1-06/07 feedback is physically right (fixed end inverts, free end does not; diffraction depends on b/lambda).
- No Finnish left in en (grep for ä/ö clean).
- check_i18n: 0 errors.
