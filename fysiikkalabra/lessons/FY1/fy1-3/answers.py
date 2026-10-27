"""Every answer in exercises.json and inquiry.json for fy1-3, computed from the task data (python -I answers.py).
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

# Inquiry numbers (inquiry.json), not exercises
r, m = sim(40, 0.15, 0.30)
a["inq-exp2-vir"] = m - T                                          # experiment 2, n = 40: mean − T = 2,6995 s − 2,40 s = 0,2995 s (about 0,30 s)
a["inq-exp3-suhde"] = half(sim(40, 0.30, 0.0)[0]) / half(sim(40, 0.05, 0.0)[0])    # half-range at δ_sat 0,30 s over that at 0,05 s: 0,525 / 0,085 = 6,2
coins = [27.9, 28.1, 28.0, 27.8, 28.2]
a["inq-siirto"] = (mean(coins) - 0.8) / 5                          # one coin: (28,0 g − 0,8 g) / 5 = 5,44 g
a["inq-siirto-ilman-korjausta"] = mean(coins) / 5                  # mistake: zero error forgotten = 5,6 g
a["inq-siirto-ei-jakoa"] = mean(coins) - 0.8                       # mistake: five coins, not one = 27,2 g
a["inq-siirto-korjaus-per-kolikko"] = mean(coins) / 5 - 0.8        # mistake: zero error subtracted from one coin = 4,8 g
t5 = [2.36, 2.41, 2.38, 2.46, 2.39]
a["inq-check2"] = half(t5) / mean(t5) * 100                        # relative error = 0,05 s / 2,40 s = 2,1 %
ex = [3.12, 3.25, 3.07, 3.31, 3.19, 3.15]
a["inq-example-mean"] = mean(ex)                                   # worked example: mean = 19,09 s / 6 = 3,18 s
a["inq-example-half"] = half(ex)                                   # half-range = (3,31 s − 3,07 s) / 2 = 0,12 s
a["inq-example-rel"] = half(ex) / mean(ex) * 100                   # relative error = 0,12 s / 3,18 s = 3,8 %
ice = [1.4, 1.6, 1.5, 1.5, 1.6, 1.4, 1.5, 1.5]
a["inq-ice-zero"] = mean(ice)                                      # thermometer in melting ice: mean reading 1,5 °C, true 0 °C
a["inq-ice-corrected"] = 62.3 - mean(ice)                          # 62,3 °C − 1,5 °C = 60,8 °C

print(json.dumps(a))
