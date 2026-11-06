"""Every answer in exercises.json for fy6-16, computed from the task data (python -I answers.py).
Home charging of an electric car: energy into the battery W_akku = (share of capacity) · capacity; charging efficiency
eta = W_akku : W_verkko; time t = W_verkko : P = W_akku : (eta P); single-phase P = U I, three-phase P = 3 U I with the
phase voltage U = 230 V and the same current I in every phase conductor; cost K = a W_verkko; cable heating
P = R I^2 with R = rho · 2 l : A (the current goes out along the phase conductor and back along the neutral).
Copper rho = 1,7 · 10^-8 ohm m (the table in the chapter on resistance). Prints {exercise id: number} as JSON."""
import json

U = 230.0          # phase voltage of the Finnish mains (V)
RHO = 1.7e-8       # copper (ohm m)
a = {}
# Level 1: one formula, values given
a["fy6-16-L1-01"] = (0.80 - 0.15) * 64                    # 15 % -> 80 % of 64 kWh: 0,65 · 64 kWh = 41,6 kWh into the battery
a["fy6-16-L1-02"] = U * 10 / 1000                         # charging cable 10 A on 230 V: P = U I = 2300 W = 2,3 kW
a["fy6-16-L1-03"] = 11000 / (3 * U)                       # 11 kW three-phase: I = P : (3 U) = 11000 W : 690 V = 15,9 A
a["fy6-16-L1-04"] = 45 * 0.14                             # 45 kWh from the grid at 14 snt/kWh = 0,14 EUR/kWh: 6,30 EUR
a["fy6-16-L1-05"] = 44 / 50 * 100                         # 44 kWh into the battery of 50 kWh taken: eta = 0,88 = 88 %
a["fy6-16-L1-07"] = 7.4 * 5.5                             # 7,4 kW for 5,5 h: W = P t = 40,7 kWh from the grid
a["fy6-16-L1-08"] = 0.25 * 16 ** 2                        # cable R = 0,25 ohm, I = 16 A: P = R I^2 = 64 W
# (fy6-16-L1-06 is a multiple-choice concept task: no number)
# (fy6-16-L2-08 is a computed-value choice: t = 24 kWh : (0,85 · 1,84 kW) = 15,3 h; wrong options 11,1 h (times eta), 13,0 h (no eta), 5,1 h (P = 3UI))
# Level 2: two steps, a conversion or a figure
# figure fy6-16/lataus-ex: 11 kW for 0-2,0 h, 5,5 kW for 2,0-3,0 h, then 0
a["fy6-16-L2-01"] = 11 * 2.0 + 5.5 * 1.0                  # area under (t, P): 22 kWh + 5,5 kWh = 27,5 kWh from the grid
P1 = U * 16 / 1000                                        # single-phase charger 16 A: 3,68 kW
a["fy6-16-L2-02"] = (0.80 - 0.20) * 60 / (0.90 * P1)      # 36 kWh : (0,90 · 3,68 kW) = 10,9 h
a["fy6-16-L2-03"] = 25 - 9000 / (3 * U)                   # sauna stove 9,0 kW evenly on three phases: 13,04 A each; 25 A - 13,04 A = 11,96 A
R_cable = RHO * 2 * 30 / 2.5e-6                           # 30 m, 2,5 mm^2, out and back: 60 m of copper, 0,408 ohm
a["fy6-16-L2-04"] = R_cable * 16                          # voltage drop U = R I = 0,408 ohm · 16 A = 6,53 V
# L2-05: house power 17-22 h (kW): 2,1; 3,4; 6,8; 5,2; 3,9; main fuses 3 x 25 A
a["fy6-16-L2-05"] = 3 * U * 25 / 1000 - max([2.1, 3.4, 6.8, 5.2, 3.9])   # 17,25 kW - 6,8 kW (19-20 h) = 10,45 kW for the charger
a["fy6-16-L2-06"] = (0.80 - 0.20) * 60 / (0.92 * 7.4)     # error analysis: 36 kWh : (0,92 · 7,4 kW) = 5,29 h (student: 60 : 7,4 = 8,1 h)
P_tab = [11.0, 11.0, 10.8, 8.7, 5.9, 3.1, 1.4]            # figure data, every 0,5 h for 3,0 h
a["fy6-16-L2-07"] = 0.5 * ((P_tab[0] + P_tab[-1]) / 2 + sum(P_tab[1:-1]))   # trapezoids: 0,5 h · (6,2 + 39,5) kW = 22,85 kWh (mean power 22,85 : 3,0 = 7,62 kW)
# Level 3: reasoning
a["fy6-16-L3-01"] = (3000 / 0.82 - 3000 / 0.92) * 0.15    # 3000 kWh a year into the battery: 3658,5 - 3260,9 = 397,7 kWh less at 0,15 EUR: 59,7 EUR
a["fy6-16-L3-02"] = ((16 / 10) ** 2 - 1) * 100            # P = R I^2, the same cable: (16/10)^2 = 2,56 -> grows by 156 %
W_grid = 40 / 0.90                                        # 40 kWh into the battery at eta 0,90: 44,44 kWh from the grid
P_need = W_grid / 9.0                                     # in 9,0 h (22.00-07.00): 4,94 kW
a["fy6-16-L3-03"] = P_need * 1000 / (3 * U)               # three-phase: I = P : (3 U) = 4938 W : 690 V = 7,16 A
km = [1050, 980, 1150, 1240, 1380, 1420, 1100, 1260, 1350, 1290, 1170, 1250]   # monthly distances (km), sum 14 640 km
n100 = sum(km) / 100                                      # number of 100 km: 146,4
K_el = n100 * 16.0 / 0.900 * 0.15                         # grid energy 2602,7 kWh at 0,15 EUR/kWh: 390,4 EUR
K_pet = n100 * 6.50 * 1.85                                # 146,4 · 6,50 l · 1,85 EUR/l = 1760,5 EUR
a["fy6-16-L3-04"] = K_pet - K_el                          # the petrol car costs 1370,1 EUR more (public charging 0,45 EUR/kWh: 1171,2 EUR, still less)
I_house = (6.0 + 3.3 + 1.8 + 0.90) * 1000 / (3 * U)       # 12,0 kW on three phases: 17,39 A per phase
a["fy6-16-L3-05"] = 25 - I_house                          # charger phase: 25 A - 17,39 A = 7,61 A (cable loss 0,408 ohm · 7,61^2 = 23,6 W; at 16 A 104,4 W)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
