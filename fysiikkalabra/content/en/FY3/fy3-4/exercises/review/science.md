VERDICT: PASS
CONTENT-HASH: 35a61f460a2d50f3
SCOPE: delta added-exercise from 15b0a0fdf9fe9772 base 89bcb63b7431
Round: 1
Mode: delta

## Blocking
(none)

## Polish
- content/en/FY3/fy3-4/exercises/solutions.md (fy3-4-L2-08, Answer) — stated accepted range 1450–1600 kg/m3 is wider than the 4 % tolerance (1468–1590); same in the Finnish — align when next edited.

## Checked
- fy3-4-L1-10: p = p0 + rho g h = 101 kPa + 1020*9.81*25.0 Pa = 351.2 kPa; MAFY sea water 1.02e3 kg/m3; three figures justified.
- fy3-4-L2-08: slope of line B (0;100)->(10;250) = 15 kPa/m = rho g -> 1529 kg/m3; unit derivation Pa/m / m/s2 = kg/m3 correct; check via liquid A (1019 kg/m3) consistent.
- Figure fy3-4/two-liquids: grid crossings give the points; description lists points, not densities.
- Solutions complete, symbolic first, real reasonableness checks.
- answers.py equal to my recomputation; numbers, unit, tolerance and figure identical to the passed Finnish.
- Hash identical at start and end.
