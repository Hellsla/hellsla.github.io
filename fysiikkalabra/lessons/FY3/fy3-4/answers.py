"""Every answer in exercises.json for fy3-4, computed from the task data (python -I answers.py).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

g = 9.81          # m/s²
rho_w = 1000      # kg/m³, water
a = {}
# Level 1: one formula, values given
a["fy3-4-L1-01"] = 720 / 0.30                          # p = F/A = 2400 Pa (skis on snow)
a["fy3-4-L1-02"] = rho_w * g * 95 / 1000               # ρgh = 931 950 Pa -> 931,95 kPa -> 930 kPa (Päijänne)
a["fy3-4-L1-03"] = 98.5 + rho_w * g * 18.0 / 1000      # p = p0 + ρgh = 98,5 kPa + 176,58 kPa = 275,08 kPa -> 275 kPa
a["fy3-4-L1-04"] = 750 / 0.0025 / 1000                 # p = F/A = 300 000 Pa = 300 kPa (sauna stove legs)
a["fy3-4-L1-05"] = rho_w * g * 0.45                    # ρgh = 4414,5 Pa -> 4400 Pa (water tub)
# Level 2: two steps, one conversion or one rearrangement
A_heel = 1.5e-4                                        # 1,5 cm² = 1,5 · 10⁻⁴ m²
a["fy3-4-L2-01"] = 600 / A_heel / 1e6                  # p = F/A = 4 000 000 Pa = 4,0 MPa
a["fy3-4-L2-02"] = 350e3 / (rho_w * g)                 # h = p/(ρg) = 35,68 m -> 35,7 m (water tower)
k_A = (200 - 100) / 10                                 # figure fy3-4/two-liquids: line A through (0 m; 100 kPa), (10 m; 200 kPa): 10 kPa/m
k_B = (250 - 100) / 10                                 # line B through (0 m; 100 kPa), (10 m; 250 kPa): 15 kPa/m
p_B4 = 100 + k_B * 4.0                                 # liquid B at 4,0 m: 160 kPa
a["fy3-4-L2-03"] = (p_B4 - 100) / k_A                  # liquid A reaches 160 kPa at h = 60 / 10 = 6,0 m
p_cooker = 0.85 * 100e3                                # 0,85 bar = 85 kPa = 85 000 Pa
A_lid = 380e-4                                         # 380 cm² = 0,0380 m²
a["fy3-4-L2-04"] = p_cooker * A_lid / 1000             # F = pA = 3230 N -> 3,2 kN
# Level 3: reasoning or an unfamiliar context
G_hiker = 85 * g                                       # weight G = mg = 833,85 N, all on one foot while walking
a["fy3-4-L3-01"] = G_hiker / 6.0e3                     # A = G/p_max = 0,139 m² -> 0,14 m² (snowshoe)
dp_lid = rho_w * g * 4.0                               # extra pressure under the lid = ρgh of the 4,0 m tube = 39 240 Pa
a["fy3-4-L3-02"] = dp_lid * 0.25 / 1000                # extra force on the lid ΔF = Δp·A = 9810 N -> 9,8 kN
p_oil = 850 * g * 0.40                                 # oil layer: 3335,4 Pa
p_water = rho_w * g * 1.60                             # water layer below it: 15 696 Pa
a["fy3-4-L3-03"] = (p_oil + p_water) / 1000            # overpressure at the bottom = 19,03 kPa -> 19 kPa
# Exercise-bank additions (L1-06 and L1-08 are multiple-choice tasks without a number)
a["fy3-4-L1-07"] = 1005 * g * 40 / 1000                # ρgh = 394 362 Pa = 394,4 kPa -> 390 kPa (Baltic Sea, ρ = 1005 kg/m³)
# L2-05: sukeltajan (h, p) data, line slope k = 9,78 kPa/m (least squares of the table: 9,777)
h_tab = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]                # m
p_tab = [99.6, 119.5, 138.6, 158.7, 178.1, 197.3]      # kPa
k_fit = 9.78                                           # kPa/m, given in the task
h_ka = sum(h_tab) / len(h_tab)                         # sum 30,0 m -> 5,0 m
p_ka = sum(p_tab) / len(p_tab)                         # sum 891,8 kPa -> 148,63 kPa
a["fy3-4-L2-05"] = p_ka - k_fit * h_ka                 # p0 = p_ka - k h_ka = 148,63 - 48,9 = 99,73 kPa -> 99,7 kPa (ρ = k/g = 997 kg/m³)
a["fy3-4-L2-06"] = rho_w * g * 0.300 / 1000            # ρgh = 2943 Pa = 2,94 kPa (table 2,9...3,0 kPa)
dh_ka = (14.2 + 14.8 + 14.5) / 3                       # sum 43,5 cm -> 14,5 cm
a["fy3-4-L2-07"] = rho_w * g * dh_ka / 100 / 1000      # Δp = ρgΔh = 1422,45 Pa = 1,42 kPa
# L3-04: layered lake, ρ per layer
layers = [(5.0, 998.2), (10.0, 999.7), (5.0, 1000.0)]  # (d in m, ρ in kg/m³)
dp_layers = sum(d_ * r_ * g for d_, r_ in layers) / 1000   # 196,082 kPa
dp_const = rho_w * g * 20.0 / 1000                     # 196,2 kPa
a["fy3-4-L3-04"] = dp_const - dp_layers                # difference 0,118 kPa -> 0,12 kPa
# L3-05: dam wall strip, 4 parts of 5,0 m, width 1,0 m, F = mean pressure of the edges · area
def F_part(h1, h2):
    return (rho_w * g * h1 + rho_w * g * h2) / 2 * (5.0 * 1.0) / 1000   # kN
a["fy3-4-L3-05"] = F_part(15.0, 20.0)                  # (147,15 + 196,2)/2 kPa · 5,0 m² = 858,375 kN -> 858 kN
assert abs(sum(F_part(5.0 * i, 5.0 * i + 5.0) for i in range(4)) - (196.2 / 2) * 20.0) < 1e-9   # sum 1962 kN = whole-wall check
a["fy3-4-L1-10"] = 101 + 1.02e3 * g * 25 / 1000        # sea water: MAFY (Tiheyksiä: Nesteiden tiheyksiä) rho = 1,02 · 10³ kg/m³; p = p0 + rho g h = 101 kPa + 250,2 kPa = 351,2 kPa
a["fy3-4-L2-08"] = k_B * 1000 / g                         # figure fy3-4/two-liquids: k_B = 15 kPa/m = rho g, rho = 15 000 Pa/m / 9,81 m/s² = 1529 kg/m³
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
