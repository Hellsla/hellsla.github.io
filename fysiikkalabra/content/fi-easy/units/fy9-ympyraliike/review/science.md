VERDICT: PASS
CONTENT-HASH: cf5c9debf0427a60
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- (none)

## Checked
- s7 a Periaate: the range 370–460 km is now described as the band the station is kept in over a long time, not the variation within one orbit; its width 90 km is 90/6771 = 1,3 % of the orbit radius, so the circular model is justified. Correct and more careful than before.
- s7 b Järkevyys: 4π²r/T² = 8,773 m/s² against γM/r² = 8,69 m/s², difference 0,9 %; now attributed to the rounded period and the chosen model altitude together. Right: the period that fits 400 km is 92,4 min.
- s7 e: the angle θ is now defined (from the Earth's centre, between the station's direction at the shadow edge and the direction away from the Sun); for a cylindrical shadow of radius R this gives r sin θ = R, θ = 70,2°, shadow share 2θ/360° = 39 % = 36 min, 84 kW / 0,61 = 138 kW ≈ 140 kW. The condition "kun Aurinko on ratatasossa" is stated.
- `python scripts/practice.py check units/fy9-ympyraliike`: OK (7 tasks, 110 points). Hash equal at start and end.
