VERDICT: PASS
CONTENT-HASH: afe57b4cbe0531f3
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- solutions.md fy7-10-L2-07 — 'the true value is within the limits only probably' reworded to 'the true value probably lies within the limits' (natural English, same meaning, no numbers touched).

## Polish
(none)

## Checked
- Script comparison of exercises.json against content/fi: same ids (20), levels, kinds, answers, units, tolerances, correct flags, choice order, data cells and every number in texts and feedback; decimal point in en JSON and LaTeX where fi has a comma.
- solutions.md: all 20 solutions carry the same numbers in the same steps as fi (one word-order difference in L3-04, no value differs).
- Re-derived L1-07 416.4 nm, L1-08 25.50, L2-05 slope 1.498, L2-06 35.17, L2-07 dn 0.038, L3-04 mean 1.3301, L3-05 19.47 mm: all agree with fi.
- No Finnish left in en exercises.json or solutions.md (grep).
- check_i18n.py en: 0 errors.
