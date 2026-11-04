VERDICT: PASS
CONTENT-HASH: a7033a860cc7acce

Science review, round 2, of the English translation of fy9-energia (source content/fi/units/fy9-energia/, already passed).

## Blocking
None (round 1 had none).

## Round-1 findings
- Polish 1 (hero description "chimney and cooling"): fixed, now "its chimney and its cooling tower" in figures.json and unit.md.
- Polish 2 ("the share of X in Y"): fixed in inquiry.json (activities 7, 10, 15, 19 and the efficiency link), tasks 2b and 5a; now "the fraction of the power entering it that comes out" etc. Meaning unchanged and correct. The one remaining "a larger share of the energy" (solutions.md, task 5 inquiry plan) is idiomatic English.

## Checks done
- python3 scripts/check_i18n.py: en 0 errors (answers, units, tolerances, correct flags, formulas, figures, sections unchanged).
- git diff of the round-2 fixes touches only wording: no number, formula, answer or correct flag changed. Round-1 recomputations (chain 198 MW, pumped storage 75 %, kettle 83.4 %, pellets 3.7 t, January extrapolation 230 kWh etc.) still stand.

## Polish
None.
