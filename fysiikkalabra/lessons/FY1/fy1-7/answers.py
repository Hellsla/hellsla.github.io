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
dV = 54 - 46                                    # figure fy1-7/cylinders-read: levels 46 ml and 54 ml -> displaced volume 8 ml = 8 cm3
a["fy1-7-L2-03"] = 57.0e-3 / (dV * 1e-6)         # rho = 0,0570 kg / 8e-6 m3 = 7125 kg/m3 -> 7100 kg/m3 (two figures)
a["fy1-7-L2-04"] = (412 - 215) / 250 * 1000      # liquid: m = 412 g − 215 g = 197 g; rho = 197/250 g/cm3 = 0,788 g/cm3 = 788 kg/m3
# Level 3: reasoning or an unfamiliar context
a["fy1-7-L3-01"] = rho["kupari"] / rho["alumiini"]   # equal masses: V_Al / V_Cu = rho_Cu / rho_Al = 8960 / 2700 = 3,32
a["fy1-7-L3-02"] = (2.70 * 100 + 7.87 * 50) / (100 + 50)   # alloy: total m / total V = (270 + 393,5) g / 150 cm3 = 4,42 g/cm3
V_wire = 0.50 / rho["kupari"]                    # copper wire: V = m/rho = 0,50 kg / 8960 kg/m3 = 5,58e-5 m3
A_wire = math.pi * (0.50e-3) ** 2                # cross-section from radius 0,50 mm: 7,854e-7 m2
a["fy1-7-L3-03"] = V_wire / A_wire               # length L = V/A = 71,05 m -> 71 m
# inquiry.json numeric tasks (not exercises; printed with their own keys)
a["fy1-7-inq-metalli"] = (224.3 - 45.1) / (25.0 - 5.0)         # copper-like metal, slope between first and last point = 8,96 g/cm3
a["fy1-7-inq-siirto"] = 0.187 / (70e-6)          # stone: 187 g, displaced 70 ml: rho = 0,187 kg / 70e-6 m3 = 2671 kg/m3 -> 2,7e3
a["fy1-7-inq-virhe"] = 2.70 * 250   # Etsi virhe (not numeric): aluminium 250 cm3: m = 2,70 g/cm3 · 250 cm3 = 675 g
a["fy1-7-inq-tarkistus-2"] = 500 * 0.200 ** 3   # pine cube: m = 500 kg/m3 · (0,200 m)^3 = 4,00 kg
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
