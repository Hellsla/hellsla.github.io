"""Numbers of the lesson text and inquiry.json for fy3-13, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
import json

a = {}
# Lesson and inquiry numbers (not exercises): data θ 10…100 °C, p 105…138 kPa, ±1 kPa
th, p = [10, 25, 40, 55, 70, 85, 100], [105, 110, 116, 122, 127, 132, 138]
ks, p0s = (133 - 104) / (85 - 10), 104 - (133 - 104) / (85 - 10) * 10      # steepest line through bar ends (10;104), (85;133): 0,3867 kPa/°C, 100,13 kPa
kl, p0l = (137 - 111) / (100 - 25), 111 - (137 - 111) / (100 - 25) * 25    # shallowest line through bar ends (25;111), (100;137): 0,3467 kPa/°C, 102,33 kPa
assert all(abs(p0s + ks * t - q) <= 1 + 1e-9 and abs(p0l + kl * t - q) <= 1 + 1e-9 for t, q in zip(th, p))   # both pass every ±1 kPa bar
a["esimerkki-theta0"] = -101.3 / ((138.0 - 101.3) / 100)                   # best line read at (0;101,3), (100;138,0): θ0 = −276,0 °C
a["esimerkki-theta0-max"] = -100.1 / 0.387                                # steep line as printed: −258,7 °C (exact −258,97)
a["esimerkki-theta0-min"] = -102.3 / 0.347                                # shallow line as printed: −294,8 °C (exact −295,19)
a["epavarmuus"] = (a["esimerkki-theta0-max"] - a["esimerkki-theta0-min"]) / 2   # Δθ0 = 18,07 °C ≈ 18 °C (exact lines 18,11)
a["epavarmuus-exact"] = (-p0s / ks - (-p0l / kl)) / 2                      # 18,11 °C
k_ab = (134.3 - 108.6) / 70                                                # suora: k from A, B
a["suora"] = 20 - 108.6 / k_ab                                             # θ0 = θA − pA/k = −275,8 °C
a["siirto"] = 30 - 133.0 / (26.0 / 60)                                     # −276,9 °C
a["tarkistus-2"] = 15 - 108 / (29 / 80)                                    # −282,9 °C
a["s2-misses"] = sum(abs(98.9 + 0.42 * t - q) > 1 for t, q in zip(th, p))  # candidate s2: p = 98,9 + 0,42θ (through (55;122)) misses 4 bars: 10, 70, 85, 100 °C
print(json.dumps({key: round(v, 6) for key, v in a.items()}))
