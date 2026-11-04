"""Every answer in exercises.json for fy1-3, computed from the task data (python -I answers.py).
Mean x̄ = (x1 + ... + xn) / n, half-range Δx = (x_max − x_min) / 2, error = result − true value, zero correction x = reading − zero reading.
The simulation's fixed series G is the same list as in assets/sims/fy1/fy1-3/sim.js: reading i = round(T + δ_sys + δ_sat · G[i], 0,01 s).
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json
import math

G = [-1.456, 0.349, 1.893, 1.797, -0.027, 0.952, 1.758, -0.424, 0.468, -0.802, -0.526, 1.699, 1.314, 0.066, 0.709, -1.129,
     -0.944, -0.639, 0.965, -1.381, -0.978, 0.13, 0.198, -0.042, 1.333, -0.149, -0.148, -1.166, -0.816, 0.345, 0.271, 0.053,
     -1.585, -1.344, 0.406, 0.146, -0.705, 0.644, -1.141, -0.113]
T = 2.40                                                           # the simulation's true rolling time (s), a model value


def sim(n, sat, sys):
    """The first n readings of the simulation (s) and their mean, as the page shows them."""
    r = [round((T + sys + sat * G[i]) * 100) / 100 for i in range(n)]
    return r, sum(r) / n


mean = lambda xs: sum(xs) / len(xs)
half = lambda xs: (max(xs) - min(xs)) / 2

a = {}
# Level 1: one formula, values given
a["fy1-3-L1-01"] = mean([0.52, 0.48, 0.55, 0.49])                  # mean = 2,04 s / 4 = 0,51 s
a["fy1-3-L1-02"] = 20.3 - 20.0                                     # error = result − true = 20,3 cm − 20,0 cm = +0,3 cm
a["fy1-3-L1-03"] = half([12.4, 12.9, 12.6, 12.2, 12.7])            # read off figure fy1-3/pendulum-dots: (12,9 s − 12,2 s) / 2 = 0,35 s
a["fy1-3-L1-04"] = 48.7 - 1.2                                      # zero correction: m = 48,7 g − 1,2 g = 47,5 g
a["fy1-3-L1-05"] = 1.0 / 2                                         # reading uncertainty estimated as half the smallest division = 1 mm / 2 = 0,5 mm
# Level 2: conversion, two steps or a rearrangement
t6 = [1.84, 1.91, 1.78, 1.88, 1.96, 1.82]
a["fy1-3-L2-01"] = half(t6) / mean(t6) * 100                       # relative error = Δt / mean = 0,09 s / 1,865 s = 4,8 %
tape = [1.012, 1.009, 1.011]
a["fy1-3-L2-02"] = (mean(tape) - 1.000) * 1000                     # tape zero error = mean − 1,000 m = 0,01067 m = 10,7 mm
a["fy1-3-L2-03"] = mean([12.4, 0.125 * 100, 123 / 10])             # 12,4 cm; 0,125 m = 12,5 cm; 123 mm = 12,3 cm; mean 12,4 cm
a["fy1-3-L2-04"] = half([5.2, 5.6, 5.4, 5.3, 5.5]) / half([5.40, 5.43, 5.41, 5.42, 5.44])   # 0,2 cm / 0,02 cm = 10
# Level 3: reasoning and combining ideas
a["fy1-3-L3-01"] = -0.18 + 0.12                                    # reading = true − start delay + stop delay: error = −0,18 s + 0,12 s = −0,06 s
a["fy1-3-L3-02"] = 0.5 / 250 * 1000                                # one sheet: 0,5 mm / 250 = 0,002 mm = 2,0 µm
a["fy1-3-L3-03"] = mean([8.24, 8.27, 8.25, 8.29, 8.25]) - 8.00    # systematic error = mean − true = 8,26 cm − 8,00 cm = 0,26 cm
# Exercise bank additions (teacher 2026-11-04): L1-06 is multiple choice (no number)
w = [5.41, 5.47, 5.39, 5.44, 5.43]                                 # block width (cm): mean 5,428 cm, half-range 0,04 cm (one figure) -> mean to hundredths
a["fy1-3-L1-07"] = round(mean(w), 2)                               # 27,14 cm / 5 = 5,428 cm -> 5,43 cm (± 0,04 cm)
a["fy1-3-L1-08"] = round(0.2 / 2, 2)                               # thermometer: half of the smallest division 0,2 °C = 0,1 °C
rec = [18.12, 18.31, 18.05, 18.27, 18.19, 18.35, 18.10, 18.22]     # 10 revolutions (s), data of L2-05: mean 18,20125 s, half-range 0,15 s
a["fy1-3-L2-05"] = round(mean(rec) / 10, 2)                        # T = 18,20125 s / 10 = 1,820 s (ΔT = 0,15 s / 10 = 0,015 s, two figures) -> 1,82 s
vA = [50.9, 51.1, 50.8, 51.0, 50.9]                                # data of L2-06 (ml), true value 50,0 ml; B: 49,4 50,5 49,8 50,3 50,1 (mean 50,02, half-range 0,55)
a["fy1-3-L2-06"] = round(mean(vA) - 50.0, 2)                       # A: mean 50,94 ml, deviation +0,94 ml, half-range 0,15 ml
a["fy1-3-L2-07"] = math.ceil(0.2 / (1.5 * 0.01))                   # ΔT/T = 0,2 s / (N · 1,5 s) <= 0,01 -> N >= 13,3 -> 14 swings
cart = [2.41, 2.38, 2.44, 2.40, 2.43, 2.39, 2.42]                  # data of L3-04 without the 2,97 s (clock stopped late, cause noted): 16,87 s / 7
a["fy1-3-L3-04"] = round(mean(cart), 2)                            # 2,41 s (with the outlier 19,84 s / 8 = 2,48 s)
a["fy1-3-L3-05"] = round((2.74 - 2.60) - (0.05 + 0.05), 2)         # difference 0,14 g/cm³ − 0,10 g/cm³ = 0,04 g/cm³ (intervals 2,69…2,79 and 2,55…2,65 do not overlap)
print(json.dumps(a))
