"""Numbers of the lesson text and inquiry.json for fy7-7, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Rotating coil: Φ = BA cos(2πft), e = e0 sin(2πft), e0 = NBA · 2πf;
effective values U = U0 / √2, I = I0 / √2. Prints {id: number} as JSON."""
import json, math

r2 = math.sqrt(2)
a = {}
# Mains (Ydinajatus, Kaava, virhe, exit ticket 1): 230 V, 50 Hz
a["mains-U0"] = 230 * r2                             # peak 325,3 V -> 325 V
a["mains-T"] = 1 / 50                                # period 0,020 s = 20 ms
a["mains-reversals"] = 2 * 50                        # the voltage changes sign twice per period: 100 times a second
a["mains-wrong-sqrt2"] = 230 / r2                    # virhe distractor: 230 V / √2 = 162,6 V
# Grid frequency band (Fingrid): 49,9–50,1 Hz, i.e. ±0,2 %
a["grid-band-pct"] = 0.1 / 50 * 100                  # 0,2 %
# Worked example: N = 250, A = 4,0 cm · 5,0 cm, B = 0,18 T, f = 12 Hz
A = 4.0 * 0.01 * 5.0 * 0.01                          # 0,0020 m²
a["ex-A"] = A
a["ex-e0"] = 250 * 0.18 * A * 2 * math.pi * 12       # e0 = 6,786 V
a["ex-U"] = a["ex-e0"] / r2                          # U = 4,798 V -> 4,8 V
a["ex-T"] = 1 / 12                                   # Järkevyys: period 0,083 s
a["ex-check-e0"] = 250 * 0.2 * 0.002 * 2 * math.pi * 10   # round-number estimate 250 · 0,2 · 0,002 · 6 · 10 ≈ 6 V (exact 6,28 V)
# Simulation: A = 20 cm² = 0,0020 m², defaults N = 500, B = 0,20 T, f = 2,0 Hz
a["sim-e0-default"] = 500 * 0.20 * A * 2 * math.pi * 2.0   # 2,513 V
a["sim-U-default"] = a["sim-e0-default"] / r2              # 1,777 V
a["sim-phimax-mWb"] = 0.20 * A * 1e3                        # BA = 0,40 mWb
for fq in (1.0, 2.0, 4.0):                                   # koe-1: e0 at 1, 2 and 4 Hz (N = 500, B = 0,20 T)
    a[f"koe1-e0-{fq:g}Hz"] = 500 * 0.20 * A * 2 * math.pi * fq   # 1,257; 2,513; 5,027 V
    a[f"koe1-T-{fq:g}Hz"] = 1 / fq                                # 1,0; 0,50; 0,25 s
for B in (0.10, 0.20, 0.30):                                 # koe-2: e0 at 0,10/0,20/0,30 T (N = 500, f = 2,0 Hz)
    a[f"koe2-e0-{B:g}T"] = 500 * B * A * 2 * math.pi * 2.0      # 1,257; 2,513; 3,770 V
a["sim-e0-max"] = 1000 * 0.30 * A * 2 * math.pi * 5.0       # largest e0 in the sim: 18,85 V (graph scale ±20 V)
# Kaava: the derivation from e = vBl, a side at radius b/2 moves at v = 2πf · b/2 = πfb; two sides, A = lb
# e_turn = 2 · B l v sin θ = 2 B l π f b sin θ = BA · 2πf sin θ  (identity, no number)
# Kaava: mean power of a resistor, p = U0 I0 sin² -> mean U0 I0 / 2 = (U0/√2)(I0/√2)
a["sin2-mean"] = sum(math.sin(2 * math.pi * k / 1000) ** 2 for k in range(1000)) / 1000   # 0,5
# Kertaus (retrieval): flux constant -> e = 0
a["kertaus-e"] = 0.0
# siirto: small wind turbine, N = 120, A = 0,015 m², B = 0,40 T, 300 r/min
f_s = 300 / 60                                        # 5,0 Hz
a["siirto-e0"] = 120 * 0.40 * 0.015 * 2 * math.pi * f_s    # 22,62 V
a["siirto"] = a["siirto-e0"] / r2                     # U = 15,99 V -> 16 V
a["siirto-peak"] = a["siirto-e0"]                     # mistake: peak given as the answer, 22,6 V
a["siirto-rpm"] = 120 * 0.40 * 0.015 * 2 * math.pi * 300 / r2   # mistake: 300 used as Hz: 959,6 V
a["siirto-times-sqrt2"] = a["siirto-e0"] * r2         # mistake: multiplied by √2: 32,0 V
a["siirto-no-2pi"] = 120 * 0.40 * 0.015 * f_s / r2    # mistake: 2π left out: 2,546 V
# tarkistus-2: kettle 2,00 kW at 230 V: effective current and its peak
I_eff = 2000 / 230
a["check-I"] = I_eff                                  # 8,696 A
a["check-I0"] = I_eff * r2                            # 12,30 A -> 12,3 A
a["check-I0-div"] = I_eff / r2                        # mistake: divided by √2: 6,149 A
# Wind power in Finland 2024 (Suomen Uusiutuvat ry): 1835 turbines, 8358 MW, 19,8 TWh, 24 % of consumption
a["wind-mean-MW-per-turbine"] = 8358 / 1835           # 4,55 MW
a["wind-mean-GW"] = 19.8e12 / (366 * 24) / 1e9        # 2,254 GW mean power over 2024 (8784 h)
a["wind-rotor-f"] = 12 / 60                           # a rotor at 12 r/min turns 0,20 times a second
a["wind-gear"] = 1500 / 12                            # gearbox 12 r/min -> 1500 r/min: ratio 125
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
