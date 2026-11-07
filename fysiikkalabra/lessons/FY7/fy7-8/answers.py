"""Every answer in exercises.json for fy7-8, computed from the task data (python -I answers.py).
Ideal transformer U1 : U2 = N1 : N2 = I2 : I1 (power conserved, U1 I1 = U2 I2); P = U I; line loss P_h = R I².
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy7-8-L1-01"] = 230 * 60 / 1200                  # U2 = U1 N2 / N1 = 230 V · 60 / 1200 = 11,5 V
a["fy7-8-L1-02"] = 40 * 230 / 8.0                   # N1 = N2 U1 / U2 = 40 · 230 V / 8,0 V = 1150
a["fy7-8-L1-03"] = 250 * 400 / 20e3                 # I1 = I2 U2 / U1 = 250 A · 400 V / 20 000 V = 5,0 A
a["fy7-8-L1-04"] = 2.5 * 120 ** 2 / 1e3             # P_h = R I² = 2,5 Ω · (120 A)² = 36 000 W = 36 kW
a["fy7-8-L1-05"] = 3 ** 0.5 * 400e3 * 800 / 1e6     # three-phase P = √3 U I cos φ, cos φ = 1: √3 · 400 kV · 800 A = 554,3 MW
# Level 2: two steps, a conversion or a rearrangement
I = 50e6 / 110e3                                    # I = P / U = 454,5 A
a["fy7-8-L2-01"] = 4.0 * I ** 2 / 1e3               # P_h = R I² = 826,4 kW -> 8,3 · 10² kW
a["fy7-8-L2-02"] = 5.0 * 2.0 / 230 * 1e3            # I1 = U2 I2 / U1 = 10 W / 230 V = 0,04348 A = 43 mA
a["fy7-8-L2-03"] = 4.8 * 100e6 / (220e3) ** 2 * 100  # P_h / P = R I² / P = R P / U² = 0,9917 % -> 0,99 %
# figure fy7-8/loss-current: fitted curve P_h = R I² through the grid point (5,0 A; 20 W)
a["fy7-8-L2-04"] = 20 / 5.0 ** 2                    # R = P_h / I² = 20 W / 25 A² = 0,80 Ω
# Level 3: reasoning or an unfamiliar context
I3 = 150e6 / 400e3                                  # 150 MW raised to 400 kV: I = 375 A
a["fy7-8-L3-01"] = 8.0 * I3 ** 2 / 150e6 * 100      # P_h = 1,125 MW, share 0,75 %
a["fy7-8-L3-02"] = 0.010 * (400e3) ** 2 / 400e6     # P_h ≤ 0,010 P with P_h = R P² / U²: R ≤ 0,010 U² / P = 4,0 Ω
a["fy7-8-L3-03"] = (400 / 220) ** 2                 # same share R P / U²: P ∝ U², ratio (400 : 220)² = 3,31
# Exercise bank additions (level 1-3)
a["fy7-8-L1-07"] = 840 * 1 / 4                      # P_h ∝ 1 / U²: doubling U gives 840 kW / 4 = 210 kW
a["fy7-8-L1-08"] = 72 / 80 * 100                    # η = P2 / P1 = 72 W / 80 W = 90 %
Nn = [100, 200, 300, 400, 600, 800]
Un = [1.22, 2.53, 3.70, 4.93, 7.41, 9.88]
k5 = sum(n * u for n, u in zip(Nn, Un)) / sum(n * n for n in Nn)  # slope through origin k = ΣN U / ΣN² = 0,012354 V
a["fy7-8-L2-05"] = 6.00 / k5                        # N1 = U1 / k = 6,00 V / 0,012354 V = 485,7
a["fy7-8-L2-06"] = 2.00 * 11.5 / (230 * 0.114) * 100  # η = U2 I2 / (U1 I1) = 23,0 W / 26,22 W = 87,7 %
a["fy7-8-L2-07"] = 230 * 2.0 / 2300                 # I2 = U1 I1 / U2 = 460 W / 2300 V = 0,20 A
# L2-08 is multiple choice (order of magnitude): I = 3,0 MW / 20 kV = 150 A, P_h = 0,50 Ω · (150 A)² = 11,25 kW ≈ 10 kW; no number
R4 = 0.040 * 150                                    # R = 6,0 Ω
PhA = R4 * (200e6 / 220e3) ** 2                     # 4,959 MW at 220 kV (I = 909 A)
PhB = R4 * (200e6 / 400e3) ** 2                     # 1,500 MW at 400 kV (I = 500 A)
a["fy7-8-L3-04"] = (PhA - PhB) * 8760 / 1e6 * 50 / 1e6  # saving: 30 300 MWh · 50 €/MWh = 1,515 M€
P0 = 0.6                                            # idle loss, kW (row P_out = 0)
a5 = (81.9 - 80.0 - P0) / 80.0 ** 2                 # a = (P_h - P0) / P_out² = 2,03e-4 1/kW from the 80 kW row
a["fy7-8-L3-05"] = (P0 / a5) ** 0.5                 # P0 = a P²: P = sqrt(P0 / a) = 54,35 kW
# L1-06 (multiple choice) has no number
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
