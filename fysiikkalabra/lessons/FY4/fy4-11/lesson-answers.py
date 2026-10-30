"""Numbers of the lesson text and inquiry.json for fy4-11, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Model: reaction time t_r at constant speed, then constant deceleration a until the
car stops (level road, air resistance neglected); a = 9,0 m/s² on a dry road and t_r = 1,0 s are the assumptions of
Liikenneturva's collision-speed calculator (extrat.liikenneturva.fi/tormaysnopeus). Collision: impulse principle,
mean force F_ka = m Δv / Δt. g = 9,81 m/s². Prints {id: value} as JSON."""
import json, math

g = 9.81
a = {}
kmh = lambda v: v / 3.6                                   # km/h to m/s
def stop(v_kmh, tr, dec):                                 # reaction distance, braking distance, stopping distance, stopping time
    v = kmh(v_kmh); sr = v * tr; sj = v * v / (2 * dec)
    return sr, sj, sr + sj, tr + v / dec
def impact(v_kmh, tr, dec, d):                            # speed (km/h) at an obstacle d metres ahead, 0 if the car stops before it
    v = kmh(v_kmh); sr = v * tr
    if d <= sr: return v_kmh                              # hit before braking starts
    v2 = v * v - 2 * dec * (d - sr)
    return 0.0 if v2 <= 0 else math.sqrt(v2) * 3.6

# Ydinajatus figure "pysahtyminen" and the Miksi question: 50 and 100 km/h, t_r = 1,0 s, a = 9,0 m/s²
for v in (50, 100):
    sr, sj, sp, tp = stop(v, 1.0, 9.0)
    a[f"sr-{v}"] = sr                                     # 13,9 m / 27,8 m
    a[f"sj-{v}"] = sj                                     # 10,7 m / 42,9 m
    a[f"sp-{v}"] = sp                                     # 24,6 m / 70,7 m
    a[f"tp-{v}"] = tp                                     # 2,54 s / 4,09 s
a["sp-ratio"] = a["sp-100"] / a["sp-50"]                  # 2,87: "lähes kolminkertainen"
a["sj-ratio"] = a["sj-100"] / a["sj-50"]                  # 4,00
# Kaava: braking deceleration from friction a = μ g, μ = 0,92 gives 9,0 m/s²
a["mu-dry"] = 9.0 / g                                     # 0,917
# Kaava figure "jarrutus" (force diagram): m = 1200 kg, a = 9,0 m/s² backwards
a["fbd-G"] = 1200 * g                                     # 11 772 N
a["fbd-Fmu"] = 1200 * 9.0                                 # 10 800 N
# Simulation runs (model values): obstacle 25 m, dry, t_r 1,0 s
for v in (30, 40, 50, 60, 80):
    a[f"imp25-{v}"] = impact(v, 1.0, 9.0, 25.0)           # 0 / 0 / 0 / 41,8 / 75,8 km/h
for v in (80, 100):
    a[f"imp50-{v}"] = impact(v, 1.0, 9.0, 50.0)           # 0 / 69,4 km/h
for v in (30, 40, 60, 80, 120):
    sr, sj, sp, tp = stop(v, 1.0, 9.0)
    a[f"sr-{v}"] = sr; a[f"sj-{v}"] = sj; a[f"sp-{v}"] = sp
# Road conditions at 80 km/h, t_r = 1,0 s (sim's example decelerations 9,0; 6,0; 3,0; 1,5 m/s²)
for name, dec in (("kuiva", 9.0), ("marka", 6.0), ("luminen", 3.0), ("jainen", 1.5)):
    a[f"sj-80-{name}"] = stop(80, 1.0, dec)[1]            # 27,4 / 41,2 / 82,3 / 164,6 m
# Worked example: 80 km/h, t_r = 2,0 s (looking at a phone), a = 9,0 m/s²
v = kmh(80)
a["ex-v"] = v                                             # 22,22 m/s
a["ex-sr"] = v * 2.0                                      # 44,44 m
a["ex-sj"] = v * v / (2 * 9.0)                            # 27,43 m
a["ex-sp"] = a["ex-sr"] + a["ex-sj"]                      # 71,9 m
a["ex-sp-1s"] = v * 1.0 + a["ex-sj"]                      # 49,7 m with t_r = 1,0 s
# Collision table (example data): 75 kg occupant, 50 km/h to 0
m, dv = 75.0, kmh(50)
a["dp"] = m * dv                                          # 1041,7 kg·m/s
a["F-belt"] = m * dv / 0.10                               # 10 417 N
a["F-nobelt"] = m * dv / 0.010                            # 104 167 N
a["F-ratio"] = a["F-nobelt"] / a["F-belt"]                # 10
a["G-75"] = m * g                                         # 735,75 N: F-belt is about 14 G
a["F-belt-per-G"] = a["F-belt"] / a["G-75"]               # 14,2
# Statistics (OTI-Turvavyöraportti 2023, crashes 2017–2021): 278 belted and 198 unbelted car and van occupants killed
a["killed"] = 278 + 198                                   # 476
a["unbelted-share"] = 198 / 476 * 100                     # 41,6 %
# Transfer task: moose 45 m ahead, 80 km/h, wet road a = 6,0 m/s², t_r = 1,0 s
a["siirto"] = impact(80, 1.0, 6.0, 45.0)                  # 53,5 km/h
a["siirto-sr"] = kmh(80) * 1.0                            # 22,2 m
a["siirto-v2"] = kmh(80) ** 2 - 2 * 6.0 * (45.0 - kmh(80))  # 220,5 m²/s²
a["siirto-nobrake-sp"] = stop(80, 1.0, 6.0)[2]            # 63,4 m > 45 m
# Error-spotting task: braking distance with km/h left unconverted: 50²/(2·9,0) = 138,9 "m"
a["virhe-wrong"] = 50 ** 2 / (2 * 9.0)                    # 138,9
a["virhe-right"] = kmh(50) ** 2 / (2 * 9.0)               # 10,7 m
# Check 2: snowy road, 60 km/h, t_r = 1,0 s, a = 3,0 m/s²
sr, sj, sp, tp = stop(60, 1.0, 3.0)
a["check2-sr"] = sr; a["check2-sj"] = sj; a["check2"] = sp   # 16,67 + 46,30 = 62,96 m
# Check 1: 50 → 70 km/h, braking distance ratio (70/50)² = 1,96
a["check1-ratio"] = (70 / 50) ** 2
# Exit ticket: 72 km/h, looking at a phone 2,0 s: distance driven blind
a["exit-phone"] = kmh(72) * 2.0                           # 40 m
print(json.dumps(a))
