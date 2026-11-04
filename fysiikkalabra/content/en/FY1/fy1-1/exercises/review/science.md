VERDICT: PASS
CONTENT-HASH: ed984c15280d5149
Mode: full (translation review against the reviewed Finnish set, teacher procedure 2026-10-28)
Round 1

## Blocking
(none)

## Fixed
- exercises.json L1-06 feedback (two choices): "a falling model" changed to "a free-fall model" (fi: putoamismalli), the standard physics term.

## Polish
(none)

## Checked
- All 20 tasks (new: L1-06..08, L2-05..07, L3-04..05) compared field by field with the Finnish: ids, levels, kinds, answers (numbers and the L1-06 answer string), tolerances, correct flags, choice order, figure and data cells (every number, decimal point in JSON) are identical; only the unit strings are translated (orders of magnitude, times, thousand, million people, million times, billion).
- solutions.md: all 21 sections in the same order; every formula and number equals the Finnish (decimal comma to point); only subscripts are translated (e.g. d_sand, r_model,J, V_drop, d_S/d_E for Aurinko/Maa), consistently within each task.
- Physics wording kept: order of magnitude rule (a under about 3), model vs observation, uniform-motion model d = d0 + vt, unit error in the student's Voyager solution, ruler reading uncertainty and fit through the origin.
- No Finnish words or letters left in exercises.json or solutions.md.
- check_i18n en: 0 errors.
