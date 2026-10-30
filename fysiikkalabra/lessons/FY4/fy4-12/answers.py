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
print(json.dumps(a))
