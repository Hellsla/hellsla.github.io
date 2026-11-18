"""fy9-kokeellisuus task set: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json (and the intermediate values the
solutions quote); `python scripts/practice.py check units/fy9-kokeellisuus` compares them with tasks.json."""
import json, math

g = 9.81
PI4 = 4 * math.pi ** 2


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


out = {}

# s2: rapeseed oil, 50 W heater, 200 g, 20 K, c about 2,0 kJ/(kg K) (the task's estimate)
P, m_oil, dT, c_oil = 50.0, 0.200, 20.0, 2000.0
out["fy9-kokeellisuus-s2-c"] = round(c_oil * m_oil * dT / P, 2)              # s
out["fy9-kokeellisuus-s2-Q"] = c_oil * m_oil * dT                             # J
out["fy9-kokeellisuus-s2-slope"] = round(P / (c_oil * m_oil), 4)               # K/s, the expected slope

# s3: the report: h = 3,0 m, three hand-timed drops
h = 3.0
ts = [0.82, 0.75, 0.79]
tm = sum(ts) / 3
out["fy9-kokeellisuus-s3-tmean"] = round(tm, 4)
out["fy9-kokeellisuus-s3-b-g"] = round(2 * h / tm ** 2, 3)
gmax, gmin = 2 * h / min(ts) ** 2, 2 * h / max(ts) ** 2
out["fy9-kokeellisuus-s3-gmax"] = round(gmax, 3); out["fy9-kokeellisuus-s3-gmin"] = round(gmin, 3)
out["fy9-kokeellisuus-s3-b-dg"] = round((gmax - gmin) / 2, 3)
out["fy9-kokeellisuus-s3-free"] = round(math.sqrt(2 * h / g), 3)             # the fall time in a vacuum
out["fy9-kokeellisuus-s3-eps"] = round(0.1 / tm, 3)                           # a 0,1 s reaction time as a share of t

# s4: the pendulum, l measured to the top of the bob (simulated: r = 2,5 cm, g = 9,81, noise in t10, see figures.py)
L4 = [0.250, 0.400, 0.550, 0.700, 0.850, 1.000]
T10 = [10.55, 13.04, 15.23, 17.06, 18.81, 20.28]
T2 = [(t / 10) ** 2 for t in T10]
k4, b4 = fit(L4, T2)
out["fy9-kokeellisuus-s4-T2"] = [round(x, 3) for x in T2]
out["fy9-kokeellisuus-s4-fit-k"] = round(k4, 4); out["fy9-kokeellisuus-s4-fit-b"] = round(b4, 4)
# read from the drawn line at l = 0,200 m and l = 1,000 m (the model graph marks them): 0,91 s^2 and 4,12 s^2
kr = (4.12 - 0.91) / (1.000 - 0.200)
out["fy9-kokeellisuus-s4-kread"] = round(kr, 4)
out["fy9-kokeellisuus-s4-b"] = round(PI4 / kr, 3)
b_read = 0.10                                                                  # s^2, the intercept read off
r = b_read / kr
out["fy9-kokeellisuus-s4-r"] = round(r * 100, 2)                              # cm
out["fy9-kokeellisuus-s4-c"] = round(2 * r * 100, 2)                          # cm, the diameter
out["fy9-kokeellisuus-s4-single"] = [round(PI4 * l / t, 2) for l, t in zip(L4, T2)]   # g row by row (too small)
out["fy9-kokeellisuus-s4-gfast"] = round(PI4 / (kr - 0.1), 3); out["fy9-kokeellisuus-s4-gslow"] = round(PI4 / (kr + 0.1), 3)

# s5: the stone
m5, V1, V2, dm, dV1 = 187.4, 120.0, 190.0, 0.1, 1.0
V5 = V2 - V1
rho = m5 / V5                                                                  # g/cm^3
out["fy9-kokeellisuus-s5-a"] = round(rho * 1000, 1)                           # kg/m^3
rmax, rmin = (m5 + dm) / (V5 - 2 * dV1), (m5 - dm) / (V5 + 2 * dV1)
out["fy9-kokeellisuus-s5-rmax"] = round(rmax * 1000, 1); out["fy9-kokeellisuus-s5-rmin"] = round(rmin * 1000, 1)
out["fy9-kokeellisuus-s5-b"] = round((rmax - rmin) / 2 * 1000, 1)            # kg/m^3
out["fy9-kokeellisuus-s5-epsm"] = round(dm / m5 * 100, 3); out["fy9-kokeellisuus-s5-epsV"] = round(2 * dV1 / V5 * 100, 2)   # %

# s6: the bicycle (simulated: a = 4,2 m/s^2 plus noise in s, see figures.py)
VK = [10, 15, 20, 25, 30]
S6 = [1.0, 2.0, 3.8, 5.6, 8.5]
v2 = [(v / 3.6) ** 2 for v in VK]
out["fy9-kokeellisuus-s6-v2"] = [round(x, 1) for x in v2]
k_fit = sum(x * y for x, y in zip(v2, S6)) / sum(x * x for x in v2)            # least squares through the origin
out["fy9-kokeellisuus-s6-fit-k"] = round(k_fit, 4)
k6 = 7.2 / 60.0                                                                # read: the line passes (60 m^2/s^2; 7,2 m)
a6 = 1 / (2 * k6)
out["fy9-kokeellisuus-s6-b"] = round(a6, 3)
out["fy9-kokeellisuus-s6-c"] = round(a6 / g, 4)
out["fy9-kokeellisuus-s6-d"] = round((1.05 ** 2 - 1) * 100, 2)                # %
out["fy9-kokeellisuus-s6-atrue"] = round(a6 / 1.05 ** 2, 3)

# s7: kinetic friction measurement (fy4-6/mittaus; values read from the figure: N = 5...25 N, F = 1,1; 2,1; 3,3; 4,2; 5,4 N)
N7 = [5.0, 10.0, 15.0, 20.0, 25.0]
F7 = [1.1, 2.1, 3.3, 4.2, 5.4]
q7 = [f / n for f, n in zip(F7, N7)]
mu7 = sum(q7) / len(q7)                                                        # mean of the ratios
dmu7 = (max(q7) - min(q7)) / 2                                                 # half the range
k7, b7 = fit(N7, F7)                                                           # least squares: slope and intercept (check)
k7o = sum(n * f for n, f in zip(N7, F7)) / sum(n * n for n in N7)              # through the origin
res7 = [f - k7o * n for f, n in zip(F7, N7)]                                   # residuals N
out.update({"fy9-kokeellisuus-s7-q": [round(x, 3) for x in q7], "fy9-kokeellisuus-s7-b": round(mu7, 4),
            "fy9-kokeellisuus-s7-db": round(dmu7, 4), "fy9-kokeellisuus-s7-fitk": round(k7, 4),
            "fy9-kokeellisuus-s7-fitb": round(b7, 3), "fy9-kokeellisuus-s7-origink": round(k7o, 4),
            "fy9-kokeellisuus-s7-res": [round(x, 3) for x in res7]})
F0, Fr, Nc = 0.3, 2.4, 10.0                                                    # zero error N, reading N, normal force N
mu_w, mu_r = Fr / Nc, (Fr - F0) / Nc
out.update({"fy9-kokeellisuus-s7-c-mu_wrong": round(mu_w, 3), "fy9-kokeellisuus-s7-c-mu_right": round(mu_r, 3),
            "fy9-kokeellisuus-s7-c-err": round((mu_w - mu_r) / mu_r * 100, 2)})
out["fy9-kokeellisuus-s7-d-rel5"] = round(0.05 / F7[0] * 100, 1)               # % half the 0,1 N division at N = 5 N
out["fy9-kokeellisuus-s7-d-rel25"] = round(0.05 / F7[-1] * 100, 1)

# s8: coil, B against I (fy7-3/coil-fit; read from the fitted line: (1,0 A; 2,5 mT) and (2,5 A; 6,2 mT))
mu0 = 4 * math.pi * 1e-7
k8 = (6.2 - 2.5) / (2.5 - 1.0)                                                 # mT/A
n8 = k8 * 1e-3 / mu0                                                           # 1/m
out["fy9-kokeellisuus-s8-a-k"] = round(k8, 4)
out["fy9-kokeellisuus-s8-a"] = round(n8, 1)
out["fy9-kokeellisuus-s8-a-percm"] = round(n8 / 100, 1)
B8 = 12.0                                                                      # mT wanted
out["fy9-kokeellisuus-s8-b"] = round(B8 / k8, 3)                               # A
out["fy9-kokeellisuus-s8-b-ratio"] = round(B8 / k8 / 2.5, 2)                   # times the largest measured current
B05, B25, B00 = 1.3, 6.2, 0.04                                                 # mT read at 0,5 A and 2,5 A; zero reading
out["fy9-kokeellisuus-s8-c-r05"] = round(B00 / B05 * 100, 2)
out["fy9-kokeellisuus-s8-c-r25"] = round(B00 / B25 * 100, 3)

print(json.dumps(out))
