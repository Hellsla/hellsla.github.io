"""FY9 fy9-magnetismi-valo, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-magnetismi-valo` compares them with tasks.json.
The unit's own numbers (the hook, the inquiry tasks) are at the end under "inq-"."""
import json, math

g = 9.81
pi = math.pi
c = 3.00e8
mu0 = 4 * pi * 1e-7
e = 1.602e-19
m_p = 1.673e-27


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


out = {}
S = "fy9-magnetismi-valo"

# s1: the small hydro plant (example data): one-coil generator model, ideal transformer, line resistance
N1g, B1, A1, f1 = 60, 0.50, 0.060, 50.0
e0 = N1g * B1 * A1 * 2 * pi * f1                  # V, the peak value
U_gen = e0 / math.sqrt(2)                          # V, the effective value
P1 = 150e3                                         # W
U_lo, U_hi = 400.0, 20.0e3                         # V, the generator side and the line
ratio = U_hi / U_lo                                # N2 : N1
I_lo, I_hi = P1 / U_lo, P1 / U_hi                  # A
R1 = 6.0                                           # ohm, the line
Ph_hi = R1 * I_hi ** 2
Ph_lo = R1 * I_lo ** 2                             # if the same power were sent at 400 V
out.update({f"{S}-s1-a-e0": round(e0, 1), f"{S}-s1-a-U": round(U_gen, 1),
            f"{S}-s1-b-ratio": ratio, f"{S}-s1-b-I1": round(I_lo, 2), f"{S}-s1-b-I2": round(I_hi, 3),
            f"{S}-s1-c-P": round(Ph_hi, 1), f"{S}-s1-c": round(100 * Ph_hi / P1, 3),
            f"{S}-s1-c-Plo": round(Ph_lo, 0), f"{S}-s1-c-factor": round(Ph_lo / Ph_hi, 1)})

# s2: the fibre link to the island (example data; typical single-mode values)
n_core, n_clad = 1.470, 1.455
L2 = 14.0e3                                        # m
a2, splices, a_splice, P0 = 0.22, 4, 0.10, 2.0     # dB/km, count, dB each, mW
sin_r = n_clad / n_core
ar = math.degrees(math.asin(sin_r))
t_axis = n_core * L2 / c
t_steep = t_axis / sin_r                           # the steepest guided ray: path longer by 1/sin(alpha_r)
A_tot = a2 * L2 / 1000 + splices * a_splice
P_end = P0 * 10 ** (-A_tot / 10)
out.update({f"{S}-s2-a-ar": round(ar, 2), f"{S}-s2-a-sin": round(sin_r, 5), f"{S}-s2-a-axis": round(90 - ar, 2),
            f"{S}-s2-b-t": round(t_axis * 1e6, 2), f"{S}-s2-b-steep": round(t_steep * 1e6, 2),
            f"{S}-s2-b-diff": round((t_steep - t_axis) * 1e6, 3), f"{S}-s2-b-v": round(c / n_core, -5),
            f"{S}-s2-c-A": round(A_tot, 2), f"{S}-s2-c": round(P_end, 3), f"{S}-s2-c-share": round(100 * P_end / P0, 1)})

# s3: the field of a long straight wire (invented data: mu0 I/(2 pi) = 2,40 uT m with I = 12,0 A, a background of
# about 11 uT along the sensor's axis, and reading noise of about 1 uT)
r3 = [0.020, 0.030, 0.040, 0.060, 0.080, 0.120]          # m
B3 = [132, 90, 72, 50, 41, 31]                          # uT
I3 = 12.0
inv = [1 / r for r in r3]                                # 1/m
k3, b3 = fit(inv, B3)                                    # uT m and uT
# read in the solution from two far-apart points of the drawn line: (5,0 1/m; 23 uT) and (50 1/m; 132 uT)
x1, y1, x2, y2 = 5.0, 23.0, 50.0, 132.0
k_read = (y2 - y1) / (x2 - x1)                           # uT m
b_read = y1 - k_read * x1
mu_read = 2 * pi * k_read * 1e-6 / I3
out.update({f"{S}-s3-inv": [round(v, 2) for v in inv], f"{S}-s3-Br": [round(b * r * 100, 1) for b, r in zip(B3, r3)],
            f"{S}-s3-k-fit": round(k3, 3), f"{S}-s3-b-fit": round(b3, 2), f"{S}-s3-mu-fit": round(2 * pi * k3 * 1e-6 / I3, 10),
            f"{S}-s3-k-read": round(k_read, 3), f"{S}-s3-b-read": round(b_read, 2),
            f"{S}-s3-c": round(mu_read * 1e6, 4), f"{S}-s3-c-mu-fit": round(2 * pi * k3 / I3, 4), f"{S}-s3-c-diff": round(100 * (mu_read - mu0) / mu0, 2),
            f"{S}-s3-d": round(k_read / 0.50 + b_read, 2), f"{S}-s3-d-wire50": round(k_read / 0.50, 2), f"{S}-s3-d-half": round(2 * B3[2] - B3[0], 1),
            f"{S}-s3-d-wire4": round(k_read / 4, 1)})

# s4: the colours (word task; the numbers its model answers quote)
d_cd = 1.6e-6                                      # m, the track spacing of a CD
out.update({f"{S}-s4-cd-red": round(math.degrees(math.asin(650e-9 / d_cd)), 1),
            f"{S}-s4-cd-violet": round(math.degrees(math.asin(400e-9 / d_cd)), 1),
            f"{S}-s4-film-k0": round(550e-9 / (4 * 1.33) * 1e9, 1)})

# s5: the grating report (invented data: 600 lines/mm, a 532 nm laser, L = 80,0 cm)
d5 = 1e-3 / 600
L5 = 0.800
x5 = {1: 0.270, 2: 0.664}
lam5 = {k: d5 * math.sin(math.atan(x / L5)) / k for k, x in x5.items()}
th5 = {k: math.degrees(math.atan(x / L5)) for k, x in x5.items()}
th3 = math.degrees(math.asin(3 * 532e-9 / d5))
lam_small = d5 * x5[2] / (2 * L5)                  # the group's sin = x/L
dx, dL = 0.003, 0.003                              # m
lam2_hi = d5 * math.sin(math.atan((x5[2] + dx) / (L5 - dL))) / 2
lam2_lo = d5 * math.sin(math.atan((x5[2] - dx) / (L5 + dL))) / 2
lam1_hi = d5 * math.sin(math.atan((x5[1] + dx) / (L5 - dL)))
lam1_lo = d5 * math.sin(math.atan((x5[1] - dx) / (L5 + dL)))
out.update({f"{S}-s5-d": round(d5 * 1e6, 4), f"{S}-s5-a-l1": round(lam5[1] * 1e9, 1), f"{S}-s5-a-l2": round(lam5[2] * 1e9, 1),
            f"{S}-s5-th1": round(th5[1], 2), f"{S}-s5-th2": round(th5[2], 2),
            f"{S}-s5-small": round(lam_small * 1e9, 0), f"{S}-s5-small-k1": round(d5 * x5[1] / L5 * 1e9, 0),
            f"{S}-s5-l2-range": [round(lam2_lo * 1e9, 1), round(lam2_hi * 1e9, 1)],
            f"{S}-s5-l1-range": [round(lam1_lo * 1e9, 1), round(lam1_hi * 1e9, 1)],
            f"{S}-s5-kmax": int(d5 / 532e-9), f"{S}-s5-th3": round(th3, 1), f"{S}-s5-x3": round(L5 * math.tan(math.radians(th3)), 2)})

# s6: the cyclotron (example data; classical mechanics, v about 0,13 c)
B6, Ek_MeV, U6 = 1.20, 8.0, 50e3
T6 = 2 * pi * m_p / (e * B6)
f6 = 1 / T6
Ek = Ek_MeV * 1e6 * e
v6 = math.sqrt(2 * Ek / m_p)
r6 = m_p * v6 / (e * B6)
per_rev = 2 * e * U6                               # J, two gap crossings per revolution
nrev = Ek / per_rev
an = v6 ** 2 / r6
out.update({f"{S}-s6-a-T": round(T6 * 1e9, 2), f"{S}-s6-a": round(f6 / 1e6, 2),
            f"{S}-s6-b-v": round(v6 / 1e7, 3), f"{S}-s6-b-r": round(r6, 4), f"{S}-s6-b-c": round(v6 / c, 3),
            f"{S}-s6-b-Ek": Ek, f"{S}-s6-c-n": round(nrev, 1), f"{S}-s6-c-t": round(nrev * T6 * 1e6, 2),
            f"{S}-s6-d": round(an / 1e15, 3), f"{S}-s6-d-F": round(m_p * an * 1e12, 3),
            f"{S}-s6-d-check": round(e * v6 * B6 * 1e12, 3)})

# the unit's own numbers (hook, Ennusta, Tutki, Sovella, Tarkista, exit ticket), quoted in inquiry.json and unit.md
P_h0, R_h0 = 40e3, 0.50
for U in (230.0, 20e3):
    I = P_h0 / U
    out[f"inq-hook-I-{int(U)}"] = round(I, 2)
    out[f"inq-hook-P-{int(U)}"] = round(R_h0 * I ** 2, 2)
    out[f"inq-hook-share-{int(U)}"] = round(100 * R_h0 * I ** 2 / P_h0, 4)
    out[f"inq-hook-drop-{int(U)}"] = round(R_h0 * I, 2)
# Tutki: the falling magnet (12,0 g, 1,00 m)
m_t, h_t = 0.0120, 1.00
times = {"muovi": 0.46, "alumiini": 3.4, "kupari": 6.3, "rako": 0.62}
out["inq-tutki-free"] = round(math.sqrt(2 * h_t / g), 3)
out["inq-tutki-v-cu"] = round(h_t / times["kupari"], 4)
out["inq-tutki-P-cu"] = round(1000 * m_t * g * h_t / times["kupari"], 2)            # mW
out["inq-tutki-P-al"] = round(1000 * m_t * g * h_t / times["alumiini"], 2)
out["inq-tutki-mgh"] = round(1000 * m_t * g * h_t, 1)                               # mJ
out["inq-tutki-Ek-cu"] = round(1000 * 0.5 * m_t * (h_t / times["kupari"]) ** 2, 3)  # mJ
# Sovella numerics
out["inq-siipi"] = round(230 * 50e-6 * 34, 4)
out["inq-siipi-52"] = round(230 * 52e-6 * 34, 4)
out["inq-siipi-14"] = round(230 * 14e-6 * 34, 4)
out["inq-sirius"] = round(2.898e-3 / 292e-9, 0)
out["inq-ikkuna-ar"] = round(math.degrees(math.asin(1 / 1.33)), 2)
out["inq-ikkuna"] = round(3.0 * math.tan(math.asin(1 / 1.33)), 3)
out["inq-ikkuna-sin"] = round(3.0 * (1 / 1.33), 3)
out["inq-oljy"] = round(2 * 1.45 * 300 / 1.5, 1)                                   # nm, k = 1
out["inq-oljy-all"] = [round(2 * 1.45 * 300 / (k + 0.5), 1) for k in range(4)]
out["inq-oljy-wrong"] = [round(2 * 1.45 * 300 / k, 1) for k in range(1, 4)]
# the Sovella choices
I_c1 = 50e6 / 110e3
out["inq-c1-I"] = round(I_c1, 1)
out["inq-c1-Ph"] = round(4.0 * I_c1 ** 2 / 1000, 1)                                 # kW
out["inq-c1-wrong"] = round(110e3 ** 2 / 4.0 / 1e9, 3)                             # GW
out["inq-c2-U"] = round(12 / math.sqrt(2), 2)
# Tarkista and exit ticket
out["inq-muuntaja-U2"] = round(230 * 48 / 920, 2)
out["inq-muuntaja-I1"] = round(4.6 * 48 / 920, 4)
out["inq-muuntaja-wrong"] = round(4.6 * 920 / 48, 2)
out["inq-timantti"] = round(3.00e8 / 1.24e8, 3)
out["inq-lt-wire"] = round(2e-7 * 10 * 10 / 0.05 * 1000, 3)                        # mN per metre
print(json.dumps(out))
