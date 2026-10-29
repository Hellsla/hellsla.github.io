"""Numbers of the lesson text and inquiry.json for fy4-2, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Uniformly accelerated motion on a line: a = Δv/Δt, v = v₀ + a t,
x = x₀ + v₀ t + ½ a t². Prints {id: number} as JSON on the last line."""
import json, math

g = 9.81
a = {}
# Hook: a stone dropped from a bridge, fall distance s = ½ g t²
a["hook-s05"] = 0.5 * g * 0.5 ** 2                       # first half second: 1,23 m
a["hook-s10-s05"] = 0.5 * g * 1.0 ** 2 - a["hook-s05"]   # second half second: 4,91 m − 1,23 m = 3,68 m
# Retrieval: slope of a (t,x) line through (0 s; 2,0 m) and (4,0 s; 14 m)
a["pr-v"] = (14 - 2.0) / (4.0 - 0)                       # 3,0 m/s
# Experiment 1 (sim, v0 = 0, a = 2,0 m/s²): x(t) = ½ a t²
x1 = lambda t: 0.5 * 2.0 * t ** 2
a["exp1-x1"], a["exp1-x2"], a["exp1-x3"] = x1(1), x1(2), x1(3)          # 1,0 m, 4,0 m, 9,0 m
a["exp1-third-second"] = x1(3) - x1(2)                    # 5,0 m (1 : 3 : 5)
a["exp1-mistake-x3"] = x1(3)                              # mistake: position, not the distance in the 3rd second
# Experiment 2 (sim, v0 = 6,0 m/s, a = −2,0 m/s²)
v2 = lambda t: 6.0 - 2.0 * t
x2 = lambda t: 6.0 * t - 0.5 * 2.0 * t ** 2
a["exp2-v2"], a["exp2-v3"], a["exp2-v4"] = v2(2), v2(3), v2(4)          # 2,0; 0; −2,0 m/s
a["exp2-x3"] = x2(3)                                       # turning point 9,0 m
a["exp2-x6"] = x2(6)                                       # back at 0 m at 6 s
# Free-fall data (example data, video analysis): least-squares s = A t² + B t + C, g = 2A
t_d = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
s_d = [0.002, 0.018, 0.065, 0.128, 0.223, 0.338, 0.477, 0.646, 0.832]
n = len(t_d)
S = lambda k: sum(t ** k for t in t_d); Sy = lambda k: sum(t ** k * s for t, s in zip(t_d, s_d))
M = [[S(4), S(3), S(2)], [S(3), S(2), S(1)], [S(2), S(1), n]]; r = [Sy(2), Sy(1), Sy(0)]
def det(m): return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                    + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
D = det(M); col = lambda j: [[r[i] if k == j else M[i][k] for k in range(3)] for i in range(3)]
A, B, C = (det(col(j)) / D for j in range(3))
a["data-A"], a["data-B"], a["data-C"] = A, B, C          # 4,88 m/s², 0,126 m/s, 0,0013 m
a["data-g"] = 2 * A                                        # 9,77 m/s²
a["data-g-lastpoint"] = 2 * s_d[-1] / t_d[-1] ** 2         # mistake: one point only, 2 s / t² = 10,4 m/s²
# Worked example: cyclist downhill, v0 = 4,0 m/s, a = 0,50 m/s², Δx = 60 m
v0, acc, dx = 4.0, 0.50, 60
t_ex = (-v0 + math.sqrt(v0 ** 2 + 2 * acc * dx)) / acc
a["ex-disc"] = v0 ** 2 + 2 * acc * dx                      # 76 m²/s²
a["ex-sqrt"] = math.sqrt(a["ex-disc"])                     # 8,72 m/s
a["ex-t"] = t_ex                                           # 9,44 s
a["ex-t-neg"] = (-v0 - math.sqrt(v0 ** 2 + 2 * acc * dx)) / acc     # −25,4 s (rejected)
a["ex-v"] = v0 + acc * t_ex                                # 8,72 m/s
a["ex-check"] = (v0 + a["ex-v"]) / 2 * t_ex                # mean velocity · t = 60 m
# Error spotting: car from rest, a = 3,0 m/s², t = 4,0 s
a["virhe-wrong"] = (3.0 * 4.0) * 4.0                       # 48 m (final velocity used as if constant)
a["virhe-right"] = 0.5 * 3.0 * 4.0 ** 2                    # 24 m
# Transfer: plane needs 75 m/s on a 1500 m runway: t = v/a, Δx = ½ a t² = v²/(2a) -> a = v²/(2Δx)
a["siirto"] = 75 ** 2 / (2 * 1500)                         # 1,875 -> 1,9 m/s²
a["siirto-noHalf"] = 75 ** 2 / 1500                        # mistake 3,75
a["siirto-v-over-x"] = 75 / 1500                           # mistake 0,05
a["siirto-t"] = 75 / a["siirto"]                           # 40 s
# Check 2: scooter (t,v) line from 2,0 m/s to 6,0 m/s in 8,0 s: area = displacement
a["check2"] = (2.0 + 6.0) / 2 * 8.0                        # 32 m
a["check2-rect"] = 6.0 * 8.0                               # mistake 48 m (v_end · t)
a["check2-a"] = (6.0 - 2.0) / 8.0                          # 0,50 m/s² (the slope, a mistake when Δx is asked)
# Check 3 model answer: stone, first and second second of the fall
a["check3-s1"] = 0.5 * g * 1 ** 2                          # 4,91 m
a["check3-s2"] = 0.5 * g * 2 ** 2 - a["check3-s1"]         # 14,7 m
a["check3-v1"], a["check3-v2"] = g * 1, g * 2              # 9,81 and 19,6 m/s
print(json.dumps(a))
