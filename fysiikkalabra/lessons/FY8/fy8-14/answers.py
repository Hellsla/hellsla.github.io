"""Every answer in exercises.json for fy8-14, computed from the task data (python -I answers.py).
I = I0 (1/2)^(d/d½) layer by layer (d½ the puoliintumispaksuus); A = A0 (1/2)^(t/T½); D = E / m; H = Hdot t;
Hdot2 = Hdot1 (r1/r2)^2; E = m_e c^2 and E = hf = hc / λ. Data as in lesson-answers.py (NIST XCOM half-value
thicknesses, rounded; ICRP 128 dose coefficient of FDG 0,019 mSv/MBq; half-lives Tc-99m 6,01 h, F-18 110 min,
Am-241 432,2 a, C-14 5700 a). Prints {exercise id: number} as JSON on the last line; the lint and the gate compare
it with exercises.json."""
import json, math

a = {}
# Level 1: one formula, values given
a["fy8-14-L1-01"] = 100 * 0.5 ** (6.8 / 3.4)              # 6,8 cm soft tissue, d½ 3,4 cm: 25 % gets through
a["fy8-14-L1-02"] = 600 * 0.5 ** (24.0 / 6.01)            # Tc-99m 600 MBq after 24,0 h: 37,7 MBq -> 38 MBq
a["fy8-14-L1-03"] = 300 * 0.019                           # FDG 300 MBq · 0,019 mSv/MBq = 5,7 mSv
a["fy8-14-L1-04"] = 2.0 * 0.050                           # tumour 50 g gets 2,0 Gy: E = D m = 0,10 J
a["fy8-14-L1-05"] = 37 * 0.5 ** (100 / 432)               # Am-241 37 kBq after 100 a (T½ 432 a as in the task): 31,5 kBq -> 32 kBq
# Level 2: two steps, a conversion or a rearrangement
a["fy8-14-L2-01"] = 5700 * math.log2(0.23 / 0.029)        # C-14 0,029 vs 0,23 Bq/g: 17 030 a -> 17 000 a
a["fy8-14-L2-02"] = 0.73 * math.log2(1200 / 900)          # steel sheet, d½ 0,73 mm, 1200 -> 900 1/s: 0,303 mm
a["fy8-14-L2-03"] = 8.0 / 5.1 * 365                       # body CT 8,0 mSv vs natural 5,1 mSv/a: 572,5 d -> 570 d
a["fy8-14-L2-04"] = 30 * (1.0 / 0.50) ** 2 * 5.0 / 60     # 30 µSv/h at 1,0 m -> 0,50 m for 5,0 min: 10 µSv
# Level 3: reasoning or an unfamiliar context
a["fy8-14-L3-01"] = 30 * 1.3 * 2.0 / 5                    # 5 beams, 30 fractions, entrance 1,3 x the beam's tumour dose: 15,6 Gy
a["fy8-14-L3-02"] = 2 ** (1.0 / 0.27 - 1.0 / 1.8)         # 30 keV, 1,0 cm bone instead of tissue: 8,87 -> 8,9
a["fy8-14-L3-03"] = 3.9 * math.log2(1 / 0.050)            # F-18 511 keV, lead d½ 3,9 mm, down to 5,0 %: 16,9 mm -> 17 mm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
