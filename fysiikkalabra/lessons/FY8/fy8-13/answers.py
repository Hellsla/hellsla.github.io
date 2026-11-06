"""Every answer in exercises.json for fy8-13, computed from the task data (python -I answers.py).
D = E / m (Gy = J/kg), H_T = w_R D_T, H_E = sum of w_T H_T, H = Hdot t, Hdot2 = Hdot1 (r1 / r2)^2,
Hdot = Hdot0 (1/2)^(x / d½). Weighting factors ICRP 103 (2007): w_R photons and electrons 1, alpha 20; w_T lungs 0,12,
thyroid 0,04. STUK figures (STUK-A263, 2020, rounded): radon about 4,0 mSv/a at the average indoor concentration
94 Bq/m³; all other sources 5,9 - 4,0 = 1,9 mSv/a. Flight: a typical long-haul cruise dose rate of about 3 µSv/h.
Shield: d½ is the puoliintumispaksuus, d the thickness. Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

a = {}
# Level 1: one formula, values given
a["fy8-13-L1-01"] = 0.130 / 65.0 * 1e3                 # 0,130 J in 65,0 kg: D = 0,002 Gy = 2,00 mGy
a["fy8-13-L1-02"] = 20 * 0.30                          # alpha 0,30 mGy, w_R = 20: H = 6,0 mSv
a["fy8-13-L1-03"] = 3.0 * 5.0                          # flight about 3 µSv/h for 5,0 h: H = 15 µSv
a["fy8-13-L1-04"] = 120 * (1.0 / 4.0) ** 2             # 120 µSv/h at 1,0 m -> at 4,0 m: 7,5 µSv/h
a["fy8-13-L1-05"] = 64 * 0.5 ** (18 / 6.0)             # 64 µSv/h behind 18 mm lead, d½ 6,0 mm: 8,0 µSv/h
# Level 2: two steps, a conversion or a rearrangement
D = 0.60e-3 / 0.020                                    # thyroid 0,60 mJ in 20 g: D = 0,030 Gy = 30 mGy, beta w_R = 1
a["fy8-13-L2-01"] = 0.04 * 1 * D * 1e3                 # H_E = 0,04 · 30 mSv = 1,2 mSv
Hd = 150 * (1.0 / 2.5) ** 2                            # 150 µSv/h at 1,0 m -> 24 µSv/h at 2,5 m
a["fy8-13-L2-02"] = 100 / Hd                           # t = 100 µSv : 24 µSv/h = 4,17 h -> 4,2 h
a["fy8-13-L2-03"] = 4.0 * 300 / 94                     # radon dose ∝ concentration: 12,77 mSv -> 13 mSv
a["fy8-13-L2-04"] = 6.0 * math.log2(96 / 3.0)          # 96 -> 3,0 µSv/h = 1/32 = 5 half-value layers: 30 mm
# Level 3: reasoning or an unfamiliar context
HA = 80 * (1.0 / 2.0) ** 2 * 0.5                       # A: 2,0 m, no shield, 30 min: 20 µSv/h · 0,5 h = 10 µSv
HB = 80 * 0.5 ** (18 / 6.0) * 0.5                      # B: 1,0 m, 18 mm lead, 30 min: 10 µSv/h · 0,5 h = 5,0 µSv
a["fy8-13-L3-01"] = HA - HB                            # H_A - H_B = +5,0 µSv: B gives the smaller dose
a["fy8-13-L3-02"] = 4.0 * 400 / 94 + 1.9               # 400 Bq/m³: radon 17,02 + others 1,9 = 18,92 mSv -> 19 mSv
a["fy8-13-L3-03"] = 0.12 * 20 * 0.10 + 1 * 0.50        # lungs alpha 0,10 mGy -> 0,24 mSv; whole body gamma 0,50 mGy -> 0,50: 0,74 mSv
# Exercise-bank additions (L1-06 is a multiple-choice task: no number)
a["fy8-13-L1-07"] = 0.04 * 2.0 + 0.12 * 1.0            # liver 0,04 · 2,0 + stomach 0,12 · 1,0 = 0,080 + 0,12 = 0,20 mSv
a["fy8-13-L1-08"] = 0.10 / 5.9 * 100                   # chest X-ray 0,10 mSv of 5,9 mSv: 1,69 % -> 1,7 %
a["fy8-13-L2-05"] = 4.0 / (4.0 + 1.1 + 0.8) * 100   # radon 4,0 + other natural 1,1 + medical 0,8 = sum 5,9 mSv; radon share 4,0 / 5,9 = 67,8 % -> 68 %
k = [r * r * h for r, h in [(0.50, 410), (1.00, 98.0), (1.50, 44.0), (2.00, 26.0)]]   # H r^2: 102,5; 98,0; 99,0; 104,0
a["fy8-13-L2-06"] = sum(k) / len(k) / 3.0 ** 2         # k_ka = 100,875 (sum 403,5 / 4); H(3,0 m) = 11,2 µSv/h
a["fy8-13-L2-07"] = 20 * 0.63e-3 / 1.8 * 1e3           # liver 0,63 mJ in 1,8 kg: D = 0,35 mGy; alpha w_R = 20: 7,0 mSv
cm = (380 + 260 + 140 + 300) / 4                       # sum 1080 / 4 = 270 Bq/m³ (annual mean); dose now 4,0 · 270/94 · 0,80 = 9,19 mSv
a["fy8-13-L3-04"] = 2.0 / (4.0 * 0.80) * 94            # target 2,0 mSv: c = 2,0 / (4,0 · 0,80) · 94 = 58,75 Bq/m³ -> 59
# fy8-13-L2-08 is a multiple-choice task (no number): 12 · 6 · 9,0 h = 648 h; 3,0 µSv/h · 648 h = 1944 µSv ≈ 2 mSv
Hd5 = 240 * (1.0 / 2.0) ** 2 * 0.5 ** (10 / 4.0)       # 240 µSv/h at 1,0 m, 2,0 m, 10 cm concrete d½ 4,0 cm: 10,61 µSv/h
a["fy8-13-L3-05"] = 25 / Hd5                           # t = 25 µSv : 10,61 µSv/h = 2,357 h -> 2,4 h
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
