VERDICT: PASS
CONTENT-HASH: 79448261a661cbdd
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none needed: the fi-easy text already matched fi in every number and was clear plain Finnish)

## Polish
- solutions.md L1-04 Reasonableness and L3-03 "about 410 V" (414 V is exact) are inherited from the reviewed fi; not changed here to keep parity, worth a later fi fix.

## Checked
- New tasks L1-06..08, L2-05..07, L3-04..05: ids, kinds, answers, units, tolerances and choice `correct` flags equal fi (script comparison of exercises.json).
- Data tables (L2-05 14 rows, L2-06, L3-04) cell by cell equal fi; en/fi-easy JSON keep the decimal point, LaTeX keeps the fi numbers.
- Every number in all solutions.md sections equals fi (decimal comma normalised); no Finnish left in en.
- Recomputed: 20.0 ms, 12.02 V, 5.94 V, 2.44 %, 0.2609 A, B = 0.3404 T, P2 = 56.85 W, p_max = 113.7 W; all match.
- Formulas unchanged; check_i18n fi-easy: 0 errors.
