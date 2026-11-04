VERDICT: PASS
CONTENT-HASH: 6c0500f6ebd3bb23

## Blocking
(none)

## Fixed
- exercises.json L3-05 text: "A steel, rigid and sealed air tank" reworded to "A rigid, sealed steel air tank" (no number changed).

## Polish
- none

## Checked
- Scripted comparison against the reviewed Finnish: all 40 ids present, answers, units (L2-04 and L2-06 "times" for "kertaa"), tolerances, kind, choices count and correct flags, data rows identical; decimal points in JSON and LaTeX.
- New tasks L1-06, L1-08, L2-05..07, L3-04, L3-05: every number in text, data tables and solutions equals the Finnish (1.5 K, 1.7 times, 40 s, 0.6 K, 145 degC, 797 and 696 kPa, 13.6 %, 16 %, 37.1 and 37.0 degC).
- Choice feedback of L1-06 and L1-08 keeps the same physics as the Finnish (open/closed decided by matter crossing the boundary; rigid container keeps volume).
- Table headers and symbols translated consistently (theta_ref, theta_forehead, theta_ear, theta_mouth, "Measurement").
- solutions.md follows the Finnish step for step with identical formulas and substitutions; no Finnish left in en.
- check_i18n.py en: 0 errors.
