"""Every answer in exercises.json for fy3-11, computed from the task data (python -I answers.py).
Gas work at constant pressure W_k = pΔV (p in Pa, V in m³, 1 l = 10⁻³ m³). Heat engine per cycle W = Q₁ − Q₂, η = W/Q₁ = P_hyöty/P_in.
First law on this page: ΔU = Q − W_k (fy3-5's ΔU = Q + W with W = −W_k, the work done ON the gas).
Heat pump: lämpökerroin ε = Q_sisälle/E_s (E_s electrical energy), heat from outside air = Q_sisälle − E_s. 1 MWh = 3,6 · 10⁹ J, 1 h = 3600 s.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy3-11-L1-01"] = 480e3 * 0.0250 / 1000          # locomotive steam: W_k = pΔV = 480 000 Pa · 0,0250 m³ = 12 000 J -> 12,0 kJ
a["fy3-11-L1-02"] = 101e3 * 1.70e-3                # sauna steam: 1,70 l = 0,00170 m³, W_k = pΔV = 101 000 Pa · 0,00170 m³ = 171,7 J -> 172 J
a["fy3-11-L1-03"] = 1600 / 4300 * 100              # OL3: η = P_sähkö/P_lämpö = 1600 MW / 4300 MW = 0,3721 -> 37 %
# fy3-11/pv-isobaari: p = 250 kPa read at the gridline, V from 1,0 l to 4,0 l (gridline crossings)
a["fy3-11-L1-04"] = 250e3 * (4.0 - 1.0) * 1e-3     # W_k = pΔV = 250 000 Pa · 0,0030 m³ = 750 J
a["fy3-11-L1-05"] = 2.6 / 12 * 100                 # cottage generator: η = W/Q₁ = 2,6 kWh / 12 kWh = 0,2167 -> 22 %
# Level 2: two steps or a conversion
W_sahko = 3830 * 3.6e9                             # condensing plant, one day: 3830 MWh · 3,6·10⁹ J/MWh = 1,379·10¹³ J
a["fy3-11-L2-01"] = W_sahko / 33.6e12 * 100        # η = W/Q₁ = 1,379·10¹³ J / 3,36·10¹³ J = 0,4104 -> 41,0 %
Q1_puu = 120 * 15e6                                # steamboat, one hour: Q₁ = m · lämpöarvo = 120 kg · 15 MJ/kg = 1,8·10⁹ J
W_kone = 45e3 * 3600                               # W = Pt = 45 000 W · 3600 s = 1,62·10⁸ J
a["fy3-11-L2-02"] = W_kone / Q1_puu * 100          # η = W/Q₁ = 0,090 -> 9,0 %
W_kaasu = 125e3 * 1.60e-3                          # lab cylinder: gas work W_k = pΔV = 125 000 Pa · 0,00160 m³ = 200 J
a["fy3-11-L2-03"] = 700 + (-W_kaasu)               # ΔU = Q − W_k = 700 J − 200 J = 500 J
P_in_lautta = 480 / 0.40                           # ferry diesel: P_in = P_mek/η = 480 kW / 0,40 = 1200 kW
a["fy3-11-L2-04"] = P_in_lautta - 480              # waste heat power = P_in − P_mek = 720 kW
# Level 3: reasoning, combining ideas, unfamiliar context
P_lauhde = 96 / 0.40                               # separate electricity: 96 MW / 0,40 = 240 MW of fuel
P_lampokeskus = 180 / 0.90                         # separate district heat: 180 MW / 0,90 = 200 MW of fuel
a["fy3-11-L3-01"] = P_lauhde + P_lampokeskus - 320 # extra fuel power of separate production: 440 MW − 320 MW = 120 MW (CHP η_tot = 276/320 = 86 %)
E_s = 16.0 / 2.50                                  # heat pump electricity E_s per year: 16,0 MWh / 2,50 = 6,40 MWh
a["fy3-11-L3-02"] = 16.0 - E_s                     # saved electricity = heat from outside air = 16,0 − 6,40 = 9,60 MWh
m_bensa = 6.0 * 0.75                               # car, 100 km: m = ρV = 0,75 kg/l · 6,0 l = 4,5 kg
Q1_auto = m_bensa * 43e6                           # fuel energy = 4,5 kg · 43 MJ/kg = 1,935·10⁸ J
t_auto = 100 / 80 * 3600                           # time for 100 km at 80 km/h: 1,25 h = 4500 s
a["fy3-11-L3-03"] = 0.28 * Q1_auto / t_auto / 1000 # P_mek = ηQ₁/t = 0,28 · 1,935·10⁸ J / 4500 s = 12 040 W -> 12 kW

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
