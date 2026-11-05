VERDICT: PASS
CONTENT-HASH: cde76ff1bfd14f4a
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- exercises.json L1-06: the `answer` string was still the Finnish sentence while the choices were English, so the answer would never match the correct option; replaced it with the English text of the correct choice (the same string).
- exercises.json L2-07 and L3-05: gendered "She writes" / "his head" (fi has the neutral "Hän" and no gender) changed to "The student writes" / "their head".

## Polish
(none)

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) and the older ones compared with content/fi by script: ids, levels, kinds, answers, units, tolerances, correct flags, choices, feedback numbers, data table cells and every number in texts and solutions.md are identical (decimal point in en, comma in fi-easy as in fi).
- Re-derived: L1-07 98.70 W/m2, L1-08 55.59 deg, L2-05 314 lx (line through 7 and 321 lx), L2-06 50.77 deg, L2-07 53.67 deg (36.33 deg is the refraction angle), L3-04 12.5 % (120 W/m2), L3-05 h = 36.94 deg, I = 7.144 W/m2, tint breakeven theta 56.8 deg (tilt 33.2 deg). All agree with fi.
- L1-06: one correct option, distractor feedback explains the same error as fi; no Finnish left in the English text (grep).
- Wording: natural English; terms consistent with the glossary (transmission axis / läpäisysuunta, Brewster's angle, analyser).
- check_i18n.py en: 0 errors.
