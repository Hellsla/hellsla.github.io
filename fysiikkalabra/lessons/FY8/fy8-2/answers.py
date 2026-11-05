"""Every answer in exercises.json for fy8-2, computed from the task data (python -I answers.py).
A photon emitted or absorbed in a transition carries the difference of two energy states: E_y - E_a = hf = hc/λ.
Constants h = 6,626e-34 J s, c = 2,998e8 m/s, 1 eV = 1,602e-19 J (FY8 conventions).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19
a = {}
# Level 1: one formula, values given
a["fy8-2-L1-01"] = h * c / (502e-9 * e)            # helium line 502 nm: ΔE = hc/λ = 3,957e-19 J = 2,470 eV -> 2,47 eV
a["fy8-2-L1-02"] = h * c / (2.86 * e) * 1e9        # levels 2,86 eV apart: λ = hc/ΔE = 4,3356e-7 m -> 434 nm
a["fy8-2-L1-03"] = c / 656e-9 / 1e14               # hydrogen red line 656 nm: f = c/λ = 4,570e14 Hz -> 4,57 · 10¹⁴ Hz
a["fy8-2-L1-04"] = -1.51 - (-3.40)                 # hydrogen levels E3 = -1,51 eV, E2 = -3,40 eV: photon 1,89 eV
a["fy8-2-L1-05"] = h * c / 3.03e-19 * 1e9          # levels 3,03e-19 J apart: λ = hc/ΔE = 6,556e-7 m -> 656 nm
# Level 2: two steps, a conversion or a rearrangement
a["fy8-2-L2-01"] = h * c / ((-0.85 - (-3.40)) * e) * 1e9   # E4 = -0,85 eV -> E2 = -3,40 eV: ΔE = 2,55 eV, λ = 486,27 nm -> 486 nm
a["fy8-2-L2-02"] = h * c / ((1.85 - 0) * e) * 1e9  # model atom 0; 1,85; 4,00 eV: smallest ΔE = min(1,85; 2,15; 4,00) = 1,85 eV -> 670 nm
a["fy8-2-L2-03"] = h * c / ((-3.40 - (-13.6)) * e) * 1e9   # cold hydrogen n = 1 -> 2: ΔE = 10,2 eV, λ = 121,6 nm -> 122 nm (UV)
a["fy8-2-L2-04"] = h * 5.09e14 / e                 # sodium line f = 5,09e14 Hz: ΔE = hf = 3,3726e-19 J = 2,105 eV -> 2,11 eV
# Level 3: reasoning or an unfamiliar context
a["fy8-2-L3-01"] = h * c / ((0 - (-3.40)) * e) * 1e9       # Balmer limit: from E = 0 (n -> ∞) to E2 = -3,40 eV, λ = 364,7 nm -> 365 nm
a["fy8-2-L3-02"] = h * c / (15.0e-6 * e) * 1000    # CO2 band 15,0 µm: ΔE = hc/λ = 1,3243e-20 J = 0,08267 eV = 82,7 meV
E_in = h * c / (365e-9 * e)                        # cascade: UV photon 365 nm gives 3,3973 eV
a["fy8-2-L3-03"] = h * c / ((E_in - 1.20) * e) * 1e9       # first photon 1,20 eV, second ΔE = 2,1973 eV -> λ = 564,3 nm -> 564 nm
# Exercise-bank additions: level 1 (concept tasks have text answers, no number)
# Level 2
a["fy8-2-L2-05"] = h * c / (546.3e-9 * e)          # mercury lamp, green line 546,3 nm: E = hc/λ = 3,6362e-19 J = 2,2698 eV -> 2,27 eV
a["fy8-2-L2-06"] = -3.40 + h * c / (486.0e-9 * e)  # Sun, dark line C 486,0 nm absorbed from n = 2 (-3,40 eV): E_y = -3,40 + 2,5514 = -0,8486 eV -> -0,85 eV
k, b0 = 12.0095, 299.65                            # spectroscope calibration: least-squares line through the four mercury lines, λ = k x + b
a["fy8-2-L2-07"] = k * 16.4 + b0                   # reading x = 16,4 mm: λ = 12,01 · 16,4 + 299,65 = 496,6 nm -> 497 nm
# Level 3
E3 = h * c / (318e-9 * e)                          # model atom, line A 318 nm: E3 = 3,8994 eV (highest level)
EB = h * c / (443e-9 * e)                          # line B 443 nm: E3 - E1 = 2,7991 eV
a["fy8-2-L3-04"] = h * c / ((E3 - EB) * e) * 1e9   # missing line = E1 = E3 - (E3 - E1) = 1,1003 eV, λ = hc/E1 = 1127 nm -> 1130 nm
a["fy8-2-L3-05"] = (1 - 405 / 520) * 100           # dye B: heat share = 1 - λ_abs/λ_fl = 1 - 405/520 = 0,2212 -> 22,1 % (A 18,9 %, C 15,1 %)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
