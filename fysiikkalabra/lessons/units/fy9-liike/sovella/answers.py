"""FY9 fy9-liike, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-liike` compares them with tasks.json."""
import json, math

g = 9.81
KMH = 1000 / 3600                     # m/s per km/h, by substitution: 1 km/h = 1000 m : 3600 s


def fit(x, y):
    """Least-squares line y = kx + b."""
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def fit2(x, y):
    """Least-squares parabola y = A x^2 + B x + C (normal equations, Cramer's rule)."""
    S = lambda p: sum(a ** p for a in x)
    T = lambda p: sum(b * a ** p for a, b in zip(x, y))
    M = [[S(4), S(3), S(2)], [S(3), S(2), S(1)], [S(2), S(1), len(x)]]
    r = [T(2), T(1), T(0)]
    det = lambda m: (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                     + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    D = det(M)
    col = lambda j: [[r[i] if c == j else M[i][c] for c in range(3)] for i in range(3)]
    return tuple(det(col(j)) / D for j in range(3))


out = {}

# s1: the motorway on-ramp (example data). Origin at the start of the ramp, positive in the driving direction.
L, v0, v1, vt, d0 = 270.0, 54 * KMH, 108 * KMH, 81 * KMH, -40.0      # m, m/s (15, 30, 22,5), truck 40 m behind
t1 = 2 * L / (v0 + v1)                 # s: the area of the (t,v) trapezoid, mean speed (v0 + v) / 2
a1 = (v1 - v0) / t1                    # m/s^2
t_eq = (vt - v0) / a1                  # s: equal speeds, the smallest gap
xA = lambda t: v0 * t + 0.5 * a1 * t ** 2
xB = lambda t: d0 + vt * t
gap = xA(t_eq) - xB(t_eq)
disc = (v0 - vt) ** 2 - 4 * 0.5 * a1 * (-d0)   # discriminant of 1/2 a t^2 + (v0 - vt) t - d0 = 0: negative, no meeting
# d: a driver who accelerates only to 72 km/h on the same ramp
v1d = 72 * KMH
t1d = 2 * L / (v0 + v1d)
xB_end_d = xB(t1d)
out.update({"fy9-liike-s1-a": round(t1, 3), "fy9-liike-s1-b": round(a1, 4), "fy9-liike-s1-c": round(gap, 2),
            "fy9-liike-s1-teq": round(t_eq, 2), "fy9-liike-s1-xA-teq": round(xA(t_eq), 2), "fy9-liike-s1-xB-teq": round(xB(t_eq), 2),
            "fy9-liike-s1-disc": round(disc, 2), "fy9-liike-s1-xB-end": round(xB(t1), 1), "fy9-liike-s1-gap-end": round(L - xB(t1), 1),
            "fy9-liike-s1-d-t": round(t1d, 2), "fy9-liike-s1-d-truck": round(xB_end_d, 1)})

# s2: two balls in the school atrium (example data). y up from the floor, air resistance neglected.
yA0, vA0, yB0 = 1.5, 12.0, 9.0
t_top = vA0 / g
h_top = yA0 + vA0 * t_top - 0.5 * g * t_top ** 2
t_m = (yB0 - yA0) / vA0                # s: both accelerate equally, so the gap shrinks at the constant 12,0 m/s
y_m = yA0 + vA0 * t_m - 0.5 * g * t_m ** 2
yB_check = yB0 - 0.5 * g * t_m ** 2
vA, vB = vA0 - g * t_m, -g * t_m
t_floor_B = math.sqrt(2 * yB0 / g)
out.update({"fy9-liike-s2-a": round(h_top, 3), "fy9-liike-s2-ttop": round(t_top, 4), "fy9-liike-s2-rise": round(h_top - yA0, 3),
            "fy9-liike-s2-b-t": round(t_m, 4), "fy9-liike-s2-b-y": round(y_m, 3), "fy9-liike-s2-yB": round(yB_check, 3),
            "fy9-liike-s2-fallB": round(0.5 * g * t_m ** 2, 3),
            "fy9-liike-s2-d-vA": round(vA, 3), "fy9-liike-s2-d-vB": round(vB, 3), "fy9-liike-s2-tfloorB": round(t_floor_B, 3)})

# s3: a commuter train arrives at a station; GPS speed every 4 s (invented data: 90 km/h until 10 s, then
# 0,65 m/s^2 of braking, rounded to whole km/h with +-1 km/h of noise; figures.py draws the same points)
T3 = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
V3 = [91, 89, 90, 84, 77, 67, 56, 49, 39, 28, 21]       # km/h
const = sum(V3[:3]) / 3                                  # km/h, the level of the three first points
k3, b3 = fit(T3[3:], V3[3:])                             # km/h per s and km/h
t_start = (const - b3) / k3                              # s: where the braking line meets the 90 km/h level
t_stop = -b3 / k3                                        # s: where it meets the time axis
# the slope as read in the solution from two far-apart points of the drawn line: (12 s; 85 km/h) and (40 s; 20 km/h)
k_read = (20 - 85) / (40 - 12)
a_read = k_read * KMH
d_area = 0.5 * (const * KMH) * (t_stop - t_start)        # m: the triangle under the braking line
d_read = 0.5 * (90 * KMH) * (48.5 - 10)                  # m: the same with read-off values 10 s and 48,5 s
out.update({"fy9-liike-s3-k": round(k3, 4), "fy9-liike-s3-b0": round(b3, 2), "fy9-liike-s3-kread": round(k_read, 4),
            "fy9-liike-s3-b": round(a_read, 4), "fy9-liike-s3-afit": round(k3 * KMH, 4), "fy9-liike-s3-tstart": round(t_start, 2),
            "fy9-liike-s3-tstop": round(t_stop, 2), "fy9-liike-s3-c": round(d_read, 1), "fy9-liike-s3-cfit": round(d_area, 1),
            "fy9-liike-s3-v90": 90 * KMH, "fy9-liike-s3-line12": round(b3 + k3 * 12, 2), "fy9-liike-s3-line40": round(b3 + k3 * 40, 2)})

# s4: average-speed enforcement over a 3,0 km section, limit 80 km/h (word task; the numbers its model answers quote)
t_a, t_b = 2.0 / 100, 1.0 / 60                           # h
v_mean = 3.0 / (t_a + t_b)                               # km/h
t_limit = 3000 / (80 * KMH)                              # s at exactly 80 km/h
dv_long = 80 * 1.0 / t_limit                             # km/h for 1 s of timing uncertainty (two readings of 0,5 s)
t_short = 100 / (80 * KMH)
dv_short = 80 * 1.0 / t_short
out.update({"fy9-liike-s4-b": round(v_mean, 2), "fy9-liike-s4-ta": t_a * 3600, "fy9-liike-s4-tb": t_b * 3600,
            "fy9-liike-s4-tlim": round(t_limit, 1), "fy9-liike-s4-dvlong": round(dv_long, 2), "fy9-liike-s4-tshort": round(t_short, 2),
            "fy9-liike-s4-dvshort": round(dv_short, 1)})

# s5: the cart on a ramp, a report (example data)
s5, t5, dt5 = 1.20, 1.6, 0.2
a5 = 2 * s5 / t5 ** 2
a5_lo, a5_hi = 2 * s5 / (t5 + dt5) ** 2, 2 * s5 / (t5 - dt5) ** 2
out.update({"fy9-liike-s5-a": round(a5, 4), "fy9-liike-s5-lo": round(a5_lo, 3), "fy9-liike-s5-hi": round(a5_hi, 3),
            "fy9-liike-s5-rel": round(2 * dt5 / t5, 3)})

# s6: a ball dropped in front of a phone camera, video analysis (example data: drawn with an apparent g of
# 9,81 * 3,00 / 3,30 because the scale tape was 0,30 m nearer the camera than the ball, plus +-4 mm of noise)
T6 = [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
Y6 = [1.653, 1.635, 1.607, 1.554, 1.469, 1.371, 1.253, 1.100, 0.939, 0.745, 0.538]
A6, B6, C6 = fit2(T6, Y6)
A_given, dA_given = -4.44, 0.05                          # the spreadsheet's result as the task gives it
g_meas = 2 * -A_given
dg = 2 * dA_given
corr = 3.30 / 3.00
g_corr, dg_corr = g_meas * corr, dg * corr
g_last = 2 * (Y6[0] - Y6[-1]) / T6[-1] ** 2              # from the first and last point only
out.update({"fy9-liike-s6-A": round(A6, 3), "fy9-liike-s6-B": round(B6, 4), "fy9-liike-s6-C": round(C6, 3),
            "fy9-liike-s6-a": round(g_meas, 3), "fy9-liike-s6-b": round(dg, 3), "fy9-liike-s6-rel": round(dg / g_meas, 4),
            "fy9-liike-s6-diff": round(9.81 - g_meas, 3), "fy9-liike-s6-c": round(g_corr, 3), "fy9-liike-s6-dgc": round(dg_corr, 3),
            "fy9-liike-s6-last": round(g_last, 3)})

print(json.dumps(out))
