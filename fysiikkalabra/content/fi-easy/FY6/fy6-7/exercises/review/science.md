VERDICT: PASS
CONTENT-HASH: dddbd64aaa8cb35d
Mode: full (translation review against the reviewed Finnish set)
Round: 2. Re-review: the only change since the PASS is the boxed value moved to the start of the first answer-step line (answers_shown).

## Blocking
(none)

## Fixed
- exercises.json L1-06, feedback of the distractor "Virtaa": clumsy sentence "Kilowattitunnissa teho eli jännite ja virta yhdessä on kerrottu ajalla." split into two short sentences ("... teho on kerrottu ajalla. Teho on jännite ja virta yhdessä."); meaning unchanged.

## Polish
(none)

## Checked
- Ids, kinds, answers, units, tolerances, correct flags, choice order, data cells and figure refs equal to content/fi by script (all 25 exercises incl. the 8 new L1-06..08, L2-05..07, L3-04..05); every number in texts, choices, feedback and solutions.md equal to fi (629 numbers each, decimal point in en / comma in fi-easy text).
- Formulas and answers unchanged; check_i18n.py fi-easy: 0 errors.
- Plain Finnish: short sentences, terms explained as in fi; decimal comma in text, decimal point in JSON data cells as in fi.
- Answer steps start with the boxed value: L2-05 730 kWh (key 733,65, tol 0,02), L2-06 335 W (335,119), L2-07 300 kWh (299,3, tol 0,05), L3-04 0,93 € (0,93), L3-05 13 a (12,957); each equals its own b) and Sijoitus and the fi set, same unit, LaTeX with decimal comma; the lines read well.
