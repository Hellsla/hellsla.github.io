"""FY9 fy9-tasavirta, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-tasavirta` compares them with tasks.json."""
import json, math


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


out = {}
S = "fy9-tasavirta"

# s1: the rear-window heater of a car (example data): ten parallel strips, 13,5 V and 12,0 A with the engine running
n1, U1, I1, l1, rho1, w1 = 10, 13.5, 12.0, 1.10, 3.0e-7, 3.0e-3
P1 = U1 * I1                                        # W
I_strip = I1 / n1                                   # A, the same voltage over every strip
R_strip = U1 / I_strip                              # ohm
A1 = rho1 * l1 / R_strip                            # m^2
th1 = A1 / w1                                       # m, the thickness of a 3,0 mm wide strip
# c: one strip broken, nine left at the same 13,5 V
I1c = (n1 - 1) * I_strip
P1c = U1 * I1c
# d: engine off, the battery alone: E 12,6 V, R_s 0,020 ohm, the heater 10 strips in parallel
E1, Rs1 = 12.6, 0.020
R_heat = R_strip / n1
I1d = E1 / (R_heat + Rs1)
U1d = E1 - Rs1 * I1d
P1d = U1d ** 2 / R_heat
out.update({f"{S}-s1-a-R": round(R_strip, 4), f"{S}-s1-a-P": P1, f"{S}-s1-a-Istrip": I_strip,
            f"{S}-s1-b": round(th1 * 1e6, 3), f"{S}-s1-b-A": round(A1 * 1e6, 5),
            f"{S}-s1-c-I": I1c, f"{S}-s1-c-P": round(P1c, 2),
            f"{S}-s1-d-Rheat": round(R_heat, 4), f"{S}-s1-d-I": round(I1d, 4), f"{S}-s1-d-U": round(U1d, 4),
            f"{S}-s1-d": round(P1d, 2), f"{S}-s1-d-share": round(100 * P1d / P1, 1)})

# s2: an electric kick scooter's battery (example data)
U2, Q2 = 36.0, 10.4                                 # V nominal, Ah
W2 = U2 * Q2                                        # Wh
I2b, v2 = 7.5, 20.0                                 # A while riding, km/h
t2b = Q2 / I2b                                      # h
s2b = v2 * t2b                                      # km
U_lat, E2c, R2, Rs2 = 42.0, 34.5, 2.6, 0.40
I2c = (U_lat - E2c) / (R2 + Rs2)                    # A, the charging current at the start
U2c = E2c + Rs2 * I2c                               # V, the terminal voltage while charging
W_lat = U_lat * Q2                                  # Wh from a constant 42,0 V charger for the charge Q2
eta2 = W2 / W_lat
cost2 = W_lat / 1000 * 0.15                         # € at 15 snt/kWh
out.update({f"{S}-s2-a": round(W2, 2), f"{S}-s2-a-MJ": round(W2 * 3600 / 1e6, 4),
            f"{S}-s2-b": round(s2b, 3), f"{S}-s2-b-t": round(t2b, 4), f"{S}-s2-b-min": round(t2b * 60, 2),
            f"{S}-s2-c-I": round(I2c, 4), f"{S}-s2-c-U": round(U2c, 3),
            f"{S}-s2-d": round(100 * eta2, 2), f"{S}-s2-d-Wlat": round(W_lat, 2), f"{S}-s2-d-cost": round(100 * cost2, 2),
            f"{S}-s2-d-loss": round(W_lat - W2, 2)})

# s3: three AA cells in series under a variable load (invented data: E 4,62 V, R_s 0,72 ohm and meter scatter)
I3 = [0.10, 0.25, 0.40, 0.60, 0.80, 1.00]           # A
U3 = [4.56, 4.43, 4.34, 4.18, 4.06, 3.89]           # V
k3, b3 = fit(I3, U3)
# read from the drawn line in the solution: (0 A; 4,63 V) and (1,20 A; 3,75 V)
E_read = 4.63
Rs_read = (4.63 - 3.75) / (1.20 - 0.00)
Ik = E_read / Rs_read
R_lamp = 3.6
I3d = E_read / (R_lamp + Rs_read)
P3d = R_lamp * I3d ** 2
P3src = E_read * I3d
out.update({f"{S}-s3-k-fit": round(k3, 4), f"{S}-s3-b-fit": round(b3, 4), f"{S}-s3-Ik-fit": round(-b3 / k3, 3),
            f"{S}-s3-b-E": E_read, f"{S}-s3-b-Rs": round(Rs_read, 4), f"{S}-s3-b-Rs-cell": round(Rs_read / 3, 4),
            f"{S}-s3-b-E-cell": round(E_read / 3, 3),
            f"{S}-s3-c": round(Ik, 3), f"{S}-s3-c-ratio": round(Ik / max(I3), 2),
            f"{S}-s3-d-I": round(I3d, 4), f"{S}-s3-d-U": round(R_lamp * I3d, 3), f"{S}-s3-d": round(P3d, 3),
            f"{S}-s3-d-src": round(P3src, 3), f"{S}-s3-d-share": round(100 * P3d / P3src, 1),
            f"{S}-s3-d-loss": round(Rs_read * I3d ** 2, 3)})

# s4: three claims (word task; the numbers its model answers quote)
rho_cu = 1.7e-8
R_cord = rho_cu * 2 * 15.0 / 0.75e-6                # ohm, a 15 m cord with two 0,75 mm^2 conductors
P_cord = R_cord * 10.0 ** 2                         # W at 10 A
R_cord15 = rho_cu * 2 * 15.0 / 1.5e-6
I_kettle, I_toaster = 2000 / 230, 850 / 230
I_bird = 600.0                                      # A in the line
R_line_bird = 2.7e-8 * 0.040 / 400e-6                # ohm, 4,0 cm of a 400 mm^2 aluminium line between the feet
U_bird = R_line_bird * I_bird
out.update({f"{S}-s4-Rcord": round(R_cord, 4), f"{S}-s4-Pcord": round(P_cord, 2), f"{S}-s4-Pcord15": round(R_cord15 * 100, 2),
            f"{S}-s4-Ikettle": round(I_kettle, 3), f"{S}-s4-Itoaster": round(I_toaster, 3),
            f"{S}-s4-Isum": round(I_kettle + I_toaster, 3), f"{S}-s4-Ubird-mV": round(U_bird * 1000, 3)})

# s5: the resistor report (invented data); multimeter error limits as in fy6-2:
# 20 V range resolution 0,01 V, +-(0,5 % + 2 digits); 200 mA range resolution 0,1 mA, +-(1,0 % + 2 digits)
U5 = [0.51, 1.50, 3.02]                             # V
I5 = [5.3e-3, 15.0e-3, 29.6e-3]                     # A
R5 = [u / i for u, i in zip(U5, I5)]
dU = [0.005 * u + 2 * 0.01 for u in U5]
dI = [0.010 * i + 2 * 0.1e-3 for i in I5]
Rmin = [(u - du) / (i + di) for u, du, i, di in zip(U5, dU, I5, dI)]
Rmax = [(u + du) / (i - di) for u, du, i, di in zip(U5, dU, I5, dI)]
rel = [du / u + di / i for u, du, i, di in zip(U5, dU, I5, dI)]
P5 = [u * i for u, i in zip(U5, I5)]
dU2V = 0.005 * 0.51 + 2 * 0.001                     # the 2 V range for the first reading
out.update({f"{S}-s5-a": round(R5[0], 3), f"{S}-s5-R": [round(r, 2) for r in R5], f"{S}-s5-dU": [round(x, 4) for x in dU],
            f"{S}-s5-dI-mA": [round(x * 1000, 4) for x in dI], f"{S}-s5-Rmin": [round(r, 2) for r in Rmin],
            f"{S}-s5-Rmax": [round(r, 2) for r in Rmax], f"{S}-s5-rel": [round(100 * r, 2) for r in rel],
            f"{S}-s5-P-mW": [round(1000 * p, 2) for p in P5], f"{S}-s5-dU-2V": round(dU2V, 5),
            f"{S}-s5-rel-2V": round(100 * dU2V / 0.51, 2)})

# s6: the hot-water heater (example data), cross-module with fy3-6 Q = c m dT
c_w, V6, T1, T2, P6 = 4190.0, 300.0, 15.0, 70.0, 3.0e3
m6 = V6 * 1.0                                       # kg, 1,0 kg per litre
Q6 = c_w * m6 * (T2 - T1)                           # J
t6 = Q6 / P6                                        # s
loss_day = 1.6                                      # kWh a day
P_loss = loss_day * 1000 / 24                       # W
E_year = loss_day * 365
cost_year = E_year * 0.14
P6c = P6 * (220 / 230) ** 2
t6c = Q6 / P6c
I6 = P6 / 230
R6 = 230 ** 2 / P6
m_shower = 8.0 * 10                                 # kg, 8,0 l/min for 10 min
hot_share = (40 - T1) / (T2 - T1)                   # the share of 70 °C water in 40 °C shower water
Q_shower = c_w * m_shower * (40 - T1)
out.update({f"{S}-s6-Q": round(Q6 / 1e6, 4), f"{S}-s6-Q-kWh": round(Q6 / 3.6e6, 3), f"{S}-s6-a": round(t6 / 3600, 4),
            f"{S}-s6-b": round(P_loss, 2), f"{S}-s6-b-year": round(E_year, 1), f"{S}-s6-b-cost": round(cost_year, 2),
            f"{S}-s6-c": round(P6c / 1000, 4), f"{S}-s6-c-t": round(t6c / 3600, 3), f"{S}-s6-c-I": round(I6, 3), f"{S}-s6-c-R": round(R6, 3),
            f"{S}-s6-d": round(Q_shower / 3.6e6, 4), f"{S}-s6-d-MJ": round(Q_shower / 1e6, 4),
            f"{S}-s6-d-cost": round(100 * Q_shower / 3.6e6 * 0.14, 2), f"{S}-s6-d-showers": round(Q6 / Q_shower, 2),
            f"{S}-s6-d-hot-l": round(hot_share * m_shower, 1), f"{S}-s6-a-cost": round(Q6 / 3.6e6 * 0.14, 2)})

print(json.dumps(out))
