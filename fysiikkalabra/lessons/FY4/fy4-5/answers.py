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
print(json.dumps(a))
