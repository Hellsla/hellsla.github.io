"""Every answer in exercises.json for fy4-6, computed from the task data (python -I answers.py).
Each solution starts from the force diagram: on a slope x points down the slope (or along the motion) and y away from
the surface; on level ground x along the motion and y up; g = 9,81 m/s² (on the Moon 1,62 m/s²).
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g, gK = 9.81, 1.62


def sf(x, n):
    """x rounded to n significant figures (the answer a student gets by rounding to the data's precision)."""
    return float(f"{x:.{n - 1}e}")


r = math.radians
a = {}
# Level 1: one equation from the diagram
a["fy4-6-L1-01"] = sf(160 * gK, 3)                                # weight on the Moon: G = m g_Kuu = 259,2 N
a["fy4-6-L1-02"] = sf(0.12 * 30 * g, 2)                           # sled on level snow: N = mg, F_mu = mu N = 35,3 N
a["fy4-6-L1-03"] = sf(120 / (40 * g), 2)                          # constant velocity: F − F_mu = 0, N = mg → mu = F/(mg) = 0,306
a["fy4-6-L1-04"] = sf(0.80 * g * math.cos(r(20)), 2)              # book on a 20° lid: y: N − mg cos α = 0 → N = 7,37 N
a["fy4-6-L1-05"] = sf(12 * g * math.sin(r(30)), 2)                # component along the slope: G_x = mg sin α = 58,9 N
# Level 2: two steps
a["fy4-6-L2-01"] = sf((g * math.sin(r(12)) - 3.0 / 4.0) / (g * math.cos(r(12))), 2)   # sled from rest, v = 3,0 m/s after 4,0 s (a = 0,75 m/s²): mu = (g sin α − a)/(g cos α) = 0,134
a["fy4-6-L2-02"] = sf((150 - 0.30 * 40 * g) / 40, 2)              # pallet pulled by a level rope: x: T − mu mg = ma → a = 0,807 m/s²
pts = [(5.0, 1.1), (10.0, 2.1), (15.0, 3.3), (20.0, 4.2), (25.0, 5.4)]   # graph: (N, F_mu) of the figure "mittaus"
a["fy4-6-L2-03"] = sf(sum(n * f for n, f in pts) / sum(n * n for n, f in pts), 2)   # slope of the line through the origin = 0,213
a["fy4-6-L2-04"] = sf(10 * g * math.sin(r(35)) - 0.60 * 10 * g * math.cos(r(35)), 2)   # G_x − mu0 mg cos α = 56,3 − 48,2 = 8,1 N > 0: it slides
# Level 3: reasoning, two ideas
a["fy4-6-L3-01"] = sf(3.5 / g, 2)                                 # box on a truck bed: F_mu0 = ma ≤ mu0 mg → mu0 ≥ a/g = 0,357
aup = g * (math.sin(r(20)) + 0.25 * math.cos(r(20)))       # sliding up a 20° slope: both G_x and F_mu point down the slope, 5,66 m/s²
a["fy4-6-L3-02"] = sf(3.0 ** 2 / (2 * aup), 2)                    # v² = v0² − 2as, v = 0 → s = v0²/(2a) = 0,795 m
muE = math.tan(r(30)) - 2.0 / (g * math.cos(r(30)))      # friction coefficient implied by a = 2,0 m/s² on Earth (0,342)
a["fy4-6-L3-03"] = sf(gK * (math.sin(r(30)) - muE * math.cos(r(30))), 2)   # Moon: a = 2,0·g_Kuu/g = 0,33 m/s²
print(json.dumps(a))
