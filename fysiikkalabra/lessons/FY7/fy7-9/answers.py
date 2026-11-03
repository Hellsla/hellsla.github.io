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
# Level 2: two steps, a conversion or a rearrangement
a["fy7-9-L2-01"] = b / (450 + 273.15) * 1e6            # pizza oven vault 450 °C = 723,15 K: λ_max = 4,007 µm
# figure fy7-9/spectrum-task: the curve's peak sits on the gridline λ = 1,20 µm
a["fy7-9-L2-02"] = b / 1.20e-6                         # T = b / λ_max = 2415 K -> 2,4 · 10³ K (λ read to two figures)
a["fy7-9-L2-03"] = (b / (27 + 273.15) - b / (327 + 273.15)) * 1e6   # 9,655 µm - 4,829 µm = 4,826 µm
lam = c / 6.0e14                                       # star: peak frequency 6,0 · 10¹⁴ Hz -> λ_max = 5,0 · 10⁻⁷ m
a["fy7-9-L2-04"] = b / lam                             # T = b / λ_max = 5796 K -> 5,8 · 10³ K
# Level 3: reasoning or an unfamiliar context
a["fy7-9-L3-01"] = b / 2.7255 * 1e3                    # CMB 2,7255 K (Fixsen 2009): λ_max = 1,0633 mm (microwaves)
a["fy7-9-L3-02"] = b / 8.0e-6 - 273.15                 # thermal camera 8,0–14 µm: peak at 8,0 µm when T = 362,25 K = 89,1 °C
a["fy7-9-L3-03"] = c * 2.56 / 2 / 1e3                  # lunar laser ranging, round trip 2,56 s: s = c t / 2 = 3,84 · 10⁵ km
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
