VERDICT: PASS
CONTENT-HASH: 4b38dc6f7110fbf5
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- solutions.md L1-03 Reasonableness: 'a good $10 m' (literal of 'reilut') changed to 'a little over $10 m'.

## Polish
(none)

## Checked
- Script comparison of exercises.json with content/fi: ids, levels, kinds, answers, units, tolerances, correct flags, choices, figures and every table cell are identical for all 25 exercises (new: L1-06..08, L2-05..07, L3-04..05); numbers in all strings equal (decimal point in en JSON and LaTeX).
- solutions.md: same 25 sections, same line structure and same numbers as fi (re-derived 3.61 m, 128.3 m, 1.15 m/s2, 0.84 m/s2).
- No Finnish left in en (grep); no wrong-language text in fi-easy.
- check_i18n.py en: 0 errors.
