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

# s7: a steel beam heated, fy3-8/length-graph: (20 C; 0 mm) and (70 C; 3,0 mm) on a line; l0 = 5,0 m; table steel 12e-6 1/K
l7, T7a, T7b, D7a, D7b = 5.0, 20.0, 70.0, 0.0, 3.0           # m, C, C, mm, mm
dT7 = T7b - T7a                                               # K (a difference of Celsius temperatures)
k7 = (D7b - D7a) / dT7                                        # mm/K: the slope read from the end points
alpha7 = k7 * 1e-3 / l7                                       # 1/K: alpha = k / l0 (mm -> m)
alpha_tab = 12e-6                                             # 1/K: MAFY, steel (fy3-8 row of mafy-arvot.tsv)
out["fy9-kokeellisuus-s7-a"] = round(k7, 4)
out["fy9-kokeellisuus-s7-b"] = alpha7
out["fy9-kokeellisuus-s7-check"] = round(alpha_tab * l7 * dT7 * 1e3, 3)           # mm: the elongation the table value predicts
out["fy9-kokeellisuus-s7-dev"] = round((alpha7 - alpha_tab) / alpha_tab * 100, 2)   # % deviation from the table
rT = 2 * 1.0 / dT7                                            # thermometer +-1 C twice: +-2 K
rl = 2 * 0.1 / (D7b - D7a)                                    # ruler +-0,1 mm twice: +-0,2 mm
out["fy9-kokeellisuus-s7-rT"] = round(rT * 100, 2); out["fy9-kokeellisuus-s7-rl"] = round(rl * 100, 2)
out["fy9-kokeellisuus-s7-d"] = round((rT + rl) * 100, 2)      # % relative uncertainty of alpha
out["fy9-kokeellisuus-s7-dalpha"] = round(alpha7 * (rT + rl) * 1e6, 3)           # 1e-6 1/K
out["fy9-kokeellisuus-s7-lo"] = round(alpha7 * (1 - rT - rl) * 1e6, 2); out["fy9-kokeellisuus-s7-hi"] = round(alpha7 * (1 + rT + rl) * 1e6, 2)
rl2 = 2 * 0.01 / (D7b - D7a)                                  # an improvement: a dial gauge, +-0,01 mm
out["fy9-kokeellisuus-s7-rl2"] = round(rl2 * 100, 2); out["fy9-kokeellisuus-s7-d2"] = round((rT + rl2) * 100, 2)
out["fy9-kokeellisuus-s7-dalpha2"] = round(alpha7 * (rT + rl2) * 1e6, 3)
out["fy9-kokeellisuus-s7-growth"] = round(alpha7 * dT7 * 100, 3)  # % of the length

# s8: a cart, fy1-4/scatter-points: six (t; s) points, no fitted line (the catalog's numbers)
T8 = [1, 2, 3, 4, 5, 6]
S8 = [0.6, 0.8, 1.6, 2.1, 2.4, 2.9]
k8_ls, b8_ls = fit(T8, S8)                                     # least squares as a reference for the eye fit
res8 = [round(y - (k8_ls * x + b8_ls), 3) for x, y in zip(T8, S8)]
P8a, P8b = (1.0, 0.53), (6.0, 2.93)                            # two far-apart points read on the fitted line
k8 = (P8b[1] - P8a[1]) / (P8b[0] - P8a[0])                     # m/s
s08 = P8a[1] - k8 * P8a[0]                                     # m: the intercept s0 = s - v t
s9 = s08 + k8 * 9.0                                            # m: at t = 9 s
dk8 = 0.04                                                     # m/s: the slope's uncertainty (steepest and shallowest line through the cloud)
out["fy9-kokeellisuus-s8-ls-k"] = round(k8_ls, 4); out["fy9-kokeellisuus-s8-ls-b"] = round(b8_ls, 4)
out["fy9-kokeellisuus-s8-res"] = res8
out["fy9-kokeellisuus-s8-a"] = round(k8, 4)
out["fy9-kokeellisuus-s8-alt"] = round((S8[5] - S8[0]) / (T8[5] - T8[0]), 4)     # from the first and last data points
out["fy9-kokeellisuus-s8-b"] = round(s08, 4)
out["fy9-kokeellisuus-s8-c"] = round(s9, 3)
out["fy9-kokeellisuus-s8-c-ds"] = round(9.0 * dk8, 3)
out["fy9-kokeellisuus-s8-c-ls"] = round(k8_ls * 9 + b8_ls, 3)
out["fy9-kokeellisuus-s8-dt"] = [round(abs(r) / k8, 2) for r in res8]            # s: the deviation as a timing error
out["fy9-kokeellisuus-s8-timing"] = round(0.25 * k8, 3)                           # m: a 0,25 s timing error at this speed
out["fy9-kokeellisuus-s8-extra"] = round((9 - 6) / (6 - 1) * 100, 1)             # %: the extrapolated 3 s as a share of the 5 s data span

print(json.dumps(out))
