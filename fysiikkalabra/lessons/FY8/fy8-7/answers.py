"""Every answer in exercises.json for fy8-7, computed from the task data (python -I answers.py).
Photon E = hf = hc / lambda, 1 eV = 1,602 · 10⁻¹⁹ J; a laser's photons all carry the transition energy E_2 - E_1, so
P = (N / t) hf. Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19      # J s, m/s, J per eV
hc = h * c                                    # 1,9865e-25 J m
def eV(nm): return hc / (nm * 1e-9) / e       # photon energy in eV of a wavelength in nm

a = {}
# Level 1: one formula, values given
a["fy8-7-L1-01"] = eV(633)                                # He-Ne 633 nm: 3,1382e-19 J = 1,9589 eV -> 1,96 eV
a["fy8-7-L1-02"] = eV(1550)                               # fibre-optic 1550 nm: 0,80000 eV -> 0,800 eV
a["fy8-7-L1-03"] = hc / (1.79 * e) * 1e9                  # ruby transition 1,79 eV: lambda = 692,74 nm -> 693 nm
a["fy8-7-L1-04"] = 3.0e-3 / (hc / 1064e-9)               # pulse 3,0 mJ of 1064 nm photons (1,8670e-19 J): 1,6068e16 -> 1,6e16
a["fy8-7-L1-05"] = 4.0e15 * 2.33 * e * 1e3                # 4,0e15 photons/s of 2,33 eV: 1,4931e-3 W -> 1,5 mW
a["fy8-7-L1-07"] = 5.0e-3 / (hc / 532e-9)                 # 5,0 mW of 532 nm photons (3,7340e-19 J): 1,3391e16 1/s -> 1,3e16 (box 1,34e16)
# Level 2: two steps, a conversion or a rearrangement
a["fy8-7-L2-01"] = 100 * eV(1064) / eV(808)               # one 808 nm pump photon -> one 1064 nm photon: 808 / 1064 = 75,94 %
a["fy8-7-L2-02"] = 650 / 405                              # same power: N/t = P lambda / hc, ratio 650 / 405 = 1,605 -> 1,60
E_small = eV(620) + 0.35                                  # 2,0000 eV + 0,35 eV = 2,3500 eV
a["fy8-7-L2-03"] = hc / (E_small * e) * 1e9               # 527,66 nm -> 528 nm
E_pulse = 2.7e17 * hc / 1064e-9                           # 2,7e17 photons of 1,8670e-19 J: 0,05041 J
a["fy8-7-L2-04"] = E_pulse / 10e-9 / 1e6                  # P = E / t = 0,05041 J : 10e-9 s = 5,04e6 W -> 5,0 MW
a["fy8-7-L2-05"] = eV(486) - eV(617)                      # 2,5514 eV - 2,0097 eV = 0,5417 eV (d 2,0 nm vs 6,0 nm)
diodes = [(405, 10), (520, 6.0), (650, 5.0), (980, 4.0)]   # (nm, mW)
rate = [p * 1e-3 * l * 1e-9 / hc for l, p in diodes]      # N/t = P lambda / hc: 2,039e16; 1,571e16; 1,636e16; 1,973e16 1/s
a["fy8-7-L2-06"] = max(rate) / min(rate)                  # 2,0388e16 / 1,5706e16 = 1,298 -> 1,30
# Level 3: reasoning or an unfamiliar context
a["fy8-7-L3-01"] = 0.5 * 1.0e19 * hc / 550e-9             # just over half of 1,0e19 ions lifted, one 550 nm photon each: 1,806 J -> 1,8 J
a["fy8-7-L3-02"] = 0.5 * 1.0 * 808e-9 / hc                # 1,0 W of 808 nm: 4,067e18 pump photons/s -> as many 1064 nm, half as many 532 nm: 2,03e18
a["fy8-7-L3-03"] = c / (650e-9 * 5.0e9)                   # (hc/lambda) : (hf_q) = c / (lambda f_q) = 9,22e4
a["fy8-7-L3-04"] = 100 * (15.0 * 1070e-9 / hc) / (20.0 * 976e-9 / hc)   # 8,0796e19 / 9,8265e19 = 0,8222 -> 82,2 %
def _polyfit1(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    k = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return k, my - k * mx
pp = [10, 20, 30, 40, 50, 60, 70.]; pl = [0.0, 0.1, 2.1, 6.1, 10.0, 13.9, 18.1]
k, b0 = _polyfit1(pp[2:], pl[2:])                     # fit above threshold: slope 0,398, intercept -9,86 mW, threshold 24,8 mW
a["fy8-7-L3-05"] = k * 1064 / 808                         # N_L / N_p = (dP_L / dP_p) lambda_L / lambda_p = 0,398 * 1,3168 = 0,524
print(json.dumps({k: float(f"{v:.7g}") for k, v in a.items()}))
