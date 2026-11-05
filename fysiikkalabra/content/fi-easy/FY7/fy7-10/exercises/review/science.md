VERDICT: PASS
CONTENT-HASH: 42fcf9545eae0e70
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none needed: fi-easy matches fi in every number, unit, tolerance and flag, and the wording is plain)

## Polish
(none)

## Checked
- Script comparison of exercises.json against content/fi: same ids (20), kinds, answers, units, tolerances, correct flags, choice order, data cells and every number in texts and feedback (fi-easy keeps the decimal comma in text, as fi).
- solutions.md: all 20 solutions have the same numbers and steps as fi; check_i18n formula parity passes.
- Re-derived L1-07 416.4 nm, L1-08 25.50, L2-05 slope 1.498, L2-06 35.17, L2-07 dn 0.038, L3-04 mean 1.3301, L3-05 19.47 mm: all agree.
- Selkosuomi: short sentences; the new tasks split fi's long sentences (L2-05, L2-07, L3-04, L3-05) and L3-04 defines apparent depth in its own sentence.
- check_i18n.py fi-easy: 0 errors.
