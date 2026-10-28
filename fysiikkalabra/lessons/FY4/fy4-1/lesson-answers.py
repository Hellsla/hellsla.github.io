"""Numbers of the lesson text and inquiry.json for fy4-1, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
import json

a = {}
# Inquiry numbers (inquiry.json), not exercises
a["inq-exp1-vB"] = (40 - 0) / (10 - 0)               # tapaus 1, cart B: 4,0 m/s
a["inq-exp3-vD"] = (0 - 30) / (10 - 0)               # tapaus 3, cart D: −3,0 m/s
t_d = [0, 2, 4, 6, 8, 10]; x_d = [4.2, 6.8, 10.2, 13.3, 15.8, 19.1]       # measured positions (m) at times (s)
mt = sum(t_d) / len(t_d); mx = sum(x_d) / len(x_d)
a["inq-data-slope"] = sum((p - mt) * (q - mx) for p, q in zip(t_d, x_d)) / sum((p - mt) ** 2 for p in t_d)   # least squares, 1,49 m/s
a["inq-data-endpoint"] = x_d[-1] / t_d[-1]           # mistake: x(10 s) / 10 s = 1,91 (line does not pass the origin)
a["inq-data-neighbours"] = (x_d[1] - x_d[0]) / (t_d[1] - t_d[0])           # mistake: two neighbouring points = 1,3
v_pulkka = (24 - 4.0) / (7.0 - 3.0)                  # sledge: v = (24 m − 4,0 m) / (7,0 s − 3,0 s) = 5,0 m/s
a["inq-siirto"] = 24 + v_pulkka * (10 - 7.0)         # x(10 s) = x₂ + v (10 s − 7,0 s) = 24 m + 15 m = 39 m
a["inq-siirto-v0"] = v_pulkka * 10                   # mistake: x = v t = 50 m
a["inq-siirto-t10"] = 24 + v_pulkka * 10             # mistake: x₂ + v · 10 s = 74 m
a["inq-check2"] = -12 + 2.5 * 10                     # x = x₀ + v t = −12 m + 2,5 m/s · 10 s = 13 m
a["inq-example-v"] = (120 - 20) / (40 - 0)           # example: v = 100 m / 40 s = 2,5 m/s
a["inq-example-x60"] = 20 + a["inq-example-v"] * 60  # x(60 s) = 20 m + 2,5 m/s · 60 s = 170 m
a["inq-roundtrip-path"] = 2 * 4 * 2                  # tapaus 4, cart E: 4 s at 2 m/s out and 4 s back = 16 m, Δx = 0

print(json.dumps(a))
