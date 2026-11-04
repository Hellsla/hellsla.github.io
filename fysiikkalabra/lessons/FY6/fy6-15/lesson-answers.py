"""Numbers of the lesson text and inquiry.json for fy6-15, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Loads of a group are in parallel at U = 230 V (the effective value of the mains
voltage), so I = (P1 + P2 + ...) : U and a fuse with rated current I_s allows P_max = U I_s. Conductors heat with
P = R I^2. The current through the body is I = U : R with R the resistance of the whole current path. Prints {id: number}."""
import json

U = 230.0
a = {}
# --- Ydinajatus and Kaava ---
a["pmax-10A"] = U * 10                                       # 2300 W on a 10 A group
a["pmax-16A"] = U * 16                                       # 3680 W on a 16 A group
a["double-I-power"] = 2 ** 2                                 # P = R I^2: twice the current, four times the power
a["wet-1k-mA"] = U / 1.0e3 * 1e3                             # 230 V over about 1 kOhm: 230 mA

# --- retrieval: kettle 2000 W on 230 V ---
a["kertaus"] = 2000 / U                                      # I = P : U = 8,70 A
a["kertaus-wrong-UP"] = U / 2000                             # U : P = 0,115 (not a current)

# --- the kitchen table (10 A group): each device's current I = P : U ---
for k, P in {"kettle": 2000, "coffee": 1000, "micro": 1200, "toaster": 900, "fridge": 100}.items():
    a[f"keittio-{k}-A"] = P / U                              # 8,70 / 4,35 / 5,22 / 3,91 / 0,435 A
a["keittio"] = (2000 + 1200) / U                             # kettle + microwave: 3200 W : 230 V = 13,9 A > 10 A
a["keittio-mistake-UP"] = U / 3200                           # U : P = 0,0719
a["keittio-all"] = (2000 + 1000 + 1200 + 900 + 100) / U      # everything at once: 5200 W : 230 V = 22,6 A

# --- the skin table at 230 V ---
a["iho-shoes-mA"] = U / 200e3 * 1e3                          # rubber soles on a dry floor, 200 kOhm: 1,15 mA
a["iho-dry-mA"] = U / 20e3 * 1e3                             # dry skin, bare feet on a dry floor, 20 kOhm: 11,5 mA
a["iho"] = U / 1.0e3 * 1e3                                   # wet skin, bare feet on a wet floor, 1,0 kOhm: 230 mA
a["iho-ratio"] = 200e3 / 1.0e3                               # 200 times the current from shoes to wet
a["iho-mistake-A"] = U / 1.0e3                               # 0,23 (amperes, not milliamperes)

# --- prediction 1: 0,1 A through a person, 10 A fuse, 30 mA RCD ---
a["ennuste-I-mA"] = 0.1 * 1e3                                # 100 mA, over 30 mA but one hundredth of 10 A
a["ennuste-fuse-ratio"] = 10 / 0.1                           # the fuse's rated current is 100 times the body current

# --- worked example: 16 A group, kettle 2,2 kW, coffee maker 1,0 kW, microwave 1,3 kW ---
P_ex = 2200 + 1000 + 1300                                    # 4500 W
a["ex-I"] = P_ex / U                                         # 19,6 A > 16 A
a["ex-I1"] = 2200 / U                                        # 9,57 A
a["ex-I2"] = 1000 / U                                        # 4,35 A
a["ex-I3"] = 1300 / U                                        # 5,65 A
a["ex-check"] = P_ex / 200                                   # estimate with 200 V: 22,5 A (a little too large)

# --- error spotting: kettle 2000 W and toaster 900 W on a 10 A group ---
a["virhe-I1"] = 2000 / U                                     # 8,7 A
a["virhe-I2"] = 900 / U                                      # 3,9 A
a["virhe-sum"] = (2000 + 900) / U                            # 12,6 A > 10 A

# --- transfer: building site, heater 2,0 kW + angle grinder 1,4 kW through a cord of 0,60 ohm ---
I_site = (2000 + 1400) / U                                   # 14,8 A
a["siirto-I"] = I_site
a["siirto"] = 0.60 * I_site ** 2                             # P = R I^2 = 131 W
a["siirto-mistake-nosquare"] = 0.60 * I_site                 # R I = 8,87 (a voltage, not a power)
a["siirto-mistake-heater"] = 0.60 * (2000 / U) ** 2          # only the heater: 45,4 W
a["siirto-mistake-U2R"] = U ** 2 / 0.60                      # U^2 : R with 230 V: 88 kW (wrong voltage)
a["siirto-drop"] = 0.60 * I_site                             # voltage over the cord 8,9 V, small beside 230 V

# --- exit ticket: a 16 A fuse on a wire designed for 10 A ---
a["exit-ratio"] = (16 / 10) ** 2                             # 2,56 times the heating power
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
