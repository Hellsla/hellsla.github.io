VERDICT: PASS
CONTENT-HASH: 54c5f5e52ae9b6aa
SCOPE: delta added-exercise from daa6fc4f95361ced base 89bcb63b7431

## Blocking
(none)

## Polish
- content/en/FY3/fy3-13/exercises/exercises.json fy3-13-L1-09 — tolerance 0.04 on -273.15 accepts about -262 ... -284 °C for an exact table value — a tighter tolerance would suit a lookup (same in the Finnish; not blocking).

## Checked
- fy3-13-L1-09: T = theta + T0 with MAFY T0 = 273.15 K gives theta0 = -273.15 °C; no negative kelvin temperature stated correctly.
- fy3-13-L2-09: end points (0; 75) and (100; 102.5) from fy3-3/extrapolation-points; k = 0.275 kPa/°C, theta0 = -272.7 °C; by-eye range -259 ... -286 matches 5 % tolerance; uncertainty discussion honest; extrapolation reasoned (constant V and n).
- fy3-13-L2-10: theta = -73.15 °C, p = 54.9 kPa -> 55 kPa; linearity beyond range stated in the task; p proportional to T check consistent.
- en vs fi: answer, unit, tolerance, figure, lookup, kind and every number of task text and solution identical (script comparison).
- Recomputed in one independent script; answers.py lines agree; tolerances fit the data's significant figures and graph reading.
