VERDICT: PASS
CONTENT-HASH: 15f19034f31ca8a5
Round 2: delta against the version round 1 reviewed (fix round 1).
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- C: s7 b reasonableness: the 0.9 % difference comes almost wholly from the period (a 400 km orbit has T = 92.4 min, and (92.4 : 92)^2 = 1.009); "and by the height chosen for the model together" is harmless, since the two given values are simply not an exactly matching pair.

## Checked
- s7 a: the new sentence says correctly that 370-460 km is the range in which the altitude is kept over time and not a variation within one orbit; 90 km : 6771 km = 1.3 %, and the conclusion (circular orbit is a good model) still follows.
- s7 b: recomputed a_n = 4 pi^2 r : T^2 = 8.773 m/s^2, field strength 8.69 m/s^2, difference 0.9 %; the corrected explanation is consistent with these.
- s7 e: the angle is now defined (at the centre of the Earth, from the direction pointing straight away from the Sun). For a cylindrical shadow the station is at its edge when r sin(theta) = R, so the statement is right; theta = 70.2 degrees, 2 theta : 360 = 39 %, 35.9 min, 84 kW : 0.61 = 138 kW, all as in the text.
- practice.py check OK (7 tasks, 110 points). Hash the same at the start and the end.
