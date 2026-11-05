VERDICT: PASS
CONTENT-HASH: 8544fb54b522a8ea
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none needed: the English text already matched fi in every number and was correct)

## Polish
(none)

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) and the older ones compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags, choices order, data cells (JSON structure identical). Only the three text answers (L1-06, L1-07, L2-06) differ, as translated, and each equals the text of its correct choice.
- solutions.md: 897 numbers in the same order as fi (script, decimal separator normalised); formulas and LaTeX unchanged.
- No Finnish left (grep for ä/ö/å in json and md: none); decimal point in JSON and LaTeX; terms dielectric, dielectric strength, relative permittivity, capacitance used consistently.
- Re-derived: L1-08 144 mJ, L2-05 3.4 mJ (C about 47 uF), L2-07 63.4 mJ (half of QU = 127 mJ), L3-04 C = 150 uF, W = 243 J, P = 48.6 kW, t = 18 s, L3-05 ratio 6.89; all agree with fi.
- check_i18n.py en: 0 errors.
