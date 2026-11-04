"""Numbers of the lesson text and inquiry.json for fy6-12, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Model: a homogeneous field E = U / d between two parallel plates (chapter
Homogeeninen sähkökenttä), the force F = q E is the same everywhere between the plates; potential V = E x measured from
the negative plate (zero), potential energy E_p = q V, the field's work W_AB = q (V_A - V_B) = q U_AB, and when only
the electric force does work, E_k + E_p stays constant. Gravity is left out (in the sim's weakest field it is at least about 10^-10 of the
electric force, 2e-11 in 5000 V/m for a proton). Constants from the table: e = 1,602e-19 C, m_p = 1,673e-27 kg, m_e = 9,109e-31 kg,
m_alpha = 6,645e-27 kg; 1 eV = 1,602e-19 J. Prints {id: number} as JSON."""
import json, math

e, m_p, m_e, m_a = 1.602e-19, 1.673e-27, 9.109e-31, 6.645e-27
a = {}

# --- Ydinajatus and Kaava figures: plates 4,0 cm apart, U = 200 V ---
U, d = 200.0, 0.040
a["fig-E"] = U / d                                   # 5000 V/m
a["fig-V-1cm"] = a["fig-E"] * 0.010                  # equipotential lines 1,0 cm apart: 50 V, 100 V, 150 V
a["fig-W-proton-J"] = e * U                          # proton from + plate to - plate: 3,204e-17 J
a["fig-W-proton-eV"] = U                             # = 200 eV
a["fig-F-proton"] = e * a["fig-E"]                   # F = qE = 8,01e-16 N
a["fig-W-Fd"] = a["fig-F-proton"] * d                # W = F d = 3,204e-17 J (the same as e U)
a["fig-Ep-proton-150"] = 150.0                       # proton on the 150 V line: E_p = +150 eV
a["fig-Ep-electron-150"] = -150.0                    # electron on the 150 V line: E_p = -150 eV
a["eV-J"] = e * 1.0                                  # 1 eV = 1,602e-19 J

# --- worked example: an auroral electron from rest through 3,0 kV ---
Uex = 3.0e3
a["ex-Ek-J"] = e * Uex                               # 4,806e-16 J
a["ex-Ek-eV"] = Uex                                  # 3000 eV = 3,0 keV
a["ex-v"] = math.sqrt(2 * e * Uex / m_e)             # 3,248e7 m/s
a["ex-v-c"] = a["ex-v"] / 3.00e8                     # about 0,11 of the speed of light
a["ex-check-v"] = math.sqrt(2 * 5e-16 / 1e-30)       # round-number estimate: about 3e7 m/s

# --- simulation on load and experiments: U = 500 V, d = 5,0 cm, proton ---
def run(U, dcm, q, m):
    d = dcm / 100
    E = U / d
    acc = q * E / m
    t = math.sqrt(2 * d / acc)
    v = acc * t
    return dict(E=E, F=q * E, t=t, tns=t * 1e9, v=v, vkms=v / 1000, Ek=0.5 * m * v * v, EkeV=0.5 * m * v * v / e)

for dcm in (2.5, 5.0, 10.0):                         # experiment 1: d varied, U = 500 V, proton
    r = run(500, dcm, e, m_p)
    a[f"koe1-d{dcm}-E"] = r["E"]                     # 20 000 / 10 000 / 5000 V/m
    a[f"koe1-d{dcm}-tns"] = r["tns"]                 # 161,6 / 323,2 / 646,4 ns
    a[f"koe1-d{dcm}-EkeV"] = r["EkeV"]               # 500 eV every time
for name, q, m in (("p", e, m_p), ("e", e, m_e), ("a", 2 * e, m_a)):   # experiment 2: particle varied, U = 500 V, d = 5,0 cm
    r = run(500, 5.0, q, m)
    a[f"koe2-{name}-EkeV"] = r["EkeV"]               # 500 / 500 / 1000 eV
    a[f"koe2-{name}-vkms"] = r["vkms"]               # 309,5 / 13 262 / 219,6 km/s
    a[f"koe2-{name}-tns"] = r["tns"]                 # 323,2 / 7,54 / 455,4 ns
a["koe2-ratio-v"] = a["koe2-e-vkms"] / a["koe2-p-vkms"]   # electron about 43 times faster

# (the kertaus item is qualitative: the force F = qE is the same everywhere between the plates; no numbers)

# --- error spotting: an electron from the - plate to the + plate, U = 300 V ---
a["virhe-dEp"] = -e * 300                           # Delta E_p = q Delta V = (-e)(+300 V) = -4,806e-17 J
a["virhe-wrong"] = +e * 300                          # the student's +4,806e-17 J

# --- transfer task: xenon ion thruster, q = e, m = 2,18e-25 kg, U = 1,2 kV ---
m_xe, Uxe = 2.18e-25, 1.2e3
a["siirto-Ek"] = e * Uxe                             # 1,9224e-16 J
a["siirto"] = math.sqrt(2 * e * Uxe / m_xe) / 1000   # 42,0 km/s
a["siirto-mistake-kV"] = math.sqrt(2 * e * 1.2 / m_xe) / 1000      # kV not converted: 1,33 km/s
a["siirto-mistake-half"] = math.sqrt(e * Uxe / m_xe) / 1000        # the 2 forgotten: 29,7 km/s
a["siirto-mistake-ms"] = math.sqrt(2 * e * Uxe / m_xe)             # answered in m/s: 41 996
a["siirto-check"] = math.sqrt(2 * 2e-16 / 2e-25)                   # round numbers: about 4,5e4 m/s

# --- check 2: proton 2,0 cm along a field of 1,5e4 V/m ---
a["tarkistus-2"] = 1.5e4 * 0.020                     # potential falls 300 V: E_k grows 300 eV
a["tarkistus-2-J"] = e * a["tarkistus-2"]            # 4,806e-17 J
a["tarkistus-2-mistake-cm"] = 1.5e4 * 2.0            # cm not converted: 30 000 eV
a["tarkistus-2-mistake-J"] = a["tarkistus-2-J"]      # joules given as eV

# --- hook: auroral electrons a few kV, the Miksi answer: 5 keV electron speed (classical) ---
a["hook-v-5keV"] = math.sqrt(2 * 5e3 * e / m_e)      # 4,19e7 m/s

# --- simulation model box: the largest speed (electron, 1000 V) and the weakest field (100 V over 10 cm) ---
a["sim-vmax-c"] = math.sqrt(2 * e * 1000 / m_e) / 3.00e8          # 0,0625: under 7 % of c
a["sim-weight-ratio-min"] = e * (100 / 0.10) / (m_p * 9.81)        # proton: F / G = 9,8e9
a["sim-weight-ratio-min-alpha"] = 2 * e * (100 / 0.10) / (m_a * 9.81)   # alpha, the weakest case: 4,9e9, still "billions"
assert a["sim-weight-ratio-min-alpha"] > 1e9 and a["sim-weight-ratio-min"] > 1e9
a["fig-weight-ratio"] = e * 5000 / (m_p * 9.81)                    # in the figure's field 5000 V/m: 4,9e10
a["siirto-mass-ratio"] = m_xe / m_e                                 # xenon ion 2,4e5 times the electron

# --- exit ticket ---
a["exit-1"] = -(70 - 20)                                            # electron 20 V -> 70 V: Delta E_p = -50 eV
a["exit-2"] = 3.0e3 * e                                             # 3,0 keV = 4,806e-16 J

print(json.dumps({k: round(v, 6) if abs(v) >= 1e-3 or v == 0 else float(f"{v:.6g}") for k, v in a.items()}))
