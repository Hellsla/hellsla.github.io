"""Every answer in exercises.json for fy6-6, computed from the task data (python -I answers.py).
Electric power P = U I; with Ohm's law U = R I also P = R I^2 = U^2 / R (Joule's law for a resistor); energy E = P t.
Resistances are taken as constant (a lamp's too, where the task says so); sources and wires are ideal unless a task
gives the wire's resistance. Water: c = 4190 J/(kg K), no heat losses where the task says so.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy6-6-L1-01"] = 5.0 * 2.4                              # USB charger: P = U I = 5,0 V · 2,4 A = 12 W
a["fy6-6-L1-02"] = 47 * 0.20 ** 2                         # P = R I^2 = 47 ohm · (0,20 A)^2 = 1,88 W
a["fy6-6-L1-03"] = 230 ** 2 / 26.5 / 1000                 # kettle: P = U^2 / R = 230^2 / 26,5 = 1996 W = 2,00 kW
a["fy6-6-L1-04"] = 9.0 * 2.0 * 3600 / 1000                # E = P t = 9,0 W · 7200 s = 64 800 J = 64,8 kJ
# figure fy6-6/ex-pi: points (0,50 A; 1,25 W), (1,0 A; 5,0 W), (1,5 A; 11,25 W), (2,0 A; 20 W)
a["fy6-6-L1-05"] = 20 / 2.0 ** 2                          # R = P / I^2 = 20 W : (2,0 A)^2 = 5,0 ohm
# Level 2: two steps, a conversion or a rearrangement
a["fy6-6-L2-01"] = 1.8 * 1000 / 230                       # hair dryer: I = P / U = 1800 W : 230 V = 7,83 A
I_s = 12 / (10 + 20)                                      # series 10 + 20 ohm on 12 V: I = 0,40 A
a["fy6-6-L2-02"] = 20 * I_s ** 2                          # P2 = R2 I^2 = 20 ohm · 0,16 A^2 = 3,2 W
a["fy6-6-L2-03"] = (0.25 * 1.0 * 1000) ** 0.5             # rated 0,25 W, 1,0 kOhm: U = sqrt(P R) = sqrt(250) V = 15,8 V
a["fy6-6-L2-04"] = 200 * 5.0 * 60 / (4190 * 0.80)         # immersion heater: dT = P t / (c m) = 60 000 J / 3352 J/K = 17,9 K
# Level 3: reasoning
R40 = 230 ** 2 / 40                                       # 40 W lamp at 230 V: 1322,5 ohm (assumed constant)
R100 = 230 ** 2 / 100                                     # 100 W lamp: 529 ohm
I_l = 230 / (R40 + R100)                                  # in series on 230 V: 0,1242 A
a["fy6-6-L3-01"] = R40 * I_l ** 2                         # P40 = R40 I^2 = 20,4 W (the 40 W lamp glows more)
I_lights = 9.2 / 230                                      # light string: 20 equal lamps in series, 9,2 W on 230 V: I = 0,040 A
a["fy6-6-L3-02"] = (230 / 20) / I_lights                  # each lamp 230 V : 20 = 11,5 V, R = 11,5 V : 0,040 A = 287,5 ohm
P1 = 12 ** 2 / 6.0                                        # parallel on 12 V: 6,0 ohm takes U^2/R = 24 W
a["fy6-6-L3-03"] = 12 ** 2 / (36 - P1)                    # the other takes 36 W - 24 W = 12 W, so R2 = U^2 / P2 = 12 ohm
# Level 1 additions
a["fy6-6-L1-07"] = 12 * 350 / 1000                        # LED strip: P = U I = 12 V · 0,350 A = 4,2 W
R_18 = 2.0 ** 2 / 0.80                                    # R = U1^2 / P1 = 4,0 V^2 : 0,80 W = 5,0 ohm
a["fy6-6-L1-08"] = 6.0 ** 2 / R_18                        # P2 = U2^2 / R = 36 V^2 : 5,0 ohm = 7,2 W
# Level 2 additions
T_k = [24.4, 31.0, 42.6, 58.9, 80.2]                      # surface temperature, ambient 22,0 degC (example data)
P_k = [3.0 * 0.064, 6.0 * 0.127, 9.0 * 0.192, 12.0 * 0.254, 15.0 * 0.320]   # P = U I per row
a["fy6-6-L2-05"] = sum(p * (t - 22.0) for p, t in zip(P_k, T_k)) / sum(p * p for p in P_k)   # least-squares slope through origin 12,1 K/W
a["fy6-6-L2-06"] = (6.0 * 0.346 / (3.0 * 0.254) - 1) * 100   # bulb: P(6,0 V) = 2,076 W, P(3,0 V) = 0,762 W -> +172 %
a["fy6-6-L2-07"] = (9.0 - 3.0) * 0.50                     # series lamps, same I: P_A - P_B = (9,0 V - 3,0 V) 0,50 A = 3,0 W
# Level 3 additions
R1_t = 230 ** 2 / 1100                                    # toaster element 1 alone: 48,09 ohm
R2_t = 230 ** 2 / 420 - R1_t                              # series 420 W: R1 + R2 = 125,95 ohm -> R2 = 77,86 ohm
a["fy6-6-L3-04"] = 253 ** 2 / R2_t                        # at 253 V: R2 takes 822 W > 750 W (R1: 1331 W < 1400 W)
R_heater = 230 ** 2 / 2000                                # 2,0 kW heater at 230 V: 26,45 ohm
I_thin = 230 / (R_heater + 2.4)                           # thin cord in series: 7,97 A
a["fy6-6-L3-05"] = 2.4 * I_thin ** 2                      # thin cord P = R I^2 = 152,5 W (thick: 0,71 ohm, 8,47 A -> 50,9 W)
# figure fy6-6/ex-pt: P = 2000 W for 0-3,0 min, 1000 W for 3,0-8,0 min, 500 W for 8,0-12 min
a["fy6-6-L2-09"] = (2000 * 3.0 * 60 + 1000 * 5.0 * 60 + 500 * 4.0 * 60) / 1000   # E = sum P t = 360 kJ + 300 kJ + 120 kJ = 780 kJ
# L2-08 is multiple choice (prediction): R1 = 24 ohm on 12 V, then R2 = 24 ohm in series; I 0,50 A -> 0,25 A, P1 6,0 W -> 1,5 W (a quarter); no number
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
