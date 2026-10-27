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
a["fy1-2-L1-04"] = 15.341 * 1000                        # 15,341 km/s · 1000 m/km = 15 341 m/s
a["fy1-2-L1-05"] = 1.392e6 / MOON                       # 1,392e6 km / 3474 km per px = 400,69 px
# Level 2: two steps, a conversion plus a formula
a["fy1-2-L2-01"] = 5.20 * AU / C / 60                   # s = 5,20 · 1,496e8 km = 7,779e8 km; t = s/c = 2594,9 s; /60 = 43,25 min
a["fy1-2-L2-02"] = 1.0e-3 / 2.0e-6                      # 1,0 mm = 1,0e-3 m, 2,0 um = 2,0e-6 m: 500
a["fy1-2-L2-03"] = 2.4 * 1e6 / 1e4                      # 1 km^2 = (1000 m)^2 = 1e6 m^2 -> 2,4e6 m^2; /1e4 m^2 per ha = 240 ha
a["fy1-2-L2-04"] = 15.341 * 86400 / 1e6                 # 15,341 km/s · 86 400 s = 1 325 462 km = 1,325 milj. km
# Level 3: reasoning, several conversions
a["fy1-2-L3-01"] = C * YEAR / AU                        # 1 ly = 2,998e5 · 3,156e7 km = 9,461e12 km; / 1,496e8 km/AU = 63 247 AU -> 63 250
a["fy1-2-L3-02"] = 30.07 * AU / MOON / 1920             # 30,07 AU = 4,498e9 km = 1,295e6 px; / 1920 px = 674,4
a["fy1-2-L3-03"] = 2 * 145 * AU / C / 3600              # one way 145 AU = 2,169e10 km, 72 356 s; there and back twice: 144 713 s = 40,2 h
# Worked example (not in exercises.json): Neptune 30,1 AU
s_nep = 30.1 * AU                                       # 4,503e9 km
t_nep = s_nep / C                                       # 15 020 s = 4,17 h
# inquiry.json numeric tasks
siirto = 15.341 * YEAR / AU                             # Voyager 2: 15,341 km/s · 3,156e7 s/a / 1,496e8 km/AU = 3,236 AU/a
tark2 = 0.387 * AU / C / 60                             # Mercury 0,387 AU: 5,790e7 km / 2,998e5 km/s = 193,1 s = 3,22 min
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
