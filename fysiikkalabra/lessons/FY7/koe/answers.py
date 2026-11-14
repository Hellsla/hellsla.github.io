"""FY7 Esimerkkikoe: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-name]": value}; `python scripts/practice.py check FY7/koe` compares them with tasks.json."""
import json, math, itertools

e, me, c = 1.602e-19, 9.109e-31, 2.998e8
mu0 = 4e-7 * math.pi
out = {}


def lsq(x, y):
    n = len(x); mx, my = sum(x) / n, sum(y) / n
    s = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return s, my - s * mx


# ---------------------------------------------------------------- k1: Osa 1 numbers
PHI1 = [(0, 0.0), (2, 0.6), (4, 0.6), (5.5, 0.0)]          # s, mWb
N1 = 200
out["k1-d"] = {"e_first": N1 * 0.6e-3 / 2, "e_last": N1 * 0.6e-3 / 1.5, "no_dt": N1 * 0.6e-3, "no_N_mV": 0.6 / 1.5}
out["k1-g"] = {"loss_ratio": 1 / 10 ** 2}
n_core, n_clad = 1.50, 1.44
out["k1-i"] = {"crit": math.degrees(math.asin(n_clad / n_core))}

# ---------------------------------------------------------------- k2: electron beam, r^2 against U
B2 = 0.80e-3                                         # T
U2 = [80, 120, 160, 200, 240]                        # V
R2 = [0.038, 0.046, 0.054, 0.059, 0.066]             # m, +-1 mm
dR2 = 0.001
Q2 = [r * r for r in R2]                             # m^2
DQ2 = [2 * r * dR2 for r in R2]
s2, b2 = lsq(U2, Q2)                                 # m^2/V
em2 = 2 / (B2 ** 2 * s2)                             # C/kg
out["fy7-k2-b"] = em2
_pts = [(u, q + sg * d) for u, q, d in zip(U2, Q2, DQ2) for sg in (-1, 1)]
_ok = []
for _p, _q in itertools.combinations(_pts, 2):
    if _p[0] == _q[0]: continue
    _a = (_q[1] - _p[1]) / (_q[0] - _p[0]); _b = _p[1] - _a * _p[0]
    if all(abs(q - (_a * u + _b)) <= d + 1e-12 for u, q, d in zip(U2, Q2, DQ2)): _ok.append((_a, _p, _q))
_ok.sort()
smin, smax = _ok[0][0], _ok[-1][0]
em_lo, em_hi = 2 / (B2 ** 2 * smax), 2 / (B2 ** 2 * smin)
out["fy7-k2-c"] = (em_hi - em_lo) / 2
out["k2"] = {"Q": [round(q * 1e3, 3) for q in Q2], "DQ": [round(d * 1e3, 3) for d in DQ2], "s_ls": s2, "b_ls": b2, "em": em2,
             "smax": smax, "smin": smin, "pts_max": _ok[-1][1:], "pts_min": _ok[0][1:], "em_lo": em_lo, "em_hi": em_hi,
             "rel": (em_hi - em_lo) / 2 / em2, "lit": 1.759e11, "dev": em2 / 1.759e11 - 1, "n_ok": len(_ok),
             "v240": math.sqrt(2 * e * 240 / me), "r_theory_240": math.sqrt(2 * 240 / (1.759e11 * B2 ** 2)),
             "s_read": (Q2[4] - Q2[0]) / (U2[4] - U2[0])}

# ---------------------------------------------------------------- k3: rod on rails
l3, B3, v3, R3 = 0.30, 0.40, 2.5, 0.60
e3 = v3 * B3 * l3
I3 = e3 / R3
F3 = I3 * l3 * B3
P3 = F3 * v3
out["fy7-k3-a"] = e3
out["fy7-k3-c-F"] = F3
out["fy7-k3-c-P"] = P3
out["k3"] = {"e": e3, "I": I3, "F": F3, "P": P3, "Pheat": I3 ** 2 * R3, "P_e_I": e3 * I3, "v_half": F3 * v3 / 2,
             "dPhi_per_s": B3 * l3 * v3, "area_rate": l3 * v3}

# ---------------------------------------------------------------- k4: generator and transformer
e0_4, T4 = 17.5, 0.025
N4, A4 = 90, 0.0150
f4 = 1 / T4
U4 = e0_4 / math.sqrt(2)
out["fy7-k4-a-f"] = f4
out["fy7-k4-a-U"] = U4
B4 = e0_4 / (N4 * A4 * 2 * math.pi * f4)
out["fy7-k4-b"] = B4
N1_4, U2_4, P4 = 150, 230.0, 46.0
N2_4 = N1_4 * U2_4 / U4
I2_4 = P4 / U2_4
I1_4 = I2_4 * U2_4 / U4
out["fy7-k4-c-N"] = N2_4
out["fy7-k4-c-I"] = I1_4
out["k4"] = {"omega": 2 * math.pi * f4, "NBA": e0_4 / (2 * math.pi * f4), "ratio": U2_4 / U4, "I2": I2_4, "P_check": U4 * I1_4,
             "U_dc_wrong": e0_4}

# ---------------------------------------------------------------- k5: grating
lam5, L5 = 532e-9, 1.500
X5 = [0.243, 0.503, 0.822]                           # m, orders 1..3, +-2 mm
dX5 = 0.002
th5 = [math.atan(x / L5) for x in X5]
d5 = [k * lam5 / math.sin(t) for k, t in zip((1, 2, 3), th5)]
out["fy7-k5-a"] = d5[0]
dd = []
for k, x in zip((1, 2, 3), X5):
    lo = k * lam5 / math.sin(math.atan((x + dX5) / L5)); hi = k * lam5 / math.sin(math.atan((x - dX5) / L5))
    dd.append((hi - lo) / 2)
out["fy7-k5-b"] = sum(d5) / 3
dmean = sum(d5) / 3
out["fy7-k5-c"] = math.floor(dmean / lam5)
out["k5"] = {"theta": [math.degrees(t) for t in th5], "sin": [math.sin(t) for t in th5], "d": d5, "dd": dd, "rel": [a / b for a, b in zip(dd, d5)],
             "mean": dmean, "spread": (max(d5) - min(d5)) / 2, "lines_per_mm": 1e-3 / dmean, "kmax_exact": dmean / lam5,
             "n_max": 2 * math.floor(dmean / lam5) + 1, "theta6": math.degrees(math.asin(6 * lam5 / dmean)),
             "x6": L5 * math.tan(math.asin(6 * lam5 / dmean))}

# ---------------------------------------------------------------- k6: wind farm line
P6, R6, U_a, U_b = 12e6, 4.8, 20e3, 110e3
Ia, Ib = P6 / U_a, P6 / U_b
Pha, Phb = R6 * Ia ** 2, R6 * Ib ** 2
out["fy7-k6-a-I"] = Ia
out["fy7-k6-a-Ph"] = Pha
N2_6 = 2750
N1_6 = N2_6 * U_a / U_b
out["fy7-k6-b-I"] = Ib
out["fy7-k6-b-Ph"] = Phb
out["fy7-k6-c-N"] = N1_6
out["fy7-k6-c-I"] = Ia
hrs, price, cost_tr = 4000.0, 50.0, 3.0e6               # h/a, EUR/MWh, EUR for both transformers
Ea, Eb = Pha * hrs / 1e6, Phb * hrs / 1e6               # MWh
sav = (Ea - Eb) * price
out["fy7-k6-d-sav"] = sav
out["fy7-k6-d-pay"] = cost_tr / sav
out["k6"] = {"share_a": Pha / P6, "share_b": Phb / P6, "Ea": Ea, "Eb": Eb, "cost_a": Ea * price, "cost_b": Eb * price, "ratio": U_b / U_a,
             "loss_ratio": Pha / Phb, "I_ratio": Ia / Ib, "Phb_kW": Phb / 1e3, "Pha_MW": Pha / 1e6, "Pa_ok": P6 - Pha,
             "Ulinedrop_a": Ia * R6, "dropshare_a": Ia * R6 / U_a, "Ulinedrop_b": Ib * R6, "dropshare_b": Ib * R6 / U_b}

# ---------------------------------------------------------------- k7: lamp spectrum, lambda_max against 1/T
T7 = [2200, 2400, 2600, 2800, 3000]                  # K
L7 = [1262, 1139, 1070, 975, 921]                    # nm
inv7 = [1 / t * 1e4 for t in T7]                     # 1e-4 1/K
b_each = [l * 1e-9 * t for l, t in zip(L7, T7)]
b7 = sum(a * l for a, l in zip(inv7, L7)) / sum(a * a for a in inv7) * 1e-5   # m K, through the origin (nm per 1e-4 1/K)
b_th = 2.898e-3
out["fy7-k7-b"] = b7
out["fy7-k7-c"] = 100 * (b_th - b7) / b_th
Tb = 273.15 + 33
out["fy7-k7-d"] = b_th / Tb * 1e6                      # um
out["fy7-k7-e"] = b_th / 550e-9
out["k7"] = {"inv": [round(v, 3) for v in inv7], "b_each": b_each, "b_mean": sum(b_each) / 5, "b": b7,
             "spread": (max(b_each) - min(b_each)) / 2, "dev": (b_th - b7) / b_th, "lam_lamp_2800": b_th / 2800 * 1e9,
             "lam_body_um": b_th / Tb * 1e6, "T_550": b_th / 550e-9, "T_melt": 3695, "T_body": Tb,
             "s_read": (L7[4] - L7[0]) / (inv7[4] - inv7[0]), "T_for_500": b_th / 500e-9}
print(json.dumps(out, ensure_ascii=False))
