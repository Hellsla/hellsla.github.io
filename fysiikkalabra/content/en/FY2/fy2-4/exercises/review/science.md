VERDICT: PASS
CONTENT-HASH: 094b25cee3a6cbf1
Mode: full
Round: 2

## Blocking
(none)

## Fixed
- none needed for the new task fy2-4-L2-08.

## Polish
- none

## Checked
- Scripted comparison with fi over all 20 exercises: ids, order, answers, units, tolerances, level/core/kind and correct flags equal.
- L2-08: numbers equal fi (2.5 kW, 4.0 min, 360 kJ, 600 kJ, 240 kJ, 0.60 = 60 %, 167 %); English decimal point; natural English ("mains", "divided the wrong way round").
- Recomputed L2-08: E_o = 2500 W * 240 s = 600 kJ; E_h = 240 kJ; eta = 360/600 = 0.60 (line 4 swapped, 167 % > 100 %); 240/600 = 0.40, 60 % + 40 % = 100 %. Line 4 is the only wrong line; each distractor's feedback is true.
- Physics same as the reviewed Finnish: steady-power E = P t, conservation, eta = E_a/E_o <= 100 %; within FY2 scope.
- solutions.md L2-08 equals fi in content, steps and numbers.
- check_i18n.py shows nothing for fy2-4; build.py fy2-4 succeeds.
