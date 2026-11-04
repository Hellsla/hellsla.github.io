VERDICT: PASS
CONTENT-HASH: d8785cdaf35b2966
Mode: full
Round: 1

## Blocking
(none)

## Fixed
- solutions.md:136 (L2-07 Principle) - ungrammatical 'is a line in the frequency' rewritten to 'is a straight line as a function of the frequency' (text only, no maths changed).

## Polish
(none)

## Checked
- Scripted comparison against content/fi (20 of 20 ids, same order): every number, unit, tolerance, answer, correct flag, choice and data table cell in exercises.json equals the Finnish (decimal comma vs point normalised); 0 differences.
- solutions.md: same 20 ids; all numbers equal the Finnish (L1-06..08, L2-05..07, L3-04..05 read in full).
- Recomputed new answers: L1-07 f0 = 5.56e14 Hz (539 nm); L2-07 W = 2.14 eV; L3-04 eta = 0.093 %, W = 2.30 eV; L3-05 I = 1.81 uA; L2-06 D = 0.90 eV; L2-05 h about 6.7e-34 Js.
- Physics statements (one photon per electron, intensity gives number not energy, threshold read at the frequency axis) match the Finnish.
- Language: no Finnish left; natural English, decimal point in JSON and LaTeX.
- check_i18n.py en: 0 errors for fy8-1 (the remaining errors are fy8-4 only).
