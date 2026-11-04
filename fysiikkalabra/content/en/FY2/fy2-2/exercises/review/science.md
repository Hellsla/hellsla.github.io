VERDICT: PASS
CONTENT-HASH: fbb196b146849b7c
Mode: delta
Round: 1

## Blocking
(none)

## Fixed
- L2-07 exercises.json: "What does the slope tell?" changed to "What does the slope tell you?".
- L2-06 solutions.md Principle: "are not of the same size class even if their numbers are combined" replaced with "are not in the same unit, even though their numbers can be added together" (clearer).

## Polish
- (none)

## Checked
- New exercises L1-06..08, L2-05..07, L3-04..05 compared with the reviewed Finnish in exercises.json: ids, kind, level, answers (incl. the choice answer 0.0033 GJ), units, tolerances, correct flag, all four choices and their feedback, all data table cells and every number are identical.
- solutions.md: all math segments of the 8 new solutions equal the Finnish (formula parity); numbers recomputed: 1200 kJ, 350 MJ, 1.6 MJ and 7.3 km, 2.5 MJ, 6.0 km (slope 250 kJ/km), 49 000 times (3 200 000 / 65 GJ), 0.89 kg (1.10 MJ/day x 30 / 37).
- Decimal point used throughout in JSON and LaTeX; no mixed separators.
- Unit labels ("km", "kJ", "MJ", "times"/"kertaa", "kg") translated correctly.
- check_i18n.py en: 0 errors. No Finnish left in the English text.
