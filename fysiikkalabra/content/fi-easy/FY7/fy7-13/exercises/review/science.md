VERDICT: PASS
CONTENT-HASH: 24f527adb3299ded
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none needed: numbers, units, formulas and answers equal to fi)

## Polish
- solutions.md L2-05 uses "kulmakerroin" without explanation; the idea (slope of the line) is stated in the same Principle line ("sen kulmakerroin on lambda : d"), so left as is.

## Checked
- All 20 exercises compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags and every number in texts, choices, feedback, data cells identical (decimal point in en, comma in fi-easy); solutions.md numbers equal to fi (1160/843 tokens, normalised).
- Formula parity with fi: check_i18n.py fi-easy 0 errors.
- Physics statements (tan for the screen triangle, sin in the grating equation, kλ < d, zeroth-order reflection back through the hole) are the same as in fi.
- L1-06 and L2-07: answer string equals the single correct choice.
