"""Numbers of the lesson text and inquiry.json for fy6-1, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Current I = Q / t, voltage U = E / Q, charge Q = N e with e = 1,602 · 10^-19 C.
Prints {id: number} as JSON on the last line."""
import json

e = 1.602e-19                                     # C, the elementary charge
a = {}
# Worked example: a flashlight lamp, I = 0,25 A for 12 min
t_ex = 12 * 60                                    # 12 min = 12 · 60 s = 720 s
a["ex-t"] = t_ex
a["ex-Q"] = 0.25 * t_ex                           # Q = I t = 180 C
a["ex-N"] = 0.25 * t_ex / e                       # Järkevyys: N = Q / e = 1,12 · 10^21 electrons
# Ydinajatus / Kaava: 1 C of charge is 1 / e electrons; an AA cell gives 1,5 J to every coulomb
a["N-per-C"] = 1 / e                              # 6,24 · 10^18
# Simulation model: lamp current I = U / (n · 15 Ω) (hidden), one dot = 0,05 C, a measurement lasts 10,0 s
R_lamp, q_dot, t_m = 15, 0.05, 10.0
for cells in (1, 2, 3):
    for lamps in (1, 2):
        I = 1.5 * cells / (lamps * R_lamp)
        a[f"sim-I-{cells}-{lamps}"] = I               # 0,10 / 0,20 / 0,30 A with one lamp, half of it with two
        a[f"sim-Q-{cells}-{lamps}"] = I * t_m         # Q_A = Q_B = 1,00 / 2,00 / 3,00 C in 10 s with one lamp
        a[f"sim-dots-{cells}-{lamps}"] = I * t_m / q_dot   # whole dots: 20, 40, 60 (one lamp), 10, 20, 30 (two)
# exp-1 question: two cells, one lamp, Q = 2,00 C in t = 10,0 s
a["exp1-I"] = 2.00 / 10.0                         # I = Q / t = 0,200 A
a["exp1-mistake-Qt"] = 2.00 * 10.0                # mistake Q t = 20
a["exp1-mistake-tQ"] = 10.0 / 2.00                # mistake t / Q = 5
# exp-2: two cells, two lamps: Q = 1,00 C at A and at B; I = 0,100 A
a["exp2-I"] = 1.00 / 10.0
# Jännite: an AA cell (1,5 V) and 2,0 C of charge
a["U-AA-E-2C"] = 1.5 * 2.0                        # E = U Q = 3,0 J
# siirto: e-scooter battery 36 V, motor current 8,0 A for 25 min
t_s = 25 * 60                                     # 1500 s
Q_s = 8.0 * t_s                                   # Q = I t = 12 000 C
a["siirto-Q"] = Q_s
a["siirto"] = 36 * Q_s / 1000                     # E = U Q = 432 000 J = 432 kJ
a["siirto-min"] = 36 * 8.0 * 25 / 1000            # mistake: minutes not converted, 7,2 kJ
a["siirto-Qonly"] = Q_s                           # mistake: the charge 12 000 given as the answer
a["siirto-kWh"] = 36 * Q_s / 3.6e6                 # Järkevyys: 0,12 kWh
a["siirto-est"] = 300 * 1500                        # Järkevyys: about 300 J per second for 1500 s, 450 000 J
# check-2: phone charger 2,0 A for 45 min
t_c = 45 * 60                                     # 2700 s
a["check2"] = 2.0 * t_c                           # Q = 5400 C
a["check2-min"] = 2.0 * 45                        # mistake: minutes, 90
a["check2-div"] = t_c / 2.0                       # mistake: t / I = 1350
a["check2-Ah"] = 2.0 * t_c / 3600                  # Järkevyys: 1,5 Ah = 1500 mAh
# exit ticket: 1,5 V means 1,5 J per coulomb; 4,0 C through the cell → 6,0 J
a["exit-E"] = 1.5 * 4.0
print(json.dumps(a))
