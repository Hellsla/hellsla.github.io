VERDICT: PASS
CONTENT-HASH: 463a31211947975a
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- content/en/FY7/fy7-5/exercises/exercises.json — L1-06 feedback — reworded two clumsy phrases ("due to the fact that no voltage appears" -> "There is no current because no voltage appears"; "would need" -> "needs").

## Polish
(none)

## Checked
- Structural diff against content/fi: same ids, keys, answers, units, tolerances, correct flags, choice order, data-table cells for all 8 new tasks (L1-06..08, L2-05..07, L3-04..05); every number in text, feedback and solutions matches fi (script check, decimal separators normalised).
- Re-derived the answers from the data: L1-07 2.25 -> 2.3 V, L1-08 0.060 T, L2-05 1.45 V (steepest interval 0.40-0.50 s), L2-06 slope 30 mV/(m/s) -> 0.15 T, L3-04 a = 1.64 -> 1.6 m/s2 and s = 1.18 m, L3-05 0.0778 and 0.0787 -> 0.078 mWb.
- L2-07 and L1-06: correct choice and feedback say the same as fi (v parallel to B gives zero force; no change of flux means zero voltage).
- Formulas, LaTeX and units in solutions.md identical to fi; only prose translated. check_i18n en: 0 errors.
