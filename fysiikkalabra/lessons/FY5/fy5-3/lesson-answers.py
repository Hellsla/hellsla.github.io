"""Numbers of the lesson text and inquiry.json for fy5-3, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model as the simulation (assets/sims/fy5/fy5-3/sim.js): v = 2πr/T, f = 1/T.
Prints {id: number} as JSON on the last line."""
import json, math

pi = math.pi
a = {}
# Kaava text
a["text-f-T050"] = 1 / 0.50                              # T = 0,50 s -> f = 2,0 1/s
a["text-f-45min"] = 45 / 60                              # 45 1/min = 45 / 60 s = 0,75 1/s
# Esimerkki: washing machine drum, d = 46 cm, 1200 1/min
f_ex = 1200 / 60                                         # 20 1/s
a["ex-v"] = pi * 0.46 * f_ex                             # v = π d f = 28,90 m/s -> 29 m/s
a["ex-T"] = 1 / f_ex                                     # 0,050 s
a["ex-circ"] = pi * 0.46                                 # kehä 1,445 m
a["ex-kmh"] = 29 * 3.6                                   # 104 km/h
# Simulation model values used in predictions and conclusions (T = 4,0 s)
a["sim-v-r1"] = 2 * pi * 1.0 / 4.0                       # 1,571 m/s
a["sim-v-r2"] = 2 * pi * 2.0 / 4.0                       # 3,142 m/s
a["sim-v-r3"] = 2 * pi * 3.0 / 4.0                       # 4,712 m/s
a["sim-ratio"] = a["sim-v-r2"] / a["sim-v-r1"]           # 2,0
a["sim-dv-factor"] = 2 * math.sin(pi / 12)               # |Δv̄| / v over a twelfth of a lap = 0,5176
a["sim-dv-r2"] = a["sim-dv-factor"] * a["sim-v-r2"]      # 1,626 m/s
a["sim-alpha"] = 90.0                                    # the path after the release ⟂ the string
a["sim-T-r2-T2"] = 2 * pi * 2.0 / 2.0                    # koe 3: T = 2 s -> 6,283 m/s
a["sim-T-r2-T8"] = 2 * pi * 2.0 / 8.0                    # koe 3: T = 8 s -> 1,571 m/s
# Etsi virhe: bicycle wheel d = 0,70 m, f = 3,0 1/s
a["virhe-wrong"] = 2 * pi * 0.70 * 3.0                   # 13,19 m/s (diameter used as radius)
a["virhe-right"] = 2 * pi * 0.35 * 3.0                   # 6,597 m/s -> 6,6 m/s
a["virhe-26"] = 2 * a["virhe-wrong"]                     # 26,4 m/s
# Siirto: the Earth around the Sun, r = 1,50e11 m, T = 365 d
T_year = 365 * 24 * 3600                                 # 3,1536e7 s
a["siirto"] = 2 * pi * 1.50e11 / T_year / 1000           # 29,89 km/s -> 29,9 km/s
a["siirto-no2pi"] = 1.50e11 / T_year / 1000              # 4,757 km/s
a["siirto-hours"] = 2 * pi * 1.50e11 / (365 * 24) / 1000 # T in hours used as seconds: 1,076e5 km/s
a["siirto-ms"] = 2 * pi * 1.50e11 / T_year               # 29 887 (answered in m/s)
# Tarkistus 2: angle grinder, d = 125 mm, 11 000 1/min
f_gr = 11000 / 60                                        # 183,3 1/s
a["check2"] = pi * 0.125 * f_gr                          # v = π d f = 71,99 m/s -> 72,0 m/s
a["check2-diam"] = 2 * pi * 0.125 * f_gr                 # 144,0 m/s
a["check2-min"] = pi * 0.125 * 11000                     # 4320 (minutes not converted)
# Exit ticket
a["exit-f"] = 15 / 60                                    # 0,25 1/s
a["exit-T"] = 1 / a["exit-f"]                            # 4,0 s
a["exit-ratio"] = 9.0 / 3.0                              # 3,0
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
