"""Every answer in exercises.json for fy3-5, computed from the task data (python -I answers.py).
Sign convention of the lesson: ΔU = Q + W, Q > 0 into the system, W > 0 when the surroundings do work on it.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

g = 9.81          # m/s²
a = {}
# Level 1: one formula, values given (ΔU = Q + W with the signs read from the text)
a["fy3-5-L1-01"] = 120 + 450                           # dough: Q = +120 J (warm hands), W = +450 J (kneading) -> ΔU = 570 J
a["fy3-5-L1-02"] = -8.4 + 0                            # coffee cools: Q = −8,4 kJ, W = 0 -> ΔU = −8,4 kJ
a["fy3-5-L1-03"] = 350 + (-100)                        # balloon in sauna: Q = +350 J, expands W = −100 J -> ΔU = 250 J
a["fy3-5-L1-04"] = -180 + (-320)                       # car engine power stroke: Q = −180 J, W = −320 J -> ΔU = −500 J
a["fy3-5-L1-05"] = 15 + (-85)                          # tyre valve: Q = +15 J, air expands W = −85 J -> ΔU = −70 J
# Level 2: two steps, one conversion or one rearrangement
W_comp = 0.20 * (200 + 400) / 2                        # figure fy3-5/piston-force: (0; 200 N) to (0,20 m; 400 N), W = area = s·(F₁+F₂)/2 = 60 J (on the air, positive)
a["fy3-5-L2-01"] = 45 - W_comp                         # Q = ΔU − W = 45 J − 60 J = −15 J (heat leaves the air)
Q_kettle = 2.0e3 * 90 / 1000                           # Q_in = P t = 2000 W · 90 s = 180 000 J = 180 kJ
a["fy3-5-L2-02"] = Q_kettle + (-20)                    # ΔU = 180 kJ − 20 kJ = 160 kJ
a["fy3-5-L2-03"] = (-1.2e3) - (-2.0e3)                 # steam: ΔU = −1200 J, W = −2000 J -> Q = ΔU − W = +800 J
W_blend = (12 - 2.0) * 1000                            # smoothie: ΔU = 12 kJ, Q = +2,0 kJ -> blade work W = ΔU − Q = 10 kJ = 10 000 J
a["fy3-5-L2-04"] = W_blend / 250                       # blending time t = W / P = 10 000 J / 250 W = 40 s
# Level 3: reasoning or an unfamiliar context
W_pump = 120 * 0.15                                    # plugged pump: W = F s = 18 J on the air
a["fy3-5-L3-01"] = 0 - W_pump                          # constant temperature, same air -> ΔU = 0, Q = −W = −18 J
n, m = 12, 5.0                                         # 12 descents of a 5,0 kg mass, insulated bath: Q = 0, ΔU = W
a["fy3-5-L3-02"] = 1.0e3 / (n * m * g)                 # ΔU = n m g h -> h = 1000 J / (12 · 5,0 kg · 9,81 m/s²) = 1,699 m -> 1,7 m
dU_A = 400 + (-150)                                    # route A: Q = +400 J, gas does 150 J of work W = −150 J -> ΔU = 250 J
a["fy3-5-L3-03"] = dU_A - (-60)                        # route B: same initial and final temperature, so same ΔU; W = −60 J -> Q = ΔU − W = 310 J
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
