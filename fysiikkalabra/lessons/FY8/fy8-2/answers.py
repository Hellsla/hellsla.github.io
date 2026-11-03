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
a["fy8-2-L2-01"] = h * c / ((-0.85 - (-3.40)) * e) * 1e9   # E4 = -0,85 eV -> E2 = -3,40 eV: ΔE = 2,55 eV, λ = 486,2 nm -> 486 nm
a["fy8-2-L2-02"] = h * c / ((1.85 - 0) * e) * 1e9  # model atom 0; 1,85; 4,00 eV: smallest ΔE = min(1,85; 2,15; 4,00) = 1,85 eV -> 670 nm
a["fy8-2-L2-03"] = h * c / ((-3.40 - (-13.6)) * e) * 1e9   # cold hydrogen n = 1 -> 2: ΔE = 10,2 eV, λ = 121,6 nm -> 122 nm (UV)
a["fy8-2-L2-04"] = h * 5.09e14 / e                 # sodium line f = 5,09e14 Hz: ΔE = hf = 3,3726e-19 J = 2,105 eV -> 2,11 eV
# Level 3: reasoning or an unfamiliar context
a["fy8-2-L3-01"] = h * c / ((0 - (-3.40)) * e) * 1e9       # Balmer limit: from E = 0 (n -> ∞) to E2 = -3,40 eV, λ = 364,7 nm -> 365 nm
a["fy8-2-L3-02"] = h * c / (15.0e-6 * e) * 1000    # CO2 band 15,0 µm: ΔE = hc/λ = 1,3243e-20 J = 0,08267 eV = 82,7 meV
E_in = h * c / (365e-9 * e)                        # cascade: UV photon 365 nm gives 3,3973 eV
a["fy8-2-L3-03"] = h * c / ((E_in - 1.20) * e) * 1e9       # first photon 1,20 eV, second ΔE = 2,1973 eV -> λ = 564,3 nm -> 564 nm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
