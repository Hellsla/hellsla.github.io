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
# L3-01: Omega- (sss) -> K- + pi0 breaks B (1 -> 0); -> Sigma0 + K- conserves q and B but Q < 0; -> Lambda0 + K- allowed
m_Om, m_La, m_Si, m_K, m_pi0 = 1672.45, 1115.683, 1192.642, 493.677, 134.977
assert charge("sss") == -1 and charge("uds") == 0 and float(sum(QQ[k] for k in "s") - F(2, 3)) == -1   # K- = s anti-u
assert m_Om - m_Si - m_K < 0                            # Sigma0 + K-: Q = -13,869 MeV, forbidden
a["fy8-15-L3-01"] = m_Om - m_La - m_K                   # Lambda0 + K-: Q = 63,090 MeV -> 63,09 MeV
a["fy8-15-L3-02"] = 2 * 1.0e-3 * c ** 2 / 1e14          # 1,0 g antimatter + 1,0 g matter: E = 1,798e14 J -> 1,8 · 10^14 J
a["fy8-15-L3-03"] = -1                                  # anti-nu_e + p -> n + X: q of X +1, B 0, L of X = -1 (positron)
# Exercise bank additions (teacher 2026-11-04): L1-06, L1-07 and L2-07 are multiple choice (no number); L1-09 is a true-or-false list (no number)
a["fy8-15-L1-08"] = charge("u", "s")                    # K+ = u anti-s: +2/3 + 1/3 = +1
def is_hadron(qk, aq=""):                               # B and q both integers
    B = F(len(qk) - len(aq), 3); q = sum(QQ[k] for k in qk) - sum(QQ[k] for k in aq)
    return B.denominator == 1 and q.denominator == 1
rows = [("uud", ""), ("ud", ""), ("d", "s"), ("uu", "d"), ("", "uud"), ("sss", ""), ("u", "s")]   # L2-05 rows: (quarks, antiquarks)
a["fy8-15-L2-05"] = sum(is_hadron(*r) for r in rows)   # rows 1, 3, 5, 6, 7 are hadrons: 5
# L2-06: (q, B, L) before and after for the seven reactions; 3 (L), 5 (q) and 7 (B) break a law
rx = [((0, 1, 0), (0, 1, 0)),                           # n -> p + e- + anti-nu: q 0 = 1 - 1, B 1, L 0 = 1 - 1
      ((0, 0, 0), (0, 0, 0)),                           # p + anti-p -> gamma gamma
      ((0, 1, 0), (0, 1, 1)),                           # n -> p + e-: L 0 -> 1
      ((0, 1, 1), (0, 1, 1)),                           # p + e- -> n + nu: q 0, B 1, L 1 on both sides
      ((1, 2, 0), (2, 2, 0)),                           # p + n -> p + p: q 1 -> 2
      ((-1, 0, 0), (-1, 0, 0)),                         # pi- -> e- + anti-nu: L 0 = 1 - 1
      ((0, 2, 0), (0, 0, 0))]                           # n + n -> pi0 pi0: B 2 -> 0
a["fy8-15-L2-06"] = sum(x != y for x, y in rx)          # 3 forbidden reactions: 3, 5, 7
# Level 3
a["fy8-15-L3-04"] = (2.615 - 2 * 0.511) / 2             # Tl-208 line: T_total = 1,593 MeV, each particle 0,7965 MeV -> 0,797 MeV
m_pi, m_p, m_La, m_K0 = 139.570, 938.272, 1115.683, 497.611
assert abs(m_pi + m_p - m_La) > 0 and charge("d", "u") == -1   # L3-05 a): pi- = d anti-u, q = -1; both sides q 0, B 1, u 1, d 2, s 0
a["fy8-15-L3-05"] = m_K0 - 2 * m_pi                     # K0 -> pi+ + pi-: Q = 218,471 MeV (stored 218,5)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
