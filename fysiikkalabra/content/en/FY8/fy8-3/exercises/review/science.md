VERDICT: PASS
CONTENT-HASH: 6e95f62f7996146a
Mode: full
Round: 1

## Blocking
(none)

## Fixed
- exercises.json L3-04 — "the initial levels are different levels" -> "each line has a different initial level"; "limiting wavelength" -> "threshold wavelength".
- exercises.json L3-05 — "level of excitation" -> "excitation level" (also in solutions.md).
- solutions.md L2-06 Answer — "$3$ photons" was split by the answer box into "3" + "Photons. ..."; now "$3$. The atom absorbs three photons: ...".
- solutions.md L3-04 — "limiting wavelength" -> "threshold wavelength".

## Polish
- L3-05 solution Substitution is one long paragraph (same in fi); structure left as in the reviewed Finnish.

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) compared with content/fi by script: ids, answers, units, tolerances, correct flags, choices, feedback, data cells and every number identical (decimal point in JSON, LaTeX per language).
- solutions.md of the new tasks: all numbers and formulas equal the Finnish; check_i18n.py en: 0 errors.
- Recomputed: L1-06 4->1 (97.3 nm), L1-07 121.6 nm, L1-08 2.55 eV, L2-05 13.6 eV, L2-06 3 photons, L2-07 13.06 eV, L3-04 n=3 and 365 THz, L3-05 n=4 and 97.25 nm; all match.
- No Finnish left in the English text where it should not be.
