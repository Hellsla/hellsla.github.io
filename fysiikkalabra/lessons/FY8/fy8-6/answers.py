"""Every answer in exercises.json for fy8-6, computed from the task data (python -I answers.py).
LED threshold e U_k ≈ hf = hc/λ, the (f, U_k) line's slope k = h/e so h = e k, photon energy E = hc/λ,
1 eV = 1,602 · 10⁻¹⁹ J. Prints {exercise id: number} as JSON on the last line."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19                    # J s, m/s, C
a = {}
# Level 1: one formula, values given
a["fy8-6-L1-01"] = e * 1.95                                # electron across 1,95 V: E = eU = 3,124e-19 J -> 3,12e-19 J
a["fy8-6-L1-02"] = h * c / 525e-9 / e                      # green LED 525 nm: E = hc/λ = 2,362 eV -> 2,36 eV
a["fy8-6-L1-03"] = c / 650e-9                              # red laser diode 650 nm: f = c/λ = 4,612e14 Hz -> 4,61e14 Hz
a["fy8-6-L1-04"] = h * c / (1.42 * e) * 1e9                # GaAs band gap 1,42 eV: λ = hc/E_g = 873,3 nm -> 873 nm
a["fy8-6-L1-05"] = e * 4.10e-15                            # fitted slope k = 4,10e-15 V s: h = e k = 6,568e-34 J s -> 6,57e-34 J s
a["fy8-6-L1-07"] = h * c / (e * 2.30) * 1e9                # green LED U_k = 2,30 V: λ = hc/(eU_k) = 539,1 nm -> 539 nm
a["fy8-6-L1-08"] = 0.0100 / e / 1e16                       # current 10,0 mA: N = I/e = 6,242e16 1/s -> 6,24 (unit 10^16 1/s)
# Level 2: two steps, a conversion or a rearrangement
a["fy8-6-L2-01"] = h * c / (e * 470e-9)                    # blue LED 470 nm: U_k ≈ hc/(eλ) = 2,638 V -> 2,64 V
a["fy8-6-L2-02"] = e * 1.95 * 605e-9 / c                   # one orange LED, 605 nm and 1,95 V: h ≈ e U_k λ / c = 6,304e-34 J s -> 6,30e-34
a["fy8-6-L2-03"] = 0.020 / e * (h * c / 630e-9) * 1000     # 20 mA, one 630 nm photon per electron: P = (I/e) hc/λ = 39,37 mW -> 39 mW
a["fy8-6-L2-04"] = h * c / e * (1 / 450e-9 - 1 / 560e-9)   # white LED: 450 nm photon absorbed, 560 nm emitted: 2,756 − 2,214 = 0,541 eV
UI = [(1.90, 2.6), (2.00, 8.8), (2.10, 15.0), (2.20, 20.9), (2.30, 27.3)]   # linear part of the I–U table (U in V, I in mA)
ku = sum((x - 2.10) * (y - sum(v for _, v in UI) / 5) for x, y in UI) / sum((x - 2.10) ** 2 for x, _ in UI)   # slope 61,5 mA/V
a["fy8-6-L2-05"] = 2.10 - (sum(v for _, v in UI) / 5) / ku  # U_k = U_mean − I_mean/k = 1,857 V -> 1,86 V (hc/(eλ) at 650 nm = 1,908 V)
a["fy8-6-L2-06"] = (e * 2.04 * 630e-9 / c - 6.626e-34) / 6.626e-34 * 100   # Salla (2,04 V, 10 mA): h = 6,868e-34 J s, +3,645 % -> 3,65 % (Aino 5,858e-34, Eero 6,329e-34)
a["fy8-6-L2-07"] = h * c / e * (1 / 610e-9 - 1 / 650e-9)   # half-maximum points 610 nm and 650 nm: 2,0328 − 1,9077 = 0,1251 eV -> 0,125 eV
# Level 3: reasoning or an unfamiliar context
L3 = [(625, 1.86), (590, 1.97), (520, 2.27), (465, 2.55)]  # four LEDs: λ (nm), U_k (V)
pts = [(c / (lam * 1e-9), U) for lam, U in L3]
mx = sum(x for x, _ in pts) / 4; my = sum(y for _, y in pts) / 4
k = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, _ in pts)   # least squares: 4,212e-15 V s, b = −0,164 V
a["fy8-6-L3-01"] = e * k                                   # h = e k = 6,748e-34 J s -> 6,75e-34 J s
a["fy8-6-L3-02"] = e * (4.25e-15 - 3.95e-15) / 2           # steepest and shallowest line: Δh = e (k_max − k_min)/2 = 2,403e-35 J s -> 2,4e-35
N_ph = 0.015 * 365e-9 / (h * c)                            # UV LED 365 nm, light power 15 mW: 2,756e16 photons per second
N_e = 0.020 / e                                            # current 20 mA: 1,248e17 electrons per second
a["fy8-6-L3-03"] = N_ph / N_e * 100                        # 22,08 % of the electrons give a photon that leaves the LED -> 22 %
LD = [(630, 1.93), (590, 2.08), (570, 2.15), (525, 2.36), (465, 2.64)]   # five LEDs: λ (nm), U measured (V), voltmeter zero error +0,05 V
fd = [c / (l * 1e-9) for l, _ in LD]
mf = sum(fd) / 5; mu = sum(u for _, u in LD) / 5
kd = sum((x - mf) * (u - mu) for x, (_, u) in zip(fd, LD)) / sum((x - mf) ** 2 for x in fd)   # slope 4,208e-15 V s, same before and after the correction
a["fy8-6-L3-04"] = e * kd                                  # h = e k = 6,742e-34 J s -> 6,74e-34 J s (+1,7 %); intercept −0,062 V -> −0,112 V after the correction
a["fy8-6-L3-05"] = c / ((2.46 + 0.10) / 4.15e-15) * 1e9    # calibration line f = (U_k − b)/k = 6,169e14 Hz -> λ = 486,0 nm (direct hc/(eU_k) = 504,1 nm; Δλ = 9,5 nm)
print(json.dumps({k_: (round(v, 8) if abs(v) >= 1e-3 else float(f"{v:.6g}")) for k_, v in a.items()}))
