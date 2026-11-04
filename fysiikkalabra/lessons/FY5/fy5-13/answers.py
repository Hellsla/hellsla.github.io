"""Every answer in exercises.json for fy5-13, computed from the task data (python -I answers.py).
String fixed at both ends and pipe open at both ends: f_n = n v / (2L), λ_n = 2L/n; pipe closed at one end:
f_n = n v / (4L) with n = 1, 3, 5, …; neighbouring nodes λ/2 apart; v = f λ.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy5-13-L1-01"] = 86.1 / (2 * 1.05)                    # double bass E string: f1 = v/(2L) = 86,1 / 2,10 = 41,0 Hz
a["fy5-13-L1-02"] = 340 / (2 * 0.330)                    # pipe open at both ends: f1 = 340 / 0,660 = 515,15 Hz -> 515 Hz
a["fy5-13-L1-03"] = 340 / (4 * 2.60)                     # stopped organ pipe: f1 = v/(4L) = 340 / 10,4 = 32,69 Hz -> 32,7 Hz
a["fy5-13-L1-04"] = 2 * 0.35                             # rope, neighbouring nodes 0,35 m apart: λ = 2 · 0,35 m = 0,70 m
a["fy5-13-L1-05"] = 4 * 98.0                             # cello string f1 = 98,0 Hz: f4 = 4 f1 = 392 Hz
# Level 2: two steps, one conversion or one rearrangement
# L2-01 guitar string tightened: L = 0,650 m, v from 141 m/s to 148 m/s; Δf1 = Δv/(2L) = 7 / 1,30 = 5,38 Hz
a["fy5-13-L2-01"] = 148 / (2 * 0.650) - 141 / (2 * 0.650)
# L2-02 resonance tube: tuning fork 440 Hz, shortest resonating air column (closed at the water) 19,3 cm:
# λ = 4L = 0,772 m, v = f λ = 339,68 m/s -> 340 m/s
a["fy5-13-L2-02"] = 440 * 4 * 0.193
# L2-03 pipe open at both ends, third eigenfrequency 1530 Hz: L = 3 v/(2 f3) = 1020 / 3060 = 0,3333 m -> 33,3 cm
a["fy5-13-L2-03"] = 3 * 340 / (2 * 1530) * 100
# L2-04 figure fy5-13/kuvio-tehtava: string 1,20 m between the fixed ends, four loops, f = 100 Hz:
# λ = 2L/4 = 0,60 m, v = f λ = 60 m/s
a["fy5-13-L2-04"] = 100 * 2 * 1.20 / 4
# Level 3: reasoning or an unfamiliar context
a["fy5-13-L3-01"] = 262 / 2                              # open pipe f1 = v/(2L) = 262 Hz; stopped: v/(4L) = 131 Hz
a["fy5-13-L3-02"] = 440 - 330                            # successive eigenfrequencies of a string differ by f1: 110 Hz
# L3-03 closed pipe, successive resonances 510 Hz and 850 Hz: they differ by 2 f1 -> f1 = 170 Hz (510 = 3 f1, 850 = 5 f1),
# L = v/(4 f1) = 340 / 680 = 0,500 m
f1 = (850 - 510) / 2
a["fy5-13-L3-03"] = 340 / (4 * f1)
# Exercise-bank additions (L1-06, L1-07 and L2-07 are multiple choice with a text answer: no number here)
# L1-08 error analysis: student took λ = L; correct f1 = v/(2L) = 120 / 1,20 = 100 Hz
a["fy5-13-L1-08"] = 120 / (2 * 0.60)
# L2-05 data: f/n for each row, mean = f1, v = 2 L f1 (example data, L = 0,640 m)
f_n = [96.0, 191.0, 289.0, 383.0, 481.0]
f1_ka = sum(f / n for n, f in enumerate(f_n, start=1)) / len(f_n)   # 479,78 / 5 = 95,96 Hz
a["fy5-13-L2-05"] = round(2 * 0.640 * f1_ka)             # 122,8 m/s -> 123 m/s
# L2-06 resonance tube, 512 Hz: λ = L3 - L1 = 83,3 - 16,3 = 67,0 cm; v = f λ = 343,0 m/s -> 343 m/s
a["fy5-13-L2-06"] = round(512 * (83.3 - 16.3) / 100)
# L3-04 string tension data: f1^2/F is constant (mean 330,1 Hz^2/N); f1(120 N) = sqrt(k * 120) = 199,0 Hz
F = [20.0, 40.0, 60.0, 80.0]
f1 = [81.0, 115.5, 140.0, 163.0]
k = sum(f * f / t for f, t in zip(f1, F)) / len(F)
a["fy5-13-L3-04"] = round((k * 120) ** 0.5)              # 199 Hz
# L3-05 pipes A (open: f/n) and B (closed: f/n with n = 1, 3, 5), L = 0,800 m, example data
fa = sum(f / n for n, f in zip((1, 2, 3), (207, 413, 621))) / 3     # 206,83 Hz
fb = sum(f / n for n, f in zip((1, 3, 5), (103, 311, 517))) / 3     # 103,36 Hz
v_a = 2 * 0.800 * fa                                     # 330,9 m/s
v_b = 4 * 0.800 * fb                                     # 330,7 m/s
a["fy5-13-L3-05"] = round((v_a + v_b) / 2)               # 330,8 -> 331 m/s
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
