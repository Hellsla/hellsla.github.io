"""Numbers of the lesson text and inquiry.json for fy5-8, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Harmonic force: the spring's force on the body F = -k x (x the displacement from
the equilibrium position, the force towards it); the force stretching or compressing the spring F_v = k x (Newton III:
the body pushes or pulls the spring as hard as the spring the body); spring potential energy E_p = 1/2 k x² is the area
under the (x, F_v) graph. g = 9,81 m/s². Prints {id: number} as JSON."""
import json, math

g = 9.81
a = {}
# Simulation (model values): springs A, B, C with k = 20, 50 and 80 N/m (hidden from the student)
K = {"A": 20.0, "B": 50.0, "C": 80.0}
k = K["B"]
for x in (-0.10, -0.05, 0.05, 0.10, 0.20):              # Koe 1, spring B
    a[f"exp1-F-{x:+.2f}"] = -k * x                       # spring's force on the cart: +5,0 +2,5 -2,5 -5,0 -10 N
    a[f"exp1-Fv-{x:+.2f}"] = k * x                       # the hand's force (stretching force): -5,0 -2,5 +2,5 +5,0 +10 N
for x in (0.05, 0.10, 0.20):                             # Koe 2, spring B
    a[f"exp2-Ep-{x:.2f}"] = 0.5 * k * x ** 2             # 0,0625 J, 0,250 J, 1,00 J: doubling x gives four times
a["exp2-ratio"] = a["exp2-Ep-0.10"] / a["exp2-Ep-0.05"]  # 4
a["exp2-Ep-neg0.10"] = 0.5 * k * (-0.10) ** 2            # compressed by 0,10 m: the same 0,250 J
for s, kk in K.items():                                  # Koe 3 (optional): x = 0,10 m, each spring
    a[f"exp3-Fv-{s}"] = kk * 0.10                        # 2,0 N, 5,0 N, 8,0 N
a["exp3-kC"] = a["exp3-Fv-C"] / 0.10                     # k = F_v / x = 80 N/m
a["exp3-kC-cm"] = a["exp3-Fv-C"] / 10                    # mistake: x in cm, 0,80
# Predictions (spring B): 5 cm gives 2,5 N; 10 cm gives 5,0 N; energy 0,0625 J -> 0,250 J
a["pred2-F5"] = k * 0.05
a["pred2-F10"] = k * 0.10
# Kaava, graph "kulmakerroin": example spring, two points on the fitted line (0,025 m; 1,0 N) and (0,100 m; 4,0 N)
a["kaava-dx"] = 0.100 - 0.025                            # Δx = 0,075 m
a["kaava-dF"] = 4.0 - 1.0                                # ΔF_v = 3,0 N
a["kaava-k"] = a["kaava-dF"] / a["kaava-dx"]             # k = ΔF_v / Δx = 40 N/m
# Worked example: a fish of 1,20 kg hangs at rest from a spring balance stretched 3,0 cm
m, x = 1.20, 0.030
a["ex-G"] = m * g                                        # 11,772 N = the stretching force (the fish at rest)
a["ex-k"] = m * g / x                                    # k = mg/x = 392,4 N/m
a["ex-Ep"] = 0.5 * a["ex-k"] * x ** 2                    # E_p = 1/2 k x² = 0,1766 J
a["ex-Ep-area"] = 0.5 * a["ex-G"] * x                    # check: triangle 1/2 · F_v · x = 0,1766 J
# Measurement (interpret "mittaus"): hanging masses on a spring, extension measured (example data)
ms = [0.050, 0.100, 0.150, 0.200, 0.250, 0.300]          # kg
xs = [0.017, 0.032, 0.050, 0.064, 0.083, 0.098]          # m (1,7 ... 9,8 cm)
Fs = [mm * g for mm in ms]                               # F_v = mg: 0,49 ... 2,94 N
for mm, F in zip(ms, Fs): a[f"mit-F-{int(mm * 1000)}"] = F
a["mit-k-fit"] = sum(F * xx for F, xx in zip(Fs, xs)) / sum(xx * xx for xx in xs)   # least squares through the origin: 29,95 N/m
a["mit-k-read"] = 3.0 / 0.100                            # read from the fitted line: (10,0 cm, 3,0 N) -> 30 N/m
a["mit-k-cm"] = 3.0 / 10.0                               # mistake: slope in N/cm, 0,30
a["mit-k-mass"] = 0.300 / 0.098                          # mistake: mass (kg) instead of the force on the axis, 3,06
# Transfer "siirto": pinball plunger k = 250 N/m pulled back 6,0 cm, ball 80 g; E_p -> E_k
kp, xp, mb = 250.0, 0.060, 0.080
a["siirto-Ep"] = 0.5 * kp * xp ** 2                      # 0,45 J
a["siirto-v"] = math.sqrt(2 * a["siirto-Ep"] / mb)       # v = x sqrt(k/m) = 3,354 m/s
a["siirto-v-nohalf"] = xp * math.sqrt(2 * kp / mb)       # mistake: E_p = k x², 4,743 m/s
a["siirto-v-grams"] = xp * math.sqrt(kp / 80)            # mistake: mass in grams, 0,106 m/s
a["siirto-v-cm"] = 6.0 * math.sqrt(kp / mb)              # mistake: x in cm, 335 m/s
# Check 2: F = -6,0 N at x = 0,12 m -> k = 50 N/m; at x = -0,20 m F = +10 N
k2 = 6.0 / 0.12
a["check2-k"] = k2                                       # 50 N/m
a["check2-F"] = -k2 * (-0.20)                            # +10 N
# Check 3 (draw): a box pulled by a spring at constant velocity, k = 120 N/m, kinetic friction 18 N, m = 6,0 kg
a["check3-x"] = 18 / 120                                 # x: k x - F_mu = 0 -> x = F_mu/k = 0,15 m
a["check3-G"] = 6.0 * g                                  # 58,86 N = N
# Exit ticket: k = 200 N/m compressed or stretched 0,10 m: E_p = 1,0 J either way
a["exit-Ep"] = 0.5 * 200 * 0.10 ** 2
print(json.dumps(a))
