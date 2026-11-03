"""Every answer in exercises.json for fy8-13, computed from the task data (python -I answers.py).
D = E / m (Gy = J/kg), H_T = w_R D_T, H_E = sum of w_T H_T, H = Hdot t, Hdot2 = Hdot1 (r1 / r2)^2,
Hdot = Hdot0 (1/2)^(x / d½). Weighting factors ICRP 103 (2007): w_R photons and electrons 1, alpha 20; w_T lungs 0,12,
thyroid 0,04. STUK figures (2023, rounded): radon 4,1 mSv/a at the average indoor concentration 94 Bq/m³; all other
sources 1,8 mSv/a. Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

a = {}
# Level 1: one formula, values given
a["fy8-13-L1-01"] = 0.130 / 65.0 * 1e3                 # 0,130 J in 65,0 kg: D = 0,002 Gy = 2,00 mGy
a["fy8-13-L1-02"] = 20 * 0.30                          # alpha 0,30 mGy, w_R = 20: H = 6,0 mSv
a["fy8-13-L1-03"] = 3.2 * 5.0                          # flight 3,2 µSv/h for 5,0 h: H = 16 µSv
a["fy8-13-L1-04"] = 120 * (1.0 / 4.0) ** 2             # 120 µSv/h at 1,0 m -> at 4,0 m: 7,5 µSv/h
a["fy8-13-L1-05"] = 64 * 0.5 ** (18 / 6.0)             # 64 µSv/h behind 18 mm lead, d½ 6,0 mm: 8,0 µSv/h
# Level 2: two steps, a conversion or a rearrangement
D = 0.60e-3 / 0.020                                    # thyroid 0,60 mJ in 20 g: D = 0,030 Gy = 30 mGy, beta w_R = 1
a["fy8-13-L2-01"] = 0.04 * 1 * D * 1e3                 # H_E = 0,04 · 30 mSv = 1,2 mSv
Hd = 150 * (1.0 / 2.5) ** 2                            # 150 µSv/h at 1,0 m -> 24 µSv/h at 2,5 m
a["fy8-13-L2-02"] = 100 / Hd                           # t = 100 µSv : 24 µSv/h = 4,17 h -> 4,2 h
a["fy8-13-L2-03"] = 4.1 * 300 / 94                     # radon dose ∝ concentration: 13,09 mSv -> 13 mSv
a["fy8-13-L2-04"] = 6.0 * math.log2(96 / 3.0)          # 96 -> 3,0 µSv/h = 1/32 = 5 half-value layers: 30 mm
# Level 3: reasoning or an unfamiliar context
HA = 80 * (1.0 / 2.0) ** 2 * 0.5                       # A: 2,0 m, no shield, 30 min: 20 µSv/h · 0,5 h = 10 µSv
HB = 80 * 0.5 ** (18 / 6.0) * 0.5                      # B: 1,0 m, 18 mm lead, 30 min: 10 µSv/h · 0,5 h = 5,0 µSv
a["fy8-13-L3-01"] = HA - HB                            # B gives 5,0 µSv less
a["fy8-13-L3-02"] = 4.1 * 400 / 94 + 1.8               # 400 Bq/m³: radon 17,45 + others 1,8 = 19,25 mSv -> 19 mSv
a["fy8-13-L3-03"] = 0.12 * 20 * 0.10 + 1 * 0.50        # lungs alpha 0,10 mGy -> 0,24 mSv; whole body gamma 0,50 mGy -> 0,50: 0,74 mSv
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
