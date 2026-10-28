"""Every answer in exercises.json for fy2-8, computed from the task data (python -I answers.py).
Emission m = e · E with e from the lesson's table (IPCC AR5 WG3 Annex III medians, g CO2-eq/kWh); petrol and diesel
combustion factors in g/MJ (IPCC 2006 default values). Prints {exercise id: number} as JSON on the last line."""
import json

e_kivihiili, e_kaasu, e_biomassa, e_katto, e_vesi, e_ydin, e_tuuli = 820, 490, 230, 41, 24, 12, 12   # g/kWh, lesson table
a = {}
# Level 1: one formula, values given
a["fy2-8-L1-01"] = e_vesi * 3000 / 1e3                 # hydro: m = 24 g/kWh · 3000 kWh = 72 000 g -> 72 kg
a["fy2-8-L1-02"] = e_kivihiili * 3.0 / 1e3             # coal sauna: m = 820 · 3,0 kWh = 2460 g -> 2,5 kg
a["fy2-8-L1-03"] = e_tuuli * 18                        # wind, electric car 100 km: m = 12 · 18 kWh = 216 g -> 220 g
a["fy2-8-L1-04"] = e_kaasu / e_katto                  # same energy, gas vs rooftop PV: 490 : 41 = 11,95 -> 12 times
a["fy2-8-L1-05"] = e_kaasu * 2.4 / 1e3                 # gas, laundry: m = 490 · 2,4 kWh = 1176 g -> 1,2 kg
# Level 2: a conversion or a rearrangement
a["fy2-8-L2-01"] = e_biomassa * 2.0e6 / 1e6            # biomass, 2,0 GWh = 2,0·10^6 kWh: m = 230 · 2,0·10^6 g = 4,6·10^8 g -> 460 t
a["fy2-8-L2-02"] = (e_kivihiili - e_tuuli) * 3600 / 1e6   # switch coal -> wind, 3600 kWh: saving (820 − 12) · 3600 g = 2 908 800 g -> 2,9 t
a["fy2-8-L2-03"] = 12e6 / e_kaasu                      # 12 t = 12·10^6 g; E = m / e = 12·10^6 g / (490 g/kWh) = 24 490 kWh -> 24 000 kWh
a["fy2-8-L2-04"] = 69 * 3.6                            # petrol 69 g/MJ · 3,6 MJ/kWh = 248,4 g/kWh -> 250 g/kWh
# Level 3: reasoning or an unfamiliar context
m_bensa = 6.0 * 32 * 69                                # petrol car 100 km: 6,0 l · 32 MJ/l = 192 MJ; · 69 g/MJ = 13 248 g
a["fy2-8-L3-01"] = m_bensa / 18                        # equal emission with an electric car (18 kWh): e = 13 248 g / 18 kWh = 736 g/kWh -> 740 g/kWh
A_bio_ha = 100 / 0.010                                 # land use: 100 GWh : 0,010 GWh/ha = 10 000 ha of energy crops
A_bio = A_bio_ha * 0.01                                # 1 ha = 0,01 km^2: 100 km^2
A_sol = 100 / 0.50 * 0.01                              # solar park 100 : 0,50 = 200 ha = 2,0 km^2
a["fy2-8-L3-02"] = A_bio / A_sol                       # ratio of areas: 100 : 2,0 = 50 times
m_bussi = 30 * 36 * 74 / 25                            # bus per passenger: 30 l · 36 MJ/l · 74 g/MJ = 79 920 g, / 25 = 3196,8 g
a["fy2-8-L3-03"] = m_bensa / m_bussi                   # car alone / bus per passenger = 13 248 / 3196,8 = 4,14 -> 4,1
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
