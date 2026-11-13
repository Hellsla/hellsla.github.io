"""Every answer in exercises.json for fy1-2, computed from the task data (python -I answers.py).
Unit conversions with prefixes, powers of ten, AU and light-time; t = s/c is the given formula of the lesson (uniform motion of light).
Constants as the lesson gives them: 1 AU = 1,496e8 km, c = 2,998e5 km/s, 1 a = 3,156e7 s, Moon diameter 3474 km.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

AU, C, YEAR, MOON = 1.496e8, 2.998e5, 3.156e7, 3474     # km per AU, km/s, s per year, km
a = {}
# Level 1: one conversion or one formula
a["fy1-2-L1-01"] = 82 / 1000                            # 82 um = 82 · 10^-6 m = 82 · 10^-3 mm = 0,082 mm
a["fy1-2-L1-02"] = 384400 / 1000                        # 1 Mm = 10^6 m = 10^3 km -> 384 400 km / 1000 = 384,4 Mm
a["fy1-2-L1-03"] = 1.85 * 0.92                          # A = l w = 1,702 m^2 -> 1,7 m^2 (two significant figures, from 0,92 m)
a["fy1-2-L1-04"] = (13.6 - 2.0) * 10                       # figure fy1-2/ruler-read: ends at 2,0 cm and 13,6 cm -> 11,6 cm · 10 mm/cm = 116 mm
a["fy1-2-L1-05"] = 1.392e6 / MOON                       # 1,392e6 km / 3474 km per px = 400,69 px
# Level 2: two steps, a conversion plus a formula
a["fy1-2-L2-01"] = 3.2e9 * 5.0e-3                   # 3,2 GHz = 3,2e9 1/s, 5,0 ms = 5,0e-3 s: N = f t = 1,6e7
a["fy1-2-L2-02"] = 1.0e-3 / 2.0e-6                      # 1,0 mm = 1,0e-3 m, 2,0 um = 2,0e-6 m: 500
a["fy1-2-L2-03"] = 2.4 * 1e6 / 1e4                      # 1 km^2 = (1000 m)^2 = 1e6 m^2 -> 2,4e6 m^2; /1e4 m^2 per ha = 240 ha
a["fy1-2-L2-04"] = 15.341 * 86400 / 1e6                 # 15,341 km/s · 86 400 s = 1 325 462 km = 1,3255 milj. km
# Level 3: reasoning, several conversions
a["fy1-2-L3-01"] = C * YEAR / AU                        # 1 ly = 2,998e5 · 3,156e7 km = 9,461e12 km; / 1,496e8 km/AU = 63 247 AU -> 63 250
a["fy1-2-L3-02"] = 30.07 * AU / MOON / 1920             # 30,07 AU = 4,498e9 km = 1,295e6 px; / 1920 px (exact) = 674,4 (four figures)
a["fy1-2-L3-03"] = 2 * 145 * AU / C / 3600              # one way 145 AU = 2,169e10 km, 72 356 s; there and back twice: 144 713 s = 40,2 h
# Exercise bank additions (teacher 2026-11-04): L1-06 and L1-08 are multiple choice (no number)
a["fy1-2-L1-07"] = 18 * 1000 / 3600                     # 18 km/h = 18 · 1000 m / 3600 s = 5,0 m/s
KN = 1.852                                              # km/h per knot (exact)
speeds = {"pikalaiva": 38.0 * KN / 3.6, "juna": 66.0 / 3.6, "pyoraili": 9.0, "vene": 12.0 * KN / 3.6}   # table of L2-05 in m/s: 19,55; 18,33; 9,0; 6,17
a["fy1-2-L2-05"] = round(max(speeds.values()), 1)       # fastest = the 38,0 knot ship: 19,549 -> 19,5 m/s (three figures)
apples = [152.4, 147.9, 160.8, 155.3, 158.1]            # data of L2-06 in grams (the head wrongly says kg)
a["fy1-2-L2-06"] = round(sum(apples) / len(apples) / 1000, 4)   # mean 154,9 g = 154,9 · 10^-3 kg = 0,1549 kg
a["fy1-2-L2-07"] = 12 / 0.20 / 60                       # t = V/q = 12 l / 0,20 l/s = 60 s = 1,0 min (pupil's t = qV has the unit l²/s)
# L3-04: [T] = s = m^a (m/s²)^b kg^c -> c = 0, -2b = 1, a + b = 0 -> T = k sqrt(L/g), so T ∝ sqrt(L)
a["fy1-2-L3-04"] = round(1.00 * (1.00 / 0.250) ** 0.5, 2)   # 1,00 s · sqrt(1,00/0,250) = 2,00 s
tA = 0.65 * 1000 * 3600 / 85.0                          # A: 0,65 kWh = 0,65 · 1000 W · 3600 s = 2,34e6 J; / 85,0 W = 27 529 s = 7,647 h
tB = 2.20e6 / (0.100 * 1000)                            # B: 2,20 MJ = 2,20e6 J; 0,100 kW = 100 W: 22 000 s = 6,111 h
a["fy1-2-L3-05"] = round((tA - tB) / 3600, 1)           # A lasts 1,536 h longer -> 1,5 h (two figures from 0,65 kWh; tolerance 0,03: 1,455…1,545)
# Worked example (not in exercises.json): Neptune 30,1 AU
s_nep = 30.1 * AU                                       # 4,503e9 km
t_nep = s_nep / C                                       # 15 020 s = 4,17 h
# inquiry.json numeric tasks
siirto = 15.341 * YEAR / AU                             # Voyager 2: 15,341 km/s · 3,156e7 s/a / 1,496e8 km/AU = 3,236 AU/a
# Voyager 2 model of the simulation (round 2, 2026-11-07): d = d0 + v (t - t0), d0 = 119,0 AU from the Sun on 2018-11-05
# (Burlaga et al. 2019), v = 15,341 km/s; exact constants 1 AU = 149 597 870,7 km, c = 299 792,458 km/s as in sim.js
import datetime as _dt
def voyager(y, m, d, d0=119.0, v=15.341, au=149597870.7, c=299792.458):
    km = d0 * au + v * (_dt.date(y, m, d) - _dt.date(2018, 11, 5)).days * 86400
    return km / au, km, km / c / 3600                 # AU, km, light time from the Sun in h
voy_table = {y: voyager(y, 11, 5) for y in (2018, 2022, 2026, 2030)}   # 119,0 / 131,9 / 144,9 / 157,8 AU; 1,78 / 1,97 / 2,17 / 2,36 e10 km; 16,5 / 18,3 / 20,1 / 21,9 h
voy_2026 = voyager(2026, 1, 1)                         # 142,2 AU, 19,7 h; 19,71 h / 8,317 min = 142 (the ratio in the inquiry)
voy_feb = (voyager(2026, 2, 1)[0], voyager(2026, 2, 28)[0])   # 142,4 … 142,7 AU from the Sun ~ 142,5; JPL Feb 2026: 143,05 AU from the Earth (|Earth - Sun| <= 1 AU)
tark2 = 0.387 * AU / C / 60                             # Mercury 0,387 AU: 5,790e7 km / 2,998e5 km/s = 193,1 s = 3,22 min
a["fy1-2-L1-10"] = round(384400e3 / 2.998e8, 2)            # MAFY table (Aurinkokunta): Moon mean distance 384 400 km = 3,844·10⁸ m; t = s / c = 1,282 s, given to three significant figures: 1,28 s
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
