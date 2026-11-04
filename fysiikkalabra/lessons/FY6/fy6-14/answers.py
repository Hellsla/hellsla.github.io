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
# Exercise-bank additions: multiple choice (answer = the correct option's text), data, error and modelling tasks
a["fy6-14-L1-06"] = "Diodi on päästösuunnassa, joten virta kulkee ja diodin yli on vain pieni jännite."
a["fy6-14-L1-07"] = "LEDin virta kasvaa jyrkästi jännitteen kasvaessa, joten vastus ottaa ylimääräisen jännitteen."
a["fy6-14-L1-08"] = (2.0 * 0.100) / (1000 * 12e-4) * 100    # eta = P : (G A) = 0,20 W : 1,2 W = 16,7 %
leds = {"sininen": 3.10, "punainen": 1.90, "keltainen": 2.10}
low = min(leds, key=leds.get)                              # the smallest U_D leaves the largest U_R, so the largest R
a["fy6-14-L2-05"] = (5.0 - leds[low]) / 0.015              # R = (5,0 V - 1,90 V) : 0,015 A = 207 ohm
cell = [(10, 0.99, 99), (15, 1.48, 99), (20, 1.89, 94), (22, 1.99, 91), (27, 2.12, 78), (33, 2.20, 66), (47, 2.28, 48), (100, 2.34, 23)]
a["fy6-14-L2-06"] = max(u * i for _, u, i in cell)         # P = U I in mW: largest 1,99 V · 91 mA = 181 mW (22 ohm)
a["fy6-14-L2-07"] = (9.0 - 3.2) / 0.015                    # correct R = (U - U_D) : I = 5,8 V : 0,015 A = 387 ohm (student: 9,0 V : I = 600 ohm)
H = [12, 32, 80, 120, 160, 170, 170, 135, 85, 40, 15, 8]   # kWh/m2 per month
C = [620, 560, 520, 400, 330, 290, 280, 300, 370, 460, 560, 650]  # kWh per month
E_year = 0.19 * 24 * sum(H)                                # E = eta A sum(H) = 0,19 · 24 m2 · 1027 kWh/m2 = 4683 kWh
a["fy6-14-L3-04"] = E_year / sum(C) * 100                  # share of the yearly consumption 5340 kWh: 87,7 %
# diode table of L3-05: the load-line current (4,5 V - U_D) : 180 ohm against the diode's current; linear between 2,00 V and 2,05 V
d0, d1 = (2.00, 9.8), (2.05, 20.0)
slope = (d1[1] - d0[1]) / (d1[0] - d0[0])                  # diode: 204 mA/V between the rows
x = (((4.5 - d0[0]) / 180 * 1e3) - d0[1]) / (slope + 1e3 / 180)  # offset from 2,00 V where the two currents meet
# threshold: the steep straight part (2,05 V; 20 mA)-(2,10 V; 41 mA) extended to I = 0
slope2 = (41 - 20) / (2.10 - 2.05)                         # 420 mA/V
threshold = 2.05 - 20 / slope2                            # 2,00 V (not an answer field; checked in solutions)
assert abs(threshold - 2.0) < 0.01
a["fy6-14-L3-05"] = round(d0[1] + slope * x, 2)            # I = 13,78 mA at U_D = 2,02 V
print(json.dumps({k: (v if isinstance(v, str) else round(v, 6)) for k, v in a.items()}))
