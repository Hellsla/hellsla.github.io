"""Every answer in exercises.json for fy4-6, computed from the task data (python -I answers.py).
Each solution starts from the force diagram: on a slope x points down the slope (or along the motion) and y away from
the surface; on level ground x along the motion and y up; g = 9,81 m/s² (on the Moon 1,62 m/s²).
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g, gK = 9.81, 1.62
r = math.radians
a = {}
# Level 1: one equation from the diagram
a["fy4-6-L1-01"] = 160 * gK                                # weight on the Moon: G = m g_Kuu = 259,2 N
a["fy4-6-L1-02"] = 0.12 * 30 * g                           # sled on level snow: N = mg, F_mu = mu N = 35,3 N
a["fy4-6-L1-03"] = 120 / (40 * g)                          # constant velocity: F − F_mu = 0, N = mg → mu = F/(mg) = 0,306
a["fy4-6-L1-04"] = 0.80 * g * math.cos(r(20))              # book on a 20° lid: y: N − mg cos α = 0 → N = 7,37 N
a["fy4-6-L1-05"] = 12 * g * math.sin(r(30))                # component along the slope: G_x = mg sin α = 58,9 N
# Level 2: two steps
a["fy4-6-L2-01"] = math.tan(r(12))                         # constant velocity down 12°: mg sin α = mu mg cos α → mu = tan α = 0,213
a["fy4-6-L2-02"] = (150 - 0.30 * 40 * g) / 40              # pallet pulled by a level rope: x: T − mu mg = ma → a = 0,807 m/s²
pts = [(5.0, 1.1), (10.0, 2.1), (15.0, 3.3), (20.0, 4.2), (25.0, 5.4)]   # graph: (N, F_mu) of the figure "mittaus"
a["fy4-6-L2-03"] = sum(n * f for n, f in pts) / sum(n * n for n, f in pts)   # slope of the line through the origin = 0,213
a["fy4-6-L2-04"] = 0.60 * 10 * g * math.cos(r(35))         # largest static friction mu0 mg cos α = 48,2 N (needed: mg sin α = 56,3 N, so it slides)
# Level 3: reasoning, two ideas
a["fy4-6-L3-01"] = 3.5 / g                                 # box on a truck bed: F_mu0 = ma ≤ mu0 mg → mu0 ≥ a/g = 0,357
aup = g * (math.sin(r(20)) + 0.25 * math.cos(r(20)))       # sliding up a 20° slope: both G_x and F_mu point down the slope, 5,66 m/s²
a["fy4-6-L3-02"] = 3.0 ** 2 / (2 * aup)                    # v² = v0² − 2as, v = 0 → s = v0²/(2a) = 0,795 m
a["fy4-6-L3-03"] = gK * (math.sin(r(30)) - 0.20 * math.cos(r(30)))   # Moon: a = g_Kuu(sin α − mu cos α) = 0,529 m/s²
print(json.dumps(a))
