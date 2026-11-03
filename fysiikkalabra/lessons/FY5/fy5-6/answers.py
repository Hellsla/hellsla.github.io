"""Every answer in exercises.json for fy5-6, computed from the task data (python -I answers.py).
Circular orbit: gravity is the net force, γMm/r² = mv²/r, so v = sqrt(γM/r), T = 2πr/v and a_n = γM/r².
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

gam = 6.674e-11                    # gravitational constant γ, N·m²/kg²
M_E, R_E = 5.97e24, 6.371e6        # the Earth: mass (kg) and radius (m)
a = {}
# Level 1: one formula, values given
a["fy5-6-L1-01"] = math.sqrt(gam * M_E / 7.196e6) / 1e3           # NOAA-20, r = 7196 km: v = sqrt(γM/r) = 7441 m/s -> 7,44 km/s
a["fy5-6-L1-02"] = 2 * math.pi * 26.56e6 / 3.87e3 / 3600           # GPS, r = 26 560 km, v = 3,87 km/s: T = 2πr/v = 43 122 s = 11,98 h -> 12,0 h
a["fy5-6-L1-03"] = gam * M_E / 42.164e6 ** 2                       # geostationary, r = 42 164 km: a_n = γM/r² = 0,2241 m/s² -> 0,224 m/s²
a["fy5-6-L1-04"] = 2 * math.pi * 384.4e6 / (27.3 * 86400) / 1e3    # the Moon, r = 384 400 km, T = 27,3 d: v = 2πr/T = 1024 m/s -> 1,02 km/s
a["fy5-6-L1-05"] = math.sqrt(gam * 7.35e22 / 1.847e6) / 1e3        # orbiter round the Moon, M = 7,35·10²² kg, r = 1847 km: v = 1630 m/s -> 1,63 km/s
# Level 2: two steps, one conversion or one rearrangement
r = gam * M_E / 5.00e3 ** 2                                        # v = 5,00 km/s: r = γM/v² = 1,594·10⁷ m
a["fy5-6-L2-01"] = (r - R_E) / 1e3                                 # height h = r − R = 9566 km -> 9570 km
a["fy5-6-L2-02"] = math.sqrt(gam * 6.42e23 / (3.390e6 + 0.400e6)) / 1e3   # Mars, R = 3390 km, h = 400 km: r = 3790 km, v = 3362 m/s -> 3,36 km/s
a["fy5-6-L2-03"] = math.sqrt(1.62 * 1.737e6) / 1e3                 # low lunar orbit: γM/r² = g, so v = sqrt(g r) = sqrt(1,62 · 1 737 000) m/s = 1677 m/s -> 1,68 km/s
a["fy5-6-L2-04"] = gam * M_E * 75 / (R_E + 410e3) ** 2             # astronaut 75 kg at h = 410 km: r = 6781 km, F = γMm/r² = 649,9 N -> 650 N
# Level 3: reasoning or an unfamiliar context
T_mars = (24 * 60 + 37) * 60                                       # Mars turns once in 24 h 37 min = 88 620 s
r_mars = (gam * 6.42e23 * T_mars ** 2 / (4 * math.pi ** 2)) ** (1 / 3)   # areostationary: r³ = γM T²/(4π²), r = 2,043·10⁷ m
a["fy5-6-L3-01"] = (r_mars - 3.390e6) / 1e3                        # height above Mars h = r − R = 17 040 km -> 1,70·10⁴ km
dv = math.sqrt(gam * M_E / (R_E + 398e3)) - math.sqrt(gam * M_E / (R_E + 400e3))
a["fy5-6-L3-02"] = dv                                              # ISS sinks 400 -> 398 km: v grows by 1,13 m/s
a["fy5-6-L3-03"] = 2 * math.pi * math.sqrt(R_E ** 3 / (gam * M_E)) / 60   # weightless on the equator: v² / R = γM/R², T = 2π sqrt(R³/γM) = 5062 s = 84,4 min
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
