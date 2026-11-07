"""Every answer in exercises.json for fy7-9, computed from the task data (python -I answers.py).
Wave relation c = f λ with c = 3,00 · 10⁸ m/s; Wien's displacement law λ_max T = b with b = 2,898 · 10⁻³ m·K
(T the absolute temperature, T = t + 273,15 K). Prints {exercise id: number} as JSON on the last line."""
import json

c, b = 3.00e8, 2.898e-3
a = {}
# Level 1: one formula, values given
a["fy7-9-L1-01"] = c / 94.0e6                          # FM radio 94,0 MHz: λ = c / f = 3,191 m
a["fy7-9-L1-02"] = c / 2.45e9 * 100                    # microwave oven 2,45 GHz: λ = 0,1224 m = 12,24 cm
a["fy7-9-L1-03"] = b / 307 * 1e6                       # skin 307 K: λ_max = b / T = 9,440 · 10⁻⁶ m = 9,44 µm
a["fy7-9-L1-04"] = b / 290e-9                          # star, peak 290 nm: T = b / λ_max = 9993 K -> 1,0 · 10⁴ K
a["fy7-9-L1-05"] = c / 532e-9 / 1e12                   # green laser 532 nm: f = c / λ = 5,639 · 10¹⁴ Hz = 563,9 THz
a["fy7-9-L1-07"] = 2.02e7 / c * 1e3                    # GPS satellite 20 200 km: t = s / c = 0,06733 s = 67,33 ms
a["fy7-9-L1-08"] = c / 3.5e9 * 100                     # 5G band 3,5 GHz: λ = c / f = 0,08571 m = 8,571 cm
# fy7-9-L1-06 is a multiple-choice task (no number)
# Level 2: two steps, a conversion or a rearrangement
a["fy7-9-L2-01"] = b / (450 + 273.15) * 1e6            # pizza oven vault 450 °C = 723,15 K: λ_max = 4,007 µm
# figure fy7-9/spectrum-task: the curve's peak sits on the gridline λ = 1,20 µm
a["fy7-9-L2-02"] = b / 1.20e-6                         # T = b / λ_max = 2415 K -> 2,4 · 10³ K (λ read to two figures)
a["fy7-9-L2-03"] = (b / (27 + 273.15) - b / (327 + 273.15)) * 1e6   # 9,655 µm - 4,829 µm = 4,826 µm
lam = c / 6.0e14                                       # star: peak frequency 6,0 · 10¹⁴ Hz -> λ_max = 5,0 · 10⁻⁷ m
a["fy7-9-L2-04"] = b / lam                             # T = b / λ_max = 5796 K -> 5,8 · 10³ K
a["fy7-9-L2-05"] = b / 1.08e-6                         # filament, peak 1,08 µm: T = b / λ_max = 2683 K (flame 1789 K, Sun 5796 K)
a["fy7-9-L2-06"] = b / (1500 + 273.15) * 1e6           # steel 1500 °C = 1773,15 K: λ_max = 1,634 µm (the student's error: 1500 used as kelvins)
# lab data: products λ_max · T in 10⁻³ m·K, then their mean
prod = [T * lam * 1e-3 for T, lam in [(2000, 1.47), (2400, 1.18), (2800, 1.06), (3200, 0.89)]]   # 2,940; 2,832; 2,968; 2,848
a["fy7-9-L2-07"] = sum(prod) / len(prod)               # b_ka = 11,588 / 4 = 2,897 (·10⁻³ m·K)
# fy7-9-L2-08 is a data multiple choice (no number): T4 / T1 = 4,10 / 2,90 = 1,41 (707 K -> 999 K); settings 2 and 3 differ 0,05 µm < ±0,10 µm
# Level 3: reasoning or an unfamiliar context
a["fy7-9-L3-01"] = b / 2.7255 * 1e3                    # CMB 2,7255 K (Fixsen 2009): λ_max = 1,0633 mm (microwaves)
a["fy7-9-L3-02"] = b / 8.0e-6 - 273.15                 # thermal camera 8,0–14 µm: peak at 8,0 µm when T = 362,25 K = 89,1 °C
a["fy7-9-L3-03"] = c * 2.56 / 2 / 1e3                  # lunar laser ranging, round trip 2,56 s: s = c t / 2 = 3,84 · 10⁵ km
a["fy7-9-L3-04"] = (b / 260e-9) / (b / 830e-9)         # stars A (830 nm) and C (260 nm): T_C / T_A = 11146 K / 3492 K = 3,192
Ts = [b / lam * 1e6 for lam in (1.80, 2.05, 2.35, 2.75)]   # cooling rod: 1610, 1414, 1233, 1054 K at t = 0, 4, 8, 12 min
rate = (Ts[0] - Ts[-1]) / 12                           # mean cooling rate 46,3 K/min
a["fy7-9-L3-05"] = 12 + (Ts[-1] - 800) / rate          # glow ends (T = 800 K) at 12 min + 5,5 min = 17,5 min
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
