"""Every answer in exercises.json and inquiry.json for fy4-1, computed from the task data (python -I answers.py).
Velocity v = Δx / Δt with Δx = x₂ − x₁, position in uniform motion x = x₀ + v t. Positive direction = +x axis.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy4-1-L1-01"] = 120 / 15                          # runner: v = Δx / Δt = 120 m / 15 s = 8,0 m/s
a["fy4-1-L1-02"] = -5.0 - 12                         # displacement: Δx = x₂ − x₁ = −5,0 m − 12 m = −17 m
a["fy4-1-L1-03"] = 3.5 * 12                          # cart: Δx = v Δt = 3,5 m/s · 12 s = 42 m
a["fy4-1-L1-04"] = (24 - 4.0) / (10 - 0)             # slope of the (t,x) line: v = (24 m − 4,0 m) / (10 s − 0 s) = 2,0 m/s
a["fy4-1-L1-05"] = 15 + 1.5 * 20                     # x = x₀ + v t = 15 m + 1,5 m/s · 20 s = 45 m
# Level 2: conversion, rearrangement or two steps
v_auto = 90 / 3.6                                    # 90 km/h = 25 m/s
a["fy4-1-L2-01"] = v_auto * 12                       # car: Δx = v Δt = 25 m/s · 12 s = 300 m
a["fy4-1-L2-02"] = 1200 / 4.0 / 60                   # walk: Δt = Δx / v = 1200 m / 4,0 m/s = 300 s = 5,0 min
a["fy4-1-L2-03"] = (3.0 - 18) / (7.0 - 2.0)          # cart: v = (3,0 m − 18 m) / (7,0 s − 2,0 s) = −3,0 m/s
a["fy4-1-L2-04"] = (0 - (-24)) / 1.5                 # from x = x₀ + v t = 0: t = −x₀ / v = 24 m / 1,5 m/s = 16 s
# Level 3: reasoning and combining ideas
s_kokonais = 6.0e3 + 6.0e3                           # cyclist: path s = 6000 m + 6000 m = 12 000 m
t_kokonais = (20 + 30) * 60                          # 20 min + 30 min = 3000 s
a["fy4-1-L3-01"] = s_kokonais / t_kokonais           # mean speed = s / Δt = 12 000 m / 3000 s = 4,0 m/s (mean velocity is 0)
t_kohtaus = 90 / (1.5 + 1.2)                         # x_A = 1,5 t, x_E = 90 − 1,2 t; equal when t = 90 / 2,7 = 33,3 s
a["fy4-1-L3-02"] = 1.5 * t_kohtaus                   # meeting place x = 1,5 m/s · 33,3 s = 50 m
a["fy4-1-L3-03"] = (10 - 0) / 40                     # whole 40 s: v_ka = Δx / Δt = (10 m − 0 m) / 40 s = 0,25 m/s

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
