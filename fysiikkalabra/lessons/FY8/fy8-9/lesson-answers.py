"""Numbers of the lesson text and inquiry.json for fy8-9, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Decay law N = N0 (1/2)^(t/T½) = N0 e^(-λt), λ = ln 2 / T½, activity A = λN.
Half-lives from NNDC NuDat 3 (ENSDF evaluations), rounded: I-131 8,02 d, Tc-99m 6,01 h, Ba-137m 2,552 min,
Pa-234m 1,159 min, Cs-137 30,08 a, C-14 5700 a, Rn-222 3,82 d, U-238 4,47e9 a.
The simulation's model values (koe 1–3) come from the same seeded generator as assets/sims/fy8/fy8-9/sim.js
(mulberry32, seed 1000 · series + 42, lifetime τ = -T½/ln 2 · ln u for each nucleus). The two fitting data sets are
simulated example data (Poisson counts, seeded), never measurements; figures.py imports them from here.
Prints {id: number} as JSON on the last line."""
import json, math, random

LN2 = math.log(2)
a = {}

# ---------------------------------------------------------------- the simulation's model (same as sim.js)
M = 0xFFFFFFFF
def _i32(x):
    x &= M
    return x - 0x100000000 if x >= 0x80000000 else x
def _imul(x, y): return _i32((x & M) * (y & M))
def rng(seed):
    """mulberry32 exactly as sim.js: uniform numbers in (0, 1)."""
    st = [seed & M]
    def r():
        st[0] = (st[0] + 0x6D2B79F5) & M
        t = _imul(st[0] ^ (st[0] >> 15), st[0] | 1) & M
        t = _i32(t ^ (t + _imul(t ^ (t >> 7), t | 61))) & M
        return (((t ^ (t >> 14)) & M) + 0.5) / 4294967297
    return r
def lifetimes(series, T, n=1600):
    R = rng(1000 * series + 42)
    return [-T / LN2 * math.log(R()) for _ in range(n)]
def N_left(series, N0, T, t):
    return sum(1 for x in lifetimes(series, T)[:N0] if x > t)

# Koe 1 and prediction 1: N0 = 1600, T½ = 20 s, series 1: N at t = 0, 20, 40, 60 s -> 1600, 792, 399, 208
for t in (0, 20, 40, 60, 80):
    a[f"koe1-N-{t}"] = N_left(1, 1600, 20, t)
    a[f"koe1-f-{t}"] = N_left(1, 1600, 20, t) / 1600          # 1; 0,495; 0,249; 0,130
    a[f"koe1-model-{t}"] = 1600 * 0.5 ** (t / 20)             # 1600, 800, 400, 200 (the dashed curve)
# Koe 2 and prediction 2: N0 = 20, t = T½ = 20 s, series 1–5 -> 7, 12, 13, 7, 10 (fractions 0,35 ... 0,65)
for s in range(1, 6):
    a[f"koe2-N-s{s}"] = N_left(s, 20, 20, 20)
    a[f"koe2-f-s{s}"] = N_left(s, 20, 20, 20) / 20
# Koe 3: N0 = 1600, t = T½, series 1–5 -> 792, 800, 783, 815, 805 (fractions 0,489 ... 0,509)
for s in range(1, 6):
    a[f"koe3-N-s{s}"] = N_left(s, 1600, 20, 20)
    a[f"koe3-f-s{s}"] = N_left(s, 1600, 20, 20) / 1600
# the spread in the fraction: 20 nuclei 0,35–0,65, 1600 nuclei 0,489–0,509
a["koe2-spread"] = max(a[f"koe2-f-s{s}"] for s in range(1, 6)) - min(a[f"koe2-f-s{s}"] for s in range(1, 6))   # 0,30
a["koe3-spread"] = max(a[f"koe3-f-s{s}"] for s in range(1, 6)) - min(a[f"koe3-f-s{s}"] for s in range(1, 6))   # 0,020
# Prediction 1 wrong options: linear decay (all gone at 2 T½), "half of the original again" (also 0)
a["ennuste1-quarter"] = 1000 * 0.5 ** 2                       # 250 of 1000 after two half-lives

# ---------------------------------------------------------------- theory (Ydinajatus, Kaava)
# Figure ydin: 100 nuclei, about half left after T½ and a quarter after 2 T½ (figures.py draws a random sample)
# Kaava figure: N/N0 = 1/2, 1/4, 1/8, 1/16 at 1, 2, 3, 4 half-lives
for k in range(1, 5): a[f"halves-{k}"] = 0.5 ** k
# λ = ln 2 / T½ and the e-form: e^(-λ T½) = 1/2
a["ln2"] = LN2                                                # 0,6931
# Tc-99m (6,01 h): λ = ln 2 / (6,01 · 3600 s) = 3,20e-5 1/s
a["tc-lambda"] = LN2 / (6.01 * 3600)                          # 3,204e-5 1/s
# Activity of 1 µg of I-131 is not used; activity example in Kaava: A = λN with N = 1,0e15 Tc-99m nuclei
a["tc-A-1e15"] = a["tc-lambda"] * 1.0e15 / 1e9                # 32,0 GBq -> 3,2e10 Bq
# 25 % per T½ -> after 6 h: Tc-99m 740 MBq -> 370 MBq (hook): one half-life
a["hook-tc"] = 740 * 0.5 ** (6.01 / 6.01)                     # 370 MBq

# ---------------------------------------------------------------- worked example: I-131 capsule
A0, T_I, t_ex = 550, 8.02, 20.0                               # MBq, d, d
a["ex-ratio"] = t_ex / T_I                                    # 2,4938
a["ex-factor"] = 0.5 ** (t_ex / T_I)                          # 0,17750
a["ex-A"] = A0 * 0.5 ** (t_ex / T_I)                          # 97,62 MBq -> 97,6 MBq
a["ex-check-2"] = A0 / 4                                      # 137,5 MBq after 2 T½
a["ex-check-3"] = A0 / 8                                      # 68,75 MBq after 3 T½

# ---------------------------------------------------------------- fitting: simulated counts, least squares A e^(-Ct) + B
def _poisson(R, mu):
    L, k, p = math.exp(-mu), 0, 1.0
    while True:
        p *= R.random()
        if p <= L: return k
        k += 1
def counts(seed, T, R0, B, ts, win=10):
    """Counts in the window [t, t + win] of a source of rate R0 e^(-λt) per second plus background B per second."""
    R, lam = random.Random(seed), LN2 / T
    return [_poisson(R, R0 * math.exp(-lam * t) * (1 - math.exp(-lam * win)) / lam + B * win) for t in ts]
def fit(ts, ys, with_b=True):
    """Unweighted least squares y = A e^(-Ct) + B (or A e^(-Ct)): A and B solved exactly for each C, C by golden section."""
    def solve(C):
        e = [math.exp(-C * t) for t in ts]
        if with_b:
            n, se, see, sy, sey = len(ts), sum(e), sum(x * x for x in e), sum(ys), sum(x * y for x, y in zip(e, ys))
            d = n * see - se * se; A = (n * sey - se * sy) / d; B = (sy - A * se) / n
        else:
            A = sum(x * y for x, y in zip(e, ys)) / sum(x * x for x in e); B = 0.0
        return sum((y - A * x - B) ** 2 for x, y in zip(e, ys)), A, B
    grid = [1e-4 + i * 1e-5 for i in range(10000)]
    i = min(range(len(grid)), key=lambda k: solve(grid[k])[0])
    lo, hi, g = grid[max(i - 1, 0)], grid[min(i + 1, len(grid) - 1)], (math.sqrt(5) - 1) / 2
    for _ in range(200):
        c1, c2 = hi - g * (hi - lo), lo + g * (hi - lo)
        if solve(c1)[0] < solve(c2)[0]: hi = c2
        else: lo = c1
    C = (lo + hi) / 2; s, A, B = solve(C)
    return C, A, B, math.sqrt(s / len(ts))

# Theory figure (Kaava, fitting): Ba-137m, T½ = 2,552 min = 153,12 s, counts per 10 s every 60 s, 0–900 s
BA_T = 2.552 * 60
BA_TS = list(range(0, 901, 60))
BA_Y = counts(54, BA_T, 25, 0.5, BA_TS)
C, A, B, rmse = fit(BA_TS, BA_Y)
a["ba-T-lit"] = BA_T                                          # 153,12 s
a["ba-C"] = C                                                 # 0,004564 1/s
a["ba-A"] = A; a["ba-B"] = B; a["ba-rmse"] = rmse             # 249,8; 4,77 counts / 10 s
a["ba-T-fit"] = LN2 / C                                       # 151,9 s
a["ba-diff-pct"] = 100 * (LN2 / C - BA_T) / BA_T              # -0,8 %
for t, y in zip(BA_TS, BA_Y): a[f"ba-y-{t}"] = y

# Sovella (interpret): Pa-234m, T½ = 1,159 min = 69,54 s, counts per 10 s every 20 s, 0–400 s
PA_T = 1.159 * 60
PA_TS = list(range(0, 401, 20))
PA_Y = counts(22, PA_T, 40, 0.5, PA_TS)
C, A, B, rmse = fit(PA_TS, PA_Y)
a["pa-T-lit"] = PA_T                                          # 69,54 s
a["pa-C"] = C                                                 # 0,01013 1/s
a["pa-A"] = A; a["pa-B"] = B; a["pa-rmse"] = rmse             # 376,6; 5,54; 4,50
a["pa-T-fit"] = LN2 / C                                       # 68,45 s -> 68,4 s (the answer)
a["pa-diff-pct"] = 100 * (LN2 / C - PA_T) / PA_T              # -1,6 %
a["pa-mistake-1/C"] = 1 / C                                   # 98,7 s: T½ = 1/C forgets ln 2
a["pa-mistake-C"] = C                                         # 0,0101: the decay constant itself
C0, A0b, _, _ = fit(PA_TS, PA_Y, with_b=False)
a["pa-mistake-noB"] = LN2 / C0                                # 71,8 s: a fit without the background term
a["pa-B-per-s"] = B / 10                                      # 0,55 counts/s background from the fit
for t, y in zip(PA_TS, PA_Y): a[f"pa-y-{t}"] = y

# ---------------------------------------------------------------- Etsi virhe: number of nuclei with λ = 1/T½
A_v, T_v = 2.0e6, 6.01 * 3600                                 # Tc-99m 2,0 MBq
a["virhe-wrong"] = A_v * T_v                                  # 4,33e10: N = A T½ (λ = 1/T½)
a["virhe-right"] = A_v * T_v / LN2                            # 6,24e10: N = A T½ / ln 2

# ---------------------------------------------------------------- Tarkista 2: graph of an unknown sample, 720 kBq, T½ = 5,0 h
CHK_A0, CHK_T = 720, 5.0
a["check2"] = CHK_T                                           # read off: 360 kBq at 5,0 h
a["check2-180"] = 2 * CHK_T                                   # 180 kBq at 10 h (the check)
a["check2-mistake-quarter"] = 2 * CHK_T                       # 10 h read at 180 kBq (a quarter)

# ---------------------------------------------------------------- exit ticket
a["exit-1"] = 0.5 ** 3                                        # 6 h with T½ = 2 h: 1/8

if __name__ == "__main__":
    print(json.dumps({k: (round(v, 6) if isinstance(v, float) and abs(v) > 1e-3 else v) for k, v in a.items()}))
