"""Numbers of the lesson text and inquiry.json for fy8-10, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Mass defect Δm = Z m_H + N m_n - m_atom with atomic masses (the Z electrons of the
Z hydrogen atoms cancel those of the atom; the electrons' own binding energy, at most a few hundred keV, is left out),
binding energy E_B = Δm c², reaction energy Q = (Σ m_before - Σ m_after) c² with atomic masses (alpha decay and
reactions where Z is conserved: the electrons cancel).
Atomic masses: AME2020 (W. J. Huang et al., M. Wang et al., Chinese Physics C 45 (2021) 030002 and 030003), rounded to
six decimals in u (micro-u); the same table is NUCLIDES in assets/sims/fy8/fy8-10/sim.js (figures.py imports it from here).
1 u = 931,5 MeV/c², from CODATA 2018: 1 u = 1,66054e-27 kg, c = 2,99792e8 m/s, e = 1,602177e-19 C (computed below).
Prints {id: number} as JSON on the last line."""
import json

a = {}
M_H, M_N = 1.007825, 1.008665            # hydrogen-1 atom and the neutron, u (AME2020 1,00782503, 1,00866492)
U_MEV = 931.5                            # MeV/c² per u, as in the lesson
# (symbol, Finnish name, Z, A, atomic mass in u): AME2020, six decimals
NUCLIDES = [
    ("H", "vety", 1, 2, 2.014102), ("H", "vety", 1, 3, 3.016049), ("He", "helium", 2, 3, 3.016029),
    ("He", "helium", 2, 4, 4.002603), ("Li", "litium", 3, 6, 6.015123), ("Li", "litium", 3, 7, 7.016003),
    ("Be", "beryllium", 4, 9, 9.012183), ("B", "boori", 5, 11, 11.009305), ("C", "hiili", 6, 12, 12.000000),
    ("N", "typpi", 7, 14, 14.003074), ("O", "happi", 8, 16, 15.994915), ("Ne", "neon", 10, 20, 19.992440),
    ("Mg", "magnesium", 12, 24, 23.985042), ("Si", "pii", 14, 28, 27.976927), ("S", "rikki", 16, 32, 31.972071),
    ("Ca", "kalsium", 20, 40, 39.962591), ("Fe", "rauta", 26, 56, 55.934936), ("Ni", "nikkeli", 28, 62, 61.928345),
    ("Cu", "kupari", 29, 63, 62.929598), ("Zn", "sinkki", 30, 64, 63.929142), ("Kr", "krypton", 36, 84, 83.911498),
    ("Zr", "zirkonium", 40, 90, 89.904698), ("Ag", "hopea", 47, 107, 106.905092), ("Sn", "tina", 50, 120, 119.902202),
    ("Ba", "barium", 56, 138, 137.905247), ("W", "volframi", 74, 184, 183.950933), ("Au", "kulta", 79, 197, 196.966570),
    ("Pb", "lyijy", 82, 208, 207.976652), ("Bi", "vismutti", 83, 209, 208.980399), ("Th", "torium", 90, 232, 232.038056),
    ("U", "uraani", 92, 235, 235.043928), ("U", "uraani", 92, 238, 238.050787),
]
MASS = {f"{s}{A}": m for s, _, _, A, m in NUCLIDES}
MASS.update({"Th234": 234.043601, "Po210": 209.982874, "Pb206": 205.974465})   # AME2020, for the decays below


def defect(Z, A, m):
    """Mass defect in u from the atomic mass: Z hydrogen atoms and A - Z neutrons minus the atom."""
    return Z * M_H + (A - Z) * M_N - m


# ---------------------------------------------------------------- every nuclide of the table (sim, figure, experiments)
for s, _, Z, A, m in NUCLIDES:
    k = f"{s}{A}"
    a[f"{k}-msum"] = Z * M_H + (A - Z) * M_N               # u
    a[f"{k}-dm"] = defect(Z, A, m)                         # u, rounded to 6 decimals in the sim
    a[f"{k}-EB"] = round(defect(Z, A, m), 6) * U_MEV       # MeV
    a[f"{k}-EBA"] = round(defect(Z, A, m), 6) * U_MEV / A  # MeV per nucleon
# the largest E_B/A of the table: Ni-62 8,795 MeV (Fe-56 8,790 MeV); the smallest H-2 1,112 MeV
a["max-EBA"] = max(a[f"{s}{A}-EBA"] for s, _, _, A, _ in NUCLIDES)   # 8,7946 (Ni-62)
a["U238-ratio"] = 100 * a["U238-dm"] / MASS["U238"]                  # 0,813 % of the atom's mass
a["He4-ratio"] = 100 * a["He4-dm"] / MASS["He4"]                     # 0,759 %
a["H2-ratio"] = 100 * a["H2-dm"] / MASS["H2"]                        # 0,119 %

# ---------------------------------------------------------------- hook: helium-4 against its parts
a["hook-parts"] = 2 * M_H + 2 * M_N                       # 4,032980 u
a["hook-he"] = MASS["He4"]                                # 4,002603 u
a["hook-diff"] = a["hook-parts"] - a["hook-he"]           # 0,030377 u

# ---------------------------------------------------------------- 1 u in MeV/c² by substitution (Ydinajatus)
u_kg, c, e = 1.66054e-27, 2.99792e8, 1.602177e-19
a["u-J"] = u_kg * c ** 2                                  # 1,49241e-10 J
a["u-MeV"] = u_kg * c ** 2 / e / 1e6                      # 931,49 MeV -> 931,5 MeV
a["u-c2"] = c ** 2                                        # 8,98752e16 m²/s²
# the same with the course's four-figure constants: 931,6 MeV (why five figures are used here)
a["u-MeV-4fig"] = 1.6605e-27 * 2.998e8 ** 2 / 1.602e-19 / 1e6
# E = mc² for 1,00 g (Ydinajatus, scale): 8,99e13 J
a["gram-J"] = 1.00e-3 * 2.998e8 ** 2

# ---------------------------------------------------------------- Kaava: alpha decay of U-238, reaction energy
q_u238 = MASS["U238"] - MASS["Th234"] - MASS["He4"]
a["u238-alpha-du"] = q_u238                               # 0,004583 u
a["u238-alpha-Q"] = q_u238 * U_MEV                        # 4,269 MeV (literature Q 4,270 MeV)

# ---------------------------------------------------------------- worked example: helium-4
dm = 2 * M_H + 2 * M_N - MASS["He4"]
a["ex-2mH"] = 2 * M_H                                     # 2,015650 u
a["ex-2mn"] = 2 * M_N                                     # 2,017330 u
a["ex-dm"] = dm                                           # 0,030377 u
a["ex-EB"] = dm * U_MEV                                   # 28,296 MeV -> 28,30 MeV
a["ex-EBA"] = dm * U_MEV / 4                              # 7,074 MeV
a["ex-check"] = 0.03 * 900                                # 27 MeV, the round estimate

# ---------------------------------------------------------------- experiments: model values (the sim's table)
for k in ("H2", "He4", "Li7", "C12", "O16", "Fe56", "Ni62", "Ag107", "Pb208", "U238"):
    a[f"koe-{k}"] = round(a[f"{k}-EBA"], 3)

# ---------------------------------------------------------------- Etsi virhe: c² twice (C-12)
dm_c = a["C12-dm"]                                        # 0,098940 u
a["virhe-right"] = dm_c * U_MEV                           # 92,16 MeV
a["virhe-wrong"] = dm_c * U_MEV * 2.998e8 ** 2            # 8,28e18 "MeV": multiplied by c² twice

# ---------------------------------------------------------------- Sovella, transfer: alpha decay of Po-210
q_po = MASS["Po210"] - MASS["Pb206"] - MASS["He4"]
a["po-du"] = q_po                                         # 0,005806 u
a["po-Q"] = q_po * U_MEV                                  # 5,408 MeV (literature Q 5,407 MeV, alpha 5,304 MeV)
a["po-mistake-noHe"] = (MASS["Po210"] - MASS["Pb206"]) * U_MEV   # 3733 MeV: forgot the alpha particle
a["po-mistake-sign"] = -q_po * U_MEV                      # -5,408 MeV: after minus before
a["po-mistake-J"] = q_po * 1.66054e-27 * 2.99792e8 ** 2   # 8,66e-13 J: the right energy in joules
a["po-alpha-share"] = 206 / 210 * a["po-Q"]               # 5,30 MeV: the alpha's share (momentum), the check

# ---------------------------------------------------------------- Tarkista 3: burning carbon, C + O2 -> CO2, 393,5 kJ per mol
a["coal-dm"] = 393.5e3 / 2.998e8 ** 2                     # 4,38e-12 kg per 44,0 g of reactants
a["coal-ratio"] = a["coal-dm"] / 44.0e-3                  # 9,95e-11, about 1e-10
a["nuc-ratio"] = a["U238-ratio"] / 100                    # 0,0081 for comparison

# ---------------------------------------------------------------- Tarkista 2: the curve, E_B/A at A ≈ 240, 120, 60, 30 (read off)
a["chk-fission"] = 120 * 8.50 * 2 - 240 * 7.58            # about +220 MeV: splitting A 240 into 2 x 120 releases energy
a["chk-fe-split"] = 2 * 28 * 8.45 - 56 * 8.79             # about -19 MeV: splitting iron needs energy

# ---------------------------------------------------------------- exit ticket: Bi-209 (1640 MeV) against Ca-40 (342 MeV) per nucleon
a["exit-bi"] = 1640 / 209                                 # 7,847 MeV -> 7,85 MeV (table: Bi209-EB 1640,2 MeV)
a["exit-ca"] = 342 / 40                                   # 8,55 MeV (table: Ca40-EB 342,06 MeV)

if __name__ == "__main__":
    print(json.dumps({k: (round(v, 6) if isinstance(v, float) and abs(v) > 1e-3 else v) for k, v in a.items()}))
