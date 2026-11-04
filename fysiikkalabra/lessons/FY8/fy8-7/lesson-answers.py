"""Numbers of the lesson text and inquiry.json for fy8-7, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Prints {id: number} as JSON on the last line.
The simulation's model (assets/sims/fy8/fy8-7/sim.js) is reproduced in `model()` below: three-level medium (ground 1,
fast pump level 3 -> metastable 2, laser 2 -> 1) or two-level medium, populations as fractions of all atoms, spontaneous
lifetime tau = 1,0 ms, pump rate W = P_p / (1 W · tau), threshold inversion n2 - n1 = D = 0,10 with the mirrors
(1 without them: never reached), output P_out = 100 mW · (W tau n1 - n2) above threshold."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19
hc = h * c
def eV(nm): return hc / (nm * 1e-9) / e

def model(P, levels=3, mirrors=True):
    """Steady state of the sim's rate equations: (n2 %, n1 %, P_out mW)."""
    w = P / 1.0                                   # W tau
    D = 0.10 if mirrors else 1.0
    if levels == 2:
        n2 = w / (1 + 2 * w)                      # pump excites and stimulates down alike: n2 -> 1/2, never above
        return 100 * n2, 100 * (1 - n2), 0.0
    n2 = w / (1 + w)                              # below threshold: pump n1 W = decay n2 / tau
    if mirrors and n2 - (1 - n2) > D:             # above threshold the inversion is clamped at D
        n2 = (1 + D) / 2
        return 100 * n2, 100 * (1 - n2), 100 * (w * (1 - n2) - n2)
    return 100 * n2, 100 * (1 - n2), 0.0

a = {}
# lesson.md: Kaava graph (1,0 mW lasers) and worked example (He-Ne, transition 1,96 eV, 1,0 mW)
for nm in (405, 532, 650): a[f"rate-1mW-{nm}"] = 1.0e-3 * nm * 1e-9 / hc        # 2,04e15; 2,68e15; 3,27e15 1/s
a["ex-hf-J"] = 1.96 * e                                    # 3,1399e-19 J
a["ex-rate"] = 1.0e-3 / (1.96 * e)                         # 3,1848e15 1/s -> 3,2e15
a["ex-lambda"] = hc / (1.96 * e) * 1e9                     # 632,65 nm: the He-Ne red line 633 nm
a["ruby-694-eV"] = eV(694)                                 # 1,79 eV
a["visible-eV-700"] = eV(700); a["visible-eV-380"] = eV(380)   # 1,77 and 3,26 eV: "1,7-3,3 eV"
a["cdse-bulk-nm"] = hc / (1.74 * e) * 1e9                  # bulk CdSe gap 1,74 eV -> 713 nm
# misconception: a 1 mW red pointer and a 1 mW violet pointer, photon energies
a["mis-650"] = eV(650); a["mis-405"] = eV(405)             # 1,91 eV, 3,06 eV
# inquiry: kertaus (hydrogen 3 -> 2 gives 1,89 eV, 656 nm)
a["kert-656-eV"] = eV(656)                                 # 1,89 eV
# sim: koe-1 (three levels, mirrors), koe-2 (two levels), koe-3 (no mirrors)
for P in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0):
    n2, n1, Po = model(P); a[f"koe1-{P}-n2"] = n2; a[f"koe1-{P}-P"] = Po
a["threshold-W"] = (1 + 0.10) / (1 - 0.10)                 # W tau n1 = n2 at n2 = 0,55: P_th = 0,55 / 0,45 W = 1,22 W
for P in (1.0, 2.0, 5.0): a[f"koe2-{P}-n2"] = model(P, 2)[0]       # 33,3 %; 40,0 %; 45,5 %
for P in (2.0, 5.0): a[f"koe3-{P}-n2"] = model(P, 3, False)[0]     # 66,7 %; 83,3 %, no beam
# quantum dots table (example data): photon energy of each colour
for d, nm in ((2.0, 480), (3.0, 530), (4.0, 570), (5.0, 600), (6.0, 620)): a[f"qd-{d}"] = eV(nm)
# siirto: fibre laser 1,0 kW at 1070 nm pumped at 976 nm: least heat per second
a["siirto"] = 1000 * (1070 / 976 - 1)                      # pump >= 1000 W · 1070/976 = 1096,3 W -> heat 96,3 W
a["siirto-m-ratio"] = 1000 * (1 - 976 / 1070)              # mistake: output used as the pump power: 87,9 W
a["siirto-m-pump"] = 1000 * 1070 / 976                     # mistake: the pump power itself 1096 W
# virhe (optional): the 5,0 mW green pointer with lambda in nm left unconverted
a["virhe-right"] = 5.0e-3 * 532e-9 / hc                    # 1,34e16 1/s
# tarkistus-2: levels -3,12 eV and -5,45 eV
a["tark2"] = hc / ((5.45 - 3.12) * e) * 1e9                # 2,33 eV -> 532,19 nm -> 532 nm
a["tark2-m-312"] = hc / (3.12 * e) * 1e9                   # 397 nm
a["tark2-m-545"] = hc / (5.45 * e) * 1e9                   # 228 nm
print(json.dumps({k: float(f"{v:.7g}") for k, v in a.items()}))
