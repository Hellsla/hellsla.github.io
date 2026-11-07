"""FY6 Esimerkkikoe: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json; `python scripts/practice.py check FY6/koe` compares them."""
import json, math

g, e, k = 9.81, 1.602e-19, 8.99e9
out = {}

# ---------------------------------------------------------------- fy6-k1: Osa 1 checks of the options that need a number
R = 1.0                                                              # a: series loop, the same current before and after the lamp
out["k1-c"] = {"I_series": 2 * R, "II_parallel": R / 2, "III_mixed": R + R / 2}   # the three arrangements of equal resistors R
# d: L1 in series with L2 || (switch + L3), identical lamps R, ideal source U = 1
I_open = 1 / (2 * R); I_closed = 1 / (R + R / 2)
out["k1-d"] = {"L1_open": I_open, "L1_closed": round(I_closed, 3), "L2_open": I_open, "L2_closed": round(I_closed / 2, 3)}
W_kettle = 2.0 * 3.0 / 60; W_led = 8.0e-3 * 5.0                     # kWh
out["k1-e"] = {"kettle_kWh": W_kettle, "led_kWh": W_led, "ratio": round(W_kettle / W_led, 2), "no_min": 2.0 * 3.0,
               "power_ratio": 2000 / 8.0}
E_b, U1, I1 = 1.60, 1.20, 1.0                                        # f: the battery line through (0; 1,60 V) and (1,0 A; 1,20 V)
out["k1-f"] = {"Rs": round((E_b - U1) / I1, 3), "U_over_I": U1 / I1, "Ik": round(E_b / ((E_b - U1) / I1), 2)}
out["k1-g"] = {"ratio": 1.0}                                         # Newton III: equal forces
out["k1-h"] = {"E_ratio": 0.5, "v_ratio": 1.0}                       # same U, double d: E halves, eU and v unchanged
P_j = {"A": 3 * 700, "B": 1600 + 150, "C": 1000 + 150 + 1000, "D": 2200 + 900}       # W; only D is above 10 A
out["k1-j"] = {"limit_W": 10 * 230, **{f"I_{a}": round(p / 230, 2) for a, p in P_j.items()}}

# ---------------------------------------------------------------- fy6-k2: the resistor and the lamp, (I, U) characteristics
U2 = [0.0, 0.50, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
IR2 = [0, 28, 55, 112, 166, 223, 277, 334]                           # mA, resistor
IL2 = [0, 76, 112, 165, 204, 241, 270, 300]                          # mA, lamp
fitR = sum(u * i / 1000 for u, i in zip(U2, IR2)) / sum((i / 1000) ** 2 for i in IR2)
out["k2-fit"] = round(fitR, 2)                                       # least squares through the origin
out["fy6-k2-b"] = round(5.4 / 0.300, 1)                              # the drawn line through (0; 0) and (300 mA; 5,4 V)
out["fy6-k2-c-cold"] = round(1.0 / 0.112, 2)
out["fy6-k2-c-hot"] = round(6.0 / 0.300, 2)
# d: series, the same current: U_R(I) + U_L(I) = 6,0 V; the lamp's U(I) interpolated between the measured points
def U_lamp(i):
    for j in range(len(IL2) - 1):
        if IL2[j] <= i <= IL2[j + 1]:
            return U2[j] + (U2[j + 1] - U2[j]) * (i - IL2[j]) / (IL2[j + 1] - IL2[j])
lo, hi = 100.0, 300.0
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if 18.0 * mid / 1000 + U_lamp(mid) < 6.0 else (lo, mid)
I2d = (lo + hi) / 2
out["fy6-k2-d-I"] = round(I2d / 1000, 4)
out["fy6-k2-d-U"] = round(U_lamp(I2d), 2)
out["k2-d"] = {"I_mA": round(I2d, 1), "U_L": round(U_lamp(I2d), 2), "U_R": round(18.0 * I2d / 1000, 2),
               "smooth_model_I": None}
# the smooth model the data were made from, I = 0,300 A (U / 6 V)^0,55: the same series current
lo, hi = 0.1, 0.3
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if 18.0 * mid + 6.0 * (mid / 0.300) ** (1 / 0.55) < 6.0 else (lo, mid)
out["k2-d"]["smooth_model_I"] = round((lo + hi) / 2, 4)

# ---------------------------------------------------------------- fy6-k3: the LED indicator
Us, UD, Iw = 5.0, 2.0, 0.015
out["fy6-k3-a-R"] = round((Us - UD) / Iw, 1)
I3 = (Us - UD) / 220
out["fy6-k3-a-I"] = round(I3, 5)
UR3, R3 = 2.98, 220.0
dU3 = 0.005 * UR3 + 2 * 0.01; dR3 = 0.05 * R3
I3m = UR3 / R3
out["fy6-k3-b-I"] = round(I3m, 6)
out["fy6-k3-b-dI"] = round(I3m * (dU3 / UR3 + 0.05), 6)                 # uncertainty of the current (relative ones added)
out["k3-b"] = {"dU": round(dU3, 4), "rel_U": round(100 * dU3 / UR3, 2), "rel_R": 5.0, "rel_I": round(100 * (dU3 / UR3 + 0.05), 2),
               "dI_mA": round(1000 * I3m * (dU3 / UR3 + 0.05), 2), "I_min_mA": round(1000 * (UR3 - dU3) / (R3 + dR3), 2),
               "I_max_mA": round(1000 * (UR3 + dU3) / (R3 - dR3), 2)}
# c: (1) two branches, each LED with its own 220 ohm; (2) the LEDs in series with one 68 ohm resistor
I_1 = 2 * I3; P_1 = Us * I_1; PL_1 = 2 * UD * I3
I_2 = (Us - 2 * UD) / 68; P_2 = Us * I_2; PL_2 = 2 * UD * I_2
out["fy6-k3-c-P1"] = round(P_1, 5)
out["fy6-k3-c-P2"] = round(P_2, 5)
out["k3-c"] = {"I1_mA": round(1000 * I_1, 2), "I2_mA": round(1000 * I_2, 2), "PL1_mW": round(1000 * PL_1, 1), "PL2_mW": round(1000 * PL_2, 1),
               "share1": round(100 * PL_1 / P_1, 1), "share2": round(100 * PL_2 / P_2, 1)}
# d: LED voltages 1,9-2,1 V each
out["k3-d"] = {"conn2_min_mA": round(1000 * (Us - 4.2) / 68, 1), "conn2_max_mA": round(1000 * (Us - 3.8) / 68, 1),
               "conn1_min_mA": round(1000 * (Us - 2.1) / 220, 1), "conn1_max_mA": round(1000 * (Us - 1.9) / 220, 1)}

# ---------------------------------------------------------------- fy6-k4: the ion thruster
U4, d4, m4, I4 = 1100.0, 0.80e-3, 2.18e-25, 1.76
E4 = U4 / d4
out["fy6-k4-a-E"] = round(E4, -3)
out["fy6-k4-a-F"] = e * E4
v4 = math.sqrt(2 * e * U4 / m4)
out["fy6-k4-b"] = round(v4, -1)
out["k4-b"] = {"Ek_J": e * U4, "Ek_eV": U4}
N4 = I4 / e
out["fy6-k4-c-N"] = N4
out["fy6-k4-c-m"] = round(N4 * m4 * 86400, 4)                        # kg per day
out["k4-c"] = {"kg_per_s": N4 * m4, "kg_per_year": round(N4 * m4 * 86400 * 365, 1)}
out["fy6-k4-d"] = round(U4 * I4, 0)
out["k4-d"] = {"Ek_per_s": round(N4 * 0.5 * m4 * v4 ** 2, 0), "thrust_check_N": round(N4 * m4 * v4, 4)}

# ---------------------------------------------------------------- fy6-k5: the bicycle stand light (capacitor)
C5, U5, Umin, P5 = 0.47, 4.5, 2.0, 15e-3
out["fy6-k5-a-Q"] = round(C5 * U5, 3)
out["fy6-k5-a-W"] = round(0.5 * C5 * U5 ** 2, 3)
Wuse = 0.5 * C5 * (U5 ** 2 - Umin ** 2)
out["fy6-k5-b-W"] = round(Wuse, 3)
out["fy6-k5-b-t"] = round(Wuse / P5, 0)
out["k5-b"] = {"W_left": round(0.5 * C5 * Umin ** 2, 3), "W_use": round(Wuse, 3), "min": round(Wuse / P5 / 60, 2),
               "wrong_all": round(0.5 * C5 * U5 ** 2 / P5, 0)}
out["fy6-k5-c-start"] = round(P5 / U5, 5)
out["fy6-k5-c-end"] = round(P5 / Umin, 5)
out["k5-c"] = {"rate_start_V_per_s": round(P5 / U5 / C5, 4), "rate_end_V_per_s": round(P5 / Umin / C5, 4)}
t1 = 0.5 * C5 * (5.5 ** 2 - Umin ** 2) / P5
t2 = 0.5 * 1.0 * (U5 ** 2 - Umin ** 2) / P5
out["fy6-k5-d-t1"] = round(t1, 0)
out["fy6-k5-d-t2"] = round(t2, 0)

# ---------------------------------------------------------------- fy6-k6: Coulomb's law on a balance
r6 = [3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0]                           # cm
m6 = [0.558, 0.339, 0.228, 0.160, 0.090, 0.057, 0.041]               # g, the reading
F6 = [mm * 1e-3 * g for mm in m6]
x6 = [1 / (rr / 100) ** 2 for rr in r6]                              # 1/m^2
out["fy6-k6-a"] = round(F6[2], 6)
fit = [(x, f) for x, f, rr in zip(x6, F6, r6) if rr >= 5.0]
slope6 = sum(x * f for x, f in fit) / sum(x * x for x, _ in fit)
out["k6-b"] = {"x": [round(x, 1) for x in x6], "F_mN": [round(1000 * f, 3) for f in F6], "Fr2": [round(f * (rr / 100) ** 2 * 1e6, 3) for f, rr in zip(F6, r6)],
               "slope_fit_r_ge_5": slope6}
slope_read = (2.24e-3 - 0) / (400 - 0)                               # the drawn line through (0; 0) and (400 1/m², 2,24 mN)
out["k6-c-slope_read"] = slope_read
out["fy6-k6-c"] = round(math.sqrt(slope_read / k), 11)
out["k6-c"] = {"q_fit": math.sqrt(slope6 / k), "q_nC": round(1e9 * math.sqrt(slope_read / k), 2)}
out["k6-d"] = {"rel_F_3cm": round(100 * 2 * 0.1 / 3.0, 1), "rel_F_4cm": round(100 * 2 * 0.1 / 4.0, 1), "rel_F_12cm": round(100 * 2 * 0.1 / 12.0, 1),
               "scale_3cm": round(100 * 0.001 / 0.558, 2), "scale_12cm": round(100 * 0.001 / 0.041, 2),
               "model_3cm_mN": round(1000 * slope_read * x6[0], 3), "meas_3cm_mN": round(1000 * F6[0], 3),
               "short_3cm_pct": round(100 * (1 - F6[0] / (slope_read * x6[0])), 1),
               "model_4cm_mN": round(1000 * slope_read * x6[1], 3), "short_4cm_pct": round(100 * (1 - F6[1] / (slope_read * x6[1])), 1)}

# ---------------------------------------------------------------- fy6-k7: the home battery bank
n7, Uc, Qc, Rc = 16, 3.20, 200.0, 0.50e-3
E7 = n7 * Uc; W7 = E7 * Qc / 1000                                   # V, kWh
out["fy6-k7-a-U"] = round(E7, 2)
out["fy6-k7-a-W"] = round(W7, 3)
need = 1.2 * 6.0 / 0.95; avail = 0.90 * W7
out["fy6-k7-b"] = round(need, 3)
out["k7-b"] = {"avail_kWh": round(avail, 3), "margin_kWh": round(avail - need, 2)}
Rs7, Rk7, P7 = n7 * Rc, 4.0e-3, 5000.0
I7 = P7 / E7
out["fy6-k7-c-I"] = round(I7, 1)
out["fy6-k7-c-P"] = round((Rs7 + Rk7) * I7 ** 2, 0)
out["k7-c"] = {"Rs": Rs7, "drop_V": round((Rs7 + Rk7) * I7, 3), "P_bat": round(Rs7 * I7 ** 2, 1), "P_cable": round(Rk7 * I7 ** 2, 1),
               "share_pct": round(100 * (Rs7 + Rk7) * I7 ** 2 / P7, 2),
               "exact_I": round((E7 - math.sqrt(E7 ** 2 - 4 * (Rs7 + Rk7) * P7)) / (2 * (Rs7 + Rk7)), 1)}
Ik7 = E7 / Rs7
out["fy6-k7-d"] = round(Ik7, -1)
out["k7-d"] = {"Ik_with_cable": round(E7 / (Rs7 + Rk7), 0), "full_V": round(n7 * 3.65, 2), "ratio_to_fuse": round(Ik7 / 125, 0)}
E7b = 4 * Uc; Rs7b = 4 * Rc / 4; I7b = P7 / E7b
out["fy6-k7-e-I"] = round(I7b, 1)
out["fy6-k7-e-Pk"] = round(Rk7 * I7b ** 2, 0)
out["fy6-k7-e-Ps"] = round(Rs7b * I7b ** 2, 1)
out["k7-e"] = {"U": E7b, "I": round(I7b, 1), "P_bat": round(Rs7b * I7b ** 2, 1), "P_cable_48": round(Rk7 * I7 ** 2, 1),
               "cable_ratio": round((I7b / I7) ** 2, 1), "share_pct": round(100 * (Rs7b + Rk7) * I7b ** 2 / P7, 1)}
R7e = Rs7b + Rk7; I7e = (E7b - math.sqrt(E7b ** 2 - 4 * R7e * P7)) / (2 * R7e)
out["k7-e"].update({"drop_V": round(R7e * I7b, 2), "exact_I": round(I7e, 1), "exact_Pk": round(Rk7 * I7e ** 2, 0), "exact_Ps": round(Rs7b * I7e ** 2, 0)})
print(json.dumps(out))
