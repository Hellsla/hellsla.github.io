"""Numbers of the lesson text and inquiry.json for fy6-16, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Typical example values, not measurements: battery 64 kWh (400 V, 160 Ah),
mains phase voltage 230 V, single-phase P = U I, three-phase P = 3 U I (the same current in each phase conductor),
charging efficiency eta = W_akku : W_verkko, t = W_akku : (eta P), cost K = a W_verkko, cable heating P = R I^2 with
R = rho · 2 l : A, copper rho = 1,7 · 10^-8 ohm m. Prints {id: number} as JSON."""
import json, math

U, RHO = 230.0, 1.7e-8
a = {}
# --- Ydinajatus: the battery ---
a["battery-kWh"] = 400 * 160 / 1000                          # W = U Q = 400 V · 160 Ah = 64 000 Wh = 64 kWh
a["range-km"] = 64 / 18 * 100                                # 18 kWh per 100 km: 64 kWh lasts about 356 km
a["per100-grid-kWh"] = 18 / 0.90                             # 18 kWh into the battery at eta 0,90: 20 kWh from the grid
a["per100-EUR"] = 0.15 * 18 / 0.90                           # at 15 snt/kWh: 3,0 EUR per 100 km
a["stove-hours"] = 64 / 6                                     # a 6 kW stove uses 64 kWh in 10,7 h

# --- Ydinajatus: three ways to charge (also the table "tavat") ---
a["P-socket-W"] = U * 8                                      # 1840 W, about 1,8 kW
a["P-1ph-W"] = U * 16                                        # 3680 W, about 3,7 kW
a["P-3ph-W"] = 3 * U * 16                                    # 11 040 W, about 11 kW
a["P-ratio"] = a["P-3ph-W"] / a["P-1ph-W"]                   # 3
W40 = 40.0                                                   # 40 kWh into the battery
a["t-socket-h"] = W40 / (0.85 * a["P-socket-W"] / 1000)      # 25,6 h
a["t-1ph-h"] = W40 / (0.90 * a["P-1ph-W"] / 1000)            # 12,1 h
a["t-3ph-h"] = W40 / (0.90 * a["P-3ph-W"] / 1000)            # 4,03 h
a["tavat"] = a["t-socket-h"]                                 # the table's numeric question: 25,6 h
a["tavat-mistake-noeta"] = W40 / (a["P-socket-W"] / 1000)    # efficiency forgotten: 21,7 h
a["tavat-mistake-times"] = 0.85 * W40 / (a["P-socket-W"] / 1000)   # multiplied by eta: 18,5 h

# --- Ydinajatus: the main fuse and the evening's loads (also the table "kuormat" and prediction 2) ---
a["main-fuse-W"] = 3 * U * 25                                # 3 · 230 V · 25 A = 17 250 W, about 17 kW
a["I-sauna"] = 9000 / (3 * U)                                # 9,0 kW on three phases: 13,04 A per phase
a["I-kettle"] = 2000 / U                                     # 2,0 kW on L1: 8,70 A
a["I-car"] = 16.0                                            # 11 kW charger: 16 A per phase
a["I-L1"] = a["I-sauna"] + a["I-kettle"] + a["I-car"]        # 37,7 A
a["I-L2"] = a["I-sauna"] + a["I-car"]                        # 29,0 A (also L3)
a["kuormat"] = a["I-L1"]                                     # the table's numeric question: 37,7 A
a["kuormat-mistake-nokettle"] = a["I-L2"]                    # kettle forgotten: 29,0 A
a["kuormat-mistake-1ph"] = (9000 + 2000 + 11040) / U         # all power taken as one 230 V current: 95,8 A
a["total-W"] = 9000 + 2000 + 11040                           # 22,0 kW > 17 kW
a["car-max-A"] = 25 - a["I-sauna"]                           # with the sauna on: 11,96 A per phase
a["car-max-W"] = 3 * U * a["car-max-A"]                      # 8,25 kW
a["L1-left-A"] = 25 - a["I-sauna"] - a["I-kettle"]           # with the kettle too: 3,26 A on L1 (below the 6 A minimum)

# --- Ydinajatus: cable and contact heating ---
R_reel = RHO * 2 * 25 / 1.5e-6                               # extension reel 25 m, 1,5 mm^2: 0,567 ohm
a["reel-R"] = R_reel
a["reel-P-10A"] = R_reel * 10 ** 2                           # 56,7 W
a["contact-P"] = 0.10 * 10 ** 2                              # contact 0,10 ohm at 10 A: 10 W
a["contact-E-10h"] = 0.10 * 10 ** 2 * 10 / 1000              # in 10 h: 0,10 kWh

# --- Kaava: the model charging curve (64 kWh, 20 % -> 99 %, 11 kW from the grid, eta 0,90) ---
Pb = 0.90 * 11.0                                             # 9,9 kW into the battery
a["curve-t1"] = 0.70 * 64 / Pb                               # constant power 20 % -> 90 %: 4,53 h
tau = 0.10 * 64 / Pb                                         # the last 10 %: P falls as exp(-(t - t1) / tau), tau = 0,646 h
a["curve-tau"] = tau
a["curve-tend"] = a["curve-t1"] + tau * math.log(10)         # stops at P = 1,1 kW (99 %): 6,01 h
a["curve-E1"] = 11.0 * a["curve-t1"]                         # area of the flat part: 49,8 kWh from the grid

# --- worked example: 64 kWh, 20 % -> 80 %, three-phase 16 A, eta 0,90, 15 snt/kWh ---
W_ex = 0.60 * 64                                             # 38,4 kWh
P_ex = 3 * U * 16 / 1000                                     # 11,04 kW
a["ex-W"] = W_ex
a["ex-P"] = P_ex
a["ex-Wgrid"] = W_ex / 0.90                                  # 42,67 kWh
a["ex-t"] = W_ex / (0.90 * P_ex)                             # 3,86 h
a["ex-K"] = 0.15 * W_ex / 0.90                               # 6,40 EUR
a["ex-check-t"] = 40 / 10                                    # estimate 40 kWh : 10 kW = 4 h
a["ex-noeta-t"] = W_ex / P_ex                                # without losses: 3,48 h
a["ex-km"] = W_ex / 18 * 100                                 # 38,4 kWh at 18 kWh/100 km: 213 km

# --- retrieval: battery energy W = U Q ---
a["kertaus"] = 400 * 150 / 1000                              # 400 V · 150 Ah = 60 kWh
a["kertaus-wrong-div"] = 400 / 150                           # 2,7 (divided)

# --- error spotting: eta multiplied instead of divided ---
a["virhe-wrong"] = 0.90 * 38.4                               # 34,56 kWh
a["virhe-right"] = 38.4 / 0.90                               # 42,67 kWh

# --- transfer: a 25 m, 2,5 mm^2 cable to a single-phase charger at 16 A ---
R_s = RHO * 2 * 25 / 2.5e-6                                  # 0,34 ohm
a["siirto-R"] = R_s
a["siirto"] = R_s * 16 ** 2                                  # 87,0 W
a["siirto-mistake-one"] = RHO * 25 / 2.5e-6 * 16 ** 2        # the neutral forgotten: 43,5 W
a["siirto-mistake-I"] = R_s * 16                             # I instead of I^2: 5,44
a["siirto-share"] = a["siirto"] / (U * 16) * 100             # 2,4 % of the 3680 W
a["siirto-8A"] = R_s * 8 ** 2                                # at 8 A: 21,8 W (a quarter)

# --- check 2: single-phase 16 A, eta 0,90, 30 kWh ---
a["tarkistus-2"] = 30 / (0.90 * U * 16 / 1000)               # 9,06 h
a["tarkistus-2-mistake-noeta"] = 30 / (U * 16 / 1000)        # 8,15 h
a["tarkistus-2-mistake-3ph"] = 30 / (0.90 * 3 * U * 16 / 1000)   # 3,02 h

# --- exit ticket ---
a["exit-1"] = 3 * U * 16                                     # 11 040 W, about 11 kW
a["exit-2"] = 45 / 0.90                                      # 50 kWh
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
