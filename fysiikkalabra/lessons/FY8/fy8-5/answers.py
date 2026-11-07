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
# Exercise-bank additions (L1-06, L1-07 and L2-07 are multiple choice and L1-09 an ordering task, without a number; the others below)
a["fy8-5-L1-08"] = 2 * 7                                  # 4f: 7 orbitals, 2 electrons each = 14
a["fy8-5-L2-05"] = (118 + 171) / 400 * 100                # example data: 289 of 400 inside 0,10 nm = 72,25 % (0,15 nm: 368/400 = 92 %)
a["fy8-5-L2-06"] = 64 / (2 * 0.80 / 3)                    # string, 2 nodes -> 3 antinodes: lambda = 2L/3 = 0,5333 m, f = v/lambda = 120 Hz
lam = [657.1, 485.4, 433.5, 410.6]                        # example data: Balmer-type lines, nm
Ef = [h * c / (l * 1e-9) / e for l in lam]                # photon energies: 1,887 / 2,555 / 2,860 / 3,020 eV
n_lines = [math.sqrt(1 / (0.25 - x / 13.6)) for x in Ef]  # n = 3,00 / 4,01 / 5,02 / 5,98 -> 3, 4, 5, 6
xs = [1 / 4 - 1 / round(n) ** 2 for n in n_lines]         # horizontal axis 1/4 - 1/n^2
mx, my = sum(xs) / 4, sum(Ef) / 4
a["fy8-5-L3-04"] = sum((x - mx) * (y - my) for x, y in zip(xs, Ef)) / sum((x - mx) ** 2 for x in xs)   # least-squares slope 13,62 eV (answer 13,6)
a["fy8-5-L3-05"] = h * c / (2.10 * e) * 1e9               # Na 3s -> 3p, 2,10 eV = 3,3642e-19 J: lambda = 590,5 nm (ionisation limit 5,14 eV: 241,2 nm)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
