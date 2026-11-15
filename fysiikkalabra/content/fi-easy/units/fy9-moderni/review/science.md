VERDICT: PASS
CONTENT-HASH: 25434baad88cf0fc
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: s7 a and d: 2,05 MJ is the laser energy delivered to the target; only part of it is absorbed by the fuel itself. "Laserit toivat polttoaineeseen" is an acceptable simplification at this level; "polttoainekohtioon" would be exact.
- A: s7 d, third criterion (electricity about 1 MJ with a thermal plant's efficiency) rests on the third bullet of the task data, which part d's text does not name; add "ja lämpövoimalan hyötysuhdetta" to the part text.

## Checked
- Item 18 hunk: s6 common mistake, "Δm lasketaan sähkötehosta eikä lämpötehosta": agrees with the solution of s6 b, which computes Δm from the thermal power 4300 MW.
- s7 recomputed with own formulas: 3,15/2,05 = 1,537; difference 1,10 MJ = 53,7 % of 2,05 MJ; inverse 0,651; m = 3,15e6 J / (4190 J/(kg K) · 80 K) = 9,397 kg, cΔT = 335 200 J/kg; 3,15/300 = 1,05 %; 2,05/300 = 0,68 %; one third of 3,15 MJ = 1,05 MJ = 0,35 % of 300 MJ; Δm = 3,15e6 J / c^2 = 3,50e-11 kg = 35 ng. All agree with tasks.json, the solution and answers.py.
- s7 physics: fusion of light nuclei, which energy is which, gain above 1 only for the fuel's balance, system boundary decides the balance, Q = cmΔT without vaporisation (said), energy conservation with E = Δm c^2 and the more tightly bound products. Two significant figures in c justified by the estimated starting temperature. Points 2+3+4+3+3 = 15.
- `python scripts/practice.py check units/fy9-moderni`: OK (7 tasks, 110 points). Hash equal at start and end.
