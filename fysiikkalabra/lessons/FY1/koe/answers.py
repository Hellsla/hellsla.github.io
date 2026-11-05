"""FY1 Esimerkkikoe: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json; `python scripts/practice.py check FY1/koe` compares them."""
import json, math
from statistics import mean


def fit(xs, ys, origin=False):
    """Least-squares line (k, b); origin=True: through the origin."""
    if origin: return sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs), 0.0
    xm, ym = mean(xs), mean(ys)
    k = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sum((x - xm) ** 2 for x in xs)
    return k, ym - k * xm


out = {}
# fy1-k1: Osa 1 checks of the options that need a number
out["k1-f"] = 12.6 / 0.75                                   # km/h, 16,8 -> 17
out["k1-j"] = {"A": 40 / 50, "B": 270 / 100, "C": 1000 / 500, "D": 79 / 10}   # g/cm^3
# fy1-k2: the candle
T2 = [0, 10, 20, 30, 40, 50]; L2 = [15.0, 13.9, 12.6, 11.5, 10.4, 9.1]
k2, b2 = fit(T2, L2)
read2 = (9.0 - 15.0) / (51 - 0)                             # two points read off the drawn line: (0 min, 15,0 cm), (51 min, 9,0 cm)
out["fy1-k2-b"] = round(-read2, 3); out["k2-fit"] = (round(k2, 4), round(b2, 3))
out["fy1-k2-c"] = round((2.0 - 15.0) / read2, 0)            # min until 2,0 cm
# fy1-k3: Elina and Aaro
vE, vA, dt = 3.2, 6.0, 5 * 60
t3 = vE * dt / (vA - vE); s3 = vA * t3
out["fy1-k3-b-t"] = round(dt + t3, 1); out["fy1-k3-b-s"] = round(s3, 0)
for v in (3.0, 3.4):
    t = v * dt / (vA - v); out[f"k3-c-{v}"] = (round(t, 0), round(vA * t, 0))
# fy1-k4: ten swings
R4 = [14.2, 14.5, 13.9, 14.4, 14.1, 16.8]; ok4 = R4[:5]
out["k4-mean"] = round(mean(ok4), 3); out["fy1-k4-b-dx"] = round((max(ok4) - min(ok4)) / 2 / 10, 4)
out["fy1-k4-b-T"] = round(mean(ok4) / 10, 4)
out["k4-ratio"] = round(16.8 / (mean(ok4) / 10), 2)          # about 12 swings
# fy1-k5: screws
m5, V0, V1, dV = 96.0, 50.0, 62.5, 0.5
rho5 = m5 / (V1 - V0)
out["fy1-k5-a"] = round(rho5, 2)
out["fy1-k5-c-min"] = round(m5 / (V1 - V0 + 2 * dV), 2); out["fy1-k5-c-max"] = round(m5 / (V1 - V0 - 2 * dV), 2)
# fy1-k6: the falling balls
T6 = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
V6 = [0.47, 0.99, 1.45, 1.95, 2.44, 2.90, 3.41, 3.87]
VL6 = [round(1.5 * math.tanh(9.81 * t / 1.5), 2) for t in T6]   # the coffee filter: v_t = 1,5 m/s (the data of the task)
out["k6-light"] = VL6
k6, b6 = fit(T6, V6)
read6 = (3.87 - 0.0) / (0.40 - 0.0)                         # the drawn line through (0; 0) and (0,40 s; 3,87 m/s)
out["fy1-k6-b"] = round(read6, 2); out["k6-fit"] = (round(k6, 3), round(b6, 3))
out["fy1-k6-b-dev"] = round(100 * (9.81 - read6) / 9.81, 1)
out["k6-d-ms"] = round(read6 * 1.2, 1); out["fy1-k6-d"] = round(read6 * 1.2 * 3.6, 0)
# fy1-k7: sheets of paper
N7 = [100, 200, 300, 400, 500]; D7 = [10, 21, 30, 41, 51]   # mm
k7, _ = fit(N7, D7, origin=True)
read7 = 51 / 500                                            # the line through the origin and (500; 51 mm)
out["fy1-k7-c-d"] = round(read7 * 1000, 0)                    # um per sheet
out["fy1-k7-c-dx"] = round(1 / 500 * 1000, 1)               # +-1 mm over 500 sheets
out["k7-fit"] = round(k7 * 1000, 1)
out["fy1-k7-d"] = round(0.080 / (read7 / 1000), 0)          # kg/m^3 from 80 g/m^2
print(json.dumps(out))
