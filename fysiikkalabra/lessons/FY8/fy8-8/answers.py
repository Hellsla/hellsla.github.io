"""Every answer in exercises.json for fy8-8, computed from the task data (python -I answers.py).
Decay equations conserve the mass number A and the charge number Z; a gamma photon has E = hf = hc / lambda,
1 keV = 1000 eV, 1 eV = 1,602 · 10⁻¹⁹ J. Nuclide data: NNDC NuDat 3 (ENSDF).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19      # J s, m/s, J per eV
hc = h * c                                    # 1,9865e-25 J m
def lam_pm(E_keV): return hc / (E_keV * 1e3 * e) * 1e12   # gamma wavelength in pm

a = {}
# Level 1
a["fy8-8-L1-01"] = 235 - 92                   # U-235: N = A - Z = 143
a["fy8-8-L1-02"] = 222 - 4                    # Rn-222 alpha: A' = A - 4 = 218
a["fy8-8-L1-03"] = 6 + 1                      # C-14 beta-minus: Z' = Z + 1 = 7 (nitrogen)
a["fy8-8-L1-04"] = lam_pm(59.54)              # Am-241 gamma 59,54 keV: lambda = 20,83 pm
a["fy8-8-L1-05"] = 18 - (9 - 1)               # F-18 beta-plus: Z' = 8, A' = 18, N' = 10
# Level 2
a["fy8-8-L2-01"] = lam_pm(2505.7 - 1332.5)    # Ni-60 levels 2505,7 -> 1332,5 keV: E = 1173,2 keV, lambda = 1,057 pm
a["fy8-8-L2-02"] = 83 + 1 - 2                 # Bi-214 beta-minus -> Po-214 (84), alpha -> Pb-210 (82)
E550 = hc / 550e-9 / e                        # green photon 550 nm: 2,2546 eV
a["fy8-8-L2-03"] = 661.7e3 / E550             # Cs-137 gamma 661,7 keV / 2,2546 eV = 2,935e5
a["fy8-8-L2-04"] = 228 - (90 - 2 + 1 + 1)     # Th-232 -a-> Ra-228 (88) -b-> Ac-228 (89) -b-> Th-228 (90): N = 138
# Level 3
n_alpha = (232 - 208) // 4                    # Th-232 -> Pb-208: 6 alpha decays
a["fy8-8-L3-01"] = 82 - (90 - 2 * n_alpha)    # Z: 90 - 12 + n_beta = 82 -> 4 beta-minus decays
a["fy8-8-L3-02"] = lam_pm(1000.0)             # levels 0; 0,40; 1,00 MeV: largest gamma 1,00 MeV -> 1,240 pm
a["fy8-8-L3-03"] = 86 + 2 - 1                 # X -b-> Y -a-> Rn-222 (86): Y has Z 88, X has Z 87
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
