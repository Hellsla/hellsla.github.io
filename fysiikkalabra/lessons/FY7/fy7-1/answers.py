"""Every answer in exercises.json for fy7-1, computed from the task data (python -I answers.py).
Fields in µT unless stated. Perpendicular fields add as B = sqrt(B1² + B2²) (three components: sqrt(Bx² + By² + Bz²));
the compass needle settles along the total horizontal field, θ from north with tan θ = B_east : B_north; Earth's field
with the inclination I has B_h = B cos I and B_v = B sin I. 1 µT = 10⁻⁶ T.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

rad = math.radians
a = {}
# Level 1: one formula, values given
a["fy7-1-L1-01"] = 3.0 / (50 * 1e-6)                     # MRI 3,0 T against Earth's 50 µT = 50 · 10⁻⁶ T: 6,0 · 10⁴ times
a["fy7-1-L1-02"] = 53 * math.cos(rad(75))                # Kuopio B = 53 µT, I = 75°: B_h = B cos I = 13,7 µT
a["fy7-1-L1-03"] = math.hypot(14, 48)                    # B_h 14 µT north, magnet 48 µT east: B = 50,0 µT
# L1-04 (words): a magnet cut in two: both pieces have N and S; the cut faces are opposite poles and attract
# L1-05 (words): a compass on the axis beside the N pole: the needle's N end points away from the magnet
# Level 2: two steps, a conversion or a rearrangement
a["fy7-1-L2-01"] = math.degrees(math.atan2(25, 14))      # magnet 25 µT east, B_h 14 µT north: θ = 60,8° east of north
a["fy7-1-L2-02"] = math.sqrt(12**2 + 5.0**2 + 48**2)     # phone magnetometer (12; −5,0; −48) µT: B = 49,7 µT
a["fy7-1-L2-03"] = 52 / math.sin(rad(77))                # Rovaniemi B_v = 52 µT, I = 77°: B = B_v / sin I = 53,4 µT
a["fy7-1-L2-04"] = math.tan(rad(60)) / math.tan(rad(10)) # B_m = B_h tan θ at 10 cm (60°) and 20 cm (10°): ratio 9,82
# Level 3: reasoning, two ideas or an unfamiliar context
a["fy7-1-L3-01"] = 14 - 25                               # north component, north positive: magnet 25 µT south against B_h 14 µT north: −11 µT, the needle turns round
# L3-02 (words): a steel paper clip stroked with a magnet stays magnetised; heating towards the Curie temperature disorders the domains
a["fy7-1-L3-03"] = 53 * math.cos(rad(74)) / (55 * math.cos(rad(82.5)))   # B_h Helsinki 14,6 µT : Longyearbyen 7,18 µT = 2,03
# Exercise-bank additions
# L1-06 (words): a magnet attracts iron, not aluminium or copper: only ferromagnetic matter has domains that line up
# L1-07 (words): the compass needle's N end points to geographic north: Earth's magnetic S pole is there (unlike poles attract)
a["fy7-1-L1-08"] = 53 * math.sin(rad(76))                # Oulu B = 53 µT, I = 76°: B_v = B sin I = 51,4 µT
# L2-05: B_m = B_h tan θ at r = 12 cm (θ = 46°, B_h = 14 µT): 14,5 µT; B_m r³ is roughly constant, not B_m r
B_h = 14
a["fy7-1-L2-05"] = B_h * math.tan(rad(46))
# L2-06: magnetometer at the desk (31; 14; −62) µT: B = sqrt(Bx² + By² + Bz²) = 70,7 µT, ≈ 20 µT above Earth's 50 µT: iron nearby
a["fy7-1-L2-06"] = math.sqrt(31**2 + 14**2 + 62**2)
# L2-07 (error analysis): the student inverted the ratio; correct θ = atan(B_m / B_h) = atan(30/14) = 65,0°
a["fy7-1-L2-07"] = math.degrees(math.atan(30 / 14))
# L3-04: B_h = B cos I at Helsinki (53; 74°), Oulu (53; 76°), Utsjoki (52; 78°); magnet 20 µT east: θ = atan(20 / B_h), Utsjoki 61,6°
a["fy7-1-L3-04"] = math.degrees(math.atan(20 / (52 * math.cos(rad(78)))))
# L3-05: B_m = 14 µT · tan θ for r = 12…30 cm; k = mean of B_m r³ = 59,1 · 10³ µT cm³; B_m(r0) = B_h gives r0 = (k / B_h)^(1/3) = 16,2 cm
meas = [(12, 69), (14, 56), (16, 47), (20, 27), (24, 18), (30, 8)]
k = sum(B_h * math.tan(rad(th)) * r**3 for r, th in meas) / len(meas)
a["fy7-1-L3-05"] = (k / B_h) ** (1 / 3)
print(json.dumps(a))
