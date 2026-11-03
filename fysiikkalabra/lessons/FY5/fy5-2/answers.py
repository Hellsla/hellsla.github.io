"""Every answer in exercises.json for fy5-2, computed from the task data (python -I answers.py).
Equilibrium of a rigid body: the sum of the forces is zero and the sum of the moments M = Fr about any point is zero
(anticlockwise positive). Uniform bodies have their centre of mass (painopiste) at the middle. g = 9,81 m/s².
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}
# Level 1: one formula, values given
a["fy5-2-L1-01"] = 30 * g * 1.6 / (40 * g)               # seesaw: m1 g r1 = m2 g r2 -> r2 = 30 · 1,6 / 40 = 1,2 m (g cancels)
a["fy5-2-L1-02"] = 0.50 * 0.30 / 0.20                    # ruler balanced at its middle: F r = F_p r_p -> F = 0,50 N · 0,30 m / 0,20 m = 0,75 N
a["fy5-2-L1-03"] = 620 * 0.400 / 1.20                    # wheelbarrow, moments about the axle: F · 1,20 m = 620 N · 0,400 m -> 206,7 N
a["fy5-2-L1-04"] = 12.0 * g / 2                          # plank on supports at both ends, symmetric: N = G / 2 = 117,72 N / 2 = 58,86 N
a["fy5-2-L1-05"] = 6.0 * 0.80 / (2.0 + 6.0)              # light bar, 2,0 kg at x = 0 and 6,0 kg at 0,80 m: x = m2 x2 / (m1 + m2) = 0,60 m
# Level 2: two steps, a rearrangement or two moments
G = 25.0 * g                                             # plank 4,00 m, 25,0 kg, supports at 0,50 m and 3,00 m from the left end
a["fy5-2-L2-01"] = G * (3.00 - 2.00) / (3.00 - 0.50)     # moments about support 2: N1 · 2,50 m = G · 1,00 m -> N1 = 98,1 N
Gl, Gh = 20 * g, 70 * g                                  # bridge plank 3,0 m, 20 kg, on its ends; person 70 kg at 1,0 m from the left end
a["fy5-2-L2-02"] = (Gl * 1.5 + Gh * 2.0) / 3.0           # moments about the right end: N1 · 3,0 m = Gl · 1,5 m + Gh · 2,0 m -> 555,9 N -> 560 N
a["fy5-2-L2-03"] = math.degrees(math.atan(0.400 / 1.80)) # shelf tilted on its edge tips when the CoM is above the edge: tan θ = d / h -> 12,53°
a["fy5-2-L2-04"] = (5.0 * g * 0.32 + 15 * 0.15) / 0.040  # forearm, moments about the elbow: F · 0,040 m = 49,05 N · 0,32 m + 15 N · 0,15 m -> 448,6 N -> 450 N
# Level 3: reasoning or an unfamiliar context
# painter on the overhang: plank 4,00 m, 20,0 kg (CoM 2,00 m), supports 0,50 m and 3,00 m, painter 60,0 kg.
# Tipping starts when N1 = 0: moments about support 2: Gl (3,00 − 2,00) = Gp (x − 3,00) -> x = 3,00 + 20,0 · 1,00 / 60,0
a["fy5-2-L3-01"] = 3.00 + 20.0 * 1.00 / 60.0             # 3,333 m from the left end
# sign: uniform bar 1,20 m, 4,00 kg, hinged at the wall; sign 8,00 kg at the outer end; cable from the outer end at 30,0° to the bar.
# moments about the hinge: T sin 30° · 1,20 m = Gb · 0,60 m + Gs · 1,20 m
a["fy5-2-L3-02"] = (4.00 * g * 0.60 + 8.00 * g * 1.20) / (1.20 * math.sin(math.radians(30.0)))   # 196,2 N
# log 5,00 m, 90,0 kg; front carrier at the front end lifts 300 N; rear carrier at distance a from the rear end.
# moments about the rear carrier: 300 N · (5,00 m − a) = G (2,50 m − a) -> a = (G · 2,50 − 300 · 5,00) / (G − 300)
Glog = 90.0 * g
a["fy5-2-L3-03"] = (Glog * 2.50 - 300 * 5.00) / (Glog - 300)   # 1,213 m
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
