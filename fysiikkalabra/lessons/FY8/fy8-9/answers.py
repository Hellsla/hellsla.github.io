"""Every answer in exercises.json for fy8-9, computed from the task data (python -I answers.py).
Decay law N = N0 (1/2)^(t/T½) = N0 e^(-λt), λ = ln 2 / T½, activity A = λN (A, N and mass follow the same law).
Half-lives as in the lesson's table (NNDC NuDat 3, rounded): Tc-99m 6,01 h, Rn-222 3,82 d, Cs-137 30,1 a,
Co-60 5,27 a, I-131 8,02 d, F-18 110 min, Am-241 433 a, C-14 5700 a; 1 a = 365,25 d.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

LN2 = math.log(2)
DAY, YEAR = 24 * 3600, 365.25 * 24 * 3600          # s
a = {}
# Level 1: one formula, values given
a["fy8-9-L1-01"] = 740 * 0.5 ** (18.0 / 6.01)       # Tc-99m 740 MBq, 18,0 h, T½ 6,01 h: A = 92,82 MBq -> 92,8 MBq
a["fy8-9-L1-02"] = 100 * 0.5 ** (10.0 / 3.82)       # Rn-222 sealed 10,0 d, T½ 3,82 d: 16,28 % left -> 16,3 %
a["fy8-9-L1-03"] = LN2 / 30.1                       # Cs-137 λ = ln 2 / 30,1 a = 0,023028 1/a -> 0,0230 1/a
a["fy8-9-L1-04"] = 4.17e-9 * 3.20e12 / 1e3          # Co-60 N = 3,20e12, λ = 4,17e-9 1/s: A = 13 344 Bq -> 13,3 kBq
a["fy8-9-L1-05"] = 48.0 / 2                         # 800 kBq -> 200 kBq in 48,0 h: two halvings, T½ = 24,0 h
# Level 2: two steps, a conversion or a rearrangement
a["fy8-9-L2-01"] = LN2 / (8.02 * DAY) * 1e6         # I-131 λ in 1/s: 8,02 d = 692 928 s, λ = 1,00032e-6 -> 1,00 · 10⁻⁶ 1/s
a["fy8-9-L2-02"] = 37e3 / (LN2 / (433 * YEAR)) / 1e14   # Am-241 37 kBq: λ = 5,0727e-11 1/s, N = 7,294e14 -> 7,3 · 10¹⁴
a["fy8-9-L2-03"] = 2.00 * 0.5 ** ((2 * 60 + 30) / 110) * 1000   # F-18 2,00 GBq, 2 h 30 min = 150 min, T½ 110 min: 777 MBq
a["fy8-9-L2-04"] = 5.00 * 0.5 ** (15.0 / 5.27)      # Co-60 5,00 mg, 15,0 a, T½ 5,27 a: 0,6943 mg -> 0,694 mg
# Level 3: reasoning or an unfamiliar context
a["fy8-9-L3-01"] = 5700 * math.log(1 / 0.380) / LN2 # C-14 activity 38,0 % of a living sample: t = T½ log2(1/0,380) = 7957 a
net0, net1 = 820 - 30, 230 - 30                     # GM counter 820 and 230 pulses/min, background 30 pulses/min
a["fy8-9-L3-02"] = 10.0 * LN2 / math.log(net0 / net1)   # net 790 -> 200 in 10,0 min: T½ = 5,045 min -> 5,05 min
I = 0.5 ** (30.0 / 8.02); Cs = 0.5 ** (30.0 / (30.1 * 365.25))   # equal activities at first, after 30,0 d
a["fy8-9-L3-03"] = 100 * I / (I + Cs)               # I-131 share of the total activity: 6,96 %
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
