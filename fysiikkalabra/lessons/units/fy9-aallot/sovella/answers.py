"""FY9 fy9-aallot, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-aallot` compares them with tasks.json."""
import json, math

g = 9.81
pi = math.pi


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


out = {}
S = "fy9-aallot"

# s1: the guitar string (example data); the string's tension is the same in a and b
L1, f1, v_air1 = 0.648, 110.0, 343.0
lam_str = 2 * L1                                   # m, the fundamental: L = lambda/2
v_str = f1 * lam_str                               # m/s
lam_air = v_air1 / f1                              # m, the same frequency in the air
fH = 123.5
L_H = v_str / (2 * fH)                             # m, the vibrating length for 123,5 Hz
f_beat = 6 / 4.0                                   # Hz
f_before = 110.0 - f_beat                          # tightening slowed the beats, so it was below 110 Hz
out.update({f"{S}-s1-a-v": round(v_str, 3), f"{S}-s1-a-lam": round(lam_air, 4), f"{S}-s1-lam-str": lam_str,
            f"{S}-s1-b-L": round(1000 * L_H, 2), f"{S}-s1-b-d": round(1000 * (L1 - L_H), 2),
            f"{S}-s1-fh": f_beat, f"{S}-s1-c": f_before, f"{S}-s1-d-f2": 2 * f1})

# s2: the bat (example data)
f0, v2, vb, t_echo = 30.0e3, 340.0, 6.0, 0.0120
lam2 = v2 / f0
d2 = v2 * t_echo / 2
moved = vb * t_echo                                # m the bat moves during the echo
f_wall = f0 * v2 / (v2 - vb)                       # the wall hears a moving source
f_echo = f_wall * (v2 + vb) / v2                   # the bat is a moving listener of the wall's echo
out.update({f"{S}-s2-a": round(1000 * lam2, 3), f"{S}-s2-b": round(d2, 4), f"{S}-s2-b-moved": round(moved, 4),
            f"{S}-s2-b-share": round(100 * moved / d2, 2), f"{S}-s2-c-wall": round(f_wall / 1000, 4),
            f"{S}-s2-c": round(f_echo / 1000, 4), f"{S}-s2-c-df": round(f_echo - f0, 1),
            f"{S}-s2-d-lam3k": round(v2 / 3000, 4)})

# s3: the pendulum (invented data: g 9,81 m/s^2, the true length 1,5 cm longer than measured, hand-timing noise)
L3 = [0.200, 0.350, 0.500, 0.650, 0.800, 0.950]                # m, to the top of the ball
T10 = [9.36, 12.07, 14.44, 16.29, 18.14, 19.76]                # s, ten swings
T3 = [t / 10 for t in T10]
T3sq = [t * t for t in T3]
k3, b3 = fit(L3, T3sq)                                         # s^2/m and s^2
# read in the solution from two far-apart points of the drawn line: (0,10 m; 0,46 s^2) and (0,90 m; 3,69 s^2)
k_read = (3.69 - 0.46) / (0.90 - 0.10)
b_read = 0.46 - k_read * 0.10
g_read = 4 * pi ** 2 / k_read
l2s = (2.00 ** 2 - b_read) / k_read
out.update({f"{S}-s3-T": [round(t, 3) for t in T3], f"{S}-s3-T2": [round(t, 4) for t in T3sq],
            f"{S}-s3-k-fit": round(k3, 4), f"{S}-s3-b-fit": round(b3, 4), f"{S}-s3-g-fit": round(4 * pi ** 2 / k3, 3),
            f"{S}-s3-k-read": round(k_read, 4), f"{S}-s3-b-read": round(b_read, 4),
            f"{S}-s3-c": round(g_read, 3), f"{S}-s3-c-diff": round(100 * (g_read - g) / g, 2),
            f"{S}-s3-d-xint": round(-b_read / k_read, 4), f"{S}-s3-d": round(l2s, 4),
            f"{S}-s3-d-fit": round((4 - b3) / k3, 4), f"{S}-s3-ratio": round(T3[3 * 0 + 4] / T3[0], 3)})

# s4: the festival (word task; the numbers its model answers quote)
L20 = 106.0
out.update({f"{S}-s4-40m": round(L20 - 10 * math.log10(4), 2), f"{S}-s4-400m": round(L20 - 10 * math.log10((400 / 20) ** 2), 2),
            f"{S}-s4-lam60": round(340 / 60, 3), f"{S}-s4-lam4k": round(340 / 4000, 4),
            f"{S}-s4-n": (100 - 85) / 3, f"{S}-s4-t-min": 8 * 60 / 2 ** ((100 - 85) / 3),
            f"{S}-s4-ratio15": round(10 ** 1.5, 2), f"{S}-s4-with": 100 - 20})

# s5: the echo report (invented data)
d5 = 85.0
t5 = [0.45, 0.52, 0.41, 0.55, 0.47]
tm = sum(t5) / len(t5)
dt5 = (max(t5) - min(t5)) / 2
v5 = 2 * d5 / tm
out.update({f"{S}-s5-a": round(v5, 2), f"{S}-s5-tmean": round(tm, 4), f"{S}-s5-dt": round(dt5, 3),
            f"{S}-s5-rel": round(100 * dt5 / tm, 1), f"{S}-s5-dv": round(v5 * dt5 / tm, 1),
            f"{S}-s5-vmin": round(2 * d5 / (tm + dt5), 1), f"{S}-s5-vmax": round(2 * d5 / (tm - dt5), 1),
            f"{S}-s5-v5C": 343 - 0.6 * (20 - 5), f"{S}-s5-diff": round(100 * (343 - 334) / 343, 2)})

# s6: the bungee jump (example data); the cross-module task with FY4 energy
m6, L6, k6 = 72.0, 18.0, 120.0
v6 = math.sqrt(2 * g * L6)
A, B, C = 0.5 * k6, -m6 * g, -m6 * g * L6                      # 1/2 k x^2 - m g x - m g L0 = 0
x6 = (-B + math.sqrt(B * B - 4 * A * C)) / (2 * A)
F6 = k6 * x6
a6 = F6 / m6 - g
T6 = 2 * pi * math.sqrt(m6 / k6)
out.update({f"{S}-s6-a": round(v6, 3), f"{S}-s6-mg": round(m6 * g, 2), f"{S}-s6-mgL": round(m6 * g * L6, 1),
            f"{S}-s6-x": round(x6, 3), f"{S}-s6-b": round(L6 + x6, 3), f"{S}-s6-F": round(F6, 1),
            f"{S}-s6-c": round(a6, 3), f"{S}-s6-c-g": round(a6 / g, 3), f"{S}-s6-F-per-mg": round(F6 / (m6 * g), 3),
            f"{S}-s6-x0": round(m6 * g / k6, 3), f"{S}-s6-d": round(T6, 4),
            f"{S}-s6-check": round(m6 * g * (L6 + x6) - 0.5 * k6 * x6 ** 2, 6)})

print(json.dumps(out))
