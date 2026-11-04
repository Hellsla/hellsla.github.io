"""Every answer in exercises.json for fy8-15, computed from the task data (python -I answers.py).
Charges q in units of e: u, c +2/3; d, s -1/3; an antiquark the opposite. Baryon number B = (quarks - antiquarks) / 3,
lepton number L: lepton +1, antilepton -1. Energy released Q = (m_before - m_after) c^2 with masses in MeV/c^2,
E = m c^2 in SI units, photon E = hc / lambda. Masses: Particle Data Group 2024 (as given in the tasks).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json
from fractions import Fraction as F

QQ = {"u": F(2, 3), "d": F(-1, 3), "s": F(-1, 3)}
def charge(quarks, anti=""): return float(sum(QQ[k] for k in quarks) - sum(QQ[k] for k in anti))
h, c, e = 6.626e-34, 2.998e8, 1.602e-19

a = {}
# Level 1: one rule, values given
a["fy8-15-L1-01"] = charge("uuu")                       # Delta++ = uuu: q = 3 * 2/3 = +2
a["fy8-15-L1-02"] = charge("", "uud")                   # antiproton = anti-u anti-u anti-d: -2/3 - 2/3 + 1/3 = -1
a["fy8-15-L1-03"] = (0 - 3) / 3                         # antineutron: three antiquarks, B = (0 - 3)/3 = -1
a["fy8-15-L1-04"] = 511.0                               # e- + e+ at rest -> 2 gamma: each photon m_e c^2 = 511,0 keV
a["fy8-15-L1-05"] = 2 * 2 + 2 * 1                       # He-4: 2 protons (uud) + 2 neutrons (udd): 6 u quarks
# Level 2: two steps
a["fy8-15-L2-01"] = 6 * 1 + 6 * 2                       # C-12: 6 p with one d each, 6 n with two: 18 d quarks
a["fy8-15-L2-02"] = 1115.683 - 938.272 - 139.570        # Lambda0 -> p + pi-: Q = 37,841 MeV -> 37,8 MeV
E_pair = 2 * 0.511e6 * e                                # threshold of pair production 1,022 MeV = 1,6372e-13 J
a["fy8-15-L2-03"] = h * c / E_pair * 1e12               # lambda = 1,2133 pm -> 1,21 pm
a["fy8-15-L2-04"] = 100 * (2.16 + 2 * 4.70) / 939.565   # neutron udd: 11,56 / 939,565 = 1,230 % -> 1,23 %
# Level 3: reasoning
a["fy8-15-L3-01"] = -1 / 3                              # Omega- = sss, q = -1: one s quark -1/3 = -0,333
a["fy8-15-L3-02"] = 2 * 1.0e-3 * c ** 2 / 1e14          # 1,0 g antimatter + 1,0 g matter: E = 1,798e14 J -> 1,8 · 10^14 J
a["fy8-15-L3-03"] = -1                                  # anti-nu_e + p -> n + X: q of X +1, B 0, L of X = -1 (positron)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
