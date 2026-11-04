"""Every answer in exercises.json and the numeric tasks of inquiry.json for fy1-7, computed from the task data (python -I answers.py).
rho = m/V, m = rho V, V = m/rho; densities from the lesson's table. Prints {id: value} as JSON on the last line."""
import json, math

rho = {"vesi": 1000, "etanoli": 790, "oljy": 920, "alumiini": 2700, "rauta": 7870, "kupari": 8960, "kulta": 19300}   # kg/m3, lesson table
a = {}
# Level 1: one formula, values given
a["fy1-7-L1-01"] = 340 / 30.0                    # lead ingot: rho = m/V = 340 g / 30,0 cm3 = 11,33 g/cm3 -> 11,3 g/cm3
a["fy1-7-L1-02"] = 2.70 * 35.0                   # aluminium plate: m = rho V = 2,70 g/cm3 · 35,0 cm3 = 94,5 g
a["fy1-7-L1-03"] = 316 / 0.79                    # ethanol: V = m/rho = 316 g / 0,79 g/cm3 = 400 cm3
a["fy1-7-L1-04"] = 2400 * 0.75                   # concrete slab: m = rho V = 2400 kg/m3 · 0,75 m3 = 1800 kg
a["fy1-7-L1-05"] = 36.8 / 0.0400                 # ice block: rho = 36,8 kg / 0,0400 m3 = 920 kg/m3
# Level 2: a conversion, two steps or a rearrangement
V_bar = 10.0 * 5.0 * 2.0                         # gold bar: V = 10,0 cm · 5,0 cm · 2,0 cm = 100 cm3 = 100e-6 m3
a["fy1-7-L2-01"] = rho["kulta"] * V_bar * 1e-6   # m = 19 300 kg/m3 · 100e-6 m3 = 1,93 kg -> 1,9 kg
a["fy1-7-L2-02"] = rho["etanoli"] * 2.5e-3       # 2,5 dm3 = 2,5e-3 m3: m = 790 · 2,5e-3 = 1,975 kg -> 2,0 kg
dV = 50 - 40                                    # figure fy1-7/cylinders-read: levels 40 ml and 50 ml -> displaced volume 10 ml = 10 cm3
a["fy1-7-L2-03"] = 89.0e-3 / (dV * 1e-6)         # rho = 0,0890 kg / 10e-6 m3 = 8900 kg/m3 (two figures)
a["fy1-7-L2-04"] = (412 - 215) / 250 * 1000      # liquid: m = 412 g − 215 g = 197 g; rho = 197/250 g/cm3 = 0,788 g/cm3 = 788 kg/m3
# Level 3: reasoning or an unfamiliar context
a["fy1-7-L3-01"] = rho["kupari"] / rho["alumiini"]   # equal masses: V_Al / V_Cu = rho_Cu / rho_Al = 8960 / 2700 = 3,32
a["fy1-7-L3-02"] = (2.70 * 100 + 7.87 * 50) / (100 + 50)   # alloy: total m / total V = (270 + 393,5) g / 150 cm3 = 4,42 g/cm3
V_wire = 0.50 / rho["kupari"]                    # copper wire: V = m/rho = 0,50 kg / 8960 kg/m3 = 5,58e-5 m3
A_wire = math.pi * (0.50e-3) ** 2                # cross-section from radius 0,50 mm: 7,854e-7 m2
a["fy1-7-L3-03"] = V_wire / A_wire               # length L = V/A = 71,05 m -> 71 m
# Exercise bank additions (teacher 2026-11-04): L1-06 and L1-07 are multiple choice (no number)
a["fy1-7-L1-08"] = 11.3 * 5.00                   # lead sinker: m = rho V = 11,3 g/cm3 · 5,00 cm3 = 56,5 g


def fit(pts):
    """Least-squares line y = k x + b through the points (a student's by-eye line lands within the tolerance)."""
    n = len(pts)
    xm, ym = sum(x for x, _ in pts) / n, sum(y for _, y in pts) / n
    k = sum((x - xm) * (y - ym) for x, y in pts) / sum((x - xm) ** 2 for x, _ in pts)
    return k, ym - k * xm


pts5 = list(zip([10.0, 20.0, 30.0, 40.0, 50.0], [27.3, 53.5, 81.6, 107.9, 135.4]))   # data of L2-05
a["fy1-7-L2-05"] = round(fit(pts5)[0], 1)        # slope 2,706 g/cm3 -> 2,7 (aluminium; tolerance 0,03: 2,62...2,78)
pts6 = list(zip([20.0, 40.0, 60.0, 80.0, 100.0], [103.6, 121.2, 140.5, 158.9, 176.8]))   # data of L2-06
a["fy1-7-L2-06"] = round(fit(pts6)[0] * 100) * 10    # slope 0,9205 g/cm3 = 920 kg/m3 (intercept = empty glass 85,0 g; tolerance 0,03)
a["fy1-7-L2-07"] = round(107 / (72 - 60), 1)     # error: V = V2 - V1 = 12 cm3 (not 72): rho = 107/12 = 8,92 g/cm3 -> 8,9
a["fy1-7-L3-04"] = 113 / (62.0 - 50.0 - 2.0)   # bubble 2,0 ml: true V = 12,0 - 2,0 = 10,0 cm3, rho = 113/10,0 = 11,3 g/cm3 (student: 113/12,0 = 9,42, -16,7 %)
a["fy1-7-L3-05"] = round((520 - 2.70 * 100) / (8.96 - 2.70), 1)   # alloy: V_Cu = (m - rho_Al V)/(rho_Cu - rho_Al) = 250/6,26 = 39,9 cm3
# inquiry.json numeric tasks (not exercises; printed with their own keys)
a["fy1-7-inq-metalli"] = (224.3 - 45.1) / (25.0 - 5.0)         # copper-like metal, slope between first and last point = 8,96 g/cm3
a["fy1-7-inq-siirto"] = 0.187 / (70e-6)          # stone: 187 g, displaced 70 ml: rho = 0,187 kg / 70e-6 m3 = 2671 kg/m3 -> 2,7e3
a["fy1-7-inq-virhe"] = 2.70 * 250   # Etsi virhe (not numeric): aluminium 250 cm3: m = 2,70 g/cm3 · 250 cm3 = 675 g
a["fy1-7-inq-tarkistus-2"] = 500 * 0.200 ** 3   # pine cube: m = 500 kg/m3 · (0,200 m)^3 = 4,00 kg
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
