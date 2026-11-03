"""Numbers of the lesson text and inquiry.json for fy8-6, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. An LED lights when an electron that has crossed the voltage U_k gives about the
energy of the band gap to one photon: e U_k ≈ hf = hc/λ, so U_k = (h/e) f + b and the slope of the (f, U_k) line is h/e.
The simulation's model is the same: six LEDs with peak wavelength λ and threshold voltage U_k (model values a little
below hc/(eλ), as in real LEDs), current I = (s/R) · ln(1 + exp((U − U_k)/s)) with s = 0,035 V and R = 18 Ω: about
zero below U_k, and a straight line I = (U − U_k)/R above it, which crosses the U axis at U_k.
Prints {id: number} as JSON on the last line."""
import json, math

h, c, e = 6.626e-34, 2.998e8, 1.602e-19                     # J s, m/s, C (1 eV = e · 1 V)
S, R = 0.035, 18.0                                          # V, Ω: the onset width and the LED's resistance above U_k
LEDS = {"R": (630, 1.88), "O": (605, 1.95), "Y": (590, 2.00), "G": (525, 2.30), "B": (470, 2.52), "V": (405, 2.95)}
I_mA = lambda U, Uk: S / R * math.log1p(math.exp((U - Uk) / S)) * 1000   # the model's current in mA
E_eV = lambda lam: h * c / (lam * 1e-9) / e                 # photon energy in eV from λ in nm
f_Hz = lambda lam: c / (lam * 1e-9)                         # frequency from λ in nm


def fit(pts):
    """Least-squares line y = k x + b through the points (what Graphical Analysis' Lineaarinen gives)."""
    nx = len(pts); mx = sum(x for x, _ in pts) / nx; my = sum(y for _, y in pts) / nx
    k = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, _ in pts)
    return k, my - k * mx


a = {}
# --- theory: the LEDs of the data set, hc/(eλ) beside the model's U_k ---
a["hc-over-e-nm"] = h * c / e * 1e9                         # 1240 V nm: hc/(eλ) in volts = 1240 : λ (nm)
for key, (lam, Uk) in LEDS.items():
    a[f"f-{key}"] = f_Hz(lam)                               # R 4,759e14 · O 4,955e14 · Y 5,081e14 · G 5,710e14 · B 6,379e14 · V 7,402e14 Hz
    a[f"Eph-{key}"] = E_eV(lam)                             # 1,968 / 2,050 / 2,102 / 2,362 / 2,638 / 3,062 eV
    a[f"diff-{key}"] = Uk - E_eV(lam)                       # e U_k − hf in eV: −0,09 / −0,10 / −0,10 / −0,06 / −0,12 / −0,11
k, b = fit([(f_Hz(lam), Uk) for lam, Uk in LEDS.values()])
a["fit-k"] = k                                              # 4,054e-15 V/Hz = V s
a["fit-b"] = b                                              # −0,050 V
a["fit-h"] = e * k                                          # 6,494e-34 J s -> 6,49e-34 J s
a["fit-dev-pct"] = (e * k - h) / h * 100                    # −2,0 %
a["fit-1-over-lambda"] = k * c                              # mistake: slope of U_k against 1/λ, 1,215e-6 V m
# blue against red: the extra photon energy and the extra voltage
a["teoria-red-E"] = E_eV(630)                               # 1,97 eV
a["teoria-blue-E"] = E_eV(470)                              # 2,64 eV
# figure "iu": the extrapolated lines of the red, green and blue LEDs cross the U axis at U_k
for key in ("R", "G", "B"):
    a[f"iu-{key}-20mA"] = LEDS[key][1] + 0.020 * R          # U where the straight part reaches 20 mA: 2,24 / 2,66 / 2,88 V

# --- worked example: two points on a fitted line ---
k_ex = (2.96 - 1.74) / (7.50e14 - 4.50e14)                  # (4,50e14 Hz; 1,74 V) and (7,50e14 Hz; 2,96 V): 4,067e-15 V s
a["ex-k"] = k_ex
a["ex-h"] = e * k_ex                                        # 6,515e-34 J s -> 6,52e-34 J s
a["ex-dev-pct"] = (e * k_ex - h) / h * 100                  # −1,7 %

# --- simulation and experiments ---
a["sim-load-I"] = I_mA(2.00, LEDS["R"][1])                  # on load: red LED at 2,00 V: 6,72 mA
for key, (lam, Uk) in LEDS.items():                         # koe 1: every LED at 2,20 V
    a[f"koe1-{key}"] = I_mA(2.20, Uk)                       # R 17,8 · O 13,9 · Y 11,1 · G 0,108 · B 0,0002 · V 0,0000 mA
for U in (0.50, 1.00, 1.50, 1.70, 1.80, 1.90, 2.00, 2.10, 2.20, 2.30, 2.40):   # koe 2: the red LED's I–U curve
    a[f"koe2-{U:.2f}"] = I_mA(U, LEDS["R"][1])              # 0 / 0 / 0,000 / 0,02 / 0,24 / 1,37 / 6,72 / 12,2 / 17,8 / 23,3 / 28,9 mA
k2, b2 = fit([(U, I_mA(U, LEDS["R"][1])) for U in (2.00, 2.10, 2.20, 2.30, 2.40)])
a["koe-2"] = -b2 / k2                                       # the straight part extrapolated to I = 0: 1,879 V -> 1,88 V
a["koe-2-slope"] = k2                                       # 55,6 mA/V = 1/R
a["koe-2-mis-onset"] = 1.70                                 # mistake: the voltage where the first current shows
a["koe2-ratio-1V"] = 1.0 / R * 1000                         # a resistor of 18 Ω would carry 55,6 mA at 1,00 V
a["sim-max"] = I_mA(3.50, LEDS["R"][1])                     # red at 3,50 V: 90 mA, far over the 30 mA limit
a["sim-V-350"] = I_mA(3.50, LEDS["V"][1])                   # violet at 3,50 V: 30,6 mA
a["sim-V-320"] = I_mA(3.20, LEDS["V"][1])                   # violet at 3,20 V: 13,9 mA

# --- inquiry: interpret, error spotting, transfer, checks, exit ticket ---
a["data"] = a["fit-h"]                                      # the interpret question: h from the fitted slope, 6,49e-34 J s
a["data-mis-k"] = k                                         # mistake: the slope itself, 4,05e-15 V s
a["siirto"] = h * c / (e * 1.30) * 1e9                      # infrared LED with U_k = 1,30 V: λ ≈ hc/(eU_k) = 953,8 nm -> 954 nm
a["siirto-mis-m"] = h * c / (e * 1.30)                      # mistake: left in metres, 9,54e-7
a["siirto-mis-eV"] = h * c / 1.30 * 1e9                     # mistake: eU left as 1,30 without e
a["siirto-check"] = 1240 / 954                              # 1,30 eV back
k_g = (2.80 - 1.80) / (7.0e14 - 4.6e14)                     # check 2, the figure: the line through (4,6e14 Hz; 1,80 V) and (7,0e14 Hz; 2,80 V)
a["tarkistus-2"] = e * k_g                                  # 6,675e-34 J s -> 6,68e-34 J s
a["tarkistus-2-k"] = k_g                                    # 4,167e-15 V s
a["tarkistus-2-mis-k"] = k_g                                # mistake: the slope itself, without e
a["tarkistus-1-red"] = E_eV(630)                            # 1,97 eV
a["tarkistus-1-blue"] = E_eV(470)                           # 2,64 eV
a["exit-1"] = h * c / (e * 470e-9)                          # blue 470 nm: U_k ≈ 2,64 V (a real one a little less, about 2,5 V)
print(json.dumps({k_: round(v, 6) if abs(v) >= 1e-3 else float(f"{v:.6g}") for k_, v in a.items()}))
