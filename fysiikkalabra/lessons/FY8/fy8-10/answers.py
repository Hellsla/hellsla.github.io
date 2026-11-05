"""Every answer in exercises.json for fy8-10, computed from the task data (python -I answers.py).
Mass defect Δm = Z m_H + N m_n - m_atom (atomic masses), binding energy E_B = Δm c² with 1 u = 931,5 MeV/c²,
reaction energy Q = (Σ m_before - Σ m_after) c², E = mc² in SI units with c = 2,998e8 m/s.
Atomic masses as in the lesson: AME2020, rounded to six decimals in u; 1 u = 1,66054e-27 kg (CODATA 2018).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

M_H, M_N, U_MEV, U_KG, C = 1.007825, 1.008665, 931.5, 1.66054e-27, 2.998e8
a = {}
# Level 1: one formula, values given
a["fy8-10-L1-01"] = 6 * M_H + 6 * M_N - 12.000000      # C-12 mass defect 0,098940 u (six decimals as the data)
a["fy8-10-L1-02"] = 0.137005 * U_MEV                   # O-16, Δm = 0,137005 u: E_B = 127,62 MeV -> 127,6 MeV
a["fy8-10-L1-03"] = 1801.7 / 238                       # U-238, E_B = 1801,7 MeV: 7,5702 MeV per nucleon -> 7,570 MeV
a["fy8-10-L1-04"] = 1.00e-3 * C ** 2 / 1e13            # E = mc² for 1,00 g: 8,988e13 J -> 8,99 · 10¹³ J
a["fy8-10-L1-05"] = 2.224 / U_MEV * 1e3                # H-2, E_B = 2,224 MeV: Δm = 0,0023876 u -> 2,388 · 10⁻³ u
a["fy8-10-L1-07"] = 5.486e-4 * U_MEV                   # electron rest energy: 0,51102 MeV -> 0,5110 MeV
# Level 2: two steps, a conversion or a rearrangement
dm_fe = 26 * M_H + 30 * M_N - 55.934936                # Fe-56: Δm = 0,528464 u
a["fy8-10-L2-01"] = dm_fe * U_MEV / 56                 # E_B = 492,26 MeV, per nucleon 8,7904 MeV -> 8,790 MeV
dm_ra = 226.025410 - 222.017578 - 4.002603             # Ra-226 -> Rn-222 + He-4: 0,005229 u
a["fy8-10-L2-02"] = dm_ra * U_MEV                      # Q = 4,8708 MeV -> 4,871 MeV
dm_kg = 0.137005 * U_KG                                # O-16: 2,27502e-28 kg
a["fy8-10-L2-03"] = dm_kg * C ** 2 / 1e-11             # E_B = 2,04479e-11 J -> 2,045 · 10⁻¹¹ J
a["fy8-10-L2-04"] = 3.83e26 * 24 * 3600 / C ** 2 / 1e14   # Sun 3,83e26 W for one day: Δm = 3,682e14 kg -> 3,68 · 10¹⁴ kg
# Level 2 additions: table, error analysis (the two multiple-choice tasks L1-06, L1-08, L2-07 have text answers, no number)
masses = {4: (2, 4.002603), 12: (6, 12.000000), 20: (10, 19.992440), 40: (20, 39.962591),
          62: (28, 61.928345), 120: (50, 119.902202), 138: (56, 137.905247), 238: (92, 238.050788)}   # A: (Z, atomic mass in u)
eb_per_a = {A: (Z * M_H + (A - Z) * M_N - m) * U_MEV / A for A, (Z, m) in masses.items()}   # E_B/A of each nuclide
a["fy8-10-L2-05"] = max(eb_per_a.values())             # largest E_B/A is Ni-62: 8,7946 MeV -> 8,795 MeV
dm_li = 3 * M_H + 3 * M_N - 6.015123                   # Li-6 with hydrogen atoms: 0,034347 u
a["fy8-10-L2-06"] = dm_li * U_MEV                      # E_B = 31,994 MeV -> 31,99 MeV (the student's 30,46 MeV misses 3 electron masses)
# Level 3: reasoning or an unfamiliar context
a["fy8-10-L3-01"] = (3.016029 + M_N - 4.002603) * U_MEV   # He-4 -> He-3 + n: 0,022091 u, 20,577 MeV -> 20,58 MeV
a["fy8-10-L3-02"] = 4 * 7.074 - 2 * 2 * 1.112          # H-2 + H-2 -> He-4 from E_B/A: 28,296 - 4,448 = 23,848 MeV -> 23,85 MeV
a["fy8-10-L3-03"] = 4190 * 1.00 * (80.0 - 20.0) / C ** 2 / 1e-12   # 1,00 kg of water cools by 60,0 K: Δm = 2,797e-12 kg -> 2,80 · 10⁻¹² kg
# Level 3 additions: fission Q from masses (and from E_B/A), energy of 1,00 g; star with L = 1e28 W
q_u = (235.043930 + M_N - 140.914411 - 91.926156 - 3 * M_N) * U_MEV   # n + U-235 -> Ba-141 + Kr-92 + 3n: 0,186033 u, 173,29 MeV
q_eb = 141 * 8.326 + 92 * 8.513 - 235 * 7.591          # same Q from the table's E_B/A: 173,28 MeV (rounded table values)
n_u = 1.00e-3 / (235.043930 * U_KG)                    # nuclei in 1,00 g of U-235: 2,562e21
a["fy8-10-L3-04"] = n_u * q_u * 1.602177e-13 / 1e10    # E = N Q = 7,113e10 J -> 7,11 · 10¹⁰ J
dm_year = 1.0e28 * 365.25 * 24 * 3600 / C ** 2         # L t / c²: 3,511e18 kg per year
f_h = (4 * M_H - 4.002603) / (4 * M_H)                 # 0,028697 u / 4,031300 u = 0,007119 of the hydrogen mass becomes energy
a["fy8-10-L3-05"] = dm_year / f_h / 1e20               # hydrogen fused per year: 4,932e20 kg -> 4,9 · 10²⁰ kg
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
