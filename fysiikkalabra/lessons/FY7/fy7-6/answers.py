"""Every answer in exercises.json for fy7-6, computed from the task data (python -I answers.py).
Lenz's law and eddy currents: at constant speed the braking force equals the weight (F = m g), the heating power is
P = F v, the energy into internal energy Q = ΔE_p - ΔE_k or the kinetic energy lost; induction e = N ΔΦ / Δt, I = e / R.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}
# Level 1: one formula, values given
a["fy7-6-L1-01"] = 40e-3 * g                                            # constant speed: F = m g = 0,040 kg · 9,81 m/s² = 0,3924 N -> 0,39 N
# fy7-6-L1-02 is answered in words (S pole approaching: S face, the ring repels)
a["fy7-6-L1-03"] = 0.5 * 450 * (22.0 ** 2 - 6.0 ** 2) / 1e3             # Q = 1/2 m (v1² - v2²) = 225 · 448 J = 100 800 J -> 100 kJ
a["fy7-6-L1-04"] = 25e-3 * g * 0.30 * 1e3                               # P = m g v = 0,025 · 9,81 · 0,30 W = 0,073575 W -> 74 mW
# fy7-6-L1-05 is answered in words (induction hob: the glass does not conduct, no eddy currents in it)
# fy7-6-L1-06 and L1-07 are multiple choice (ring: a receding magnet gives an S face and attraction; aluminium tube: eddy currents brake, plastic has none)
a["fy7-6-L1-08"] = 120 * 2.5e-3 / 0.050                                 # e = N ΔΦ / Δt = 120 · 0,0025 Wb / 0,050 s = 6,0 V
# Level 2: two steps, one conversion or one rearrangement
v = 1.50 / 10                                                           # constant speed v = h / t = 0,15 m/s
a["fy7-6-L2-01"] = 20e-3 * g * v * 1e3                                  # P = m g v = 0,02943 W -> 29 mW (Q / t = 0,029408 W agrees)
e = 200 * 3.0e-3 / 0.20                                                 # e = N ΔΦ / Δt = 200 · 0,0030 Wb / 0,20 s = 3,0 V
a["fy7-6-L2-02"] = e / 15                                               # I = e / R = 3,0 V / 15 Ω = 0,20 A
a["fy7-6-L2-03"] = 20e-3 * g / 1.3                                      # k v = m g: v = 0,1962 N / 1,3 Ns/m = 0,15092 m/s -> 0,15 m/s
a["fy7-6-L2-04"] = 60e3 * 250 * 1000 / 3600 / 1e6                       # P = F v = 60 000 N · 69,44 m/s = 4,1667 MW -> 4,2 MW
t_ka = (7.4 + 7.1 + 7.6 + 7.3 + 7.2) / 5                                # thick tube: sum 36,6 s, t_ka = 7,32 s
a["fy7-6-L2-05"] = 20e-3 * g * (1.00 / t_ka) * 1e3                      # P = m g h / t_ka = 0,020 · 9,81 · 0,1366 W = 26,80 mW -> 27 mW
# fy7-6-L2-06 is answered in words (error analysis: the induced field opposes the change; an N face repels)
products = [0.40 * 0.27, 0.25 * 0.41, 0.20 * 0.53, 0.10 * 1.02]  # e · Δt = N ΔΦ: 0,108, 0,1025, 0,106, 0,102 Wb
a["fy7-6-L2-07"] = sum(products) / 4 / 300 * 1e3                        # ΔΦ = (e Δt)_ka / N = 0,10463 Wb / 300 = 0,3488 mWb -> 0,35 mWb
# L2-08 is a two-stage multiple choice (no number): the ring jumps up, Lenz: its current opposes the growing flux
# Level 3: reasoning or an unfamiliar context
Q1 = 20e-3 * g * 1.00 - 0.5 * 20e-3 * 0.15 ** 2                         # one drop: m g h - 1/2 m v² = 0,19620 - 0,000225 = 0,195975 J
a["fy7-6-L3-01"] = 50 * Q1 / (0.35 * 385)                               # ΔT = 50 Q1 / (m c) = 9,79875 J / 134,75 J/K = 0,07272 K -> 0,073 K
# fy7-6-L3-02 is answered in words (Waltenhofen pendulum: a slotted plate swings long)
e3 = 3.0 * 0.50 * 0.40                                                  # rod on rails: e = v B l = 3,0 · 0,50 · 0,40 V = 0,60 V
I3 = e3 / 0.20                                                          # I = e / R = 3,0 A
a["fy7-6-L3-03"] = I3 * 0.40 * 0.50                                     # F = I l B = 0,60 N (Järkevyys: F v = 1,8 W = R I² = 1,8 W)
v_r = (0.73 + 0.75 + 0.74) / 3                                          # terminal speed = mean of the last three values = 0,74 m/s
k = 0.050 * g / v_r                                                     # k v_r = m g: k = 0,4905 N / 0,74 m/s = 0,6628 N s/m
a["fy7-6-L3-04"] = g - k * 0.54 / 0.050                                 # a(0,10 s) = g - k v / m = 9,81 - 0,6628 · 0,54 / 0,050 = 2,652 m/s² -> 2,7 m/s² (P = m g v_r = 0,363 W)
k5 = sum(P_ / d_ ** 2 for d_, P_ in [(1.00, 1.21), (0.80, 0.76), (0.50, 0.31), (0.25, 0.073)]) / 4   # P = k d²: k = 1,2014 W/mm²
a["fy7-6-L3-05"] = k5 * 0.35 ** 2                                       # P(0,35 mm) = 1,2014 · 0,1225 W = 0,1472 W -> 0,15 W
# Figure task L2-09 (brake-task: F(v) line F = 1,6 N·s/m · v, points scatter about it): read F(0,25 m/s) = 0,40 N
a["fy7-6-L2-09"] = 0.40 * 0.25 * 1e3                                    # P = F v = 0,40 N · 0,25 m/s = 0,100 W -> 100 mW
# Figure task L3-06 (same graph): k = F / v = 0,32 N / 0,20 m/s = 1,6 N s/m; terminal speed of a 45 g magnet: k v = m g
a["fy7-6-L3-06"] = 45e-3 * g / (0.32 / 0.20)                            # v = m g / k = 0,44145 N / 1,6 N s/m = 0,27591 m/s -> 0,28 m/s
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
