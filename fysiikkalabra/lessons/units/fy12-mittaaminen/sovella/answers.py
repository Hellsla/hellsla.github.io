"""fy12-mittaaminen Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python3 scripts/practice.py check units/fy12-mittaaminen` compares them with tasks.json.
All data are invented example data (tasks.json "source": "example"), made in this file's way: a model plus small noise."""
import json, math


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def extremes(x, y, dy, k_lo, k_hi, step):
    """The shallowest and the steepest slope of a line that still passes through every vertical bar y ± dy."""
    ok = []
    for i in range(int(k_lo / step), int(k_hi / step) + 1):
        k = i * step
        lo = max(b - k * a - d for a, b, d in zip(x, y, dy)); hi = min(b - k * a + d for a, b, d in zip(x, y, dy))
        if lo <= hi: ok.append((k, (lo + hi) / 2))
    return ok[0], ok[-1]


out = {}
# s1: 100 m hand-timed by three timers; track measured with a measuring wheel, 100,0 m ± 0,3 m
s, ds = 100.0, 0.3
tL = [13.52, 13.90, 13.71]                                     # Liisa, s
tM = [13.80, 14.12, 13.96]                                     # Mira, s
tLm = sum(tL) / 3; dtL = (max(tL) - min(tL)) / 2
tMm = sum(tM) / 3; dtM = (max(tM) - min(tM)) / 2
v = s / tLm
v_max = (s + ds) / (tLm - dtL); v_min = (s - ds) / (tLm + dtL)
dv = (v_max - v_min) / 2
rel = dtL / tLm + ds / s                                       # Hyväksytään myös: the relative uncertainties added
out.update({"fy12-mittaaminen-s1-a-ms": round(v, 4), "fy12-mittaaminen-s1-a-kmh": round(v * 3.6, 3),
            "fy12-mittaaminen-s1-tL": round(tLm, 4), "fy12-mittaaminen-s1-dtL": round(dtL, 4),
            "fy12-mittaaminen-s1-b": round(dv, 4), "fy12-mittaaminen-s1-vmax": round(v_max, 4), "fy12-mittaaminen-s1-vmin": round(v_min, 4),
            "fy12-mittaaminen-s1-rel": round(rel * 100, 3), "fy12-mittaaminen-s1-dv-rel": round(rel * v, 4),
            "fy12-mittaaminen-s1-tM": round(tMm, 4), "fy12-mittaaminen-s1-dtM": round(dtM, 4)})

# s2: a ream of copy paper, 500 A4 sheets (210 mm × 297 mm), height 51 mm ± 1 mm, mass 2,49 kg
N, h, dh, M = 500, 51e-3, 1e-3, 2.49
d = h / N; dd = dh / N
A = 0.210 * 0.297; A_all = N * A
sigma = M / A_all                                              # kg/m²
rho = sigma / d
drho = rho * dd / d
out.update({"fy12-mittaaminen-s2-a": round(d * 1e6, 3), "fy12-mittaaminen-s2-a-dd": round(dd * 1e6, 3),
            "fy12-mittaaminen-s2-A": round(A, 6), "fy12-mittaaminen-s2-Aall": round(A_all, 4),
            "fy12-mittaaminen-s2-b": round(sigma * 1000, 3), "fy12-mittaaminen-s2-c": round(rho, 2),
            "fy12-mittaaminen-s2-c-drho": round(drho, 2), "fy12-mittaaminen-s2-one-sheet": round(0.5e-3 / d * 100, 1)})

# s3: an unknown liquid in a measuring cylinder; total mass of cylinder and liquid; row 60 ml written down from memory
V3 = [20, 30, 40, 50, 60, 70, 80, 90, 100]                    # cm³ (= ml)
m3 = [137.6, 145.7, 155.7, 163.9, 183.4, 183.0, 191.8, 202.0, 210.3]   # g
keep = [i for i, v_ in enumerate(V3) if v_ != 60]
Vk = [V3[i] for i in keep]; mk = [m3[i] for i in keep]
k3, b3 = fit(Vk, mk)
k3a, b3a = fit(V3, m3)                                         # with the doubtful row
dV = 1.0                                                      # ml: half of the 2 ml division
(klo, blo), (khi, bhi) = extremes(Vk, mk, [k3 * dV] * len(Vk), 0.85, 1.0, 0.0001)
dk3 = (khi - klo) / 2
# the two far-apart points read from the drawn line in the solution
p1, p2 = (20, 137.0), (100, 210.5)
k3_read = (p2[1] - p1[1]) / (p2[0] - p1[0]); b3_read = p1[1] - k3_read * p1[0]
m15 = k3_read * 1500                                          # g of 1,50 l
out.update({"fy12-mittaaminen-s3-c-rho": round(k3_read, 4), "fy12-mittaaminen-s3-c-m0": round(b3_read, 2),
            "fy12-mittaaminen-s3-fit-k": round(k3, 4), "fy12-mittaaminen-s3-fit-b": round(b3, 2),
            "fy12-mittaaminen-s3-fit-k-all": round(k3a, 4), "fy12-mittaaminen-s3-fit-b-all": round(b3a, 2),
            "fy12-mittaaminen-s3-row60-expected": round(k3 * 60 + b3, 1), "fy12-mittaaminen-s3-row60-volume": round((183.4 - b3) / k3, 1),
            "fy12-mittaaminen-s3-kmin": round(klo, 4), "fy12-mittaaminen-s3-kmax": round(khi, 4), "fy12-mittaaminen-s3-dk": round(dk3, 4),
            "fy12-mittaaminen-s3-e": round(m15 / 1000, 4)})

# s4: a kitchen scale checked with calibrated weights, three readings each
true4 = [100.0, 200.0, 500.0, 1000.0]
read4 = [[102, 101, 102], [204, 204, 205], [510, 511, 510], [1020, 1021, 1020]]
mean4 = [sum(r) / 3 for r in read4]
ratio4 = [m_ / t_ for m_, t_ in zip(mean4, true4)]
k4, b4 = fit(true4, mean4)
corr = 765 / k4
out.update({"fy12-mittaaminen-s4-ratio-1000": round(ratio4[-1], 4), "fy12-mittaaminen-s4-k": round(k4, 4), "fy12-mittaaminen-s4-b": round(b4, 2),
            "fy12-mittaaminen-s4-b-765": round(corr, 1), "fy12-mittaaminen-s4-ratios": [round(r, 4) for r in ratio4]})

# s5: a toy car on video, x = 0,35 m + 0,48 m/s · t plus noise; the point at 1,5 s was clicked on the wrong frame
t5 = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
x5 = [0.35, 0.61, 0.83, 1.32, 1.30, 1.57, 1.78]
k5 = [i for i, t_ in enumerate(t5) if t_ != 1.5]
k5f, b5f = fit([t5[i] for i in k5], [x5[i] for i in k5])
k5a, b5a = fit(t5, x5)
k5o = sum(t5[i] * x5[i] for i in k5) / sum(t5[i] ** 2 for i in k5)    # the report's line forced through the origin
v_last = (x5[-1] - x5[-2]) / 0.5
dx5 = 0.03                                                    # m: the clicking uncertainty assumed in the solution
(k5lo, _), (k5hi, _) = extremes([t5[i] for i in k5], [x5[i] for i in k5], [dx5] * len(k5), 0.3, 0.7, 0.0005)
out.update({"fy12-mittaaminen-s5-b": round(k5f, 4), "fy12-mittaaminen-s5-b0": round(b5f, 3), "fy12-mittaaminen-s5-fit-all": round(k5a, 4),
            "fy12-mittaaminen-s5-origin": round(k5o, 4), "fy12-mittaaminen-s5-last": round(v_last, 3),
            "fy12-mittaaminen-s5-expected-1.5": round(b5f + 1.5 * k5f, 3), "fy12-mittaaminen-s5-kmin": round(k5lo, 4),
            "fy12-mittaaminen-s5-kmax": round(k5hi, 4), "fy12-mittaaminen-s5-dk": round((k5hi - k5lo) / 2, 4)})

# s6: air in a syringe with a pressure sensor; the hose adds V0 = 1,8 ml; slow compression at 22 °C
R, T6 = 8.314, 22.0 + 273.15
V6 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]                 # ml, syringe scale
p6 = [189.1, 164.5, 146.6, 131.9, 119.2, 109.6, 101.2, 93.5, 87.6, 81.8]   # kPa
pV = [p_ * v_ for p_, v_ in zip(p6, V6)]                      # kPa·ml
inv = [1000 / p_ for p_ in p6]                                # 1/MPa
k6, b6 = fit(inv, V6)                                         # V = k6 · (1/p) + b6: k6 in MPa·ml = J, b6 = −V0
V0 = -b6
n6 = k6 / (R * T6)
pV0 = [p_ * (v_ + V0) for p_, v_ in zip(p6, V6)]
out.update({"fy12-mittaaminen-s6-pV-first": round(pV[0]), "fy12-mittaaminen-s6-pV-last": round(pV[-1]),
            "fy12-mittaaminen-s6-pV-change": round((pV[-1] - pV[0]) / pV[0] * 100, 2),
            "fy12-mittaaminen-s6-inv-first": round(inv[0], 3), "fy12-mittaaminen-s6-inv-last": round(inv[-1], 3),
            "fy12-mittaaminen-s6-k": round(k6, 4), "fy12-mittaaminen-s6-c-V0": round(V0, 3), "fy12-mittaaminen-s6-c-n": round(n6, 7),
            "fy12-mittaaminen-s6-pV0-first": round(pV0[0]), "fy12-mittaaminen-s6-pV0-last": round(pV0[-1]),
            "fy12-mittaaminen-s6-T": round(T6, 2),
            # the solution reads (4,0 1/MPa; 8,6 ml) and (12,0 1/MPa; 29,5 ml) off the drawn line
            "fy12-mittaaminen-s6-C-read": round((29.5 - 8.6) / 8.0, 4), "fy12-mittaaminen-s6-n-read": round((29.5 - 8.6) / 8.0 / (R * T6), 7)})

out = {k_: v_ for k_, v_ in out.items() if not isinstance(v_, list)}
print(json.dumps(out))
