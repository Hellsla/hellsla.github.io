"""Every answer in exercises.json for fy8-16, computed from the task data (python -I answers.py).
Redshift z = (λ - λ0) / λ0, recession speed v = c z for small z with c = 2,998e5 km/s, the Hubble–Lemaître law
v = H0 d, the age estimate t = 1 / H0 with 1 Mpc = 3,086e19 km and 1 a = 3,156e7 s, photon energy E = hc / λ with
h = 6,626e-34 J s, c = 2,998e8 m/s and 1 eV = 1,602e-19 J, reaction energy Q = (m_before - m_after) c² with
1 u = 931,5 MeV/c² (as in the chapter Massavaje ja ytimen sidosenergia).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

C_KMS, MPC_KM, YEAR_S = 2.998e5, 3.086e19, 3.156e7
H, C, EV = 6.626e-34, 2.998e8, 1.602e-19
a = {}
# Level 1: one formula, values given
a["fy8-16-L1-01"] = (492.4 - 486.1) / 486.1            # Hβ 486,1 -> 492,4 nm: Δλ = 6,3 nm, z = 0,01296 -> 0,013
a["fy8-16-L1-02"] = C_KMS * 0.0250                     # z = 0,0250: v = 7495 km/s -> 7,50 · 10³ km/s
a["fy8-16-L1-03"] = 70 * 120                           # d = 120 Mpc: v = 8400 km/s -> 8,4 · 10³ km/s
a["fy8-16-L1-04"] = 5250 / 70                          # v = 5250 km/s: d = 75 Mpc
a["fy8-16-L1-05"] = H * C / 1.06e-3 / EV * 1e3         # CMB photon at 1,06 mm: 1,870e-22 J = 1,167e-3 eV -> 1,17 · 10⁻³ eV
# Level 2: two steps, a conversion or a rearrangement
z = (671.0 - 656.3) / 656.3                            # Hα at 671,0 nm: Δλ = 14,7 nm, z = 0,022398
a["fy8-16-L2-01"] = C_KMS * z / 70                     # v = 6715 km/s, d = 95,9 Mpc -> 96 Mpc
a["fy8-16-L2-02"] = MPC_KM / 67.4 / YEAR_S / 1e9       # H0 = 67,4 km/s/Mpc: 1/H0 = 4,579e17 s = 14,51 · 10⁹ a -> 14,5
lam_then = 1.06e-3 / 1100                              # CMB wavelength when it was set free: 9,636e-7 m
a["fy8-16-L2-03"] = H * C / lam_then / EV              # 1,287 eV -> 1,3 eV (1100 has two figures)
a["fy8-16-L2-04"] = 42.0 * 11300 / 2950                # v ∝ d: d_B = 42,0 Mpc · 11 300 / 2950 = 160,9 Mpc -> 161 Mpc
# Level 3: reasoning or an unfamiliar context
n_, p_ = 1, 7                                          # neutrons : protons = 1 : 7, every neutron ends in He-4 (2 n + 2 p)
a["fy8-16-L3-01"] = 100 * (2 * n_) / (n_ + p_)         # helium mass fraction 2/8 = 25 % (n and p masses taken equal)
a["fy8-16-L3-02"] = (3 * 4.002603 - 12.000000) * 931.5   # 3 He-4 -> C-12: 0,007809 u, Q = 7,274 MeV
z3 = (676.2 - 656.3) / 656.3                           # the longest line is Hα: Δλ = 19,9 nm, z = 0,030322 (Hβ 500,9 and Hγ 447,2 agree)
a["fy8-16-L3-03"] = C_KMS * z3 / 70                    # v = 9091 km/s, d = 129,9 Mpc -> 1,3 · 10² Mpc
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
