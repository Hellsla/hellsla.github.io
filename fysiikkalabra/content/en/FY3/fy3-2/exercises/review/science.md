VERDICT: PASS
CONTENT-HASH: 8eacddf7d35b9750
Mode: full
Round: 1

## Blocking
(none)

## Fixed
- fy3-2-L2-06 exercises.json text: "in a staircase" changed to "while climbing a staircase" (natural English).

## Polish
- none

## Checked
- Translation review against the reviewed Finnish: all 12 exercises (focus L1-06..08, L2-05..07, L3-04..05). A structural diff of exercises.json found identical ids, kinds, answers, units, tolerances, correct flags, choice order, data rows and every number/inline-math value (decimal point in en JSON and LaTeX where applicable).
- Solutions: all formulas, substitutions and results match fi (only language words and subscripts differ: rectangle/trapezium, avg, start/end). L2-07 model answer reorders $40$ and $W = F s$ for natural English only.
- Key results recomputed: L2-05 55.3 J, L2-06 229.8 W, L2-07 588.6 J, L3-04 0.500 J and 25.5 cm, L3-05 3.6 kW; all agree with answers.
- Concept items L1-06 and L1-08: correct choice and feedback match the Finnish physics, distractor feedback intact.
- English: natural, no Finnish left in en. check_i18n.py: 0 errors.
