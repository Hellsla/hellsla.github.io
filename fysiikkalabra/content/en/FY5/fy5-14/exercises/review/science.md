VERDICT: PASS
CONTENT-HASH: 4c32264d89c055c7
Mode: full (translation review against the reviewed Finnish set)
Round 2

## Blocking
(none)

## Fixed
- exercises.json L1-06, L1-07 and the Find line of the L1-07 solution: smoothed wording ("in the problem", "high-pitched sound", "must be true", "on its distance", "how does the listener hear the pitch"); no number, flag or choice order touched.

## Polish
(none)

## Checked
- Compared by script with fi: ids, answers, units, tolerances, correct flags, choice order, table captions/columns/cells of all 8 new tasks (L1-06..08, L2-05..07, L3-04..05) are identical; the only text-number differences are decimal comma vs point.
- Solutions: all $...$ formulas identical to fi apart from localised subscripts (f_ka -> f_mean, v_v -> v_b, v_i/v_v -> v_a/v_w), consistent with the rest of the chapter; check_i18n en shows no fy5-14 errors.
- Recomputed: beats 1/6 = 0.167 s; v_s = 340(1-392/430.5) = 30.4 m/s; f1 = 262 Hz; 500*340/310 = 548 Hz; v_b = 0.475 m/s; v = 2*0.650*196 = 254.8 m/s.
- No Finnish left in en strings.
