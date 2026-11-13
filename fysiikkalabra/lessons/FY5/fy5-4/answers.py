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
# Exercise bank additions (teacher 2026-11-04): L1-06 and L1-07 are multiple choice (no number)
a["fy5-4-L1-08"] = (3 ** 2) * 1.0                                                       # a_n ∝ v²: tripled speed gives 9 · 1,0 m/s² = 9,0 m/s² (≈ 0,92 g)
a["fy5-4-L2-05"] = 1.53 / 49.0 * 0.80 * 1000                                             # fitted line through the origin and (49 m²/s², 1,53 N): k = m/r = 0,03122 kg/m, m = k r = 24,98 g
mus = [v ** 2 / (g * r) for r, v in [(20, 10.4), (30, 12.6), (40, 14.8), (50, 16.3)]]    # wet track: mu0 = v²/(g r) per row: 0,551, 0,539, 0,558, 0,542
a["fy5-4-L2-06"] = sum(mus) / len(mus)                                                   # sum 2,191, mean 0,5477
a["fy5-4-L2-07"] = 850 * 18.0 ** 2 / 75 / 1000                                           # friction alone is the net force: F = m v²/r = 3672 N = 3,672 kN (the student's 7344 N double counts a "centrifugal" force)
r_bottom = 27.2 ** 2 / 53.2                                                              # loop: r = v²/a_n = 13,91 m at the bottom (energy-consistent: v_bottom² − v_top² = 543,8 ≈ 4 g r)
r_top = 14.0 ** 2 / 14.1                                                                 # r = 13,90 m at the top
r_loop = (r_bottom + r_top) / 2                                                          # mean 13,90 m
a["fy5-4-L3-04"] = 60.0 * (14.1 - g)                                                     # top: N + mg = m a_n → N = m(a_n − g) = 257,4 N (bottom: m(g + a_n) = 3780,6 N = 6,42 mg; v_min = sqrt(g r) = 11,68 m/s < 14,0 m/s)
L3_04_bottom = 60.0 * (g + 53.2)                                                         # (Vastaus) bottom 3780,6 N
L3_04_vmin = math.sqrt(g * r_loop)                                                       # (c) 11,68 m/s
tan_al = math.tan(math.radians(8.0))                                                     # banked curve, alpha = 8,0°, r = 130 m, mu0 = 0,40
L3_05_v0 = math.sqrt(g * 130 * tan_al) * 3.6                                             # no friction: tan α = v²/(g r) → 13,39 m/s = 48,2 km/h
a["fy5-4-L3-05"] = math.sqrt(g * 130 * (tan_al + 0.40) / (1 - 0.40 * tan_al)) * 3.6     # with friction down the slope: v² = g r (tan α + μ0)/(1 − μ0 tan α) → 27,03 m/s = 97,3 km/h
L3_05_flat = math.sqrt(0.40 * g * 130) * 3.6                                             # flat curve for comparison: 81,3 km/h
# Figure tasks (teacher 2026-11-13): values read from the figures' marked points
a["fy5-4-L2-09"] = 20.0 ** 2 / 5.0                                                       # fig kuvaaja-a: point (20 m/s, 5,0 m/s²): r = v²/a_n = 80 m
a["fy5-4-L3-06"] = 8.0e3 / (1200 * g)                                                    # fig kuvaaja-b: point (20 m/s, 8,0 kN): N = mg, mu0 = F/(mg) = 0,6796
print(json.dumps(a))
