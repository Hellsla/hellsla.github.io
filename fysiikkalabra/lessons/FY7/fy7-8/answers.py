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
a["fy7-8-L1-05"] = 400e3 * 800 / 1e6                # P = U I = 400 kV · 800 A = 320 MW
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
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
