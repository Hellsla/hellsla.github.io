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
a["fy8-8-L1-06"] = "Beeta miinus -hajoaminen, koska ytimessä neutroni muuttuu protoniksi ja elektroni lähtee pois"   # MC: beta-minus gives Z + 1, A unchanged
a["fy8-8-L1-07"] = (226 - 4) - (88 - 2)       # Ra-226 alpha -> Rn-222: N' = 222 - 86 = 136
a["fy8-8-L1-08"] = 27 + 1                     # Co-60 beta-minus -> Ni-60* (Z = 28); gamma leaves Z unchanged
# Level 2
a["fy8-8-L2-01"] = lam_pm(2505.8 - 1332.5)    # Ni-60 levels 2505,8 (ENSDF 2505,753) -> 1332,5 keV: E = 1173,3 keV, lambda = 1,057 pm
a["fy8-8-L2-02"] = 83 + 1 - 2                 # Bi-214 beta-minus -> Po-214 (84), alpha -> Pb-210 (82)
E550 = hc / 550e-9 / e                        # green photon 550 nm: 2,2546 eV
a["fy8-8-L2-03"] = 661.7e3 / E550             # Cs-137 gamma 661,7 keV / 2,2546 eV = 2,935e5
a["fy8-8-L2-04"] = 228 - (90 - 2 + 1 + 1)     # Th-232 -a-> Ra-228 (88) -b-> Ac-228 (89) -b-> Th-228 (90): N = 138
# L2-05: (Z, N, Z', N') of six nuclides; beta-minus raises Z by 1 and lowers N by 1
rows = {"Ra-226": (88, 138, 86, 136), "Pb-210": (82, 128, 83, 127), "Na-22": (11, 11, 10, 12),
        "I-131": (53, 78, 54, 77), "Ba-137 (viritetty)": (56, 81, 56, 81), "Sr-90": (38, 52, 39, 51)}
a["fy8-8-L2-05"] = sum(1 for z, n, z2, n2 in rows.values() if (z2, n2) == (z + 1, n - 1))   # 3 beta-minus decays
a["fy8-8-L2-06"] = 237 - (95 - 2)             # Am-241 alpha -> Np-237 with Z' = 93: N' = 144
# L2-07: least-squares line E = k K + b through the calibration points, read at channel 1531
K = [98, 1104, 1961, 2227]; EK = [59.54, 661.7, 1173.2, 1332.5]
mK, mE = sum(K) / 4, sum(EK) / 4
k = sum((x - mK) * (y - mE) for x, y in zip(K, EK)) / sum((x - mK) ** 2 for x in K)   # 0,5978 keV per channel
b = mE - k * mK                               # 1,199 keV
a["fy8-8-L2-07"] = k * 1531 + b               # 916,4 keV
# Level 3
n_alpha = (232 - 208) // 4                    # Th-232 -> Pb-208: 6 alpha decays
a["fy8-8-L3-01"] = 82 - (90 - 2 * n_alpha)    # Z: 90 - 12 + n_beta = 82 -> 4 beta-minus decays
a["fy8-8-L3-02"] = lam_pm(1000.0)             # levels 0; 0,40; 1,00 MeV: largest gamma 1,00 MeV -> 1,240 pm
a["fy8-8-L3-03"] = 86 + 2 - 1                 # X -b-> Y -a-> Rn-222 (86): Y has Z 88, X has Z 87
# L3-04: Rn-222 (222, 86) -> Pb-206 (206, 82): alphas from A, betas from Z
nal = (222 - 206) // 4                        # 4 alpha decays
a["fy8-8-L3-04"] = 82 - 86 + 2 * nal          # Z: 86 - 8 + n_beta = 82 -> 4 beta-minus decays
# L3-05: levels 351,2; 820,5; 1501,4 keV; missing line is 1501,4 - 351,2 = 1150,2 keV
a["fy8-8-L3-05"] = lam_pm(1501.4 - 351.2)     # 1,078 pm
print(json.dumps({i: (round(v, 6) if not isinstance(v, str) else v) for i, v in a.items()}, ensure_ascii=False))
