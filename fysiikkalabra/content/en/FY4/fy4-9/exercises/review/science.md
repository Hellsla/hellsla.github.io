VERDICT: PASS
CONTENT-HASH: 4b9525e95331f53c
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- exercises.json L2-05 data table header: left-over Finnish column title "Potku" changed to "Kick" (fi shows the same column; numbers untouched).

## Polish
(none)

## Checked
- All 20 exercises compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags (L1-06 single correct option, same feedback roles), data table cells and every digit sequence in texts, choices, feedback and solutions.md (835 numbers each, equal; decimal point in en JSON and LaTeX where fi has a comma).
- New exercises L1-06..08, L2-05..07, L3-04..05 read in full: meaning, signs (L1-06, L3-04, L3-05 up positive), part labels a-c and the answer-box part (b) match fi.
- Re-derived: L1-07 1.8 m/s, L1-08 18000, L2-05 927.45 N, L2-06 5.0 N, L2-07 2.88 m/s, L3-04 50.45 km/h, L3-05 447.34 N; all agree with fi.
- Natural English throughout: sentences, feedback and solutions read idiomatically; no Finnish left after the fix (grep for Finnish words and ä/ö clean).
- check_i18n.py en: 0 errors.
