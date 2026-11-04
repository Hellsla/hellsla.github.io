VERDICT: PASS
CONTENT-HASH: f9042958b6e46deb
Mode: full
Round: 1

## Blocking

## Fixed
- None needed: no translation text had to be changed.

## Polish
- None.

## Checked
- Compared exercises.json to content/fi object by object for all 20 exercises, with focus on the 8 new ones (L1-06..08, L2-05..07, L3-04..05): ids, level, kind, answer, unit, tolerance, correct flags, choices and feedback order, data table columns and cells, and every number in the text match the Finnish.
- Maths in LaTeX identical to fi apart from the decimal separator; check_i18n.py en gives 0 errors.
- The answer of L1-06 is the translated correct choice; L1-07 (0.30 N), L1-08 (0.094 N), L2-05 (0.085 T), L2-06 (0.041 T), L2-07 (5.3 m), L3-04 (0.35 T, mu 0.20), L3-05 (54 A, opposite currents, vertically stable) agree with the fi solutions and my recomputation.
- solutions.md: structure, formulas, substituted numbers, rounding notes and the reasonableness checks equal the Finnish (L1-06..08, L2-05..07, L3-04..05 read in full).
- Text is natural English; no Finnish left (grep for ä/ö/å in exercises.json and solutions.md: none). LaTeX and JSON use the decimal point as required.
- The hash was the same at the start and the end (no edits).
