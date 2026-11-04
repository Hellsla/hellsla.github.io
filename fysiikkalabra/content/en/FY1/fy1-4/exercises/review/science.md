VERDICT: PASS
CONTENT-HASH: d125c3f6de81de21
Mode: full (translation review against the reviewed Finnish set, teacher procedure 2026-10-28)
Round 1

## Blocking
(none)

## Fixed
- exercises.json fy1-4-L2-07: unit "kertaa" (Finnish left over) -> "times", as in the other English ratio tasks (display unit only; answer and tolerance unchanged).
- solutions.md fy1-4-L2-07 Reasonableness: "B weighs roughly three times as much as A" (mass context) -> "B has roughly three times the mass of A".
- solutions.md fy1-4-L3-04: "Of the measured points" -> "Among the measured points" (two places).

## Polish
(none)

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) and the changed ones compared with content/fi: ids, answers, units, tolerances, correct flags, data cells and every number in text, choices, feedback and solutions identical (decimal point for comma).
- Recomputed with my own script: L1-08 b = 2.5 cm; L2-05 LSQ slope 0.0797 mm/g; L2-06 intercept 0.829 m; L2-07 slopes 2.71 and 7.84 g/cm3, ratio 2.89 (LSQ 2.89); L3-04 first-five slope 0.0802 mm/g, 600 and 700 g clearly above the line; L3-05 k 0.475, dk 0.075, 15.8 % (student used the full difference, 32 %). All agree with Finnish and solutions.
- MC feedback of L1-06 and L1-07 faithful: one correct option each, every distractor wrong for the stated reason.
- No Finnish left (grep); check_i18n.py en: 0 errors.
