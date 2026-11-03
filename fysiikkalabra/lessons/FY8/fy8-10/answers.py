"""Every answer in exercises.json for fy8-10, computed from the task data (python -I answers.py).
Mass defect Δm = Z m_H + N m_n - m_atom (atomic masses), binding energy E_B = Δm c² with 1 u = 931,5 MeV/c²,
reaction energy Q = (Σ m_before - Σ m_after) c², E = mc² in SI units with c = 2,998e8 m/s.
Atomic masses as in the lesson: AME2020, rounded to six decimals in u; 1 u = 1,66054e-27 kg (CODATA 2018).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

M_H, M_N, U_MEV, U_KG, C = 1.007825, 1.008665, 931.5, 1.66054e-27, 2.998e8
a = {}
# Level 1: one formula, values given
a["fy8-10-L1-01"] = 6 * M_H + 6 * M_N - 12.000000      # C-12 mass defect 0,098940 u -> 0,09894 u
a["fy8-10-L1-02"] = 0.137005 * U_MEV                   # O-16, Δm = 0,137005 u: E_B = 127,62 MeV -> 127,6 MeV
a["fy8-10-L1-03"] = 1801.7 / 238                       # U-238, E_B = 1801,7 MeV: 7,5702 MeV per nucleon -> 7,570 MeV
a["fy8-10-L1-04"] = 1.00e-3 * C ** 2 / 1e13            # E = mc² for 1,00 g: 8,988e13 J -> 8,99 · 10¹³ J
a["fy8-10-L1-05"] = 2.224 / U_MEV * 1e3                # H-2, E_B = 2,224 MeV: Δm = 0,0023876 u -> 2,388 · 10⁻³ u
# Level 2: two steps, a conversion or a rearrangement
dm_fe = 26 * M_H + 30 * M_N - 55.934936                # Fe-56: Δm = 0,528464 u
a["fy8-10-L2-01"] = dm_fe * U_MEV / 56                 # E_B = 492,26 MeV, per nucleon 8,7904 MeV -> 8,790 MeV
dm_ra = 226.025410 - 222.017578 - 4.002603             # Ra-226 -> Rn-222 + He-4: 0,005229 u
a["fy8-10-L2-02"] = dm_ra * U_MEV                      # Q = 4,8708 MeV -> 4,871 MeV
dm_kg = 0.137005 * U_KG                                # O-16: 2,27502e-28 kg
a["fy8-10-L2-03"] = dm_kg * C ** 2 / 1e-11             # E_B = 2,04477e-11 J -> 2,045 · 10⁻¹¹ J
a["fy8-10-L2-04"] = 3.83e26 * 24 * 3600 / C ** 2 / 1e14   # Sun 3,83e26 W for one day: Δm = 3,682e14 kg -> 3,68 · 10¹⁴ kg
# Level 3: reasoning or an unfamiliar context
a["fy8-10-L3-01"] = (3.016029 + M_N - 4.002603) * U_MEV   # He-4 -> He-3 + n: 0,022091 u, 20,577 MeV -> 20,58 MeV
a["fy8-10-L3-02"] = 4 * 7.074 - 2 * 2 * 1.112          # H-2 + H-2 -> He-4 from E_B/A: 28,296 - 4,448 = 23,848 MeV -> 23,85 MeV
a["fy8-10-L3-03"] = 4190 * 1.00 * (80.0 - 20.0) / C ** 2 / 1e-12   # 1,00 kg of water cools by 60,0 K: Δm = 2,797e-12 kg -> 2,80 · 10⁻¹² kg
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
