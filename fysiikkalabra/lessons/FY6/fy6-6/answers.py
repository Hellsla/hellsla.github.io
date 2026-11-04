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
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
