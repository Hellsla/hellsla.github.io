"""Numbers of the lesson text and inquiry.json for fy7-2, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Magnetic force F = qvB sin α, circular path qvB = mv²/r so r = mv/(qB),
velocity selector qE = qvB so v = E/B, acceleration from rest qU = ½mv². Constants as the lesson and the simulation
give them: e = 1,602e-19 C, m_p = 1,673e-27 kg, m_d = 3,344e-27 kg, m_α = 6,645e-27 kg, u = 1,661e-27 kg.
Prints {id: number} as JSON."""
import json, math

e, mp, md, ma, u, g = 1.602e-19, 1.673e-27, 3.344e-27, 6.645e-27, 1.661e-27, 9.81
a = {}
# Ydinajatus: a proton at 1,0e6 m/s perpendicular to B = 0,20 T
a["yd-F"] = e * 1.0e6 * 0.20                      # F = qvB = 3,204e-14 N
a["yd-r"] = mp * 1.0e6 / (e * 0.20)               # r = mv/(qB) = 0,0522 m = 5,2 cm
a["yd-G"] = mp * g                                # its weight mg = 1,64e-26 N, about 10^-12 of F
a["yd-ratio"] = a["yd-F"] / a["yd-G"]             # F : G = 2,0e12
# Kaava figure: r against v for the proton and the deuteron at B = 0,20 T
for v in (0.5, 1.0, 1.5, 2.0):
    a[f"fig-rp-{v}"] = mp * v * 1e6 / (e * 0.20) * 100   # cm: 2,61 5,22 7,83 10,44
    a[f"fig-rd-{v}"] = md * v * 1e6 / (e * 0.20) * 100   # cm: 5,22 10,44 15,66 20,87
# Worked example: Ne+ ions, selector E = 6,00e4 V/m and B1 = 0,200 T, then B2 = 0,500 T, hit 24,9 cm from the slit
v_ex = 6.00e4 / 0.200                              # v = E/B1 = 3,00e5 m/s
a["ex-v"] = v_ex
a["ex-r"] = 0.249 / 2                              # r = d/2 = 0,1245 m
a["ex-m"] = e * 0.500 * 0.1245 / v_ex              # m = qB2 r / v = 3,324e-26 kg
a["ex-m-u"] = a["ex-m"] / u                        # 20,01 u: neon-20 (19,99 u)
a["ex-qB2r"] = e * 0.500 * 0.1245                  # the numerator qB2 r = 9,973e-21 kg·m/s
a["ex-r22"] = 22 * u * v_ex / (e * 0.500)          # Järkevyys/figure: Ne-22 r = 0,1369 m, d = 27,4 cm
a["ex-d22"] = 2 * a["ex-r22"] * 100
a["ex-d20"] = 2 * 20 * u * v_ex / (e * 0.500) * 100   # Ne-20 (20 u) would land at 24,9 cm
a["ex-dm-per-u"] = 2 * u * v_ex / (e * 0.500) * 100   # 1 u more moves the spot 1,24 cm
# Misconception: speed constant, the force does no work; an electron at the same speed in the same field
a["mis-ratio"] = mp / 9.109e-31                    # m_p / m_e = 1837: the electron's circle is 1837 times smaller
# Hiukkaskiihdytin: LHC (CERN, The LHC guide 2017; Run 3 2022): 26,7 km ring, 1232 dipoles of 8,33 T, 6,8 TeV protons
a["lhc-r"] = 26659 / (2 * math.pi)                 # the ring's mean radius 4243 m (the dipoles bend on a radius of 2804 m)
a["lhc-E"] = 6.8e12 * e                            # 6,8 TeV per proton = 1,09e-6 J
a["lhc-gamma"] = a["lhc-E"] / (mp * 2.998e8 ** 2)  # E/(mc²) = 7240: far beyond r = mv/(qB) with the classical momentum
# kertaus: a proton accelerated from rest by U = 1000 V; four times the voltage doubles the speed
a["kertaus-v1"] = math.sqrt(2 * e * 1000 / mp)     # 4,38e5 m/s
a["kertaus-v4"] = math.sqrt(2 * e * 4000 / mp)     # 8,75e5 m/s = 2 · v1
# Simulation, koe-1: proton, B = 0,20 T out of the page, E = 0; the hit point d = 2r on the detector
for v in (0.5, 1.0, 1.5, 2.0, 2.5):
    a[f"koe1-d-{v}"] = 2 * mp * v * 1e6 / (e * 0.20) * 100   # 5,22 10,44 15,67 20,89 (26,1: beyond the 23 cm detector)
# koe-2: selector E = 150 kV/m, B = 0,15 T, v = 1,0e6 m/s: v = E/B for every particle
a["koe2-vEB"] = 150e3 / 0.15                       # 1,0e6 m/s
a["koe2-Fp"] = e * 1.0e6 * 0.15 * 1e14             # proton F_m = F_s = 2,40e-14 N (in 1e-14 N)
a["koe2-Fa"] = 2 * e * 1.0e6 * 0.15 * 1e14         # alpha particle 4,81e-14 N
a["koe2-ra-noE"] = ma * 1.0e6 / (2 * e * 0.15)     # without E the alpha particle would turn on r = 0,138 m
a["koe2-rp-noE"] = mp * 1.0e6 / (e * 0.15)         # the proton on 0,0696 m
# virhe: a proton accelerated by U = 2,0 kV into B = 0,10 T; the student forgot the 2 in v = sqrt(2qU/m)
v_ok = math.sqrt(2 * e * 2000 / mp)                # 6,19e5 m/s
v_bad = math.sqrt(e * 2000 / mp)                   # 4,38e5 m/s
a["virhe-v-ok"], a["virhe-v-bad"] = v_ok, v_bad
a["virhe-r-ok"] = mp * v_ok / (e * 0.10) * 100     # 6,46 cm
a["virhe-r-bad"] = mp * v_bad / (e * 0.10) * 100   # 4,57 cm
# siirto: B-11 ions (11,01 u, q = e) accelerated by U = 20 kV in an ion implanter; analysing magnet r = 0,30 m
m_B = 11.01 * u                                    # 1,829e-26 kg
v_B = math.sqrt(2 * e * 20e3 / m_B)                # 5,92e5 m/s
a["siirto-v"] = v_B
a["siirto-B"] = m_B * v_B / (e * 0.30)             # B = mv/(qr) = 0,225 T
a["siirto-mistake-no2"] = m_B * math.sqrt(e * 20e3 / m_B) / (e * 0.30)   # forgot the 2: 0,159 T
a["siirto-mistake-kV"] = m_B * math.sqrt(2 * e * 20 / m_B) / (e * 0.30)  # U = 20 V: 0,00712 T
# tarkistus-3: alpha particle v = 1,5e6 m/s, B = 0,50 T
a["t3-r"] = ma * 1.5e6 / (2 * e * 0.50) * 100      # 6,22 cm
a["t3-rp"] = mp * 1.5e6 / (e * 0.50) * 100         # Järkevyys: the proton at the same speed 3,13 cm, half of the alpha's
a["t3-r-q1"] = ma * 1.5e6 / (e * 0.50) * 100       # q = e by mistake: 12,4 cm
# siirto with U = 20,0 kV, r = 0,300 m (the same numbers): m = 1,8288e-26 kg
a["siirto-m"] = m_B
a["siirto-check-r"] = m_B * v_B / (e * a["siirto-B"])   # 0,300 m back
# exit ticket: selector E = 3,0e4 V/m, B = 0,10 T
a["exit-v"] = 3.0e4 / 0.10                         # 3,0e5 m/s
print(json.dumps({k: float(f"{v:.6g}") for k, v in a.items()}))
