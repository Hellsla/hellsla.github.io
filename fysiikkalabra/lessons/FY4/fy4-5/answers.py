"""Every answer in exercises.json for fy4-5, computed from the task data (python -I answers.py).
Each solution starts from the force diagram: x along the motion (or horizontal), y up; g = 9,81 m/s².
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
r = math.radians
a = {}
# Level 1: one equation from the diagram
a["fy4-5-L1-01"] = 1.5 * g                           # lamp at rest: T − mg = 0 → T = 14,7 N
a["fy4-5-L1-02"] = math.hypot(40 - 25, 30 - 30)      # grid: ΣF_x = 40 N − 25 N = 15 N, ΣF_y = 30 N − 30 N = 0 → 15 N
a["fy4-5-L1-03"] = 0.50 * g                          # book held against a wall: y: F_μ − mg = 0 → F_μ = 4,9 N (x: N = 20 N)
a["fy4-5-L1-04"] = 65 * g                            # lift at constant velocity: N − mg = 0 → N = 637,7 N
a["fy4-5-L1-05"] = 250 * math.cos(r(40))            # horizontal component F_x = F cos α = 191,5 N
# Level 2: the diagram, components or acceleration
a["fy4-5-L2-01"] = 60 * math.cos(r(30))             # sled at constant velocity: T cos 30° − F_μ = 0 → F_μ = 52,0 N
a["fy4-5-L2-02"] = 60 * (g + 1.2)                    # lift accelerating up: N − mg = ma → N = m(g + a) = 660,6 N
a["fy4-5-L2-03"] = (120 * math.cos(r(30)) - 80) / 40  # push down at 30°: F cos α − F_μ = ma → a = 0,598 m/s²
a["fy4-5-L2-04"] = math.hypot(30, 40) / 50           # two perpendicular pulls on ice: ΣF = √(30² + 40²) N = 50 N → a = 1,0 m/s²
# Level 3: drawing alone and reasoning
a["fy4-5-L3-01"] = 70 * (g - 1.5)                    # lift moving up, slowing 1,5 m/s²: N − mg = −ma → N = m(g − a) = 581,7 N
a["fy4-5-L3-02"] = 19 * (2.0 - 0) / 20               # curling stone: |a| = Δv/Δt = 0,10 m/s², only friction horizontal → F_μ = 1,9 N
a["fy4-5-L3-03"] = 0.10 - 0.0040 * g                 # helium balloon at the ceiling: F_noste − mg − N = 0 → N = 0,061 N
# Exercise bank additions: L1-06 and L1-08 are multiple choice (no number)
a["fy4-5-L1-07"] = 120 + 85 - 150                    # cabinet: ΣF_x = F_1 + F_2 − F_μ = 55 N
a["fy4-5-L2-05"] = round(sum(math.degrees(math.atan(c / f)) for f, c in [(3.0, 2.5), (4.5, 3.8), (6.0, 5.1)]) / 3, 1)   # ring at rest: tan α = F_C/F_A → α_ka = 40,1°
a["fy4-5-L2-06"] = 30 / 12                           # sliding crate, only friction horizontal: a = F_μ/m = 2,5 m/s² (opposite to the motion)
a["fy4-5-L2-07"] = math.hypot(6.0 + 8.0 * math.cos(r(60)), 8.0 * math.sin(r(60)))   # ΣF_x = 10,0 N, ΣF_y = 6,93 N → ΣF = 12,2 N
a["fy4-5-L3-04"] = 120 * math.cos(r(30)) - 25 * (4.01 - 0) / 5.0   # a = Δv/Δt = 0,802 m/s²; x: T cos α − F_μ = ma → F_μ = 83,9 N
_a1 = ((881 + 878 + 883) / 3 - 80 * g) / 80          # crane load: phase 1 a_1 = (T − mg)/m = 1,198 m/s²
a["fy4-5-L3-05"] = 0.5 * _a1 * 2.0**2 + _a1 * 2.0 * 4.0 + 0.5 * _a1 * 2.0 * 2.0   # h = h_1 + h_2 + h_3 = 14,38 m
# Exercise bank: L2-08 reads two oblique forces off a 2,0 N grid (fy4-5/ruutu-vinot): F_1 = (5, 6) squares, F_2 = (-2, -2) squares
_sq = 2.0
a["fy4-5-L2-08"] = math.hypot((5 - 2) * _sq, (6 - 2) * _sq) / 2.5   # ΣF_x = 6,0 N, ΣF_y = 8,0 N, ΣF = 10 N → a = ΣF/m = 4,0 m/s²
print(json.dumps(a))
