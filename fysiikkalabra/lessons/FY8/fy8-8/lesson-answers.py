"""Numbers of the lesson text and inquiry.json for fy8-8, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Nuclide data (gamma and level energies, decay modes) from NNDC NuDat 3 (ENSDF).
Prints {id: number} as JSON on the last line."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19
hc = h * c
def lam_pm(E_keV): return hc / (E_keV * 1e3 * e) * 1e12
# U-238 series (NNDC, the main branch): (Z, A, mode) per step; mode 1 alpha, 2 beta-minus, 0 stable
CHAIN = [(92, 238, 1), (90, 234, 2), (91, 234, 2), (92, 234, 1), (90, 230, 1), (88, 226, 1), (86, 222, 1), (84, 218, 1),
         (82, 214, 2), (83, 214, 2), (84, 214, 1), (82, 210, 2), (83, 210, 2), (84, 210, 1), (82, 206, 0)]

a = {}
# the chain obeys the rules alpha (Z-2, A-4), beta- (Z+1, A same), the sim's data
a["chain-ok"] = all((Z2, A2) == ((Z - 2, A - 4) if m == 1 else (Z + 1, A)) for (Z, A, m), (Z2, A2, _) in zip(CHAIN, CHAIN[1:]))
a["chain-alpha"] = sum(m == 1 for _, _, m in CHAIN)          # 8 alpha decays
a["chain-beta"] = sum(m == 2 for _, _, m in CHAIN)           # 6 beta-minus decays
for k, (Z, A, m) in enumerate(CHAIN): a[f"koe-N-{k}"] = A - Z  # N = 146, 144, 143, ...
# lesson.md: nucleus size ratio 10^-10 m / 10^-15 m
a["size-ratio"] = 1e-10 / 1e-15                               # 1e5
# Co-60 -> Ni-60: levels 2505,7 and 1332,5 keV; gammas 1173,2 and 1332,5 keV
a["co-g1"] = 2505.7 - 1332.5                                  # 1173,2 keV
a["co-sum"] = 1173.2 + 1332.5                                 # 2505,7 keV (interpret question)
a["co-g2-pm"] = lam_pm(1332.5)                                # 0,9305 pm
a["ratio-co-visible"] = 1332.5e3 / 2.0                        # gamma vs a 2 eV visible photon: ~ 7e5 ("satojatuhansia")
# worked example: Cs-137 -> Ba-137m, gamma 661,7 keV
a["ex-E-J-e14"] = 661.7e3 * e / 1e-14                         # 1,0600e-14 J
a["ex-lambda-pm"] = lam_pm(661.7)                             # 1,8740 pm
a["ex-ratio-500nm"] = 500e-9 / (lam_pm(661.7) * 1e-12)        # 2,67e5: visible 500 nm is ~ 270 000 times longer
# kertaus: hydrogen 3 -> 2 photon 1,89 eV
a["kert"] = -13.6 / 9 + 13.6 / 4                              # 1,889 eV
# siirto: U-235 -> Pb-207: alpha count and beta count
a["siirto"] = (235 - 207) / 4                                 # 7 alpha
a["siirto-beta"] = 82 - (92 - 2 * 7)                          # 4 beta-minus
a["siirto-m-28"] = 235 - 207                                  # mistake: mass difference 28 taken as the count
a["siirto-m-10"] = 92 - 82                                    # mistake: Z difference 10
# tarkistus-2: Tc-99m 140,5 keV
a["tark2"] = lam_pm(140.5)                                    # 8,825 pm
a["tark2-E-J-e14"] = 140.5e3 * e / 1e-14                       # 2,2508e-14 J
a["tark2-m-eV"] = hc / (140.5 * e) * 1e12                     # mistake: keV taken as eV: 8826 pm = 8,83 nm
a["tark2-ratio-E"] = 661.7 / 140.5                              # 4,71: Cs gamma vs Tc-99m gamma
a["tark2-ratio-l"] = lam_pm(140.5) / lam_pm(661.7)            # 4,71
a["interp-m-diff"] = 1332.5 - 1173.2                          # mistake 159,3 keV
a["siirto-m-5"] = (92 - 82) / 2                               # mistake 5
# exit: Po-210 alpha -> Pb-206; C-14: 6 p, 8 n
a["exit-pb"] = 210 - 4
a["exit-n"] = 14 - 6
print(json.dumps({k: round(v, 6) if isinstance(v, float) else v for k, v in a.items()}))
