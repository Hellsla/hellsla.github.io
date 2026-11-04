"""Numbers of the lesson text and inquiry.json for fy7-8, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Ideal transformer U1 : U2 = N1 : N2 = I2 : I1; P = U I; line loss P_h = R I².
Prints {id: number} as JSON."""
import json

a = {}
# Worked example: substation transformer 110 kV -> 20 kV, N2 = 360 turns, I2 = 450 A (ideal)
U1, U2, N2, I2 = 110e3, 20e3, 360, 450
a["ex-N1"] = N2 * U1 / U2                       # N1 = N2 U1 / U2 = 1980 turns
a["ex-I1"] = I2 * U2 / U1                       # I1 = I2 U2 / U1 = 81,82 A -> 82 A
a["ex-P1"] = U1 * a["ex-I1"] / 1e6              # Järkevyys: P1 = U1 I1 = 9,0 MW
a["ex-P2"] = U2 * I2 / 1e6                      # P2 = U2 I2 = 9,0 MW
# Simulation: generator 20 kV, line r = 0,040 Ω/km, defaults P = 200 MW, l = 150 km
r, Ug = 0.040, 20e3
R = r * 150                                     # R = 6,0 Ω
a["sim-R"] = R
for U in (50e3, 100e3, 200e3, 400e3):
    I = 200e6 / U                               # I = P / U
    Ph = R * I ** 2                             # P_h = R I²
    k = int(U / 1e3)
    a[f"sim-I-{k}"] = I                         # 4000, 2000, 1000, 500 A
    a[f"sim-Ph-{k}"] = Ph / 1e6                 # 96, 24, 6,0, 1,5 MW
    a[f"sim-osuus-{k}"] = Ph / 200e6 * 100      # 48, 12, 3,0, 0,75 %
a["sim-perille-400"] = 200 - a["sim-Ph-400"]    # 198,5 MW
a["sim-N21-400"] = 400e3 / Ug                   # step-up ratio N2 : N1 = 20
a["sim-ratio-200-400"] = a["sim-Ph-200"] / a["sim-Ph-400"]   # doubling U: loss to a quarter (4)
a["sim-mahdoton-20"] = R * (200e6 / 20e3) / 1e3  # at 20 kV the voltage drop R I = 60 kV > 20 kV: impossible
# Kaava graph: loss share 100 % · R P / U² for P = 200 MW, R = 6,0 Ω at 70 kV (top of the graph)
a["graph-70"] = R * 200e6 / 70e3 ** 2 * 100     # 24,5 %
# Fingrid: grid losses about 2 % of the electricity used in Finland (Fingrid, Yhteisillä linjoilla 2026, year 2025)
# virhe: 400 kV, R = 6,0 Ω, P = 200 MW; the student's U²/R
a["virhe-wrong"] = (400e3) ** 2 / 6.0 / 1e6     # 26 667 MW (absurd)
a["virhe-right"] = 6.0 * (200e6 / 400e3) ** 2 / 1e6   # 1,5 MW
# siirto: wind farm 33 MW at 110 kV, line R = 8,0 Ω
I = 33e6 / 110e3
a["siirto-I"] = I                               # 300 A
a["siirto"] = 8.0 * I ** 2 / 1e3                # P_h = 720 kW
a["siirto-osuus"] = 8.0 * I ** 2 / 33e6 * 100   # 2,18 %
a["siirto-U2R"] = (110e3) ** 2 / 8.0 / 1e3      # mistake U²/R: 1 512 500 kW
a["siirto-RI"] = 8.0 * I / 1e3                  # mistake R I (no square) in kW: 2,4
a["siirto-MW"] = a["siirto"] / 1e3              # answered in MW: 0,72
# check-2: low-voltage lighting transformer 230 V -> 12 V, lamps 60 W (ideal)
a["check-I2"] = 60 / 12                         # 5,0 A
a["check-I1"] = 60 / 230                        # 0,2609 A -> 0,26 A
a["check-inv"] = 5.0 * 230 / 12                 # mistake inverted ratio: 95,8 A
# ennuste-dc: battery 12 V on the primary: constant flux, 0 V on the secondary after the switching moment
# Exit ticket: N1 = 500, N2 = 25, U1 = 230 V
a["exit-U2"] = 230 * 25 / 500                   # 11,5 V
a["exit-third"] = (1 / 3) ** 2                  # current to a third: loss to a ninth
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
