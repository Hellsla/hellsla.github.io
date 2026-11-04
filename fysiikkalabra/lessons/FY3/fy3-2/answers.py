"""Every answer in exercises.json for fy3-2, computed from the task data (python -I answers.py).
Work W = F s (constant force along the motion), or the area under the (s,F) graph.
Lifting work W = G h = m g h with g = 9,81 m/s². Power P = W / t = F v.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

g = 9.81  # m/s²

a = {}
# Level 1: one formula, values given
a["fy3-2-L1-01"] = 80 * 25 / 1000                      # moped: W = F s = 80 N · 25 m = 2000 J -> 2,0 kJ
a["fy3-2-L1-02"] = 150 * 1.2                           # shelf: W = G h = 150 N · 1,2 m = 180 J
a["fy3-2-L1-03"] = 36e3 / 12 / 1000                    # lift motor: P = W / t = 36 000 J / 12 s = 3000 W -> 3,0 kW
a["fy3-2-L1-04"] = 25 * 6.0 + 10 * (10 - 6.0)           # figure fy3-2/pull-steps: two rectangles, 25 N over 0–6 m and 10 N over 6–10 m: 150 J + 40 J = 190 J
a["fy3-2-L1-05"] = 20 * 3.0                            # sledge pulled: P = F v = 20 N · 3,0 m/s = 60 W
# Level 2: rearrangement, conversion or two steps
a["fy3-2-L2-01"] = 45e3 / 1.5e3                        # tractor: s = W / F = 45 000 J / 1500 N = 30 m
a["fy3-2-L2-02"] = 1.5e3 * 4.0 * 60 / 1000             # pump: W = P t = 1500 W · 240 s = 360 000 J -> 360 kJ
a["fy3-2-L2-03"] = 850 * g * 30 / 1000                 # crane: W = m g h = 850 kg · 9,81 m/s² · 30 m = 250 155 J -> 250 kJ
a["fy3-2-L2-04"] = 10 * 2.0 + 0.5 * (10 + 30) * 4.0    # cart: W = F₁ s₁ + ½ (F₁ + F₂) s₂ = 20 J + 80 J = 100 J
# Level 3: reasoning and combining ideas
W_laatikko = 0.5 * 40 * 0.50 + 40 * 1.0 + 0.5 * 40 * 0.50  # box: area = 10 J + 40 J + 10 J = 60 J
a["fy3-2-L3-01"] = W_laatikko / 2.0                    # F_ka = W / s = 60 J / 2,0 m = 30 N
a["fy3-2-L3-02"] = 20 * 2.0 * g * 1.5                  # Joule: Q = n m g h = 20 · 29,43 J = 588,6 J -> 590 J
W_vesi = 1000 * g * 50                                 # water lifted: W = m g h = 490 500 J
a["fy3-2-L3-03"] = W_vesi / 180 / 60                   # t = W / P = 2725 s = 45,4 min -> 45 min

# Exercise-bank additions: L1-06 and L1-08 are multiple choice (no number)
a["fy3-2-L1-07"] = 1.8e3 / 1.2e3                       # belt: v = P / F = 1800 W / 1200 N = 1,5 m/s
a["fy3-2-L2-05"] = sum((F1 + F2) / 2 * 1.0 for F1, F2 in [(18.0, 17.2), (17.2, 15.1), (15.1, 11.0), (11.0, 6.0)])  # cart: trapezoids 17,6 + 16,15 + 13,05 + 8,5 = 55,3 J
a["fy3-2-L2-06"] = 62 * g * (18 * 0.17) / ((8.1 + 7.8 + 8.4) / 3)  # stairs: W = m g h = 1861,2 J, t_ka = 8,1 s, P = 229,8 W
a["fy3-2-L2-07"] = 40 * g * 1.5                        # error analysis: G = m g = 392,4 N, W = G h = 588,6 J
v_nosto = 6.52 / 8.0                                   # hoist: slope of the fitted line through the origin, 6,52 m / 8,0 s = 0,815 m/s
a["fy3-2-L3-04"] = 0.5 * 10.0 * 0.100 / (0.20 * g) * 100  # spring: W = ½ F s = 0,500 J, h = W / (m g) = 0,2548 m -> 25 cm
a["fy3-2-L3-05"] = 450 * g * v_nosto / 1000            # hoist: P = m g v = 4414,5 N · 0,815 m/s = 3598 W -> 3,6 kW

print(json.dumps(a))
