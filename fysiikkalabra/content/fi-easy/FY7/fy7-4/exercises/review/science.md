VERDICT: PASS
CONTENT-HASH: bfc9f517bb3ff29d
Mode: full
Round: 1

## Blocking

## Fixed
- None needed: no translation text had to be changed.

## Polish
- None.

## Checked
- Compared exercises.json to content/fi object by object for all 20 exercises, with focus on the 8 new ones (L1-06..08, L2-05..07, L3-04..05): ids, level, kind, answer, unit, tolerance, correct flags, choices and feedback order, data table columns and cells, and every number in the text match the Finnish.
- Maths in LaTeX identical to fi apart from the decimal separator; check_i18n.py fi-easy gives 0 errors.
- The answer of L1-06 is the translated correct choice; L1-07 (0.30 N), L1-08 (0.094 N), L2-05 (0.085 T), L2-06 (0.041 T), L2-07 (5.3 m), L3-04 (0.35 T, mu 0.20), L3-05 (54 A, opposite currents, vertically stable) agree with the fi solutions and my recomputation.
- solutions.md: structure, formulas, substituted numbers, rounding notes and the reasonableness checks equal the Finnish (L1-06..08, L2-05..07, L3-04..05 read in full).
- Text is clear plain Finnish: short sentences, common words; new terms are explained (virtavaaka explained in L2-05, hajonta defined in L2-05b). Decimal comma in text and LaTeX; data-table cells keep the decimal point as in fi.
- The hash was the same at the start and the end (no edits).
