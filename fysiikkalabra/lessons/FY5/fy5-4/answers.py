"""Every answer in exercises.json for fy5-4, computed from the task data (python -I answers.py).
Uniform circular motion: a_n = v²/r towards the centre, v = 2πr/T, f = 1/T; Newton's second law towards the centre
ΣF = m v²/r. Each force solution starts from the force diagram: x (or n) towards the centre, y up; g = 9,81 m/s².
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}
# Level 1: one formula
a["fy5-4-L1-01"] = 20.0 ** 2 / 80                         # car on a ramp curve: a_n = v²/r = 5,0 m/s²
a["fy5-4-L1-02"] = 8.00 ** 2 / 36.5                       # runner in the bend: a_n = 1,753 m/s²
a["fy5-4-L1-03"] = 0.50 * 4.0 ** 2 / 1.2                  # stone on a string: ΣF = m v²/r = 6,667 N
L1_03_rope = math.hypot(a["fy5-4-L1-03"], 0.50 * g)      # (reasonableness) the rope also holds the weight: sqrt(6,667² + 4,905²) = 8,28 N
a["fy5-4-L1-04"] = math.sqrt(2.5 * 25)                    # roundabout: v = sqrt(a_n r) = 7,906 m/s
a["fy5-4-L1-05"] = 15.0 ** 2 / 0.25                       # washing-machine drum: a_n = 900 m/s²
# Level 2: two steps or a conversion
a["fy5-4-L2-01"] = 80 * (g + 8.0 ** 2 / 16) / 1000       # cyclist in an underpass dip: N − G = m v²/r → N = m(g + v²/r) = 1,105 kN
v22 = 2 * math.pi * 3.0 / 5.0                             # carousel: v = 2πr/T = 3,770 m/s
a["fy5-4-L2-02"] = v22 ** 2 / 3.0                         # a_n = v²/r = 4,737 m/s²
a["fy5-4-L2-03"] = 1200 * (g - 12.0 ** 2 / 30) / 1000     # top of a bump: G − N = m v²/r → N = m(g − v²/r) = 6,012 kN
v24 = 2 * math.pi * 1.8 / 0.50                            # hammer: v = 2πr/T = 22,62 m/s
a["fy5-4-L2-04"] = 7.26 * v24 ** 2 / 1.8 / 1000           # ΣF = m v²/r = 2,064 kN
# Level 3: reasoning, two ideas
a["fy5-4-L3-01"] = math.sqrt(0.10 * g * 60) * 3.6         # icy curve: mu0 m g = m v²/r → v = sqrt(mu0 g r) = 7,672 m/s = 27,62 km/h
v32 = math.sqrt(25 * 0.80 / 0.40)                         # cord's limit: T = m v²/r (T the tension) → v = sqrt(T r / m) = 7,071 m/s
a["fy5-4-L3-02"] = v32 / (2 * math.pi * 0.80)             # v = 2πr f → f = v/(2πr) = 1,407 Hz
a["fy5-4-L3-03"] = (80 / 3.6) ** 2 / (0.25 * g)           # road design: m v²/r ≤ 0,25 mg → r ≥ v²/(0,25 g) = 201,4 m
print(json.dumps(a))
