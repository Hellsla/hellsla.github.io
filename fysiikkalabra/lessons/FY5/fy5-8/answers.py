"""Every answer in exercises.json for fy5-8, computed from the task data (python -I answers.py).
Harmonic force: the spring's force on the body F = -k x towards the equilibrium position, the stretching force
F_v = k x; the spring constant is the slope of the (x, F_v) graph; spring potential energy E_p = 1/2 k x², the area
under the (x, F_v) graph. g = 9,81 m/s².
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}
# Level 1: one formula
a["fy5-8-L1-01"] = 250 * 0.12                             # gym machine return spring: |F| = k x = 30 N
a["fy5-8-L1-02"] = 450 / 0.050                            # trampoline spring: k = F_v / x = 9000 N/m
a["fy5-8-L1-03"] = 0.5 * 180 * 0.15 ** 2                  # chest expander: E_p = 1/2 k x² = 2,025 J
a["fy5-8-L1-04"] = 12.0 / 0.20                            # graph ex-suora: slope through (0,20 m, 12 N) = 60 N/m
a["fy5-8-L1-05"] = 6.0 / 40                               # spring balance: F_v = k x -> x = F_v / k = 0,15 m
# Level 2: two steps or a conversion or a rearrangement
k21 = 6.0 / 0.080                                         # 8,0 cm = 0,080 m: k = F_v / x = 75 N/m
a["fy5-8-L2-01"] = 0.5 * k21 * 0.080 ** 2                 # E_p = 1/2 k x² = 0,24 J (= 1/2 F_v x, the triangle)
a["fy5-8-L2-02"] = 2 * 0.90 / 0.060 ** 2                  # E_p = 1/2 k x² -> k = 2 E_p / x² = 500 N/m
a["fy5-8-L2-03"] = 0.5 * 150 * (0.090 ** 2 - 0.030 ** 2)  # ΔE_p = 1/2 k (x2² - x1²) = 0,54 J (not 1/2 k (Δx)² = 0,27 J)
L2_03_wrong = 0.5 * 150 * 0.060 ** 2                      # (the common mistake, for the solution's check) 0,27 J
kA = 6.0 / 0.10                                           # graph ex-kaksi: spring A through (0,10 m, 6,0 N), 60 N/m
a["fy5-8-L2-04"] = 0.5 * kA * 0.080 ** 2                  # E_p = 1/2 k x² = 0,192 J at 0,080 m
# Level 3: reasoning, two ideas
a["fy5-8-L3-01"] = 300 * g / 4 / 0.030 / 1000             # car suspension: the extra 300 kg shared by four springs, ΔF = k Δx -> 24,5 kN/m
h = 0.5 * 200 * 0.030 ** 2 / (0.050 * g)                  # jumping toy: 1/2 k x² = m g h -> h = k x² / (2 m g) = 0,1835 m
a["fy5-8-L3-02"] = h
a["fy5-8-L3-03"] = (30 + 50) * 0.040                      # two springs: both forces towards equilibrium, (k1 + k2) x = 3,2 N
# Exercise-bank additions
a["fy5-8-L1-08"] = 2.5 / 0.10                             # graph ex-kaksi: spring B through (0,10 m, 2,5 N), 25 N/m
xs = [0.041, 0.079, 0.121, 0.161]                         # L2-05: linear points 100..400 g (example data), x in m
Fs = [m * g / 1000 for m in (100, 200, 300, 400)]
a["fy5-8-L2-05"] = sum(F * x for F, x in zip(Fs, xs)) / sum(x * x for x in xs)   # least squares through origin, 24,4 N/m
a["fy5-8-L2-06"] = 0.200 * g / (0.200 - 0.120)            # x = L - L0 = 0,080 m: k = m g / x = 24,5 N/m
E1 = 0.5 * 12 * (12 / 80); E2 = 0.5 * 12 * (12 / 240)     # E_p = 1/2 F_v x: 0,90 J and 0,30 J
a["fy5-8-L2-07"] = E1 - E2                                # 0,60 J
Fr = [0, 1.5, 2.2, 2.8, 4.0]                              # L3-04: rubber band, steps of 0,030 m
a["fy5-8-L3-04"] = sum(0.030 * (Fr[i] + Fr[i + 1]) / 2 for i in range(4))   # trapezoids 0,255 J (Hooke from first point: 0,36 J)
kb = 151 / 0.50                                           # L3-05: bow, fitted line through (0,50 m, 151 N), 302 N/m
a["fy5-8-L3-05"] = 100 * (0.5 * 0.025 * 47.0 ** 2) / (0.5 * kb * 0.50 ** 2)   # efficiency E_k / E_p = 73,1 %
print(json.dumps(a))
