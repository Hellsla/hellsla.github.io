VERDICT: PASS
CONTENT-HASH: e14a5605376412b0
SCOPE: delta added-exercise from 73e42d2dc825c95e base 141dc47a8c70

## Blocking
(none)

## Polish
- content/en/FY3/fy3-11/exercises/exercises.json fy3-11-L2-09 — a 50 cm2 cylinder with a gas column 0.20 -> 0.80 m is long for a 'small gas engine' — a 'laboratory cylinder' would be more realistic (same in the Finnish; not a physics error).

## Checked
- fy3-11-L1-09: MAFY 1 atm = 101 325 Pa; W = p dV = 202.65 J -> 2.0e2 J; sign (work by the gas positive on expansion) right; 200 J ~ 2 kg lifted 10 m correct.
- fy3-11-L2-09: isobar 1.0 -> 4.0 l at 250 kPa read on grid; dV = A ds gives 0.60 m; pressure correctly not needed; column-length check consistent.
- en vs fi: answer, unit, tolerance, figure, lookup, kind and every number of task text and solution identical (script comparison).
- Recomputed in one independent script; answers.py lines agree; tolerances fit the data's significant figures and graph reading.
