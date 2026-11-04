"""Numbers of the lesson text and inquiry.json for fy6-13, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Capacitance C = Q / U; plate capacitor C = eps0 eps_r A / d; the uniform field
between the plates E = U / d; breakdown U_max = E_max d; stored energy W = 1/2 Q U = 1/2 C U^2 (W, since E is the
field strength here). Charging from a source of constant voltage U: the source gives Q U, the capacitor keeps half.
The simulation (assets/sims/fy6/fy6-13): A in cm^2, d in mm, U0 in kV; connected: Q = C U0; disconnected: Q stays
what it was when the source was removed, U = Q / C. Prints {id: number} as JSON."""
import json

EPS0 = 8.854e-12                                               # F/m
ER = {"ilma": 1.0, "teflon": 2.1, "paperi": 3.7, "lasi": 5.6}  # relative permittivity (table values, rounded)
EMAX = {"ilma": 3, "teflon": 60, "paperi": 16, "lasi": 14}     # breakdown strength MV/m (table values, rounded)
a = {}


def cap(A_cm2, d_mm, er):
    """Capacitance in pF of a plate capacitor with plate area A (cm^2) and gap d (mm)."""
    return EPS0 * er * A_cm2 * 1e-4 / (d_mm * 1e-3) * 1e12


def connected(A, d, m, U_kV):
    C = cap(A, d, ER[m])
    Q = C * U_kV * 1e3 / 1e3                                    # pF · kV = nC
    return dict(C=C, Q=Q, U=U_kV, E=U_kV / d, W=0.5 * Q * U_kV) # E kV/mm = MV/m; W nC · kV = µJ


# --- the simulation on load: A = 200 cm^2, d = 2,0 mm, air, U0 = 1,0 kV, connected ---
s = connected(200, 2.0, "ilma", 1.0)
a["sim-C"] = s["C"]                                            # 8,854e-12 · 0,0200 m^2 : 0,0020 m = 88,5 pF
a["sim-Q"] = s["Q"]                                            # 88,5 pF · 1,0 kV = 88,5 nC
a["sim-E"] = s["E"]                                            # 1,0 kV : 2,0 mm = 0,50 MV/m
a["sim-W"] = s["W"]                                            # 1/2 · 88,5 nC · 1,0 kV = 44,3 µJ

# --- experiment 1: U0 varied, A 200 cm^2, d 2,0 mm, air, connected ---
for U in (0.5, 1.0, 1.5, 2.0):
    c = connected(200, 2.0, "ilma", U)
    a[f"koe1-U{U}-Q"] = c["Q"]                                 # 44,3 / 88,5 / 132,8 / 177,1 nC: Q grows like U
    a[f"koe1-U{U}-W"] = c["W"]                                 # 11,1 / 44,3 / 99,6 / 177,1 µJ: W grows like U^2
    a[f"koe1-U{U}-QU"] = c["Q"] / U                            # Q : U = 88,5 nC/kV = 88,5 pF every time
a["koe1-Wratio"] = connected(200, 2.0, "ilma", 1.0)["W"] / connected(200, 2.0, "ilma", 0.5)["W"]   # 4,0 (prediction 1)

# --- experiment 2: d varied, A 200 cm^2, air, U0 1,0 kV, connected ---
for d in (1.0, 2.0, 4.0, 8.0):
    c = connected(200, d, "ilma", 1.0)
    a[f"koe2-d{d}-C"] = c["C"]                                 # 177,1 / 88,5 / 44,3 / 22,1 pF
    a[f"koe2-d{d}-Q"] = c["Q"]                                 # the same numbers in nC
    a[f"koe2-d{d}-E"] = c["E"]                                 # 1,0 / 0,50 / 0,25 / 0,125 MV/m

# --- experiment 3: charged with air to 1,0 kV (A 200 cm^2, d 2,0 mm), disconnected, dielectric varied ---
Q0 = connected(200, 2.0, "ilma", 1.0)["Q"]                     # 88,5 nC stays
for m in ("ilma", "teflon", "paperi", "lasi"):
    C = cap(200, 2.0, ER[m])
    U = Q0 / C                                                 # nC : pF = kV
    a[f"koe3-{m}-U"] = U                                       # 1,00 / 0,476 / 0,270 / 0,179 kV
    a[f"koe3-{m}-W"] = 0.5 * Q0 * U                            # 44,3 / 21,1 / 12,0 / 7,9 µJ
    a[f"koe3-{m}-E"] = U / 2.0                                 # 0,50 / 0,24 / 0,14 / 0,089 MV/m
# the same with the source connected (experiment 4 and the table of the Kaava section)
for m in ("ilma", "lasi"):
    c = connected(200, 2.0, m, 1.0)
    a[f"koe4-{m}-Q"] = c["Q"]                                  # 88,5 / 495,8 nC
    a[f"koe4-{m}-W"] = c["W"]                                  # 44,3 / 247,9 µJ

# --- experiment 5 (optional): breakdown in air at d = 1,0 mm ---
a["koe5-Umax"] = EMAX["ilma"] * 1.0                            # U_max = E_max d = 3 MV/m · 1,0 mm = 3,0 kV

# --- Kaava: unit conversions and the dielectric table ---
a["470uF"] = 470e-6                                            # 470 µF = 470 · 10^-6 F
a["paper-Umax-V"] = 16e6 * 0.010e-3                            # paper 0,010 mm thick: 16 MV/m · 1,0e-5 m = 160 V
a["air-1cm-kV"] = 3e6 * 0.010 / 1000                           # a 1,0 cm air gap breaks down at about 30 kV

# --- worked example: flash, C = 150 µF, U = 300 V, discharged in 1,0 ms ---
C_ex, U_ex, t_ex = 150e-6, 300, 1.0e-3
a["ex-W"] = 0.5 * C_ex * U_ex ** 2                             # 1/2 · 150e-6 F · (300 V)^2 = 6,75 J
a["ex-Q"] = C_ex * U_ex                                        # 0,045 C (Järkevyys: W = 1/2 Q U)
a["ex-W-QU"] = 0.5 * a["ex-Q"] * U_ex                          # the same 6,75 J
a["ex-P"] = a["ex-W"] / t_ex                                   # 6750 W = 6,8 kW
a["ex-P-kW"] = a["ex-P"] / 1000
a["ex-charge-2W"] = a["ex-W"] / 2.0                            # at about 2 W from the batteries: 3,4 s at least
a["ex-ratio"] = a["ex-charge-2W"] / t_ex                       # the flash is over 3000 times faster than the charging

# --- retrieval: U = 300 V, d = 2,0 mm ---
a["kertaus"] = 300 / 2.0e-3                                    # 150 000 V/m = 150 kV/m
a["kertaus-nomm"] = 300 / 2.0                                  # 150 (mm not converted)
a["kertaus-mult"] = 300 * 2.0e-3                               # 0,6 (multiplied)

# --- error spotting: C = 470 µF, U = 12 V ---
a["virhe-wrong"] = 0.5 * 470 * 12 ** 2                         # 33 840 "J" (µF not converted)
a["virhe-right"] = 0.5 * 470e-6 * 12 ** 2                      # 0,0338 J = 34 mJ
a["virhe-noHalf"] = 470e-6 * 12 ** 2                           # 0,068 J (no 1/2)
a["virhe-noSquare"] = 0.5 * 470e-6 * 12                        # 0,0028 J (U not squared)

# --- transfer: C = 4,7 µF charged to 9,0 V through a resistor ---
C_s, U_s = 4.7e-6, 9.0
a["siirto-source"] = C_s * U_s ** 2 * 1e6                      # the battery gives Q U = C U^2 = 380,7 µJ
a["siirto-stored"] = 0.5 * C_s * U_s ** 2 * 1e6                # the capacitor keeps 190,35 µJ
a["siirto"] = a["siirto-source"] - a["siirto-stored"]          # 190,35 µJ to the resistor's internal energy
a["siirto-Q"] = C_s * U_s * 1e6                                # 42,3 µC

# --- check 3: a TV's capacitor 220 µF at 330 V ---
a["tarkistus-3-W"] = 0.5 * 220e-6 * 330 ** 2                  # 11,98 J, about 12 J

# --- exit ticket: C = 100 µF, U = 12 V ---
a["exit-Q"] = 100e-6 * 12 * 1e3                                # 1,2 mC

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
