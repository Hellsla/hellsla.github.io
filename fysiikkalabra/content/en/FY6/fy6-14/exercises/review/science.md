VERDICT: PASS
CONTENT-HASH: 9fb68adcdfde4a9a
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- solutions.md L1-07 model answer: "The wrong options are incorrect" -> "The other options are wrong" (redundant wording).

## Polish
- exercises.json L3-04 and solutions.md: the subscript in $E_\text{kul}$ (Finnish kulutus) stays because check_i18n requires formula parity with fi; the table column says 'electricity consumption' so the meaning is clear. Could be renamed in all languages later (e.g. $E_\text{cons}$).

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) and the older ones compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags, choices, feedback, data cells and every number in texts are identical (decimal point in JSON and LaTeX).
- solutions.md: all 537 numbers equal in order to fi (one reordering of 2.0/0.2 in the L1-05 graph reading, same values).
- Physics re-derived: L1-08 17 %, L2-05 207 ohm (red LED), L2-06 181 mW, L2-07 387 ohm, L3-04 88 %, L3-05 13.8 mA; match fi.
- Distractor feedback names the right error as in fi; one correct option each in L1-06 and L1-07.
- check_i18n.py en: 0 errors.
