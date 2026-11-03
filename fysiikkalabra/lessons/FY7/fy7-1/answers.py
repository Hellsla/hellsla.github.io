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
a["fy7-1-L2-03"] = 51 / math.sin(rad(77))                # Rovaniemi B_v = 51 µT, I = 77°: B = B_v / sin I = 52,3 µT
a["fy7-1-L2-04"] = math.tan(rad(60)) / math.tan(rad(10)) # B_m = B_h tan θ at 10 cm (60°) and 20 cm (10°): ratio 9,82
# Level 3: reasoning, two ideas or an unfamiliar context
a["fy7-1-L3-01"] = 25 - 14                               # magnet 25 µT south against B_h 14 µT north: 11 µT south, the needle turns round
# L3-02 (words): a steel paper clip stroked with a magnet stays magnetised; heating above the Curie temperature or knocks disorder the domains
a["fy7-1-L3-03"] = 52 * math.cos(rad(74)) / (55 * math.cos(rad(82)))   # B_h Helsinki 14,3 µT : Longyearbyen 7,65 µT = 1,87
print(json.dumps(a))
