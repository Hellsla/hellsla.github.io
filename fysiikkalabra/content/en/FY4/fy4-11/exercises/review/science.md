VERDICT: PASS
CONTENT-HASH: c3082ec53a25f6bb
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- exercises.json: table column headers in L2-05 ($s_j$), L2-06 ($F_{ka}$) and L3-04 ($s_p$) still carried the Finnish subscripts while stem and solutions use $s_b$, $F_{avg}$, $s_{stop}$; changed to match (text only, formula parity kept; check_i18n 0 errors).

## Polish
(none)

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags, choices, data cells and every number in texts, feedback and solutions.md are identical (decimal point in JSON/LaTeX in en; decimal comma in fi-easy as in fi).
- Solutions: all 20 sections present, numbers per section equal to fi.
- Key answers unchanged: 7.4 m/s2, 7.9 m/s2, 60 km/h, 38.9 m, 66 km/h, 18.0 kN.
- L1-06/L1-07: one correct option each, distractor feedback names the same error as fi.
- check_i18n.py en: 0 errors.
