VERDICT: PASS
CONTENT-HASH: 89f77d1ef5cc0755
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- solutions.md L3-05 Principle: garbled "The maximum is half of the distance 2x from the hole" reworded to "A maximum is half of the distance 2x away from the hole" (no formula change).
- solutions.md L2-07 and exercises.json L2-07 choice 2 feedback: "not shared among anything" -> "not divided among several maxima".

## Polish
- solutions.md L3-02 Principle (line 104) still says "half of the separation of the dots from the hole"; understandable, left as is.

## Checked
- All 20 exercises compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags and every number in texts, choices, feedback, data cells identical (decimal point in en, comma in fi-easy); solutions.md numbers equal to fi (1160/843 tokens, normalised).
- New tasks L1-06..08, L2-05..07, L3-04..05: answers recomputed (32.14 deg, 4, 633.7 nm, 5.53 %, 625 nm, 0.737 um); equal to json.
- L1-06 and L2-07: answer string equals the single correct choice; one correct flag, same as fi.
- No Finnish left in en (grep); table column "I (relative)" translated.
- check_i18n.py en: 0 errors.
