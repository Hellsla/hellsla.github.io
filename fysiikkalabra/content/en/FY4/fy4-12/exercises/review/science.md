VERDICT: PASS
CONTENT-HASH: 056e48eb6dc95ff0
Mode: delta (translation review of the new task fy4-12-L2-08 against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
(none needed): the translation already matched fi in physics, numbers and correct answers.

## Polish
(none)

## Checked
- fy4-12-L2-08 (choice of the (t,v) graph for a braking car and a moped): all numbers, units, symbols and the answer/correct flags/true flags compared with fi by script; identical (decimal point).
- Recomputed: car v = 20 - 2.0t, zero at 10 s, crosses 12 m/s at 4.0 s; x_A(8) = 96 m = x_B(8).
- Option order, figure ids and feedback meaning match fi; each distractor feedback is physically right.
- Option figures fy4-12/pick-oikea, -kohtaus, -alku, -kaari: the en descriptions in figures.json were compared with the Finnish descriptions (figures.py) and with the physics: pick-oikea 20 to 0 m/s, cross at 4 s; pick-kohtaus 20 to 10 m/s, cross at 8 s; pick-alku 12 to 0 m/s at 6 s; pick-kaari v = 20 - 0.2t^2, 15 m/s at 5 s, cross at sqrt(40) = 6.3 s. All match; no differences.
- solutions.md section fy4-12-L2-08: structure (Find/Principle/Model answer) and every formula and number match fi.
- check_i18n: no messages for fy4-12; build.py fy4-12 succeeded.
