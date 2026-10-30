"""Every answer in exercises.json for fy4-4, computed from the task data (python -I answers.py).
Each solution starts from the force diagram where forces act: the positive direction is the motion's (or up); g = 9,81 m/s².
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

g = 9.81
a = {}
# Level 1: one formula, values given
a["fy4-4-L1-01"] = 6.0 / 2.5                       # a = ΣF/m = 6,0 N : 2,5 kg = 2,4 m/s²
a["fy4-4-L1-02"] = 80 * 1.5                        # ΣF = ma = 80 kg · 1,5 m/s² = 120 N
a["fy4-4-L1-03"] = 45 / 3.0                        # m = ΣF/a = 45 N : 3,0 m/s² = 15 kg
a["fy4-4-L1-04"] = (38 - 20) / 12                  # box: x: F − F_μ = ma → a = 18 N : 12 kg = 1,5 m/s²
a["fy4-4-L1-05"] = 8.0 * g                         # bucket lifted at constant velocity: T − mg = 0 → T = 78,48 N
# Level 2: two steps, a conversion or a rearrangement
v = 90 / 3.6                                       # 90 km/h = 25 m/s
a["fy4-4-L2-01"] = 1200 * (v - 0) / 10             # a = Δv/Δt = 2,5 m/s², ΣF = ma = 3000 N
a["fy4-4-L2-02"] = 900 * (g - 1.5)                 # lift accelerating down: mg − T = ma → T = m(g − a) = 7479 N
a["fy4-4-L2-03"] = 120 * (g + (2.0 - 0) / 2.0)     # load moving down, stopping in 2,0 s: a = 1,0 m/s² up; T − mg = ma → T = 1297 N
a["fy4-4-L2-04"] = (60 - 45) / 30                  # two pulls on a cart: ΣF = 15 N → a = 0,50 m/s²
# Level 3: reasoning, two ideas, an unfamiliar context
N = 54 * g                                         # the scale shows N/g = 54 kg → N = 529,7 N
a["fy4-4-L3-01"] = (60 * g - N) / 60               # N − mg = m a_y → a_y = −0,981 m/s²: 0,98 m/s² downward
ae = (36 / 3.6) / 8.0                              # empty truck: a = 10 m/s : 8,0 s = 1,25 m/s²
F = 10000 * ae                                     # ΣF = 12 500 N, the same for the loaded truck
a["fy4-4-L3-02"] = (36 / 3.6) / (F / 25000)        # loaded: a = 0,50 m/s², t = Δv/a = 20 s
a["fy4-4-L3-03"] = 4.0 / (18 / 30)                 # sled: only friction horizontal, a = 0,60 m/s² → t = 6,67 s
print(json.dumps(a))
