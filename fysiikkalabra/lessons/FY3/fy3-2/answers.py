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

print(json.dumps(a))
