VERDICT: PASS
CONTENT-HASH: 86b73387a7a9c485

## Blocking
(none)

## Fixed
- L2-07 (answer feedback x2 and solutions.md model answer) — added the explanation "eli hajoamisessa vapautuu energiaa" after "$Q > 0$" so that the term is understood without the lesson.

## Polish
- L1-06 task adds "(Välittäjähiukkanen on hiukkanen, joka välittää voiman.)"; good, no change.

## Checked
- New exercises L1-06..08, L2-05..07, L3-04..05: ids, level, kind, answers (1; 5; 3; 0.797 MeV; 218.5 MeV), units, tolerances, correct flags and choice order match fi; a script diff of all non-text fields and of all numbers in exercises.json against fi found none.
- Data table cells and LaTeX are identical to fi (decimal point in JSON tables).
- Recomputed all eight answers (charge +1 e; 5 hadrons; 3 forbidden reactions; 0.7965 = 0.797 MeV; 218.471 MeV); solutions.md numbers equal fi.
- Terms explained in simple Finnish: välittäjähiukkanen, annihiloituu eli tuhoutuu, antikvarkin varaus vastakkainen kuin kvarkin varaus.
- check_i18n.py fi-easy: 0 errors.
