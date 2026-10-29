"""Every answer in exercises.json for fy2-6, computed from the task data (python -I answers.py).
E = P t with t = 8760 h in a year; 1 GWh = 10^6 kWh, 1 TWh = 10^9 kWh. Prints {exercise id: number} as JSON on the last line."""
import json

h_year = 8760            # h in a year (365 d · 24 h)
a = {}
# Level 1: one formula, values given
a["fy2-6-L1-01"] = 2.5 * 168                # wind turbine, mean 2,5 MW for a week 168 h: E = 420 MWh
a["fy2-6-L1-02"] = 120 * 8.0                # hydro plant, 120 MW for 8,0 h: E = 960 MWh
a["fy2-6-L1-03"] = 1.6 * 24                 # OL3, 1,6 GW for 24 h: E = 38,4 GWh -> 38 GWh
a["fy2-6-L1-04"] = (20.2 + 0.9) / 79.9 * 100  # read off fy2-6/fi-bars: wind 20,2 TWh + solar 0,9 TWh = 21,1 TWh of 79,9 TWh = 0,2641 -> 26,4 %
a["fy2-6-L1-05"] = 4.0 * 3.5                # house solar panels, 4,0 kW for 3,5 h: E = 14 kWh
# Level 2: two steps or a conversion
P_ka = 0.32 * 25                            # wind farm: mean power 32 % of rated 25 MW = 8,0 MW
a["fy2-6-L2-01"] = P_ka * h_year / 1e3      # E = 8,0 MW · 8760 h = 70 080 MWh = 70,08 GWh -> 70 GWh
a["fy2-6-L2-02"] = 14e9 / 1.6e6             # hydro 14 TWh = 14·10^9 kWh : 1,6 GW = 1,6·10^6 kW -> 8750 h
a["fy2-6-L2-03"] = 31e9 / 12e6              # nuclear 31·10^9 kWh : 12·10^6 kWh per turbine = 2583 turbines -> 2600
a["fy2-6-L2-04"] = 1.6e6 * h_year / 5000 / 1e6   # OL3 at full power 1,6·10^6 kW · 8760 h = 14,0·10^9 kWh; : 5000 kWh = 2,80·10^6 households (millions)
# Level 3: reasoning
a["fy2-6-L3-01"] = 11 - 3.5 - 0.040 * 9.0   # demand 11 GW - nuclear 3,5 GW - wind 4,0 % of 9,0 GW = 7,14 GW
a["fy2-6-L3-02"] = 0.90 / 0.33              # same rated 600 MW, same year: energy ratio = 0,90 : 0,33 = 2,727
a["fy2-6-L3-03"] = 0.90 * 1600 / 0.11 / 1e3 # solar park replacing OL3 by annual energy: 0,11 P_a = 0,90 · 1600 MW -> P_a = 13 091 MW = 13,1 GW -> 13 GW
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
