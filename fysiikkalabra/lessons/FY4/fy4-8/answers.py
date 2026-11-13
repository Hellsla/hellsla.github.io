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
# Added tasks (L1-06..08, L2-05..07, L3-04..05)
a["fy4-8-L1-07"] = 0.5 * 58.0 * (4.50 ** 2 - 7.50 ** 2) / 1000   # skater: W_kok = ΔE_k = ½m(v2² − v1²) = −1044 J = −1,044 kJ
hs = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
vs = [1.00, 1.38, 1.73, 1.96, 2.23, 2.41]
k = sum(h * v ** 2 for h, v in zip(hs, vs)) / sum(h * h for h in hs)   # least-squares line through the origin: v² = k·h
a["fy4-8-L2-05"] = k / 2                                  # pendulum: mgh = ½mv² → v² = 2g·h → g = k/2 = 9,77 m/s²
mw = 420
pts = [(18.0, 1.5), (6.0, 14.6), (12.0, 7.9), (3.0, 14.2)]   # (h, v) at A, B, C, D
Em = [(0.5 * mw * v ** 2 + mw * g * h) / 1000 for h, v in pts]   # E_mek = ½mv² + mgh in kJ: 74,6; 69,5; 62,5; 54,7
a["fy4-8-L2-06"] = Em[3] - Em[0]                          # W_muut = E_mek,D − E_mek,A = −19,93 kJ
v0 = [1.0, 1.5, 2.0, 2.5, 3.0]
ss = [0.22, 0.47, 0.88, 1.35, 1.98]
k = sum(v ** 2 * s_ for v, s_ in zip(v0, ss)) / sum(v ** 4 for v in v0)   # slope of s against v0² through the origin
a["fy4-8-L2-07"] = 0.50 / (2 * k)                         # block: −F s = −½mv0² → s = m/(2F)·v0² → F = m/(2k) = 1,144 N
runs = [29.4, 31.2, 28.7, 30.5, 29.9, 30.7]
s_ka = sum(runs) / len(runs)                              # mean stopping distance 30,07 m
a["fy4-8-L3-04"] = 70 * g * 6.0 / (45 + s_ka)             # snowboarder: mgh − F(L + s) = 0 → F = mgh/(L + s_ka) = 54,89 N
H = [1.20, 0.77, 0.49, 0.32, 0.20]
a["fy4-8-L3-05"] = 100 * sum(H[i + 1] / H[i] for i in range(4)) / 4   # E = mgh at the top; mean retained share 63,9 %
# Added exercises (figure tasks)
m_ball = 2 * 4.0 / 4.0 ** 2                                        # pallo-ek: (4,0 m/s; 4,0 J) → m = 2E_k/v² = 0,50 kg
a["fy4-8-L2-08"] = float(f"{(9.0 - 4.0) / (m_ball * g):.1e}")              # E_k1 = 9,0 J (6,0 m/s), E_k2 = 4,0 J (4,0 m/s): h = ΔE_k/(mg) = 1,02 m
a["fy4-8-L2-09"] = (40 - 25) / 6.0                                 # palkit-asteikko: W_muut = 25 − 40 = −15 J = −F s → F = 2,5 N
print(json.dumps(a))
