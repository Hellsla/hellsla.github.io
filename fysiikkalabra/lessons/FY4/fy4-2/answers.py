"""Every answer in exercises.json for fy4-2, computed from the task data (python -I answers.py).
Uniformly accelerated motion on a line: a = Δv/Δt, v = v₀ + a t, x = x₀ + v₀ t + ½ a t²; free fall a = g = 9,81 m/s².
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}
# Level 1: one formula, values given
a["fy4-2-L1-01"] = (25 - 0) / 8.0                     # car: a = Δv / Δt = 25 m/s / 8,0 s = 3,1 m/s²
a["fy4-2-L1-02"] = 6.0 + (-1.5) * 3.0                 # cyclist braking: v = v₀ + a t = 6,0 − 4,5 = 1,5 m/s
a["fy4-2-L1-03"] = 0.5 * g * 1.50 ** 2                # stone from rest: s = ½ g t² = 11,0 m
a["fy4-2-L1-04"] = (7.0 - 2.0) / (5.0 - 0)            # (t,v) line (0 s; 2,0 m/s) -> (5,0 s; 7,0 m/s): slope a = 1,0 m/s²
a["fy4-2-L1-05"] = 0.5 * 0.40 * 30 ** 2               # train from rest: Δx = ½ a t² = 180 m
# Level 2: conversion, rearrangement or two steps
v0 = 72 * 1000 / 3600                                 # 72 km/h = 72 · 1000 m : 3600 s = 20 m/s
acc = (0 - v0) / 4.0                                  # braking: a = −5,0 m/s²
a["fy4-2-L2-01"] = v0 * 4.0 + 0.5 * acc * 4.0 ** 2    # Δx = v₀ t + ½ a t² = 80 m − 40 m = 40 m
a["fy4-2-L2-02"] = (16 - 0) / (6.0 - 2.0)             # tangent of x = ½ · 1,0 · t² at t = 4 s through (2 s; 0) and (6 s; 16 m): 4,0 m/s
assert abs(a["fy4-2-L2-02"] - 1.0 * 4.0) < 1e-12      # the tangent's slope is v = a t = 4,0 m/s
t_top = 15.0 / g                                      # ball thrown up at 15,0 m/s: v = v₀ − g t = 0 at the top
a["fy4-2-L2-03"] = 15.0 * t_top - 0.5 * g * t_top ** 2   # h = v₀ t − ½ g t² = 11,5 m
a["fy4-2-L2-04"] = 2 * 1.60 / 1.41 ** 2               # Moon: h = ½ g t² -> g = 2h / t² = 1,61 m/s²
# Level 3: reasoning and combining ideas
# balcony: up positive, origin at the hand 6,00 m above the ground: −6,00 = 8,00 t − ½ g t²  ->  ½ g t² − 8,00 t − 6,00 = 0
a["fy4-2-L3-01"] = (8.00 + math.sqrt(8.00 ** 2 + 4 * 0.5 * g * 6.00)) / (2 * 0.5 * g)   # positive root 2,19 s
# metro: (t,v) area = ½ · 15,0 · 20,0 + 15,0 · 60,0 + ½ · 15,0 · 15,0
a["fy4-2-L3-02"] = 0.5 * 15.0 * 20.0 + 15.0 * 60.0 + 0.5 * 15.0 * 15.0   # 1162,5 m -> 1,16 km
# fitted y = −4,86 t² + 3,10 t + 1,20 (up positive): v = 3,10 − 2 · 4,86 t
a["fy4-2-L3-03"] = 3.10 - 2 * 4.86 * 0.50             # −1,76 m/s (moving down)
print(json.dumps(a))
