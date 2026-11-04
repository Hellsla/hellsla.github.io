"""FY9 fy9-lampo, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-lampo` compares them with tasks.json."""
import json

g = 9.81
c_w, c_i, s_i, r_w, c_fe = 4190.0, 2100.0, 334e3, 2.26e6, 450.0   # the FY3 tables: J/(kg K), J/kg

def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx

out = {}

# s1: freezing the ice of a hockey rink (example data)
A, d = 1800.0, 0.0300                     # m^2, m (water layer 3,00 cm = 3,00 * 0,01 m)
m1 = 1000.0 * A * d                       # kg: rho V
Q_cool = c_w * m1 * (15.0 - 0.0)          # water 15,0 -> 0 °C
Q_freeze = s_i * m1                       # freezing at 0 °C
Q_ice = c_i * m1 * (0.0 - (-4.0))         # ice 0 -> -4,0 °C
Q1 = Q_cool + Q_freeze + Q_ice
t1 = Q1 / 350e3                           # s at 350 kW
out.update({"fy9-lampo-s1-m": m1, "fy9-lampo-s1-Qcool": Q_cool, "fy9-lampo-s1-Qfreeze": Q_freeze, "fy9-lampo-s1-Qice": Q_ice,
            "fy9-lampo-s1-a": round(Q1 / 1e9, 3), "fy9-lampo-s1-b": round(t1 / 3600, 2), "fy9-lampo-s1-t-s": round(t1),
            "fy9-lampo-s1-share-freeze": round(100 * Q_freeze / Q1, 1), "fy9-lampo-s1-share-cool": round(100 * Q_cool / Q1, 1),
            "fy9-lampo-s1-share-ice": round(100 * Q_ice / Q1, 1), "fy9-lampo-s1-h-cool": round(Q_cool / 350e3 / 3600, 2),
            "fy9-lampo-s1-h-freeze": round(Q_freeze / 350e3 / 3600, 2), "fy9-lampo-s1-check-kJ-per-kg": round(Q1 / m1 / 1000, 1)})

# s2: a heat-storing soapstone fireplace (example data)
m_wood, H, eta, m_stone, c_stone = 12.0, 15e6, 0.80, 1800.0, 980.0
Q2 = eta * H * m_wood                     # J into the stone
dT2 = Q2 / (c_stone * m_stone)
P2 = Q2 / (24 * 3600)                     # W, mean power over the next 24 h
loss = 150.0 * (21.0 - (-10.0))           # W: the house loses 150 W per kelvin of difference
out.update({"fy9-lampo-s2-Q": Q2, "fy9-lampo-s2-a": round(dT2, 2), "fy9-lampo-s2-b": round(P2 / 1000, 3),
            "fy9-lampo-s2-loss": loss, "fy9-lampo-s2-c": round(100 * P2 / loss, 1), "fy9-lampo-s2-wood-E": H * m_wood,
            "fy9-lampo-s2-wood-loss": (1 - eta) * H * m_wood, "fy9-lampo-s2-wood-for-all": round(loss * 86400 / (eta * H), 1)})

# s3: evaporation rate against heater power (invented data: r = 2,26 MJ/kg, 70 W lost to the room, 300 s per run, noise)
P3 = [200, 400, 600, 800, 1000]                     # W
dm = [17.9, 43.1, 70.8, 96.4, 123.8]                # g in 5,00 min
t3 = 300.0
k3, b3 = fit(P3, dm)                                # g/W, g
r_fit = t3 / (k3 / 1000)                            # J/kg: slope = t/r
Ph_fit = -b3 / k3                                   # W: where the line meets the P axis
# as read in the solution from two far-apart points of the drawn line: (100 W; 4,0 g) and (1100 W; 137,0 g)
read = [(100, 4.0), (1100, 137.0)]
k_read = (read[1][1] - read[0][1]) / (read[1][0] - read[0][0])
r_read = t3 / (k_read / 1000)
Ph_read = read[0][0] - read[0][1] / k_read
single = 600 * t3 / (70.8 / 1000)                   # the one-run result of part d
out.update({"fy9-lampo-s3-k": round(k3, 5), "fy9-lampo-s3-b0": round(b3, 2), "fy9-lampo-s3-rfit": round(r_fit / 1e6, 4),
            "fy9-lampo-s3-Phfit": round(Ph_fit, 1), "fy9-lampo-s3-kread": round(k_read, 4),
            "fy9-lampo-s3-b": round(r_read / 1e6, 3), "fy9-lampo-s3-c": round(Ph_read, 1),
            "fy9-lampo-s3-line100": round(k3 * 100 + b3, 1), "fy9-lampo-s3-line1100": round(k3 * 1100 + b3, 1),
            "fy9-lampo-s3-d": round(single / 1e6, 3), "fy9-lampo-s3-d-err": round(100 * (single / 2.26e6 - 1), 1),
            "fy9-lampo-s3-loss-share600": round(100 * Ph_read / 600, 1)})

# s4 (word task): the numbers its model answer quotes
out.update({"fy9-lampo-s4-ice-per-cm-MJ": round(917 * 0.01 * s_i / 1e6, 2)})   # MJ per m^2 for 1 cm of ice

# s5: the ice calorimeter report (example data)
mv, Tv, mj, T5, Tj = 0.200, 40.0, 0.0500, 14.3, -18.0
Qv = c_w * mv * (Tv - T5)                           # J given by the water
Qmelt_water = c_w * mj * (T5 - 0.0)                 # J to warm the meltwater
s_group = (Qv - Qmelt_water) / mj                   # J/kg, ice assumed at 0 °C
Q_ice_warm = c_i * mj * (0.0 - Tj)
s_true = (Qv - Qmelt_water - Q_ice_warm) / mj
out.update({"fy9-lampo-s5-Qv": round(Qv, 1), "fy9-lampo-s5-Qmw": round(Qmelt_water, 2), "fy9-lampo-s5-a": round(s_group / 1000, 2),
            "fy9-lampo-s5-Qiw": Q_ice_warm, "fy9-lampo-s5-b": round(s_true / 1000, 2),
            "fy9-lampo-s5-a-err": round(100 * (s_group / 334e3 - 1), 1), "fy9-lampo-s5-b-err": round(100 * (s_true / 334e3 - 1), 1)})

# s6: braking heat (example data)
m6, v_kmh = 1600.0, 90.0
v6 = v_kmh / 3.6                                    # 90 km/h = 90 * 1000 m : 3600 s
Ek = 0.5 * m6 * v6 ** 2
m_disc, share = 4 * 7.5, 0.85
dT6a = share * Ek / (c_fe * m_disc)
h6, s6, F6, v6b = 250.0, 4000.0, 450.0, 60.0 / 3.6
Ep = m6 * g * h6
W_res = F6 * s6
Q_brakes = Ep - W_res
Q_discs = share * Q_brakes
dT6b = Q_discs / (c_fe * m_disc)
t6 = s6 / v6b
P6 = Q_discs / t6
kept = c_fe * m_disc * 80.0                         # J kept in the discs (they warmed 80 K)
to_air = Q_discs - kept
out.update({"fy9-lampo-s6-Ek": round(Ek), "fy9-lampo-s6-a": round(dT6a, 2), "fy9-lampo-s6-Ep": round(Ep), "fy9-lampo-s6-Wres": W_res,
            "fy9-lampo-s6-Qbrakes": round(Q_brakes), "fy9-lampo-s6-Qdiscs": round(Q_discs), "fy9-lampo-s6-b": round(dT6b, 1),
            "fy9-lampo-s6-t": round(t6, 1), "fy9-lampo-s6-P": round(P6), "fy9-lampo-s6-kept": kept,
            "fy9-lampo-s6-air": round(to_air), "fy9-lampo-s6-c": round(100 * to_air / Q_discs, 1)})

print(json.dumps(out))
