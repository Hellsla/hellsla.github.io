"""Every answer in exercises.json for fy6-14, computed from the task data (python -I answers.py).
A series circuit of a source U, a resistor R and a diode or LED: Kirchhoff's loop U = U_R + U_D, the resistor obeys
Ohm's law U_R = R I, so I = (U - U_D) / R and R = (U - U_D) / I; a component's power P = U I. In the reverse direction
no current flows, so U_R = 0 and the whole source voltage is over the diode. A solar panel is a DC source: P = U I,
efficiency eta = P : (G A), energy E = P t.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy6-14-L1-01"] = 2.0 * 15e-3 * 1e3                      # P = U_D I = 2,0 V · 0,015 A = 0,030 W = 30 mW
a["fy6-14-L1-02"] = (5.0 - 3.1) / 0.020                    # R = (U - U_D) : I = 1,9 V : 0,020 A = 95 ohm
a["fy6-14-L1-03"] = (9.0 - 0.70) / 1.0e3 * 1e3             # I = (U - U_D) : R = 8,3 V : 1000 ohm = 8,3 mA
a["fy6-14-L1-04"] = 17.5 * 5.40                            # P = U I = 17,5 V · 5,40 A = 94,5 W
# figure fy6-14/ex-led: the green LED's curve passes (2,2 V; 10 mA) on the gridlines
a["fy6-14-L1-05"] = 2.2 * 10e-3 * 1e3                      # P = U_D I = 2,2 V · 0,010 A = 22 mW
# Level 2: two steps, a conversion or a rearrangement
a["fy6-14-L2-01"] = 9.0 - 470 * 0.0                        # reverse: I = 0, U_R = R I = 0, U_D = U = 9,0 V
a["fy6-14-L2-02"] = (9.0 - 2 * 2.0) / 0.020                # two LEDs in series: R = (9,0 V - 4,0 V) : 0,020 A = 250 ohm
a["fy6-14-L2-03"] = 260 / (800 * 1.6) * 100                # eta = P : (G A) = 260 W : 1280 W = 20,3 %
a["fy6-14-L2-04"] = 0.35 * 6.0 * 3600 / 1e3                # E = P t = 0,35 W · 21 600 s = 7560 J = 7,56 kJ
# Level 3: reasoning, two ideas
I1 = (4.5 - 2.0) / 120                                     # new battery: 20,8 mA
I2 = (3.6 - 2.0) / 120                                     # run down: 13,3 mA
a["fy6-14-L3-01"] = (I1 - I2) / I1 * 100                   # the current falls 36 % while the voltage falls only 20 %
pts = [(0, 3.30), (10.0, 3.25), (14.0, 3.18), (16.0, 3.05), (17.0, 2.90), (18.0, 2.55), (19.0, 1.90), (20.0, 0.95), (21.0, 0)]
Ub, Ib = max(pts, key=lambda q: q[0] * q[1])               # the largest U I in the table: 17,0 V · 2,90 A = 49,3 W
a["fy6-14-L3-02"] = Ub / Ib                                # R = U : I = 5,86 ohm at the maximum power point
a["fy6-14-L3-03"] = (12 - 3 * 3.0) / 12 * 100              # share of the resistor: U_R I : (U I) = 3,0 V : 12 V = 25 %
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
