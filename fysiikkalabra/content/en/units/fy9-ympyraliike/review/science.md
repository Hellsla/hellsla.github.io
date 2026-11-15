VERDICT: PASS
CONTENT-HASH: edffd35f7b1b0daa
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: s7 e: say from which direction the angle is measured ("measured at the centre of the Earth from the direction pointing away from the Sun"); without it sin(theta) = R/r is hard to follow.
- C: s7 a: the 370-460 km of the source is the range in which the altitude is kept over time, not the difference between the highest and lowest point of one orbit; "so a circular orbit is a good model" still holds.

## Checked
- Item 18: s3 a "a falling curve that becomes less steep as the period grows" describes F proportional to 1/T^2 correctly (the old "downward-curving" was wrong); the factor of four on halving the period agrees.
- s7 recomputed with my own formulas: a r = 6771 km, T = 5520 s, 7707 m/s = 27 700 km/h, gravitational check 7.67 km/s, 90 km : 6771 km = 1.3 %; b 8.773 m/s^2, ratio 0.894, field strength 8.69 m/s^2 (0.9 % difference, consistent with the rounded period); d 83.9 kW, leap year 83.7 kW, 42 kettles, 2.646e12 J; e 15.7 orbits a day, theta = 70.2 degrees, 39 %, 36 min, 84 kW : 0.61 = 138 kW. All agree with tasks.json, the solution and answers.py (practice.py check OK).
- Physics of c: gravitation is the only force, G = m a_n, N = 0 from the equation of motion, weightlessness as missing normal force; the centrifugal-force error is named correctly. Symbols follow MAFY (a_n, G with overline, gamma).
- Rubric points add up (4, 3, 3, 3, 2). Hash the same at the start and the end.
