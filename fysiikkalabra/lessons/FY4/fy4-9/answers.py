"""Every answer in exercises.json for fy4-9, computed from the task data (python -I answers.py).
Momentum p = m v, impulse I = F Δt (the area under the (t, F) graph when the force varies), impulse principle
Δp = m v2 − m v1 = I; in one dimension the signs give the directions. Prints {id: number} as JSON on the last line;
the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy4-9-L1-01"] = 0.17 * 30                         # puck: p = m v = 5,1 kg·m/s
a["fy4-9-L1-02"] = 12 * 0.50                         # constant push: I = F Δt = 6,0 N·s
a["fy4-9-L1-03"] = 0.27 * 18 - 0.27 * 0              # volleyball from rest: I = Δp = m v2 − m v1 = 4,86 N·s
a["fy4-9-L1-04"] = 420 / 70                          # skier: v = p / m = 6,0 m/s
a["fy4-9-L1-05"] = 0.15 / 0.0010                     # shuttlecock: F = I / Δt = 150 N
# Level 2: two steps, a conversion or a rearrangement
a["fy4-9-L2-01"] = 1200 * (54 / 3.6) / 3.0 / 1000    # car braking to rest: F = m v1 / Δt = 6000 N = 6,0 kN
a["fy4-9-L2-02"] = 0.046 * 70 / 0.50e-3 / 1000       # golf ball from rest: F = m v / Δt = 6440 N = 6,44 kN
m, v1, v2 = 0.060, 14.0, -11.0                       # ball against a wall: positive toward the wall
a["fy4-9-L2-03"] = abs(m * v2 - m * v1)              # |I| = |Δp| = 0,060 · 25 = 1,5 N·s
a["fy4-9-L2-04"] = 8.0 + 120 * 0.025 / 0.17          # puck hit along its motion: v2 = v1 + F Δt / m = 25,65 m/s
# Level 3: reasoning, two ideas, an unfamiliar context
I = 60 * (0.60 + 1.00) / 2                           # trapezoid (parallel sides 0,60 s and 1,00 s): rise 0,20 s, 60 N for 0,60 s, fall 0,20 s: 48 N·s
a["fy4-9-L3-01"] = 1.0 + I / 24                      # sled 24 kg at 1,0 m/s: v2 = v1 + I / m = 3,0 m/s
a["fy4-9-L3-02"] = 10e3 * 0.12 / 75 * 3.6            # seat belt at most 10 kN for 0,12 s: v = F Δt / m = 16 m/s = 57,6 km/h
m, v, vk, dt = 0.20, 8.0, 6.0, 0.020                 # clay ball sticks, rubber ball bounces back at 6,0 m/s
F_savi = m * v / dt                                  # 80 N
F_kumi = m * (v + vk) / dt                           # 140 N
a["fy4-9-L3-03"] = F_kumi - F_savi                   # 60 N = m vk / Δt
print(json.dumps(a))
