"""Every answer in exercises.json for fy4-14, computed from the task data (python -I answers.py).
Each solution starts from the force diagram: the positive direction is the motion's (down for a falling body, up for a
rising one) or the slope's; g = 9,81 m/s². The air resistance F_v is given in each task (the chapter treats it
qualitatively). Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

g = 9.81
a = {}
# Level 1: one formula, values given
a["fy4-14-L1-01"] = 75.0 * g                        # jumper at terminal velocity: G − F_v = 0 → F_v = mg = 735,75 N
a["fy4-14-L1-02"] = 2.00 * g - 5.00                 # falling stone, positive down: ΣF = mg − F_v = 19,62 − 5,00 = 14,62 N
a["fy4-14-L1-03"] = abs(0.600 * g - 8.00) / 0.600   # ball thrown down fast: a = (mg − F_v)/m = (5,886 − 8,00)/0,600 = −3,523 m/s²: 3,52 m/s² up
a["fy4-14-L1-04"] = 0.450 * g + 1.20                # rising ball, positive up: ΣF = −mg − F_v, |ΣF| = 4,4145 + 1,20 = 5,6145 N
a["fy4-14-L1-05"] = 18 + 6.0                        # cyclist at constant velocity: F − F_v − F_r = 0 → F = 24 N
a["fy4-14-L1-08"] = 1500 - 60.0 * g                 # error analysis: parachute opening, positive down: ΣF = mg − F_v = 588,6 − 1500 = −911,4 N, magnitude 911,4 N up
# Level 2: two steps, a conversion or a rearrangement
a["fy4-14-L2-01"] = 5.10e-3 * g                     # shuttlecock 5,10 g = 5,10·10⁻³ kg at terminal velocity: F_v = mg = 0,05003 N
a["fy4-14-L2-02"] = 70.0 * (g - 6.00)               # mg − F_v = ma → F_v = m(g − a) = 70,0 · 3,81 = 266,7 N
a["fy4-14-L2-03"] = g + 0.250 / 57.0e-3             # rising tennis ball: −mg − F_v = ma → |a| = g + F_v/m = 14,196 m/s²
a["fy4-14-L2-04"] = (450 + 180) / 1200              # car coasting: −F_v − F_r = ma → |a| = 630 N : 1200 kg = 0,525 m/s²
a_t = (5.15 - 3.35) / (0.80 - 0.40)                 # foam ball, table at 0,40 s and 0,80 s: a = 1,80/0,40 = 4,50 m/s²
a["fy4-14-L2-05"] = 20.0e-3 * (g - a_t)             # mg − F_v = ma → F_v = m(g − a) = 0,0200 · 5,31 = 0,1062 N
a["fy4-14-L2-06"] = 4.8e-3 * g                      # paper cone 4, 4,8 g = 4,8·10⁻³ kg at terminal velocity: F_v = mg = 0,04709 N (b: 4,8 : 1,2 = 4,0; speeds 1,49 : 0,72 = 2,07)
# Level 3: reasoning, two ideas, an unfamiliar context
a["fy4-14-L3-01"] = (72.0 * g - 72.0 * g / 2) / 72.0   # F_v halves from mg to mg/2: a = (mg − mg/2)/m = g/2 = 4,905 m/s²
a["fy4-14-L3-02"] = (g + 0.600 / 0.200) - (g - 0.600 / 0.200)   # rising |a| = g + F_v/m = 12,81, falling g − F_v/m = 6,81: 6,00 m/s²
at = (15.0 - 2.0) / (2.0 - 0.0)                     # the tangent through (0 s; 2,0 m/s) and (2,0 s; 15,0 m/s): a = 6,5 m/s²
a["fy4-14-L3-03"] = 0.150 * (g - at)                # mg − F_v = ma → F_v = m(g − a) = 0,150 · 3,31 = 0,4965 N
a_j = (15.5 - 33.0) / (1.5 - 0.5)                   # jumper table at 0,5 s and 1,5 s, positive down: a = −17,5 m/s² (up)
a["fy4-14-L3-04"] = 82.0 * (g - a_j)                # mg − F_v = ma → F_v = m(g − a) = 82,0 · 27,31 = 2239,4 N (2,78 · mg; terminal: mg = 804,4 N)
a["fy4-14-L3-05"] = (2 * g * 1500) ** 0.5           # raindrop without air resistance: v² = 2gh → v = √(2 · 9,81 · 1500) = 171,55 m/s (a: F_v = mg = 1,373·10⁻⁴ N)
print(json.dumps(a))
