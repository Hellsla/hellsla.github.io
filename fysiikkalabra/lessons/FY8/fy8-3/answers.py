"""Every answer in exercises.json for fy8-3, computed from the task data (python -I answers.py).
Hydrogen levels E_n = -13,6 eV / n² (given data), photon E = hf = hc / lambda, 1 eV = 1,602 · 10⁻¹⁹ J.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19      # J s, m/s, J per eV
E1 = 13.6                                     # eV, ionisation energy of hydrogen from n = 1
def En(n): return -E1 / n ** 2               # eV
def lam_nm(dE_eV): return h * c / (dE_eV * e) * 1e9

a = {}
# Level 1: one formula, values given
a["fy8-3-L1-01"] = En(4)                                  # E_4 = -13,6 eV / 16 = -0,85 eV
a["fy8-3-L1-02"] = En(4) - En(1)                          # photon of 4 -> 1: -0,85 eV + 13,6 eV = 12,75 eV -> 12,8 eV
a["fy8-3-L1-03"] = h * c / 486e-9 / e                     # photon of 486 nm: E = hc / lambda = 4,087e-19 J = 2,551 eV -> 2,55 eV
a["fy8-3-L1-04"] = 0 - En(3)                              # ionisation from n = 3: 0 - (-1,511 eV) = 1,51 eV
a["fy8-3-L1-05"] = 1.89 * e / h / 1e12                    # f = E / h = 1,89 · 1,602e-19 J / 6,626e-34 J s = 4,57e14 Hz = 457 THz
# Level 2: two steps, a conversion or a rearrangement
a["fy8-3-L2-01"] = lam_nm(En(5) - En(2))                  # 5 -> 2: dE = 2,856 eV, lambda = 434,2 nm -> 434 nm
dE_410 = h * c / 410e-9 / e                               # 410 nm line ends at n = 2: dE = 3,0244 eV
a["fy8-3-L2-02"] = (E1 / (E1 / 4 - dE_410)) ** 0.5        # E_y = -3,40 eV + 3,024 eV = -0,376 eV; n² = 13,6 / 0,376 = 36,2 -> n = 6,02 -> 6
a["fy8-3-L2-03"] = lam_nm(-3.0 - (-5.0))                  # figure fy8-3/levels-task: E_3 = -3,0 eV -> E_2 = -5,0 eV, dE = 2,0 eV, lambda = 620 nm
a["fy8-3-L2-04"] = h * c / 80.0e-9 / e - E1               # 80,0 nm photon: E = 15,50 eV; E_k = 15,50 eV - 13,6 eV = 1,90 eV
# Level 3: reasoning or an unfamiliar context
# L3-01 electrons of 12,5 eV hit ground-state atoms: E_3 - E_1 = 12,09 eV <= 12,5 eV < E_4 - E_1 = 12,75 eV, so levels 2 and 3
# can be excited; the atoms can then emit 3 -> 2, 3 -> 1 and 2 -> 1: three different lines
reach = [m for m in range(2, 10) if En(m) - En(1) <= 12.5]
a["fy8-3-L3-01"] = len([(u, l) for u in [1] + reach for l in [1] + reach if u > l])
a["fy8-3-L3-02"] = lam_nm(54.4 * (1 / 9 - 1 / 16))         # He+ 4 -> 3: dE = 54,4 eV (1/9 - 1/16) = 2,644 eV, lambda = 468,9 nm -> 469 nm
a["fy8-3-L3-03"] = (En(2) - En(1)) - (0 - En(2))          # 2 -> 1 photon 10,2 eV ionises an atom at n = 2 (3,40 eV): E_k = 6,80 eV
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
