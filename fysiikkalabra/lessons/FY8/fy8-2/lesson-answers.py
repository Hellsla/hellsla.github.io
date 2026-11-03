"""Numbers of the lesson text and inquiry.json for fy8-2, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Photon energy E = hf = hc/λ equals the difference of two energy states.
Hydrogen levels E_n = -13,6 eV / n² are given as data (FY8 scope). Prints {id: number} as JSON on the last line."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19          # J s, m/s, C (1 eV = 1,602e-19 J)
HC_EVNM = h * c / e * 1e9                         # hc in eV·nm = 1239,99 (the sim uses the same constants)
E = lambda n: -13.6 / n ** 2                      # hydrogen level n in eV (data)
lam = lambda dE: HC_EVNM / dE                     # wavelength in nm of a photon of dE eV
a = {}
# Hydrogen level table of the lesson (Kaava): -13,6; -3,40; -1,51; -0,85; -0,54; -0,38 eV
for n in range(1, 7): a[f"E{n}"] = E(n)
# Koe 1 (emission to n = 2) and prediction 1: 656, 486, 434, 410 nm; spacing 170, 52, 24 nm
for n in range(3, 7):
    a[f"koe1-dE-{n}"] = E(n) - E(2)               # 1,89; 2,55; 2,86; 3,02 eV
    a[f"koe1-lam-{n}"] = lam(E(n) - E(2))         # 656,4; 486,2; 434,1; 410,2 nm
a["koe1-gap-34"] = lam(E(3) - E(2)) - lam(E(4) - E(2))   # 170 nm
a["koe1-gap-45"] = lam(E(4) - E(2)) - lam(E(5) - E(2))   # 52 nm
a["koe1-gap-56"] = lam(E(5) - E(2)) - lam(E(6) - E(2))   # 24 nm
a["series-limit-2"] = lam(0 - E(2))               # n = ∞ -> 2: 364,7 nm, the Balmer lines crowd towards it
# Koe 2 (absorption from n = 1) and prediction 2: 122, 103, 97, 95, 94 nm, all ultraviolet
for n in range(2, 7):
    a[f"koe2-dE-{n}"] = E(n) - E(1)               # 10,2; 12,09; 12,75; 13,06; 13,22 eV
    a[f"koe2-lam-{n}"] = lam(E(n) - E(1))         # 121,6; 102,6; 97,3; 95,0; 93,8 nm
a["ion-1"] = lam(0 - E(1))                        # ionisation from n = 1: 91,2 nm
a["visible-min-eV"] = HC_EVNM / 750               # visible light 380–750 nm is 1,65–3,26 eV
a["visible-max-eV"] = HC_EVNM / 380
# Retrieval (kertaus): red 650 nm and violet 410 nm photons
a["kertaus-650"] = HC_EVNM / 650      # 1,91 eV
a["kertaus-410"] = HC_EVNM / 410                  # 3,02 eV
# Worked example: neon line 640 nm. ΔE = hc/λ in J, then in eV
a["ex-J"] = h * c / 640e-9                        # 3,1037e-19 J
a["ex-eV"] = h * c / 640e-9 / e                   # 1,9374 eV -> 1,94 eV
a["ex-check-eV"] = 1240 / 640                     # estimate with hc ≈ 1240 eV·nm: 1,94 eV
# Etsi virhe: ΔE = 1,89 eV put in without the conversion to joules
a["virhe-wrong"] = h * c / 1.89                   # 1,05e-25 "m"
a["virhe-J"] = 1.89 * e                           # 3,028e-19 J, the conversion that was missing
a["virhe-right-nm"] = h * c / (1.89 * e) * 1e9    # 656 nm
# Transfer (siirto): highlighter absorbs 365 nm, emits 520 nm; energy left in the ink per photon
a["siirto-in"] = h * c / (365e-9 * e)             # 3,397 eV
a["siirto-out"] = h * c / (520e-9 * e)            # 2,385 eV
a["siirto"] = a["siirto-in"] - a["siirto-out"]    # 1,0126 eV -> 1,01 eV
a["siirto-mistake-nm"] = 520 - 365                # 155 (the wavelengths subtracted)
a["siirto-mistake-lam"] = h * c / (155e-9 * e)    # 8,00 eV: hc/(λ2 − λ1) is not an energy difference
# Check 2: sodium street lamp 589 nm -> ΔE = 2,105 eV
a["check2"] = h * c / (589e-9 * e)                # 2,11 eV
a["check2-J"] = h * c / 589e-9                    # 3,37e-19 J (mistake: answered in units 1e-19 J)
# Interpret: the lines of the lamp 405, 436, 546, 577, 579 nm (mercury) as photon energies
a["lamp-546-eV"] = HC_EVNM / 546                  # 2,27 eV
# Fluorescence figure: UV 365 nm in (3,40 eV), visible 520 nm out (2,38 eV)
# Greenhouse box: CO2 absorbs about 15 µm: photon energy 0,083 eV, about 30 times smaller than at 500 nm
a["co2-eV"] = HC_EVNM / 15000                     # 0,0827 eV
a["co2-ratio"] = 15000 / 500                      # 30
# Exit ticket: levels 0, 2,0 and 3,0 eV give the photon energies 1,0, 2,0 and 3,0 eV
a["exit-1"] = 3.0 - 2.0
print(json.dumps({k: round(v, 6) if abs(v) > 1e-3 else v for k, v in a.items()}))
