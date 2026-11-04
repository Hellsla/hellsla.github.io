VERDICT: PASS
CONTENT-HASH: 5a9d2e56890d8159
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none needed: the English text already matched fi in every number and was natural)

## Polish
(none)

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) and all older ones compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags, data cells, and every number in texts, choices, feedback and solutions.md are identical (decimal point in en where fi has comma; solutions.md has 613 numbers each, equal).
- Units: no Finnish left (grep); display units are translated (times / swings / g/cm³ as appropriate).
- L1-06: one correct option, distractor feedback names the right error type (random, random, gross) as in fi.
- Re-derived key answers: L1-07 5.43 cm, L2-05 1.82 s, L2-06 +0.94 ml, L2-07 N=14, L3-04 2.41 s (2.48 s with all eight), L3-05 gap 0.04 g/cm³; all agree with fi.
- check_i18n.py en: 0 errors for fy1-3; lint_lesson.py clean.
