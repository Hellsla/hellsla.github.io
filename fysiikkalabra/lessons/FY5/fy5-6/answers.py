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
# Exercise bank additions (teacher 2026-11-04): L1-06 is multiple choice (no number)
a["fy5-6-L1-07"] = math.sqrt(gam * 1.90e27 / 4.22e8) / 1e3         # Io, M_Jupiter = 1,90·10²⁷ kg, r = 4,22·10⁸ m: v = sqrt(γM/r) = 17 335 m/s -> 17,3 km/s
a["fy5-6-L1-08"] = 2 * math.pi * 1.496e11 / (365.25 * 86400) / 1e3   # Earth round the Sun: v = 2πr/T = 29 786 m/s -> 29,79 km/s
moons = [(4.217e8, 1.769), (6.711e8, 3.551), (1.070e9, 7.155), (1.883e9, 16.69)]   # table of L2-05: r (m), T (d)
k = sum(r ** 3 / (T * 86400) ** 2 for r, T in moons) / 4           # mean of r³/T² = 3,2094·10¹⁵ m³/s²
a["fy5-6-L2-05"] = 4 * math.pi ** 2 * k / gam / 1e27               # M = 4π²/γ · r³/T² = 1,898·10²⁷ kg -> 1,90·10²⁷ kg
a["fy5-6-L2-06"] = math.sqrt(gam * M_E / (R_E + 1200e3)) / 1e3     # table of L2-06: row B (h = 1200 km) should be 7,254 km/s -> 7,25 km/s (listed 7,52)
a["fy5-6-L2-07"] = math.sqrt(gam * M_E / (R_E + 800e3)) / 1e3      # mass cancels: h = 800 km, r = 7171 km, v = 7454 m/s -> 7,45 km/s
planets = [(6.0e9, 3.29), (10.5e9, 7.57), (27.0e9, 31.4)]          # table of L3-04 without planet d (T halved): r (m), T (d)
k3 = sum(r ** 3 / (T * 86400) ** 2 for r, T in planets) / 3        # mean r³/T² = 2,685·10¹⁸ m³/s²
a["fy5-6-L3-04"] = 4 * math.pi ** 2 * k3 / gam / 1e30              # M = 4π²/γ · r³/T² = 1,588·10³⁰ kg -> 1,59·10³⁰ kg
gm = gam * M_E
TA = 2 * math.pi * math.sqrt((R_E + 400e3) ** 3 / gm)              # satellite A at 400 km: 5546,0 s
TB = 2 * math.pi * math.sqrt((R_E + 1000e3) ** 3 / gm)             # satellite B at 1000 km: 6299,3 s
a["fy5-6-L3-05"] = TA * TB / (TB - TA) / 3600                      # t/T_A − t/T_B = 1: t = 46 379 s = 12,88 h -> 12,9 h
# Added batch (teacher 2026-11-12): figure tasks and a MAFY table task
M_sun = 1.99e30                                                    # mass of the Sun, kg
a["fy5-6-L1-10"] = gam * M_sun / (0.5 * (147.1e9 + 152.1e9)) ** 2 * 1e3   # figure: r = 1,496·10¹¹ m: a = γM/r² = 5,934e-3 m/s² -> 5,93 mm/s²
a["fy5-6-L1-11"] = 2 * math.pi * (6.052e6 + 0.500e6) / math.sqrt(gam * 4.867e24 / (6.052e6 + 0.500e6)) / 60   # MAFY: Venus M = 4,867·10²⁴ kg, R = 6052 km, h = 500 km: r = 6552 km, v = 7041 m/s, T = 5847 s -> 97,4 min
a["fy5-6-L2-08"] = round(math.sqrt(5250 / 88), 1)                           # figure: Halley r_min = 88, r_max = 5250 milj. km: v1/v2 = sqrt(r2/r1) = 7,724 -> 7,7 (88 milj. km has two sig. figs; unrounded 7,724)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
