VERDICT: PASS
CONTENT-HASH: 3e8591f7a1a46170
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none: no translation text needed changing)

## Polish
(none)

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05): ids, level, kind, answer, unit, tolerance, correct flags, choice order and every data table cell identical to fi (programmatic comparison of all non-string fields; every number in every string compared after normalising decimal separators: 0 differences).
- Formulas and LaTeX in exercises.json and solutions.md match fi; recomputed 6.0 V, 27 mW (7.32 s, 0.1366 m/s), 0.35 mWb, 2.7 m/s^2 (v_r 0.74 m/s, k 0.663), 0.15 W (k 1.201 W/mm^2): all agree with the fi answers.
- Physics wording faithful: Lenz opposes the change in flux, not the field; N/S pole directions in L1-06 and L2-06 as in fi; eddy-current braking explained as in fi.
- English: natural, no Finnish left (grep for ä/ö in exercises.json and solutions.md: none); decimal point in JSON and LaTeX.
- python3 scripts/check_i18n.py en: 0 errors.
