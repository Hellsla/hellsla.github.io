"""FY8 Esimerkkikoe: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json; `python scripts/practice.py check FY8/koe` compares them."""
import json, math

h, c, e = 6.626e-34, 2.998e8, 1.602e-19            # J s, m/s, C (1 eV = e * 1 V)
u_kg, u_MeV = 1.6605e-27, 931.5                    # kg, MeV per u (c^2 cancels)
out = {}
eV = lambda E_J: E_J / e


def lsq(x, y):
    n = len(x); mx, my = sum(x) / n, sum(y) / n
    s = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return s, my - s * mx


# ---------------------------------------------------------------- fy8-k1: Osa 1, the items that need a number
W_J = 2.32 * e                                     # b: work function of the metal of the stopping-voltage graph, 2,32 eV
F1 = [6.5e14, 7.5e14, 8.5e14, 9.5e14]              # Hz, the four measured frequencies
US1 = [round((h * f - W_J) / e, 2) for f in F1]    # V, stopping voltages
f0 = W_J / h
out["k1-b"] = {"US": US1, "f0_Hz": f0, "W_J": h * 5.6e14, "W_eV": round(h * 5.6e14 / e, 2), "slope_Vs": h / e}
out["k1-d-alt"] = {"inv_n": round((1 - 1 / 2) / (1 / 2 - 1 / 3), 2), "n_squared": round((4 - 1) / (9 - 4), 2)}
out["k1-d"] = {"E21": 13.6 * (1 - 1 / 4), "E32": round(13.6 * (1 / 4 - 1 / 9), 4), "ratio": round(13.6 * 0.75 / (13.6 * (1 / 4 - 1 / 9)), 2)}
out["k1-e"] = {"blue_V": round(1.9 * 650 / 450, 2), "wrong_squared": round(1.9 * (650 / 450) ** 2, 2), "wrong_inverse": round(1.9 * 450 / 650, 2)}
out["k1-g"] = {"halvings": math.log2(3.2 / 0.10), "t_h": 4.0 * math.log2(3.2 / 0.10), "linear_wrong": (3.2 - 0.10) / 1.6 * 4.0}
out["k1-h"] = {"ratio": 200e6 / 4.0}
out["k1-i"] = {"H_alpha_mSv": 20 * 1.0, "H_gamma_mSv": 1 * 1.0}

# ---------------------------------------------------------------- fy8-k2: LED thresholds and Planck's constant
LAM2 = [625, 590, 525, 470, 430]                   # nm
UK2 = [1.91, 2.07, 2.31, 2.62, 2.84]               # V, measured, +-0,05 V
dU2 = 0.05
F2 = [c / (l * 1e-9) for l in LAM2]                # Hz
out["k2-f"] = [round(f / 1e14, 3) for f in F2]
s_ls, b_ls = lsq(F2, UK2)
s2 = (UK2[4] - UK2[0]) / (F2[4] - F2[0])           # the line read from the graph's end points
out["fy8-k2-b"] = e * s_ls                          # h from the fitted line, J s
h2 = e * s2
# extreme lines through bar end points that stay inside ALL five error bars
import itertools
_pts = [(f, u + sg * dU2) for f, u in zip(F2, UK2) for sg in (-1, 1)]
_ok = []
for _p, _q in itertools.combinations(_pts, 2):
    if _p[0] == _q[0]: continue
    _a = (_q[1] - _p[1]) / (_q[0] - _p[0]); _b = _p[1] - _a * _p[0]
    if all(abs(u - (_a * f + _b)) <= dU2 + 1e-9 for f, u in zip(F2, UK2)): _ok.append((_a, _p, _q))
_ok.sort()
smin, smax = _ok[0][0], _ok[-1][0]
dh2 = e * (smax - smin) / 2
out["fy8-k2-c"] = dh2
out["k2"] = {"slope_end": s2, "h_end": h2, "slope_ls": s_ls, "h_ls": e * s_ls, "intercept_ls": b_ls, "dh": dh2,
             "rel_dh": dh2 / h2, "dev": (h2 - h) / h, "smax": smax, "smin": smin, "h_max": e * smax, "h_min": e * smin, "pts_max": _ok[-1][1:], "pts_min": _ok[0][1:], "df": F2[4] - F2[0],
             "hc_over_e_per_f": h / e, "rel_U_blue": dU2 / UK2[4], "rel_U_red": dU2 / UK2[0]}

# ---------------------------------------------------------------- fy8-k3: decay of a sample, counts in 30 s
T3 = [0, 1, 2, 3, 4, 6, 8, 10]                     # min
N3 = [803, 631, 535, 409, 345, 205, 150, 88]       # counts in the 30 s window starting at t
slope3, b3 = lsq(T3, [math.log(n) for n in N3])
lam3 = -slope3                                     # 1/min, fitted to ln N
out["fy8-k3-b"] = round(math.log(2) / lam3, 2)     # half-life, min (from the fit)
out["fy8-k3-c-lam"] = round(lam3, 3)               # decay constant, 1/min
out["fy8-k3-c-N"] = round(math.exp(b3) * math.exp(-lam3 * 15), 1)   # expected counts in the window at 15 min
out["fy8-k3-d"] = round(100 * math.sqrt(N3[0]) / N3[0], 1)          # relative uncertainty of the first count, %
out["k3"] = {"N0_fit": math.exp(b3), "lam": lam3, "T_half": math.log(2) / lam3, "t_5pct": math.log(20) / lam3,
             "model": [round(math.exp(b3) * math.exp(-lam3 * t), 1) for t in T3],
             "sqrtN": [round(math.sqrt(n), 1) for n in N3], "dev": [round(n - math.exp(b3) * math.exp(-lam3 * t), 1) for n, t in zip(N3, T3)],
             "rel_last": math.sqrt(N3[-1]) / N3[-1], "T_half_2": 4.0 * math.log(2) / math.log(N3[0] / N3[4])}
# the graph reading: the time at which the fitted curve reaches half of its start value
out["k3"]["N0_half"] = math.exp(b3) / 2

# ---------------------------------------------------------------- fy8-k4: deuterium-tritium fusion
mH, mn, mD, mT, mHe = 1.007825, 1.008665, 2.014102, 3.016049, 4.002603     # u, atomic masses
BE = lambda Z, N, m: (Z * mH + N * mn - m) * u_MeV
BE_He, BE_D, BE_T = BE(2, 2, mHe), BE(1, 1, mD), BE(1, 2, mT)
out["fy8-k4-a-E"] = BE_He
out["fy8-k4-a-per"] = BE_He / 4
out["fy8-k4-b"] = (mD + mT - mHe - mn) * u_MeV
Q4 = (mD + mT - mHe - mn) * u_MeV
Ef = Q4 * 1e6 * e / ((mD + mT) * u_kg)             # J per kg of D+T
out["fy8-k4-c"] = Ef                               # J/kg
out["k4"] = {"BE_He": BE_He, "BE_He_per_A": BE_He / 4, "BE_D": BE_D, "BE_D_per_A": BE_D / 2, "BE_T": BE_T, "BE_T_per_A": BE_T / 3,
             "dm_u": mD + mT - mHe - mn, "Q": Q4, "Q_J": Q4 * 1e6 * e, "m_fuel_kg": (mD + mT) * u_kg, "Ef": Ef,
             "ratio_coal": Ef / 30e6, "check": BE_He - BE_D - BE_T, "BE_sum_check": BE_He - BE_D - BE_T - Q4}

# ---------------------------------------------------------------- fy8-k5: hydrogen
En = lambda n: -13.6 / n ** 2
E32 = En(3) - En(2); lam32 = h * c / (E32 * e)
out["fy8-k5-a"] = round(lam32 * 1e9, 1)            # nm
E21 = En(2) - En(1); lam21 = h * c / (E21 * e)
E200 = h * c / (200e-9) / e; KE5 = E200 - (0 - En(2)); lam_ion = h * c / (-En(2) * e)
out["fy8-k5-b"] = lam21 * 1e9                       # nm
out["fy8-k5-c"] = round(KE5, 2)                    # eV
out["k5"] = {"E32": E32, "lam32_nm": lam32 * 1e9, "E21": E21, "lam21_nm": lam21 * 1e9, "E200": E200, "KE_eV": KE5, "KE_J": KE5 * e,
             "ion2_eV": -En(2), "lam_ion_nm": lam_ion * 1e9, "ion1_eV": -En(1), "lam_ion1_nm": h * c / (13.6 * e) * 1e9,
             "hc_eVnm": h * c / e * 1e9}

# ---------------------------------------------------------------- fy8-k6: lead shielding, count rate
D6 = [0, 3, 6, 9, 12, 18, 24]                      # mm
R6 = [120.9, 85.7, 61.3, 43.2, 31.4, 16.0, 8.7]    # 1/s, measured with the source
Rb = 0.8                                           # 1/s, background without the source
Rn = [round(r - Rb, 1) for r in R6]
sl6, b6 = lsq(D6, [math.log(r) for r in Rn]); mu6 = -sl6
out["fy8-k6-a"] = round(Rn[-1], 1)
out["fy8-k6-c-mu"] = mu6                 # 1/mm
out["fy8-k6-c-d"] = round(math.log(2) / mu6, 2)    # mm
H0, r0, rw, occ, lim = 160.0, 1.0, 3.0, 2000.0, 1000.0     # uSv/h at 1,0 m; m; m; h/a; uSv/a (1 mSv)
H_need = lim / occ
H_free = H0 * (r0 / rw) ** 2
out["fy8-k6-e"] = 100 * math.sqrt(R6[-1] * 100 + Rb * 100) / (R6[-1] * 100 - Rb * 100)   # %
out["fy8-k6-d"] = round(math.log(H_free / H_need) / mu6, 1)   # mm
t6 = 100.0
Nraw, Nb = R6[-1] * t6, Rb * t6
out["k6"] = {"net": Rn, "ln_net": [round(math.log(r), 3) for r in Rn], "mu": mu6, "I0_fit": math.exp(b6), "d_half": math.log(2) / mu6,
             "H_need": H_need, "H_free": H_free, "factor": H_free / H_need, "ln_factor": math.log(H_free / H_need),
             "d_req": math.log(H_free / H_need) / mu6, "dev": [round(r - math.exp(b6 - mu6 * d), 2) for r, d in zip(Rn, D6)],
             "Nraw": Nraw, "Nb": Nb, "sqrt_raw": math.sqrt(Nraw), "net_N": Nraw - Nb, "dnet": math.sqrt(Nraw + Nb),
             "rel_net": math.sqrt(Nraw + Nb) / (Nraw - Nb), "factor_30": math.exp(mu6 * 30),
             "d_req_bg_range": [math.log(H_free / H_need) / (mu6 * (1 + k)) for k in (-0.05, 0.05)],
             "no_bg_mu": -lsq(D6, [math.log(r) for r in R6])[0], "rate_at_d_req_ratio": H_free * math.exp(-mu6 * 31)}

# ---------------------------------------------------------------- fy8-k7: F-18 PET
T_F, T_C = 109.8, 20.4                             # min, half-lives of F-18 and C-11
lamF = math.log(2) / T_F
out["fy8-k7-a"] = round(0.5 ** (180 / T_F), 3)     # fraction left after 3,0 h
need, delay = 280.0, 4.5 * 60                      # MBq at injection; min from production to injection
out["fy8-k7-b"] = round(need / 0.5 ** (delay / T_F), 0)   # MBq at production
me = 9.109e-31
E511 = me * c ** 2
out["fy8-k7-c-E"] = round(E511 / e / 1e3, 0)       # keV
out["fy8-k7-c-lam"] = round(h * c / E511 * 1e12, 2)        # pm
coef = 0.019                                       # mSv / MBq (example value)
out["fy8-k7-d"] = round(need * coef, 2)            # mSv
out["k7"] = {"lamF_per_min": lamF, "lamF_per_h": lamF * 60, "left_3h": 0.5 ** (180 / T_F), "order": need / 0.5 ** (delay / T_F),
             "halvings": delay / T_F, "factor": 2 ** (delay / T_F), "E511_J": E511, "E511_keV": E511 / e / 1e3, "lam_pm": h * c / E511 * 1e12,
             "p_photon": E511 / c, "dose": need * coef, "share_year": need * coef / 5.9,
             "C11_left_3h": 0.5 ** (180 / T_C), "C11_order": need / 0.5 ** (delay / T_C), "C11_halvings_3h": 180 / T_C,
             "F18_left_3h": 0.5 ** (180 / T_F), "C11_left_1h": 0.5 ** (60 / T_C)}

print(json.dumps(out, ensure_ascii=False))
