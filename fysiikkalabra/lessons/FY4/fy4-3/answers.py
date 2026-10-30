"""Every answer in exercises.json for fy4-3, computed from the task data (python -I answers.py).
First law: at rest or at constant velocity the forces on a body sum to zero. Third law: the force of A on B and the
force of B on A are equal in size and opposite. g = 9,81 m/s². Prints {id: number} as JSON on the last line."""
import json

g = 9.81
a = {}
# Level 1: one law, values given
a["fy4-3-L1-01"] = 18.0                      # lamp at rest: T − G = 0 → T = G = 18 N
a["fy4-3-L1-02"] = 850.0                     # rope at rest: F_B − F_A = 0 → F_B = 850 N
a["fy4-3-L1-03"] = 90.0                      # third law: wall on skater = skater on wall = 90 N
a["fy4-3-L1-04"] = 620.0 - 380.0             # car at constant velocity: F − F_ilma − F_vieri = 0 → F_vieri = 240 N
a["fy4-3-L1-05"] = 0.65 * g                  # third law: book on Earth = Earth on book = mg = 6,38 N
# Level 2: two steps or a conversion
a["fy4-3-L2-01"] = 8.0 + 5.0                 # upper book presses lower with 5,0 N (I + III); lower: N = 8,0 N + 5,0 N; III → 13 N on the table
a["fy4-3-L2-02"] = 65.0                      # water pushes the swimmer forward 65 N (III); constant velocity → resistance 65 N (I)
a["fy4-3-L2-03"] = 85 * g                    # parachutist at constant velocity: F_v − mg = 0 → F_v = 833,9 N
a["fy4-3-L2-04"] = (5800 + 320 * g) / 1000   # lift at constant velocity: T = G_kori + m g = 5800 N + 3139 N = 8,94 kN
# Level 3: reasoning with both laws
a["fy4-3-L3-01"] = 4.62 - 4.35              # balloon sinking at constant velocity: F_noste + F_v − G = 0 → F_v = 0,27 kN (up)
a["fy4-3-L3-02"] = 0.30 + 0.30              # upper magnet floats: magnet force 0,30 N; III: it pushes the lower one down 0,30 N; base: 0,60 N
a["fy4-3-L3-03"] = 1.5 + 0.40               # lower scale at rest: upper hook pulls 1,5 N + 0,40 N; III: the upper scale reads 1,9 N
print(json.dumps(a))
