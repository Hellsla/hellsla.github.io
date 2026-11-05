VERDICT: PASS
CONTENT-HASH: eddb481aa99052bc
Mode: full
Round: 3

## Blocking
(none)

## Fixed
- none needed.

## Polish
- none

## Checked
- L2-08 after the split of the formula chain: correct-option feedback now reads eta = E_a : E_o, then eta = 360 kJ : 600 kJ = 0.60, then 60 % (joined by 'that is'/'which is' or 'eli'); solutions.md Rivi/Line 2 split likewise. Same numbers, formulas and correct option as the reviewed Finnish.
- Recomputed: E_o = 2500 W * 240 s = 600 kJ, E_h = 240 kJ, eta = 0.60, 240/600 = 0.40, 60 % + 40 % = 100 %.
- check_i18n.py shows nothing for fy2-4; build.py fy2-4 succeeds. Hash taken at start and end: unchanged.
- Shorter inline formulas read better at 390 px; the step order is kept and no step is lost.
- Wording stays natural English.
