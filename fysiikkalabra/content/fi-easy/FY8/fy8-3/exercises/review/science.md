VERDICT: PASS
CONTENT-HASH: 8824874f7b9c2f5a
Mode: full
Round: 1

## Blocking
(none)

## Fixed
- exercises.json L3-04 — "Lähtötasot ovat kuitenkin eri tasoja" -> "Jokaisella viivalla on kuitenkin eri lähtötaso"; "ionisoi atomin" explained ("eli irrottaa elektronin"); question about the limit wavelength shortened.
- exercises.json L3-05 — "virityksen taso" -> "viritystaso"; L2-06 — condition reworded ("perustilan ja jonkin ylemmän tason energioiden erotus").
- solutions.md L2-06 — "vastaavuuden raja" -> "sallittu poikkeama"; Answer "$3$ fotonia" -> "$3$. Atomi absorboi kolme fotonia:" (answer box split the old text).
- solutions.md L3-05 — "kaskadi" -> "siirtymäketju".

## Polish
- L3-05 solution Substitution is one long paragraph (same in fi); structure left as in the reviewed Finnish.

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) compared with content/fi by script: ids, answers, units, tolerances, correct flags, choices, feedback, data cells and every number identical (decimal point in JSON, LaTeX per language).
- solutions.md of the new tasks: all numbers and formulas equal the Finnish; check_i18n.py fi-easy: 0 errors.
- Recomputed: L1-06 4->1 (97.3 nm), L1-07 121.6 nm, L1-08 2.55 eV, L2-05 13.6 eV, L2-06 3 photons, L2-07 13.06 eV, L3-04 n=3 and 365 THz, L3-05 n=4 and 97.25 nm; all match.
- No Finnish left in the plain Finnish (selkosuomi) text where it should not be.
