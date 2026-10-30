"""Every answer in exercises.json for fy4-8, computed from the task data (python -I answers.py).
The zero level of potential energy is the lowest point of each situation; g = 9,81 m/s². Mechanical energy
E_mek = E_k + E_p; the energy principle E_k1 + E_p1 + W_muut = E_k2 + E_p2, where W_muut is the work of the forces
other than the weight (friction, air resistance, a pull or a push); the work of the net force is ΔE_k.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}
# Level 1: one formula, values given
a["fy4-8-L1-01"] = math.sqrt(2 * g * 12.0)               # stone from 12,0 m: mgh = ½mv² → v = √(2gh) = 15,344 m/s
a["fy4-8-L1-02"] = 6.0 ** 2 / (2 * g)                    # skater rises: ½mv² = mgh → h = v²/(2g) = 1,835 m
a["fy4-8-L1-03"] = -35 * 4.0                             # friction against the motion: W = −F s = −140 J
a["fy4-8-L1-04"] = 0.5 * 65 * 8.0 ** 2 / 1000            # sprinter from rest: W_kok = ΔE_k = ½mv² = 2080 J = 2,08 kJ
a["fy4-8-L1-05"] = 9.8 - 12.4                            # skier: W_muut = E_mek,2 − E_mek,1 = −2,6 kJ
# Level 2: two steps, a conversion or a rearrangement
a["fy4-8-L2-01"] = math.sqrt(8.00 ** 2 + 2 * g * 15.0)   # ball thrown down: ½mv0² + mgh = ½mv² → v = 18,929 m/s
a["fy4-8-L2-02"] = 0.5 * 1200 * (72 / 3.6) ** 2 / 6.0e3  # braking: −F s = 0 − ½mv² → s = mv²/(2F) = 40,0 m
a["fy4-8-L2-03"] = 250 * g * 18.0 / 1000                 # crane at constant speed: W_muut = ΔE_p = mgh = 44,145 kJ
a["fy4-8-L2-04"] = math.sqrt(2 * 120 * 0.30 / 0.16)      # puck: F s = ½mv² → v = √(2Fs/m) = 21,21 m/s
# Level 3: reasoning, two ideas, an unfamiliar context
m, h, v1, v2, s = 80, 12.0, 4.0, 13.0, 150
W = 0.5 * m * (v2 ** 2 - v1 ** 2) - m * g * h            # cyclist: W_muut = ΔE_k + ΔE_p = 6120 − 9417,6 = −3297,6 J
a["fy4-8-L3-01"] = -W / s                                # mean resistive force F = −W_muut / s = 21,98 N
m, h1, v0, F, s = 500, 35.0, 2.0, 150, 120
a["fy4-8-L3-02"] = h1 + v0 ** 2 / (2 * g) - F * s / (m * g)   # highest second hill: ½mv0² + mgh1 − Fs = mgh2 → 31,534 m
a["fy4-8-L3-03"] = math.sqrt(12.0 ** 2 + 2 * g * 20.0)   # stone thrown at any angle from 20,0 m: v = √(v0² + 2gh) = 23,16 m/s
print(json.dumps(a))
