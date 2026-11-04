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
# fitted y = −4,86 t² + 3,10 t + 1,20 (up positive): v = 3,10 − 2 · 4,86 t, t = 0,500 s
a["fy4-2-L3-03"] = 3.10 - 2 * 4.86 * 0.50             # −1,76 m/s (moving down)
# Level 1 additions: multiple choice and graph area
a["fy4-2-L1-06"] = "Länteen, koska nopeus pienenee ja kiihtyvyys osoittaa nopeuden muutoksen suuntaan."   # braking eastward: a points west
a["fy4-2-L1-07"] = (2.0 + 7.0) / 2 * 5.0              # trapezoid under the (t,v) line: mean speed 4,5 m/s · 5,0 s = 22,5 m
a["fy4-2-L1-08"] = "Kiven nopeus kasvaa koko ajan, joten matkaa ei saa laskea loppunopeudella vaan keskinopeudella."   # s = ½ v t, not v t
# Level 2 additions: data and reasoning
import numpy as np                                    # least-squares fits for the example data
t5 = np.array([0, .5, 1, 1.5, 2, 2.5, 3.0]); v5 = np.array([0.21, 0.66, 1.02, 1.50, 1.86, 2.35, 2.71])
a["fy4-2-L2-05"] = round(float(np.polyfit(t5, v5, 1)[0]), 2)   # slope of the (t,v) fit = 0,84 m/s²
t6 = np.array([0, .4, .8, 1.2, 1.6, 2.0]); x6 = np.array([0, .10, .37, .80, 1.46, 2.32])
a["fy4-2-L2-06"] = round(float(2 * np.polyfit(t6 ** 2, x6, 1)[0]), 2)   # x = ½ a t²: slope of (t²,x) is a/2 -> a = 1,15 m/s²
a["fy4-2-L2-07"] = "Videoanalyysilla, koska nopeus saadaan monelta hetkeltä ja nähdään, onko $(t,v)$-kuvaaja suora."   # many points show linearity
# Level 3 additions
vv = [k / 3.6 for k in (0, 36, 62, 83, 100)]          # km/h -> m/s
a["fy4-2-L3-04"] = round(sum((vv[i] + vv[i + 1]) / 2 * 2.0 for i in range(4)), 1)   # trapezoids, 2,0 s each: 128,3 m
t7 = np.array([0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4]); v7 = np.array([2.41, 2.02, 1.62, 1.19, .82, .38, -.01, -.41, -.83])
k7, b7 = np.polyfit(t7, v7, 1)                         # a = -0,81 m/s², v₀ = 2,42 m/s
a["fy4-2-L3-05"] = round(float(b7 ** 2 / (2 * -k7)), 2)   # turning point v = 0: s = v₀² / (2|a|) = 3,61 m
print(json.dumps(a))
