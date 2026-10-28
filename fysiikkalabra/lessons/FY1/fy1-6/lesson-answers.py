"""Numbers of the lesson text and inquiry.json for fy1-6, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
import json

g = 9.81                                             # m/s², putoamiskiihtyvyys Maassa
a = {}
# Inquiry tasks (inquiry.json), not exercises
a["inq-exp1"] = (g * 3.0 - g * 1.0) / (3.0 - 1.0)    # experiment 1, rows t = 1,0 s and 3,0 s: Δv/Δt = (29,43 − 9,81) / 2,0 = 9,81 m/s²
slope_fit = (4.9 - 0) / (0.50 - 0)                   # fitted line through the origin and (0,50 s; 4,9 m/s): slope 9,8 m/s²
a["inq-data"] = slope_fit
a["inq-siirto"] = 7.4 / 2.0 * 3.0                    # unknown planet: g = 7,4 / 2,0 = 3,7 m/s²; v(3,0 s) = 3,7 · 3,0 = 11,1 m/s -> 11 m/s
a["inq-check2"] = (108 / 3.6) / g                    # 108 km/h = 30,0 m/s; t = v / g = 30,0 / 9,81 = 3,058 s -> 3,06 s
a["inq-example"] = g * 1.5                           # worked example: v = g t = 9,81 · 1,5 = 14,715 m/s -> 15 m/s
a["inq-example-kmh"] = g * 1.5 * 3.6                 # 14,715 m/s · 3,6 = 52,97 km/h -> 53 km/h
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
