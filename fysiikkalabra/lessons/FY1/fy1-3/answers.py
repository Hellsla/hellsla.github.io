"""Every answer in exercises.json for fy1-3, computed from the task data (python -I answers.py).
Mean x̄ = (x1 + ... + xn) / n, half-range Δx = (x_max − x_min) / 2, error = result − true value, zero correction x = reading − zero reading.
The simulation's fixed series G is the same list as in assets/sims/fy1/fy1-3/sim.js: reading i = round(T + δ_sys + δ_sat · G[i], 0,01 s).
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

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
a["fy1-3-L1-03"] = half([12.4, 12.9, 12.6, 12.2, 12.7])            # (12,9 s − 12,2 s) / 2 = 0,35 s
a["fy1-3-L1-04"] = 48.7 - 1.2                                      # zero correction: m = 48,7 g − 1,2 g = 47,5 g
a["fy1-3-L1-05"] = 1.0 / 2                                         # reading error = half the smallest division = 1 mm / 2 = 0,5 mm
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
print(json.dumps(a))
