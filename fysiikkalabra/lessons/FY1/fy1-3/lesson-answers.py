"""Numbers of the lesson text and inquiry.json for fy1-3, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
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
