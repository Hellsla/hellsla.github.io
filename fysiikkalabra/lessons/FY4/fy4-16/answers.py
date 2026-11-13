"""Every answer in exercises.json for fy4-16, computed from the task data (python -I answers.py).
Each solution with forces starts from the force diagram: positive direction up in a lift, down for a falling jumper,
down the slope on a hill; g = 9,81 m/s². Sled tasks: straight slopes, friction coefficient the same on the slope and
the flat, air resistance neglected, no extra loss at the foot of the hill. Prints {id: number} as JSON on the last line;
the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}
# Level 1: one formula, values given
a["fy4-16-L1-01"] = 70.0 * (g + 0.80)               # lift speeds up upward: N − mg = ma → N = m(g + a) = 70,0 · 10,61 = 742,7 N
a["fy4-16-L1-02"] = (2.10e3 - 90.0 * g) / 1000      # canopy opening, positive up: ΣF = F_v − mg = 2100 − 882,9 = 1217,1 N = 1,217 kN up
a["fy4-16-L1-03"] = math.sqrt(2 * g * 3.20)         # icy chute, only the weight does work: mgh = ½mv² → v = √(2gh) = 7,924 m/s
a["fy4-16-L1-04"] = 6.0 ** 2 / (2 * 0.080 * g)      # flat run-out: N = mg, ½mv² − μmg s = 0 → s = v²/(2μg) = 22,94 m
a["fy4-16-L1-05"] = math.degrees(math.atan(0.15))   # steady slide: mg sin α − μ mg cos α = 0 → tan α = μ → α = 8,531°
# Level 2: two steps, a conversion or a rearrangement
a["fy4-16-L2-01"] = g * (66.5 / 60.0 - 1)           # scale shows N/g = 66,5 kg for m = 60,0 kg: a = N/m − g = g(66,5/60,0 − 1) = 1,063 m/s² up
L, al, v = 18.0, math.radians(12.0), 5.10           # sled from rest, slope 18,0 m at 12,0°, 5,10 m/s at the foot
a["fy4-16-L2-02"] = (g * L * math.sin(al) - v ** 2 / 2) / (g * L * math.cos(al))   # mgL sin α − μ mg cos α L = ½mv² → μ = 0,1373
m, v1, v2, h = 80.0, 52.0, 6.0, 145                 # canopy opens: 52,0 → 6,0 m/s while falling 145 m
a["fy4-16-L2-03"] = -(0.5 * m * (v2 ** 2 - v1 ** 2) - m * g * h) / 1000   # W_v = ΔE_k + ΔE_p = −106,72 − 113,80 kJ → 220,5 kJ to internal energy
a["fy4-16-L2-04"] = 850 * g * 12.0 / 15.0 / 1000    # constant speed, T = mg: W = mgh = 100,06 kJ in 15,0 s → P = W/t = 6,671 kW
# Level 3: reasoning, two ideas, an unfamiliar context
a["fy4-16-L3-01"] = 4.50 / 0.120                    # mgh − μ mg (x_slope + x_flat) = 0 whatever the slopes' angles: x = h/μ = 37,5 m
m3, Gd = 75.0, 650                                  # force plate in a lift going down (figure ex-hissi): 650 N for 2,0 s (1,0 → 3,0 s)
a3 = (m3 * g - Gd) / m3                             # mg − N = ma (positive down) → a = g − N/m = 1,143 m/s² down
a["fy4-16-L3-02"] = a3 * 2.0                        # v = a t = 2,287 m/s, the greatest speed (then 800 N slows it in 2,67 s)
m, v1, v2, h = 70.0, 50.0, 6.0, 60.0                # canopy opens: 50,0 → 6,0 m/s over 60,0 m of fall
a["fy4-16-L3-03"] = -(0.5 * m * (v2 ** 2 - v1 ** 2) - m * g * h) / h / 1000   # W_v = ΔE_mek = −127,4 kJ = −F_v h → F_v = 2,124 kN
# Exercise-bank additions: MC tasks L1-06, L1-07 have no number (they are checked as text)
a["fy4-16-L1-08"] = 0.200 * 20.0 * g * math.cos(math.radians(30.0))   # slope: N = mg cos α, F = μN = 0,200 · 169,9 = 33,98 N (the student's μmg = 39,2 N is wrong)
a["fy4-16-L2-05"] = 62.0 * (g + 1.20 / 3.0)         # lift speeds up: a = Δv/Δt = 1,20/3,0 = 0,400 m/s², N = m(g + a) = 633,0 N
v_first, v_last = 3.62 - 0.00, 10.03 - 9.57         # flat run-out: mean speeds in the 1st and 5th second = speeds at 0,5 s and 4,5 s
a["fy4-16-L2-06"] = (v_first - v_last) / (4.5 - 0.5) / g   # |a| = 0,790 m/s², μ = |a|/g = 0,0805
al_ka = (17.5 + 18.0 + 18.5 + 17.0 + 18.0) / 5      # sum 89,0°, mean 17,8°; steady slide: μ = tan α
a["fy4-16-L2-07"] = math.tan(math.radians(al_ka))   # 0,3211 (range tan 17,0° … tan 18,5° = 0,306 … 0,335, ± 0,015)
al, mu1, mu2, d = math.radians(14.0), 0.060, 0.150, 25.0 - 5.0   # hill: slope 14,0°, flat 20,0 m before the safety margin
a["fy4-16-L3-04"] = mu2 * d / (math.sin(al) - mu1 * math.cos(al))   # mgL sin α − μ1 mg L cos α − μ2 mg d = 0 → L = 16,33 m (v at foot 7,67 m/s)
mj, ts, vs = 78.0, [0, .5, 1, 1.5, 2, 2.5, 3], [46.0, 29.8, 20.1, 14.4, 11.0, 9.0, 7.9]   # canopy table, first 3,0 s
hj = sum((vs[i] + vs[i + 1]) / 2 * (ts[i + 1] - ts[i]) for i in range(6))   # trapezoids: 55,625 m
a["fy4-16-L3-05"] = (mj * g + (0.5 * mj * vs[0] ** 2 - 0.5 * mj * vs[-1] ** 2) / hj) / 1000   # F_v = mg + ΔE_k/h = 765,2 + 1439,8 N = 2,205 kN
a["fy4-16-L2-09"] = abs((550 - 60.0 * g) / 60.0)           # figure hissi-kuvaaja: N = 550 N read after 9,0 s; a = (N − mg)/m = −0,643 m/s² (down), magnitude 0,643
print(json.dumps(a))
