VERDICT: PASS
CONTENT-HASH: eda68d9188c67dc3
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- exercises.json L2-05 b): "Moninkertainenko" (awkward, abstract) changed to "Kuinka monta kertaa suurempi ..." (plain words, same meaning, no numbers touched).

## Polish
(none)

## Checked
- Script comparison with content/fi: ids, levels, kinds, answers, tolerances, correct flags, choices, data cells and every number in texts, feedback and solutions.md (684 numbers each, identical; decimal point in JSON/data, {,} in LaTeX). Units equal except the display unit "kertaa" (en: times, fi-easy: kertaa), as intended.
- Plain Finnish: short sentences, terms explained (läpilyöntilujuus, vikavirta, suojausluokka).
- Re-derived: L1-08 6.0 kV, L2-05 61.1x, L2-06 9.565 A, L2-07 115 mA, L3-04 20.5 A, L3-05 6.167 kOhm; all agree with fi.
- check_i18n.py fi-easy: 0 errors.

