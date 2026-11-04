VERDICT: PASS
CONTENT-HASH: 836787e359cdecd9
Mode: full
Round: 1

## Blocking
(none)

## Fixed
- solutions.md L2-07 Reasonableness: "63,4 % polttoaineteholle" -> "63,4 % polttoaineteosta" (correct case; the Finnish source has the same slip, left untouched).

## Polish
- None.

## Checked
- Translation review against the reviewed Finnish (teacher's procedure), new tasks L1-06..08, L2-05..07, L3-04..05: ids, answers, units, tolerances, correct flags, L1-06 choices and feedback, table cells (decimal point in JSON) and every number in texts and solutions equal content/fi (scripted number comparison of all 20 solutions, no differences).
- Recomputed L1-07 34.0 %, L1-08 12.0 GWh, L2-05 90.0 % (30.0 % / 35.0 % electrical, 84.6 -> 90.0 % overall), L2-06 1560 MW, L2-07 36.6 %, L3-04 131.9 MW, L3-05 dT mean 10.775 K and 1716 MW.
- check_i18n.py fi-easy: 0 errors for fy3-15.
