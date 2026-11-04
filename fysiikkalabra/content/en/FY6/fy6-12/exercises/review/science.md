VERDICT: PASS
CONTENT-HASH: 63fb0ff104381c6c
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none needed: the text already matched fi and was natural)

## Polish
(none)

## Checked
- Compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags, choices, feedback, data table cells and every number in exercises.json and solutions.md. All 8 new tasks (L1-06..08, L2-05..07, L3-04..05) and the older ones are identical; solutions.md has 895 numbers each, equal in order.
- Decimal point in en JSON and LaTeX; no {,} or decimal commas left; no Finnish characters left in en.
- Re-derived L1-08 900 eV, L2-04 284 V, L2-05 30.1 V, L2-07 6.66e-27 kg (He+), L3-04 2.78 mm, L3-05 4.14e6 m/s; all agree with fi.
- L1-06, L1-07, L2-06: exactly one correct option; distractor feedback keeps the same error type as fi.
- check_i18n.py en: 0 errors.
