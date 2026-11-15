VERDICT: PASS
CONTENT-HASH: 53b02751f63afd8a
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- C: s7 b reasonableness: with h = 400 km the consistent period is 92,4 min, so the rounding of T alone gives the whole 0,9 % difference (T = 92 min would fit h = 380 km). "ja malliin valitulla korkeudella yhdessä" is defensible (the pair T, h is not exactly consistent) but adds nothing; optional.

## Checked
- s7 a principle: the new sentence says the 370-460 km interval is where the altitude is kept over time, not a variation within one orbit; correct, and 90 km / 6771 km = 1,3 % still supports the circular model.
- s7 b reasonableness recomputed: a_n = 4 pi^2 r / T^2 = 8,773 m/s^2; gamma M / r^2 = 8,694 m/s^2; difference 0,9 %. The new wording is not wrong (see Polish).
- s7 e: the shadow-edge angle is now defined from the Earth's centre against the direction pointing away from the Sun, with sin(theta) = R/r: correct for a cylindrical shadow with the Sun in the orbital plane (perpendicular distance r sin(theta) = R). theta = 70,2 deg, 2 theta / 360 deg = 39,0 %, 35,9 min, 84 kW / 0,61 = 138, about 140 kW: unchanged and right.
- `practice.py check` OK (7 tasks, 110 points).
