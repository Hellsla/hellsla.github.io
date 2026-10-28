"""Every answer in exercises.json for fy2-6, computed from the task data (python -I answers.py).
E = P t with t = 8760 h in a year; 1 GWh = 10^6 kWh, 1 TWh = 10^9 kWh. Prints {exercise id: number} as JSON on the last line."""
import json

h_year = 8760            # h in a year (365 d · 24 h)
a = {}
# Level 1: one formula, values given
a["fy2-6-L1-01"] = 2500 * h_year / 1e6      # wind turbine, 2,5 MW = 2500 kW for 8760 h: E = 21 900 000 kWh = 21,9 GWh -> 22 GWh
a["fy2-6-L1-02"] = 120 * 8.0                # hydro plant, 120 MW for 8,0 h: E = 960 MWh
a["fy2-6-L1-03"] = 1.6 * 24                 # OL3, 1,6 GW for 24 h: E = 38,4 GWh -> 38 GWh
a["fy2-6-L1-04"] = 20.2 / 79.9 * 100        # wind share of production: 20,2 TWh : 79,9 TWh = 0,2528 -> 25 %
a["fy2-6-L1-05"] = 31e9 / h_year / 1e6      # nuclear 31 TWh = 31·10^9 kWh in 8760 h: P = 3 538 813 kW = 3,54 GW -> 3,5 GW
# Level 2: two steps or a conversion
P_sol = 95e6 / h_year                       # solar park: 95 GWh = 95·10^6 kWh : 8760 h = 10 845 kW
a["fy2-6-L2-01"] = P_sol / 100e3 * 100      # share of rated 100 MW = 100 000 kW: 0,1085 -> 11 %
a["fy2-6-L2-02"] = 14e9 / 1.6e6             # hydro 14 TWh = 14·10^9 kWh : 1,6 GW = 1,6·10^6 kW -> 8750 h
a["fy2-6-L2-03"] = 31e9 / 12e6              # nuclear 31·10^9 kWh : 12·10^6 kWh per turbine = 2583 turbines -> 2600
a["fy2-6-L2-04"] = 1.6e6 * h_year / 5000 / 1e6   # OL3 at full power 1,6·10^6 kW · 8760 h = 14,0·10^9 kWh; : 5000 kWh = 2,80·10^6 households (millions)
# Level 3: reasoning
a["fy2-6-L3-01"] = 11 - 3.5 - 0.040 * 9.0   # demand 11 GW - nuclear 3,5 GW - wind 4,0 % of 9,0 GW = 7,14 GW
a["fy2-6-L3-02"] = 0.90 / 0.33              # same rated 600 MW, same year: energy ratio = 0,90 : 0,33 = 2,727
a["fy2-6-L3-03"] = 0.90e9 / 1.6e6           # solar 0,90 TWh = 0,90·10^9 kWh : 1,6·10^6 kW = 562,5 h -> 560 h
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
