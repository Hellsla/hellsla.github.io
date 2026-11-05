"""FY5 Esimerkkikoe: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json; `python scripts/practice.py check FY5/koe` compares them."""
import json, math

g = 9.81
gamma = 6.674e-11
I0 = 1.0e-12
out = {}


def lg(x): return math.log10(x)


def fit(xs, ys):
    """Least-squares line y = k x + b."""
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    k = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return k, my - k * mx


def t_allowed(L, L0=85.0, t0=8.0):
    """Allowed daily exposure (h) at level L: halves for every 3 dB above L0."""
    return t0 / 2 ** ((L - L0) / 3.0)


# ---------------------------------------------------------------- fy5-k1: Osa 1 checks of the options that need a number
M1, M2, M3 = 100 * 0.30, 150 * 0.15, 120 * 0.30 * math.sin(math.radians(30))
out["k1-a"] = {"M1": M1, "M2": M2, "M3": M3, "M3_no_angle": 120 * 0.30}          # Nm: 30 > 22,5 > 18; without the angle 36
F_d = gamma * 60 * 60 / 1.0 ** 2
out["k1-d"] = {"F": F_d, "lg": round(math.log10(F_d), 2), "cm": gamma * 60 * 60 / 100 ** 2,
               "grams": gamma * 60e3 * 60e3, "weight": 60 * g}                     # 2,4e-7 N; 2,4e-11; 0,24; 589 N
out["k1-f"] = {"T_ratio": 1.0, "v_ratio": 2.0, "E_ratio": 4.0}                    # T independent of A; v_max = A sqrt(k/m)
out["k1-g"] = {"lam_air": 340 / 1000, "lam_water": 1500 / 1000}
ds_h = 3.6 - 3.0
out["k1-h"] = {"ds": round(ds_h, 2), "n": round(ds_h / 0.40, 2)}                 # 1,5 wavelengths: destructive
out["k1-j"] = {"two": round(90 + 10 * lg(2), 1), "four": round(90 + 10 * lg(4), 1)}

# ---------------------------------------------------------------- fy5-k2: the diving board (A bolt at 0, B at 1,2 m, tip at 4,0 m)
mb, mh, Lb, xB = 40.0, 60.0, 4.0, 1.2
Gb, Fh = mb * g, mh * g
arm_b, arm_h = Lb / 2 - xB, Lb - xB                                               # 0,8 m and 2,8 m from B
FA = (Gb * arm_b + Fh * arm_h) / xB
NB = FA + Gb + Fh
out["fy5-k2-b-pultti"] = round(FA, 0); out["fy5-k2-b-tuki"] = round(NB, 0)
out["k2-b"] = {"Gb": round(Gb, 1), "Fh": round(Fh, 1), "M_b": round(Gb * arm_b, 1), "M_h": round(Fh * arm_h, 1)}
x_behind = Gb * arm_b / Fh                                                        # m behind B (towards A)
out["fy5-k2-c"] = round(xB - x_behind, 3); out["k2-c"] = {"behind_B": round(x_behind, 3), "FA_at_B": round(Gb * arm_b / xB, 1)}
xs = 0.090
k2 = Fh / xs
out["fy5-k2-d-k"] = round(k2, 0); out["fy5-k2-d-T"] = round(2 * math.pi * math.sqrt(mh / k2), 3)
out["k2-d-check"] = round(2 * math.pi * math.sqrt(xs / g), 3)                     # the same: T = 2π sqrt(x/g)

# ---------------------------------------------------------------- fy5-k3: the cubesat at 520 km
M, R, ms, h = 5.97e24, 6371e3, 4.0, 520e3
r = R + h
F3 = gamma * M * ms / r ** 2
out["fy5-k3-a-F"] = round(F3, 2); out["fy5-k3-a-osuus"] = round(100 * F3 / (ms * g), 1)
out["k3-a"] = {"r": r, "g_orbit": round(gamma * M / r ** 2, 3), "G_ground": round(ms * g, 2), "g_surface_model": round(gamma * M / R ** 2, 3)}
v3 = math.sqrt(gamma * M / r)
T3 = 2 * math.pi * r / v3
out["fy5-k3-b-v"] = round(v3, 0); out["fy5-k3-b-T"] = round(T3 / 60, 1); out["k3-b-T_s"] = round(T3, 0)
out["k3-b-an"] = round(v3 ** 2 / r, 3)                                            # = g_orbit
r4 = R + 400e3
out["fy5-k3-d"] = round(math.sqrt(gamma * M / r4), 0)

# ---------------------------------------------------------------- fy5-k4: the pendulum (l to the top of the ball)
L4 = [0.300, 0.500, 0.700, 0.900, 1.100, 1.300]
t10 = [11.40, 14.43, 17.05, 19.22, 21.27, 23.02]
T4 = [t / 10 for t in t10]; T4sq = [round(T * T, 2) for T in T4]
out["fy5-k4-a-T"] = T4[0]; out["fy5-k4-a-epävarmuus"] = 0.2 / 10
out["k4-b"] = {"T": T4, "T2": T4sq}
k4, b4 = fit(L4, [T * T for T in T4])
out["k4-fit"] = {"slope": round(k4, 3), "intercept": round(b4, 3), "g_fit": round(4 * math.pi ** 2 / k4, 3), "l_axis": round(-b4 / k4, 4)}
P1, P2 = (0.10, 0.49), (1.30, 5.31)                                               # two points read off the drawn line
k4r = (P2[1] - P1[1]) / (P2[0] - P1[0])
out["fy5-k4-c"] = round(4 * math.pi ** 2 / k4r, 2); out["k4-c-slope"] = round(k4r, 3)
out["k4-d"] = {"r_from_T2_axis": round(0.088 / k4r, 4)}

# ---------------------------------------------------------------- fy5-k5: the kantele string
L5, f1, v_air = 0.550, 196.0, 343.0
lam1 = 2 * L5
out["fy5-k5-b-v"] = round(f1 * lam1, 1); out["fy5-k5-b-f2"] = 2 * f1; out["fy5-k5-b-f3"] = 3 * f1
out["fy5-k5-c"] = round(v_air / f1, 3); out["k5-c-lam_string"] = lam1
out["fy5-k5-d"] = round(62 - 10 * lg((8.0 / 1.0) ** 2), 1)

# ---------------------------------------------------------------- fy5-k6: the speed of sound from an echo
D6 = [15.0, 25.0, 35.0, 45.0, 55.0, 65.0]
dt6 = [0.090, 0.148, 0.209, 0.267, 0.328, 0.386]
s6 = [2 * d for d in D6]
out["fy5-k6-a"] = round(s6[0] / dt6[0], 1)
v_origin = sum(a * b for a, b in zip(dt6, s6)) / sum(a * a for a in dt6)         # least squares through the origin
Q1, Q2 = (0.0, 0.0), (0.40, 134.5)                                                # read off the drawn line
v_read = (Q2[1] - Q1[1]) / (Q2[0] - Q1[0])
out["fy5-k6-c"] = round(v_read, 1); out["k6-c"] = {"v_origin_fit": round(v_origin, 1), "v_each": [round(a / b, 1) for a, b in zip(s6, dt6)],
                                                     "v_theory": 331 + 0.6 * 8.0, "diff_pct": round(100 * (v_read - (331 + 0.6 * 8.0)) / (331 + 0.6 * 8.0), 2)}
rel_s = 0.1 / D6[0] + 0.002 / dt6[0]; rel_l = 0.1 / D6[-1] + 0.002 / dt6[-1]
out["fy5-k6-d-lyhin"] = round(100 * rel_s, 2); out["fy5-k6-d-pisin"] = round(100 * rel_l, 2)
out["fy5-k6-d-taso"] = round(10 * lg((s6[-1] / s6[0]) ** 2), 1)
out["k6-d"] = {"short_d": round(100 * 0.1 / D6[0], 2), "short_t": round(100 * 0.002 / dt6[0], 2), "long_d": round(100 * 0.1 / D6[-1], 2), "long_t": round(100 * 0.002 / dt6[-1], 2)}
out["k6-e"] = {"lam_300": round(336 / 300, 2), "lam_3000": round(336 / 3000, 3)}

# ---------------------------------------------------------------- fy5-k7: the steward in front of the stage
L7, real_plug, muffs = 103.0, 22.0 - 10.0, 25.0
I7 = I0 * 10 ** (L7 / 10)
out["fy5-k7-a-I"] = round(I7, 5); out["fy5-k7-a-suhde"] = round(10 ** ((L7 - 85) / 10), 1)
out["fy5-k7-b-ilman"] = round(60 * t_allowed(L7), 2); out["fy5-k7-b-tulpat"] = round(t_allowed(L7 - real_plug), 3)
out["k7-b-nominal"] = round(t_allowed(L7 - 22.0), 1)
L25 = L7 - 10 * lg((25 / 10) ** 2)
out["fy5-k7-c"] = round(L25, 2)
L25 = round(L25)                                                                  # levels in whole decibels from here on, as in the solution
out["k7-c"] = {"ear": L25 - real_plug, "t": round(t_allowed(L25 - real_plug), 2), "limit_4h": 85 + 3 * math.log2(8 / 4)}
dose_off = 1.0 / t_allowed(L25); dose_on = 3.0 / t_allowed(L25 - real_plug)
out["fy5-k7-d"] = round(100 * (dose_off + dose_on), 1)
out["k7-d"] = {"t95_min": round(60 * t_allowed(L25), 1), "off_pct": round(100 * dose_off, 1), "on_pct": round(100 * dose_on, 1),
               "all_on_pct": round(100 * 4.0 / t_allowed(L25 - real_plug), 1)}
out["fy5-k7-e"] = round(100 * 4.0 / t_allowed(L7 - muffs), 1); out["k7-e-t"] = round(t_allowed(L7 - muffs), 1)
print(json.dumps(out))
