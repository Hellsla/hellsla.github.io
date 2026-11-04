VERDICT: PASS
CONTENT-HASH: c0a8a9997259eb61
Mode: translation review of the 8 new exercises (L1-06..08, L2-05..07, L3-04..05) against the reviewed Finnish
Round: 1

## Blocking
(none)

## Fixed
- solutions.md L1-06 Model answer — "but if needed separately beside the free-body diagram" read awkwardly — split into "Velocity is not drawn as a force. If needed, it is drawn separately beside the free-body diagram."

## Polish
(none)

## Checked
- exercises.json structure, ids, kind, fbd, unit, tolerance, answers (numeric and the two string answers of L1-06 and L1-08), correct flags and choice counts identical to fi for all 8 new exercises.
- All numbers in text, choices, feedback, data captions, columns and rows equal fi (decimal point in en JSON and LaTeX; data cells 3.0/2.5/3.9, 13.4/12.3/10.1, 0.78..4.01, 881..690 identical).
- L2-05: alpha 39.8/40.2/40.4, mean 40.1, F_B 3.9 match fi. L2-06: a = 30/12 = 2.5 m/s2 (student's 0.83 is the quoted error). L2-07: 10.0 and 6.93 give 12.2 N, measured 12.3 N.
- L3-04: a = 0.802, F_mu = 83.9 ~ 84 N, N = 185 N; L3-05: a1 1.20, a2 ~0, a3 -1.19, v_max 2.397, h 14.38 ~ 14.4 m. All equal fi.
- voimakuvio specs identical to fi; check_i18n.py en 0 errors; no Finnish text left in en strings.
