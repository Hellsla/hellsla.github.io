"""Every answer in exercises.json for fy4-12, computed from the task data (python -I answers.py).
Positions in one coordinate system with a common clock: x = x0 + v0 t + a t²/2. Two bodies meet when x_A = x_B.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

a = {}
# Level 1: one formula, values given
a["fy4-12-L1-01"] = (24 - 4.0) / (2.0 + 3.0)         # x_A = 4,0 m + 2,0 m/s t, x_B = 24 m − 3,0 m/s t: t = 20 m / 5,0 m/s = 4,0 s
a["fy4-12-L1-02"] = 60 / (8.0 - 5.0)                 # cyclist 8,0 m/s from 0, runner 5,0 m/s from 60 m: 8,0 t = 60 + 5,0 t, t = 20 s
a["fy4-12-L1-03"] = 0.5 * 3.0 * 4.0 ** 2             # x = a t²/2 = 0,5 · 3,0 m/s² · (4,0 s)² = 24 m
a["fy4-12-L1-04"] = 40 / (6.0 + 2.0)                 # graph: A from 0 to 60 m in 10 s (6,0 m/s), B from 40 m to 20 m (−2,0 m/s): meet at t = 5,0 s
a["fy4-12-L1-05"] = 3.5 * (60 / (3.5 + 2.5))        # A 3,5 m/s from 0, B −2,5 m/s from 60 m: t = 60 / 6,0 = 10 s, x = 3,5 · 10 = 35 m
# Level 2: conversion, rearrangement or two steps
a["fy4-12-L2-01"] = 150 / (90 / 3.6 - 72 / 3.6)      # 90 km/h = 25 m/s, 72 km/h = 20 m/s: t = 150 m / 5,0 m/s = 30 s
a["fy4-12-L2-02"] = 12 / (90 + 54) * 60              # trains: t = 12 km / 144 km/h = 0,0833 h = 5,0 min
a["fy4-12-L2-03"] = (42 - 6.0) / (3.0 + 1.0)         # A 6,0 m + 3,0 m/s t, B 42 m − 1,0 m/s t: t = 36 m / 4,0 m/s = 9,0 s
a["fy4-12-L2-04"] = (40 - 10) / (6.0 + 2.0)          # gap 40 m − 8,0 m/s t = 10 m: t = 30 m / 8,0 m/s = 3,75 s
# Level 3: reasoning and combining ideas
a["fy4-12-L3-01"] = 5 - math.sqrt(25 - 16)           # runner x = −8,0 m + 5,0 m/s t, bus x = 0,5 · 1,0 m/s² t²: t² − 10 t + 16 = 0, smaller root 5 − 3 = 2,0 s
a["fy4-12-L3-02"] = 20 + 0.5 * 0.5 * 8.0 ** 2 - 4.0 * 8.0   # bus 0,5 · 0,50 · t² ahead by 20 m; speeds equal at t = v / a = 8,0 s; gap 20 + 16 − 32 = 4,0 m
a["fy4-12-L3-03"] = (-8.0 + math.sqrt(8.0 ** 2 + 2 * 2.0 * 180)) / 2.0   # a t²/2 + v t = D: t² + 8,0 t − 180 = 0, t = (−8 + √(64 + 720)) / 2 = 10 s
# Exercise bank additions (teacher 2026-11-04): L1-06 and L1-08 are multiple choice (no number)
a["fy4-12-L1-07"] = 7.0 * 3.0 / (7.0 - 4.0)          # A 4,0 m/s from t = 0, B 7,0 m/s from t = 3,0 s: 4,0 t = 7,0 (t − 3,0), t = 21 m / 3,0 m/s = 7,0 s
a["fy4-12-L2-05"] = (45.0 - 3.0) / ((20.4 - 3.0) / 5.0 - (32.4 - 45.0) / 5.0)   # table ends: v_A = 3,48 m/s, v_B = −2,52 m/s: t = 42,0 m / 6,00 m/s = 7,0 s
a["fy4-12-L2-06"] = (4.0 + math.sqrt(4.0 ** 2 + 2 * 2.0 * 12)) / 2.0   # error task: a t²/2 = 12 + 4,0 t, t = (4,0 + √64) / 2,0 = 6,0 s (not v = a t: 2,0 s)
a["fy4-12-L2-07"] = 0.5 * (12.0 / 2.0) * 12.0        # table: v_B = 2,0 m/s² t, equal speeds 12,0 m/s at t = 6,0 s; gap = triangle ½ · 6,0 s · 12,0 m/s = 36 m
# Level 3 additions
v_kk = 20.0; s_rel = 10 + 12 + 5.0; a_h = 1.5
t_o = math.sqrt(2 * s_rel / a_h)                      # overtaking: ½ a t² = 10 + 12 + 5,0 = 27 m, t = 6,0 s
a["fy4-12-L3-04"] = v_kk * t_o + 0.5 * a_h * t_o ** 2 + 20.0 * t_o   # car 120 + 27 = 147 m, oncoming 20 m/s · 6,0 s = 120 m: d_min = 267 m (final speed 29 m/s = 104 km/h > 80 km/h)
v_p = 6.0; td = 1.5; a_a = 2.0                        # cyclist 23,9 m / 4,0 s = 5,975 ≈ 6,0 m/s; car starts 1,5 s later
tau = (v_p + math.sqrt(v_p ** 2 + 2 * a_a * v_p * td)) / a_a   # a τ²/2 = v (τ + 1,5): τ = (6,0 + √72) / 2,0 = 7,24 s
a["fy4-12-L3-05"] = v_p * (tau + td)                  # x = 6,0 m/s · 8,74 s = 52,5 m -> 52 m (car 14,5 m/s = 52 km/h > 40 km/h)
print(json.dumps(a))
