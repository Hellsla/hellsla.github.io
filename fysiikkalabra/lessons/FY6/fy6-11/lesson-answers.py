"""Numbers of the lesson text and inquiry.json for fy6-11, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Field strength E = F / q (the force on a small test charge), in a uniform field
F = q E; between two parallel plates at the voltage U and distance d, E = U / d (W = F d = q E d and W = q U).
The simulation's plates (assets/sims/fy6/fy6-11/sim.js) are computed here with the same model: each 20 cm plate is split
into 40 strips of constant surface charge, the charges are solved so that the plates are conductors at +U/2 and -U/2
(2D strip potentials), and the field is the sum of the strips' exact fields. Prints {id: number} as JSON."""
import json
import math

a = {}
e, me, g = 1.602e-19, 9.109e-31, 9.81          # elementary charge (C), electron mass (kg), g (m/s^2)

# --- the simulation's model ---------------------------------------------------------------------------------------
L, N = 0.20, 40


def Fp(u, y):
    r2 = u * u + y * y
    v = (0.5 * u * math.log(r2) if r2 > 0 else 0.0) - u
    if y != 0:
        v += y * math.atan(u / y)
    return v


def build(d):
    """Strip charges (per volt of plate voltage) of two conductor plates at +1/2 and -1/2."""
    w = L / N
    S = [(-L / 2 + j * w, -L / 2 + (j + 1) * w, yp) for yp in (d / 2, -d / 2) for j in range(N)]
    n = len(S)
    M = [[-(Fp(b - (S[i][0] + S[i][1]) / 2, S[i][2] - y) - Fp(a_ - (S[i][0] + S[i][1]) / 2, S[i][2] - y)) for (a_, b, y) in S]
         for i in range(n)]
    r = [0.5 if S[i][2] > 0 else -0.5 for i in range(n)]
    for c in range(n):
        pv = max(range(c, n), key=lambda k: abs(M[k][c]))
        M[c], M[pv] = M[pv], M[c]; r[c], r[pv] = r[pv], r[c]
        for k in range(c + 1, n):
            f = M[k][c] / M[c][c]
            if f:
                for m in range(c, n):
                    M[k][m] -= f * M[c][m]
                r[k] -= f * r[c]
    s = [0.0] * n
    for k in range(n - 1, -1, -1):
        s[k] = (r[k] - sum(M[k][m] * s[m] for m in range(k + 1, n))) / M[k][k]
    return S, s


CACHE = {}


def sim(U_kV, d_cm, q_nC, x_cm, h_cm):
    """The sensor's force F (µN) and the field E (V/m) at the ball, as the simulation shows them."""
    d = d_cm / 100
    if d_cm not in CACHE:
        CACHE[d_cm] = build(d)
    S, s = CACHE[d_cm]
    x, y = x_cm / 100, h_cm / 100 - d / 2
    ex = ey = 0.0
    for (a_, b, yp), sj in zip(S, s):
        yy = y - yp
        ex += sj * 0.5 * math.log(((x - a_) ** 2 + yy * yy) / ((x - b) ** 2 + yy * yy))
        ey += sj * (math.atan((b - x) / yy) - math.atan((a_ - x) / yy))
    E = U_kV * 1000 * math.hypot(ex, ey)
    return abs(q_nC) * 1e-9 * E * 1e6, E


# on load: U = 2,0 kV, d = 4,0 cm, q = +2,0 nC, x = 0, h = 2,0 cm
a["sim-F"], a["sim-E"] = sim(2, 4, 2, 0, 2)                 # 100 µN, 5,0e4 V/m
a["sim-Eud"] = 2000 / 0.04                                  # U : d = 5,0e4 V/m
# experiment 1 (prediction 1): the height h between the plates, x = 0
for h in (0.5, 1, 2, 3, 3.5):
    a[f"koe1-h{h}"] = sim(2, 4, 2, 0, h)[0]                 # 100 µN at every height
# experiment 2: the ball's charge q at the same place; E = F : q
for q in (1, 2, 3, -1, -2, -3):
    a[f"koe2-q{q}"] = sim(2, 4, q, 0, 2)[0]                 # 50, 100, 150 µN
a["koe2"] = sim(2, 4, 3, 0, 2)[0] * 1e-6 / 3e-9             # E = 150 µN : 3,0 nC = 5,0e4 N/C
a["koe2-mistake-units"] = sim(2, 4, 3, 0, 2)[0] / 3         # 50 (µN : nC without the prefixes)
a["koe2-mistake-inv"] = 3e-9 / (sim(2, 4, 3, 0, 2)[0] * 1e-6)   # 2,0e-5 (q : F)
# experiment 3 (prediction 2): the distance d at U = 2,0 kV, q = +2,0 nC, h = 1,0 cm
for d in (2, 3, 4, 5, 6):
    a[f"koe3-d{d}"] = sim(2, d, 2, 0, 1)[0]                 # 200, 133, 100, 80, 66,7 µN
a["koe3"] = sim(2, 2, 2, 0, 1)[0] * 1e-6 / 2e-9 * 0.02      # E d = 1,0e5 N/C · 0,020 m = 2000 V = U
a["koe3-check-d6"] = sim(2, 6, 2, 0, 1)[0] * 1e-6 / 2e-9 * 0.06   # 2000 V again
a["koe3-mistake-cm"] = sim(2, 2, 2, 0, 1)[0] * 1e-6 / 2e-9 * 2    # 2,0e5 (d in centimetres)
# experiment 4 (optional): along the midline towards the end of the plates (the end is at x = 10 cm)
for x in (0, 4, 8, 9, 10, 11, 12):
    a[f"koe4-x{x}"] = sim(2, 4, 2, x, 2)[0]                 # 100, 100, 98, 92, 76, 53, 35 µN
# ennuste-2 feedback: at d = 2,0 cm and 4,0 cm
a["ennuste2-ratio"] = a["koe3-d4"] / a["koe3-d2"]           # 0,50

# --- theory -------------------------------------------------------------------------------------------------------
a["text-E"] = 100e-6 / 2.0e-9                               # 100 µN on 2,0 nC: 5,0e4 N/C
a["text-F-neg"] = 2.0e-9 * 5.0e4                            # the same field on -2,0 nC: 1,0e-4 N, upwards
a["text-Eud"] = 2.0e3 / 0.040                               # 2,0 kV over 4,0 cm: 5,0e4 V/m
a["text-purifier"] = 5.0e3 / 0.010                          # 5,0 kV over 1,0 cm: 5,0e5 V/m
a["text-electron-F"] = e * 5.0e4                            # 8,0e-15 N
a["text-electron-G"] = me * g                               # 8,9e-30 N
a["text-electron-a"] = e * 5.0e4 / me                       # 8,8e15 m/s^2
a["text-electron-ratio"] = a["text-electron-F"] / a["text-electron-G"]   # 9e14

# --- worked example: an oil drop hovers, m = 4,9e-15 kg, d = 6,0 mm, U = 600 V ---------------------------------------
E = 600 / 6.0e-3
a["ex-E"] = E                                               # 1,0e5 V/m
a["ex-G"] = 4.9e-15 * g                                     # 4,807e-14 N
a["ex-q"] = 4.9e-15 * g * 6.0e-3 / 600                      # q = m g d / U = 4,807e-19 C
a["ex-n"] = a["ex-q"] / e                                   # 3,0 elementary charges
a["ex-check-F"] = 3 * e * E                                 # 3 e E = 4,806e-14 N = m g

# --- kertaus: Coulomb's law, one charge doubled at the same distance ------------------------------------------------
a["kertaus"] = 12 * 2                                       # 12 µN -> 24 µN
a["kertaus-mistake-sq"] = 12 * 4                            # 48 µN (squared by mistake)

# --- error spotting: U = 1,2 kV, d = 3,0 cm -------------------------------------------------------------------------
a["virhe-right"] = 1.2e3 / 0.030                            # 4,0e4 V/m
a["virhe-wrong"] = 1.2e3 / 3.0                              # 400 (d in cm)
a["virhe-product"] = 1.2e3 * 0.030                          # 36 (U d)

# --- transfer task: an inkjet drop, m = 1,2e-10 kg, |q| = 2,0e-13 C, U = 1,6 kV, d = 2,0 mm ---------------------------
E = 1.6e3 / 2.0e-3                                          # 8,0e5 V/m
a["siirto-E"] = E
a["siirto-F"] = 2.0e-13 * E                                 # 1,6e-7 N
a["siirto"] = 2.0e-13 * E / 1.2e-10                         # a = 1333 m/s^2
a["siirto-mistake-mm"] = 2.0e-13 * (1.6e3 / 2.0) / 1.2e-10  # 1,33 m/s^2 (d in mm)
a["siirto-mistake-nod"] = 2.0e-13 * 1.6e3 / 1.2e-10         # 2,67 m/s^2 (U for E)
a["siirto-G"] = 1.2e-10 * g                                 # 1,18e-9 N, about 0,7 % of F
a["siirto-ratio"] = a["siirto-F"] / a["siirto-G"]           # 136

# --- check 1: an electron between plates, the + plate on top: force up, opposite to E -------------------------------
# --- exit ticket: 9,0 kV over 3,0 cm ---------------------------------------------------------------------------------
a["exit-E"] = 9.0e3 / 0.030                                 # 3,0e5 V/m
print(json.dumps({k: round(v, 6) if abs(v) >= 1e-3 else v for k, v in a.items()}))
