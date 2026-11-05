VERDICT: PASS
CONTENT-HASH: acf7bdc90ae62d05
Mode: full
Round: 1

## Blocking

## Fixed
- None needed: no translation text had to be changed.

## Polish
- exercises.json L1-08 - unit "kertaa" for a dimensionless ratio is acceptable; the answer is 310 (314 rounded to two significant figures) in both languages and the Finnish.

## Checked
- Scripted comparison of exercises.json against content/fi: ids, levels, kinds, answers, units (except the translated unit word of L1-08), tolerances, correct flags, data table cells and every number in text and feedback are identical for all 12 exercises, including the 8 new ones (L1-06..08, L2-05..07, L3-04..05).
- Choice sets of L1-06 and L2-07 match the Finnish: same option order, the same single correct option, the same feedback physics (right-hand rule, anticlockwise from above; B cos 60 deg = 0.50 B).
- Answers recomputed: 4.7 mT, 310, 1.26 uVs/(Am), 54 uT (and 320 uT in part d), 16 uT, 5.3 mT; L3-05 chain N = 318, l = 0.175 m, R = 2.60 ohm, I = 2.31 A all agree with the Finnish.
- solutions.md numbers, formulas and LaTeX equal the Finnish (decimal comma as in fi); principles and reasonableness checks keep the Finnish physics.
- Terms are explained in plain words (linearisointi, kierrostiheys, homogeeninen).
- python3 scripts/check_i18n.py fi-easy: 0 errors (formula parity with fi).
