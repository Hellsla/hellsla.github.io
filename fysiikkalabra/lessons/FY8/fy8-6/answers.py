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
# Level 2: two steps, a conversion or a rearrangement
a["fy8-6-L2-01"] = h * c / (e * 470e-9)                    # blue LED 470 nm: U_k ≈ hc/(eλ) = 2,638 V -> 2,64 V
a["fy8-6-L2-02"] = e * 1.95 * 605e-9 / c                   # one orange LED, 605 nm and 1,95 V: h ≈ e U_k λ / c = 6,304e-34 J s -> 6,30e-34
a["fy8-6-L2-03"] = 0.020 / e * (h * c / 630e-9) * 1000     # 20 mA, one 630 nm photon per electron: P = (I/e) hc/λ = 39,37 mW -> 39 mW
a["fy8-6-L2-04"] = h * c / e * (1 / 450e-9 - 1 / 560e-9)   # white LED: 450 nm photon absorbed, 560 nm emitted: 2,756 − 2,214 = 0,541 eV
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
print(json.dumps({k_: (round(v, 8) if abs(v) >= 1e-3 else float(f"{v:.6g}")) for k_, v in a.items()}))
