"""Every answer in exercises.json for fy8-1, computed from the task data (python -I answers.py).
Photon energy E = hf = hc/λ, photoelectric equation E_k,max = hf − W, threshold λ0 = hc/W, f0 = W/h,
1 eV = 1,602 · 10⁻¹⁹ J, E_k = ½ m v². Prints {exercise id: number} as JSON on the last line."""
import json, math

h, c, e, me = 6.626e-34, 2.998e8, 1.602e-19, 9.109e-31     # J s, m/s, C, kg
a = {}
# Level 1: one formula, values given
a["fy8-1-L1-01"] = h * c / 532e-9                          # green laser 532 nm: E = hc/λ = 3,734e-19 J -> 3,73e-19 J
a["fy8-1-L1-02"] = h * 2.45e9                              # microwave oven 2,45 GHz: E = hf = 1,623e-24 J -> 1,62e-24 J
a["fy8-1-L1-03"] = 3.2e-19 / e                             # 3,2e-19 J in eV: 1,998 eV -> 2,0 eV
a["fy8-1-L1-04"] = h * c / 254e-9 / e                      # UV-C lamp 254 nm: 7,821e-19 J = 4,882 eV -> 4,88 eV
a["fy8-1-L1-05"] = 5.00 - 4.31                             # zinc W = 4,31 eV, photon 5,00 eV: E_k,max = 0,69 eV
# Level 2: two steps, a conversion or a rearrangement
a["fy8-1-L2-01"] = h * c / (2.14 * e) * 1e9                # caesium W = 2,14 eV: λ0 = hc/W = 579,4 nm -> 579 nm
a["fy8-1-L2-02"] = 5.0e-3 / (h * c / 650e-9)               # 5,0 mW laser at 650 nm: N = P/(hc/λ) = 1,636e16 1/s -> 1,6e16
a["fy8-1-L2-03"] = h * c / 222e-9 / e - 3.68               # far-UVC 222 nm on magnesium: 5,586 eV − 3,68 eV = 1,906 eV -> 1,91 eV
a["fy8-1-L2-04"] = h * c / 300e-9 / e - 1.85               # 300 nm, E_k,max = 1,85 eV: W = 4,133 eV − 1,85 eV = 2,283 eV -> 2,28 eV
# Level 3: reasoning or an unfamiliar context
EkJ = h * c / 350e-9 - 2.28 * e                            # 350 nm on sodium: E_k,max = 5,676e-19 J − 3,653e-19 J = 2,023e-19 J
a["fy8-1-L3-01"] = math.sqrt(2 * EkJ / me)                 # v = √(2E/m) = 6,665e5 m/s -> 6,66e5 m/s
t = 2.28 * e / (1.0e-6 * 1.0e-20)                          # wave model: W = I A t with I = 1,0e-6 W/m², A = 1,0e-20 m²: t = 3,65e7 s
a["fy8-1-L3-02"] = t / 86400                               # in days: 422,8 d -> 420 d (two significant figures)
slope = (1.84 - 0.60) / (1.00e15 - 7.0e14)                 # line through (7,0e14 Hz, 0,60 eV) and (1,00e15 Hz, 1,84 eV): 4,133e-15 eV/Hz (= h/e)
a["fy8-1-L3-03"] = 7.0e14 - 0.60 / slope                    # E_k,max = 0 at f0 = f1 − E_k1/slope = 5,548e14 Hz -> 5,5e14 Hz
# Added exercises (exercise bank P1)
a["fy8-1-L1-07"] = 2.30 * e / h                            # potassium W = 2,30 eV: f0 = W/h = 5,561e14 Hz -> 5,56e14 Hz (λ0 = c/f0 = 539 nm)
lam = [365e-9, 405e-9, 436e-9, 470e-9, 505e-9]; Us = [1.12, 0.75, 0.55, 0.32, 0.17]   # example data: stopping voltage against wavelength
fs = [c / l for l in lam]; fm = sum(fs) / 5; Um = sum(Us) / 5
k = sum((x - fm) * (y - Um) for x, y in zip(fs, Us)) / sum((x - fm) ** 2 for x in fs)   # least-squares slope 4,195e-15 V/Hz
a["fy8-1-L2-05"] = e * k                                   # h = e k = 6,72e-34 J s -> 6,7e-34 J s (intercept -2,338 V: W = 2,34 eV, f0 = 5,57e14 Hz)
EA = [1.01, 1.43, 1.83, 2.26]; EB = [0.12, 0.52, 0.93, 1.35]
a["fy8-1-L2-06"] = sum(x - y for x, y in zip(EA, EB)) / 4  # two metals: differences 0,89; 0,91; 0,90; 0,91 -> mean 0,9025 eV -> 0,90 eV (W_B − W_A)
k7 = (1.79 - 0.55) / (9.5e14 - 6.5e14)                     # slope 4,133e-15 eV/Hz from the first and last point
f07 = 6.5e14 - 0.55 / k7                                   # f0 = 5,169e14 Hz
a["fy8-1-L2-07"] = k7 * f07                                # W = k f0 = 2,137 eV -> 2,14 eV (= minus the intercept of the line)
Ep = h * c / 400e-9                                        # 400 nm photon: 4,966e-19 J = 3,100 eV
N1 = 1.0e-3 / Ep; ne1 = 0.30e-6 / e                        # photons per s 2,014e15; electrons per s from I_sat = 0,30 µA: 1,873e12
a["fy8-1-L3-04"] = ne1 / N1 * 100                          # quantum yield 9,30e-4 = 0,0930 % -> 0,093 % (W = 3,100 eV − 0,80 eV = 2,30 eV)
def current_uA(l, P):                                      # 0,10 % of the photons release an electron if hf >= W = 2,30 eV
    E = h * c / l
    return P / E * 1e-3 * e * 1e6 if E >= 2.30 * e else 0.0
a["fy8-1-L3-05"] = current_uA(470e-9, 4.0e-3) + current_uA(620e-9, 8.0e-3) + current_uA(365e-9, 1.0e-3)   # 1,516 + 0 + 0,294 = 1,810 µA -> 1,8 µA
print(json.dumps({k: (round(v, 8) if abs(v) >= 1e-3 else float(f"{v:.6g}")) for k, v in a.items()}))
