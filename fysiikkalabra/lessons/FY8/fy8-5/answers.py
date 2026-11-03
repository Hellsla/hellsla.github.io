"""Every answer in exercises.json for fy8-5, computed from the task data (python -I answers.py).
Hydrogen levels E_n = -13,6 eV / n^2 (given data); photon E = hc / lambda; 1 eV = 1,602 * 10^-19 J substituted.
Shell n: n^2 orbitals, at most 2 n^2 electrons; probability P ~ k / N.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

h, c, e = 6.626e-34, 2.998e8, 1.602e-19                  # J s, m/s, J per eV
E = lambda n: -13.6 / n ** 2                              # eV
a = {}
# Level 1: one formula, values given
a["fy8-5-L1-01"] = 2 * 5 ** 2                             # shell n = 5 holds at most 2 n^2 = 50 electrons
a["fy8-5-L1-02"] = 421 / 8000 * 100                       # 421 of 8000 hits inside the 2s node sphere: P = 5,2625 % -> 5,26 %
a["fy8-5-L1-03"] = (1 - 0.90) * 3000                      # 1s, 90 % boundary, 3000 hits: about 300 outside
a["fy8-5-L1-04"] = 0 - E(3)                               # ionising from 3p: 0 - (-13,6/9) eV = 1,511 eV -> 1,51 eV
a["fy8-5-L1-05"] = E(5)                                   # E_5 = -13,6 eV / 25 = -0,544 eV
# Level 2: two steps
dE = (E(3) - E(1)) * e                                    # 3p -> 1s: 12,089 eV = 1,9366e-18 J
a["fy8-5-L2-01"] = h * c / dE * 1e9                       # lambda = hc / dE = 1,0257e-7 m = 102,6 nm
a["fy8-5-L2-02"] = 18 - 2 - 8                             # argon 18 e: shells 1 and 2 full (2 + 8), outermost n = 3 holds 8
a["fy8-5-L2-03"] = (0.90 - 0.50) * 2400                   # between the 50 % and 90 % boundaries: 0,40 * 2400 = 960
a["fy8-5-L2-04"] = h * c / (-E(2) * e) * 1e9              # ionising from n = 2 needs 3,40 eV = 5,4468e-19 J: lambda_max = 364,7 nm
# Level 3: reasoning or an unfamiliar context
Eph = h * c / 97.3e-9 / e                                 # photon 97,3 nm: 2,0416e-18 J = 12,744 eV
n_up = math.sqrt(13.6 / (13.6 - Eph))                     # E_n = -13,6 + 12,744 = -0,856 eV -> n = 3,99 -> shell 4
a["fy8-5-L3-01"] = round(n_up) ** 2                       # orbitals in shell 4: 16
a["fy8-5-L3-02"] = 2 + 2 + 6 + 2 + 3                      # 1s2 2s2 2p6 3s2 3p3 (3p half full): 15 electrons
a["fy8-5-L3-03"] = (0.90 - 0.053) * 5000                  # 2s: inside the 90 % region but outside the node sphere (5,3 %): 4235
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
