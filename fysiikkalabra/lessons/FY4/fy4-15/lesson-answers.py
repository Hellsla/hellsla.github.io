"""Numbers of the lesson text and inquiry.json for fy4-15, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. g = 9,81 m/s², water 1000 kg/m³, air 1,25 kg/m³ (the chapter's value; the power
curve's own Cp uses 1,225 kg/m³). Prints {id: number} as JSON.

Real data (sources in inquiry.json source_note):
- Vestas V82-1.65 MW power curve, rotor diameter 82 m: NREL Turbine Archive (nrel.github.io/turbine-models),
  file Onshore/VestasV82_1.65MW_82.csv, read 2026-10-30.
- Imatra 192 MW, head 24 m; Tainionkoski 62 MW, head 7,8 m: Fortum, Vuoksen vesistön voimalaitokset (fortum.com),
  read 2026-10-30. The Vuoksi's annual mean flow about 600 m³/s: Kaakkois-Suomen elinvoimakeskus, press release
  29.4.2026 (STT Info)."""
import json, math

g, rho_w, rho_a = 9.81, 1000.0, 1.25
a = {}
# The V82 power curve (kW) used in the table and the figures
V82 = {3: 0, 4: 28, 5: 144, 6: 309, 7: 511, 8: 758, 9: 1017, 10: 1285, 11: 1504, 12: 1637, 13: 1650, 14: 1650,
       16: 1650, 18: 1650, 20: 1650}
a["v82-ratio-5-10"] = V82[10] / V82[5]                 # pred-1, tuuli-data: 1285 : 144 = 8,92 ("lähes yhdeksän")
a["v82-ratio-4-8"] = V82[8] / V82[4]                   # 758 : 28 = 27 (low winds: the share η grows, text does not use)
a["v82-ratio-6-12"] = V82[12] / V82[6]                 # 1637 : 309 = 5,3 (the generator's limit nears)
a["cube-2"] = 2 ** 3                                   # v doubles: 2³ = 8
A82 = math.pi * 41.0 ** 2
a["v82-A"] = A82                                       # A = π (41 m)² = 5281 m²
for v in (5, 8, 10):
    Pw = 0.5 * rho_a * A82 * v ** 3
    a[f"v82-Pwind-{v}"] = Pw                           # wind power through the rotor: 5 m/s 412,6 kW; 8 m/s 1690 kW; 10 m/s 3301 kW
    a[f"v82-eta-{v}"] = V82[v] * 1e3 / Pw               # share turned into electricity: 0,349; 0,449; 0,389
a["v82-eta-max-data"] = 0.461                           # the archive's Cp at 7 m/s (ρ 1,225): "alle puolet"
a["betz"] = 16 / 27                                     # the theoretical upper limit 0,593 ≈ 59 %
# Figure "tehokayra": the model curve ½ η ρ A v³ with η = 0,45 reaches 1650 kW at
a["fig-v-rated"] = (1650e3 / (0.45 * 0.5 * rho_a * A82)) ** (1 / 3)   # 10,4 m/s (the real curve bends earlier: the generator limits)
# Hydro: Vuoksi, the same water through Tainionkoski and Imatra
a["vuoksi-P-ratio"] = 192 / 62                          # 3,10
a["vuoksi-h-ratio"] = 24 / 7.8                          # 3,08
a["imatra-P-per-h"] = 192 / 24                          # 8,0 MW/m
a["tainio-P-per-h"] = 62 / 7.8                          # 7,9 MW/m
a["imatra-Q-full"] = 192e6 / (0.90 * rho_w * g * 24)    # flow at full power, η = 0,90: 906 m³/s
a["tainio-Q-full"] = 62e6 / (0.90 * rho_w * g * 7.8)    # 900 m³/s: about the same water
a["imatra-P-mean"] = 0.90 * rho_w * 600 * g * 24 / 1e6  # at the mean flow 600 m³/s: about 127 MW (text: "noin 130 MW")
a["imatra-Ep-per-m3"] = rho_w * 1.0 * g * 24            # one cubic metre falling 24 m: 235 kJ
# The air's kinetic energy per kilogram at 10 m/s and the equal fall height (theory comparison)
a["air-Ek-per-kg-10"] = 0.5 * 10 ** 2                   # 50 J/kg
a["water-Ep-per-kg-24"] = g * 24                        # 235 J/kg
# Worked example: rotor diameter 120 m, v = 9,0 m/s, η = 0,45
A = math.pi * 60.0 ** 2
a["ex-A"] = A                                           # 11 309,7 m²
a["ex-Pwind"] = 0.5 * rho_a * A * 9.0 ** 3              # 5,153 MW
a["ex-P"] = 0.45 * 0.5 * rho_a * A * 9.0 ** 3           # 2,319 MW ≈ 2,3 MW
a["ex-check-v8"] = 0.45 * 0.5 * rho_a * A * 8.0 ** 3    # Järkevyys: at 8,0 m/s 1,63 MW, at 10 m/s:
a["ex-check-v10"] = 0.45 * 0.5 * rho_a * A * 10.0 ** 3  # 3,18 MW
a["ex-check-area"] = (120 / 82) ** 2                   # Järkevyys: the area is 2,14 times the V82 rotor's
a["ex-check-v82"] = 1017 * (120 / 82) ** 2 / 1e3       # V82 at 9 m/s 1017 kW scaled by area: 2,18 MW
# siirto: pumped storage, head 1,40 km, P = 75,0 MW, η = 0,850: Q = P / (η ρ g h)
P, h, eta = 75.0e6, 1400.0, 0.850
a["siirto"] = P / (eta * rho_w * g * h)                 # 6,425 m³/s
a["siirto-km"] = P / (eta * rho_w * g * 1.40)           # mistake: h in km: 6425
a["siirto-noeta"] = P / (rho_w * g * h)                 # mistake: η forgotten: 5,461
a["siirto-times-eta"] = eta * P / (rho_w * g * h)       # mistake: multiplied by η: 4,642
a["siirto-imatra-Q75"] = 75 / 192 * a["imatra-Q-full"]  # Järkevyys: Imatra would need about 354 m³/s for 75 MW
a["siirto-h-ratio"] = 1400 / 24                        # the head is 58 times Imatra's
a["check3-ratio"] = (8 / 6) ** 3                       # check-3: (8 : 6)³ = 2,37; (8 : 6)² = 1,78
a["siirto-imatra-ratio"] = a["imatra-Q-full"] / a["siirto"]   # Järkevyys: Imatra's water about 140 times more
# check-2: small hydro, h = 8,0 m, Q = 12 m³/s, η = 0,85
a["check2"] = 0.85 * rho_w * 12 * g * 8.0 / 1e3         # 800,5 kW
a["check2-noeta"] = rho_w * 12 * g * 8.0 / 1e3          # 941,8 kW
a["check2-nog"] = 0.85 * rho_w * 12 * 8.0 / 1e3         # 81,6 kW
# error-spotting (etsi-virhe): small plant P = 0,85 · 1000 · 2,0 · 9,81 · 6,0 W = 100 kW; one day 24 h
a["virhe-P"] = 0.85 * rho_w * 2.0 * g * 6.0 / 1e3       # 100,06 kW
a["virhe-E-day"] = a["virhe-P"] * 24                    # 2401 kWh ≈ 2,4 MWh
# exit ticket: P_s = 50 MW, η = 0,90 → P_o = 55,6 MW, losses 5,6 MW; same P and η, double head → half the flow
a["exit-Po"] = 50 / 0.90
a["exit-loss"] = 50 / 0.90 - 50
print(json.dumps(a))
