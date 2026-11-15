VERDICT: PASS
CONTENT-HASH: 3899b2fed1ddbaa3
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- (none)

## Checked
- s7 d part text (round-1 Blocking): now asks for the estimate of the electrical energy with a thermal plant's efficiency, so the third criterion (about 1 MJ, under half a percent of 300 MJ) asks only what the task asks and gives (third bullet of the data). The solution's Kysytty is extended the same way; 3,15 MJ / 3 = 1,05 MJ = 0,35 % of 300 MJ; 3,15/300 = 1,05 %; 2,05/300 = 0,68 %.
- s7 c Vastaus: two significant figures justified by the temperature difference 80 K (100 °C − 20 °C, both given in the part); m = 3,15e6 J / (4190 J/(kg K) · 80 K) = 9,397 kg, so 9,4 kg, as in tasks.json and the rubric.
- s7 task data: the three extra facts are now full sentences under "Lisätietoja"; values unchanged (4,19 kJ/(kg K), about 300 MJ, about one third).
- s7 e first criterion: either reason is accepted (no electricity was produced, or a grid-connected plant is decades away); both are true and the solution gives both.
- `python scripts/practice.py check units/fy9-moderni`: OK (7 tasks, 110 points). Hash equal at start and end.
