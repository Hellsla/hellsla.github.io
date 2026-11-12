"""Every answer in exercises.json for fy3-11, computed from the task data (python -I answers.py).
Gas work at constant pressure W = pΔV (MAFY; W the work the gas does) (p in Pa, V in m³, 1 l = 10⁻³ m³). Heat engine per cycle W = Q₁ − Q₂, η = W/Q₁ = P_hyöty/P_in.
First law as in fy3-5 and MAFY: ΔU = Q + W, W the work done ON the gas, so an expanding gas has W = −pΔV and ΔU = Q − pΔV.
Heat pump (MAFY): ε = Q₁/W = Q₁/(Q₁ − Q₂), Q₁ heat given indoors, Q₂ heat taken from the outside air, W = Q₁ − Q₂ the electrical energy. 1 MWh = 3,6 · 10⁹ J, 1 h = 3600 s.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy3-11-L1-01"] = 480e3 * 0.0250 / 1000          # locomotive steam: W = pΔV = 480 000 Pa · 0,0250 m³ = 12 000 J -> 12,0 kJ
a["fy3-11-L1-02"] = 101e3 * 1.70e-3                # sauna steam: 1,70 l = 0,00170 m³, W = pΔV = 101 000 Pa · 0,00170 m³ = 171,7 J -> 172 J
a["fy3-11-L1-03"] = 1600 / 4300 * 100              # OL3: η = P_sähkö/P_lämpö = 1600 MW / 4300 MW = 0,3721 -> 37 %
# fy3-11/pv-isobaari: p = 250 kPa read at the gridline, V from 1,0 l to 4,0 l (gridline crossings)
a["fy3-11-L1-04"] = 250e3 * (4.0 - 1.0) * 1e-3     # W = pΔV = 250 000 Pa · 0,0030 m³ = 750 J
a["fy3-11-L1-05"] = 2.6 / 12 * 100                 # cottage generator: η = W/Q₁ = 2,6 kWh / 12 kWh = 0,2167 -> 22 %
# Level 2: two steps or a conversion
W_sahko = 3830 * 3.6e9                             # condensing plant, one day: 3830 MWh · 3,6·10⁹ J/MWh = 1,379·10¹³ J
a["fy3-11-L2-01"] = W_sahko / 33.6e12 * 100        # η = W/Q₁ = 1,379·10¹³ J / 3,36·10¹³ J = 0,4104 -> 41,0 %
Q1_puu = 120 * 15e6                                # steamboat, one hour: Q₁ = m · lämpöarvo = 120 kg · 15 MJ/kg = 1,8·10⁹ J
W_kone = 45e3 * 3600                               # W = Pt = 45 000 W · 3600 s = 1,62·10⁸ J
a["fy3-11-L2-02"] = W_kone / Q1_puu * 100          # η = W/Q₁ = 0,090 -> 9,0 %
W_kaasu = 125e3 * 1.60e-3                          # lab cylinder: gas work W = pΔV = 125 000 Pa · 0,00160 m³ = 200 J
a["fy3-11-L2-03"] = 700 + (-W_kaasu)               # ΔU = Q − pΔV = 700 J − 200 J = 500 J
P_in_lautta = 480 / 0.40                           # ferry diesel: P_in = P_mek/η = 480 kW / 0,40 = 1200 kW
a["fy3-11-L2-04"] = P_in_lautta - 480              # waste heat power = P_in − P_mek = 720 kW
# Level 3: reasoning, combining ideas, unfamiliar context
P_lauhde = 96 / 0.40                               # separate electricity: 96 MW / 0,40 = 240 MW of fuel
P_lampokeskus = 180 / 0.90                         # separate district heat: 180 MW / 0,90 = 200 MW of fuel
a["fy3-11-L3-01"] = P_lauhde + P_lampokeskus - 320 # extra fuel power of separate production: 440 MW − 320 MW = 120 MW (CHP η_tot = 276/320 = 86 %)
E_s = 16.0 / 2.50                                  # heat pump electricity W per year: 16,0 MWh / 2,50 = 6,40 MWh
a["fy3-11-L3-02"] = 16.0 - E_s                     # saved electricity = heat from outside air = 16,0 − 6,40 = 9,60 MWh
m_bensa = 6.0 * 0.75                               # car, 100 km: m = ρV = 0,75 kg/l · 6,0 l = 4,5 kg
Q1_auto = m_bensa * 43e6                           # fuel energy = 4,5 kg · 43 MJ/kg = 1,935·10⁸ J
t_auto = 100 / 80 * 3600                           # time for 100 km at 80 km/h: 1,25 h = 4500 s
a["fy3-11-L3-03"] = 0.28 * Q1_auto / t_auto / 1000 # P_mek = ηQ₁/t = 0,28 · 1,935·10⁸ J / 4500 s = 12 040 W -> 12 kW

# Exercise bank additions (teacher 2026-11-04): L1-06, L1-07, L2-06 are multiple choice (no number)
a["fy3-11-L1-08"] = 3.90 / 1.20                    # heat pump: ε = P_sisälle/P_s = 3,90 kW / 1,20 kW = 3,25
H_diesel = 43e6                                    # diesel heating value 43 MJ/kg (L2-05)
eta_load = [(P * 1e3) / (m / 3600 * H_diesel) * 100 for P, m in [(20.0, 7.9), (40.0, 11.6), (60.0, 16.0), (80.0, 22.5)]]   # η = P/(q_m H): 21,2; 28,9; 31,4; 29,8 %
a["fy3-11-L2-05"] = max(eta_load)                  # best load 60 kW: 31,4 %
Es_day = [2.1, 3.0, 4.2, 3.6]                      # L2-07: electricity per day, kWh
Qin_day = [6.4, 8.1, 10.0, 9.3]                    # heat delivered inside per day, kWh
a["fy3-11-L2-07"] = sum(Qin_day) - sum(Es_day)     # Q₂ = Q₁ − W = 33,8 kWh − 12,9 kWh = 20,9 kWh
Q_kk = [1.8, 2.6, 4.0, 3.1, 2.2]                   # L3-04: monthly heat demand, MWh
eps_kk = [3.4, 2.9, 2.4, 2.6, 3.1]                 # monthly coefficients of performance
Es_kk = [q / e for q, e in zip(Q_kk, eps_kk)]      # W = Q/ε per month, sum 4,995 MWh
a["fy3-11-L3-04"] = sum(Q_kk) / sum(Es_kk)         # ε_kausi = ΣQ/ΣW = 13,7 / 4,995 = 2,74 (plain mean of ε would be 2,88)
Q_vastus = 260 * 4.0                               # L3-05: Q = Pt = 260 W · 4,0 s = 1040 J
W_ilma = 125e3 * 0.0200 * (0.220 - 0.100)          # W = pAΔh = 125 000 Pa · 0,0200 m² · 0,120 m = 300 J
a["fy3-11-L3-05"] = (Q_vastus - W_ilma) / 1000     # ΔU = Q − pΔV = 740 J = 0,74 kJ (W/Q = 29 % ≈ 2/7, as for a diatomic gas)

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
