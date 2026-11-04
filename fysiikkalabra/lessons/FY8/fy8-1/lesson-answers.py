"""Numbers of the lesson text and inquiry.json for fy8-1, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Photon energy E = hf = hc/λ, the photoelectric equation E_k,max = hf − W
(one photon frees at most one electron), threshold frequency f0 = W/h and threshold wavelength λ0 = hc/W.
1 eV = 1,602 · 10⁻¹⁹ J. The simulation's model is the same: light of wavelength λ and relative intensity Iv (%) on
a metal plate (natrium W = 2,28 eV, magnesium 3,68 eV, sinkki 4,31 eV); when hf ≥ W the picture frees
n = 0,4 · Iv electrons per second, each with at most E_k,max = hf − W. Prints {id: number} as JSON."""
import json

h, c, e, me = 6.626e-34, 2.998e8, 1.602e-19, 9.109e-31     # J s, m/s, C (1 eV = e · 1 V), kg
E_J = lambda lam_nm: h * c / (lam_nm * 1e-9)                # photon energy in J from λ in nm
E_eV = lambda lam_nm: E_J(lam_nm) / e                       # the same in eV
W = {"Na": 2.28, "Mg": 3.68, "Zn": 4.31}                    # work functions in eV (typical table values)
Ek = lambda lam, m: max(0.0, E_eV(lam) - W[m])              # E_k,max in eV, 0 when no electron is freed
a = {}

# --- theory: the electronvolt and the photon energy of 500 nm light ---
a["hc-Jm"] = h * c                                          # 1,986e-25 J m
a["hc-over-e-nm"] = h * c / e * 1e9                         # hc/e = 1240 eV·nm: E (eV) = 1240 : λ (nm)
a["teoria-500-J"] = E_J(500)                                # 3,973e-19 J
a["teoria-500-eV"] = E_eV(500)                              # 2,480 eV
a["teoria-500-f"] = c / 500e-9                              # 5,996e14 Hz
a["h-eVs"] = h / e                                          # 4,136e-15 eV s, the slope of the E_k,max(f) graph
for m in W:                                                 # threshold frequency and wavelength of each metal
    a[f"f0-{m}"] = W[m] * e / h                             # Na 5,51e14, Mg 8,90e14, Zn 1,04e15 Hz
    a[f"lam0-{m}"] = h * c / (W[m] * e) * 1e9               # Na 543,9 nm, Mg 337,0 nm, Zn 287,7 nm
# figure "energia": sodium, three wavelengths
for lam in (650, 544, 405):
    a[f"fig-E-{lam}"] = E_eV(lam)                           # 1,908 / 2,279 / 3,062 eV
# figure "ilmio": red 650 nm and UV 254 nm on zinc
a["fig-red"] = E_eV(650)                                    # 1,91 eV < 4,31 eV
a["fig-uv"] = E_eV(254)                                     # 4,88 eV > 4,31 eV

# --- worked example: sodium, 405 nm ---
a["ex-EJ"] = E_J(405)                                       # 4,905e-19 J
a["ex-WJ"] = 2.28 * e                                       # 3,653e-19 J
a["ex-EkJ"] = a["ex-EJ"] - a["ex-WJ"]                       # 1,252e-19 J
a["ex-Ek"] = a["ex-EkJ"] / e                                # 0,782 eV -> 0,78 eV
a["ex-E-eV"] = E_eV(405)                                    # check: 3,06 eV − 2,28 eV = 0,78 eV

# --- simulation and experiments (sodium unless named) ---
a["sim-load-E"] = E_eV(405)                                 # on load: 405 nm, 50 %, natrium
a["sim-load-Ek"] = Ek(405, "Na")
a["sim-load-n"] = 0.4 * 50                                  # 20 electrons per second in the picture
a["sim-load-f"] = c / 405e-9                                # 7,402e14 Hz
for Iv in (20, 50, 100):                                    # koe 1: 650 nm, vary intensity: nothing is freed
    a[f"koe1-I{Iv}-n"] = 0.0 if E_eV(650) < W["Na"] else 0.4 * Iv
    a[f"koe1-I{Iv}-E"] = E_eV(650)                          # 1,91 eV every time
for Iv in (20, 50, 100):                                    # koe 2: 405 nm, vary intensity
    a[f"koe2-I{Iv}-n"] = 0.4 * Iv                           # 8 / 20 / 40 per second
    a[f"koe2-I{Iv}-Ek"] = Ek(405, "Na")                     # 0,78 eV every time
for lam in (300, 400, 500, 540, 545, 550, 600):             # koe 3: intensity 50 %, vary λ
    a[f"koe3-{lam}-E"] = E_eV(lam)                          # 4,13 / 3,10 / 2,48 / 2,30 / 2,28 / 2,25 / 2,07 eV
    a[f"koe3-{lam}-Ek"] = Ek(lam, "Na")                     # 1,85 / 0,82 / 0,20 / 0,016 / 0 / 0 / 0 eV
a["koe-3"] = a["lam0-Na"]                                   # the experiment's question: λ0 of sodium = 544 nm
a["koe3-mis-f"] = a["f0-Na"]                                # mistake: the threshold frequency instead
a["koe3-check-E"] = 1240 / 544                              # 2,28 eV at 544 nm
for m in W:                                                 # extremes of the sweep: 200 nm on each metal
    a[f"sim-200-{m}-Ek"] = Ek(200, m)                       # Na 3,92 / Mg 2,52 / Zn 1,89 eV
a["sim-700-E"] = E_eV(700)                                  # 1,77 eV

# --- inquiry: retrieval, error spotting, transfer task, checks, exit ticket ---
a["virhe-right"] = E_J(500)                                 # 3,97e-19 J
a["virhe-wrong"] = h * c / 500                              # λ in nm left unconverted: 3,97e-28 J
a["siirto"] = h * c / (1.90 * e) * 1e9                      # photocathode W = 1,90 eV: λ0 = 652,6 nm -> 653 nm
a["siirto-mis-f"] = 1.90 * e / h                            # mistake: the frequency 4,594e14 Hz
a["siirto-mis-eV"] = h * c / 1.90 * 1e9                     # mistake: W left in eV: 1,05e-16 nm
a["siirto-check-E"] = E_eV(653)                             # 1,90 eV back
a["tarkistus-1-uv"] = E_eV(254)                             # 4,88 eV > 4,31 eV: zinc frees electrons
a["tarkistus-1-red"] = E_eV(650)                            # 1,91 eV < 4,31 eV: no electrons however bright
a["tarkistus-2"] = E_eV(450)                                # blue LED 450 nm: 2,755 eV -> 2,76 eV
a["tarkistus-2-J"] = E_J(450)                               # 4,414e-19 J
a["tarkistus-2-mis-J"] = E_J(450)                           # mistake: left in joules
a["exit-1"] = h * 1.0e15                                    # f = 1,0e15 Hz: 6,6e-19 J
a["exit-1-eV"] = h * 1.0e15 / e                             # 4,1 eV
a["exit-2-yellow"] = E_eV(590)                              # 2,10 eV < 2,28 eV: brighter yellow frees none
a["exit-2-blue"] = E_eV(470)                                # 2,64 eV > 2,28 eV: blue light frees electrons
print(json.dumps({k: round(v, 6) if abs(v) >= 1e-3 else float(f"{v:.6g}") for k, v in a.items()}))
