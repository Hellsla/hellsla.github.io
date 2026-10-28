"""Numbers of lesson.md and inquiry.json for fy2-6 (python -I lesson-answers.py); prints {id: value} as JSON."""
import json

h_year = 8760                                   # h in a year
a = {}
a["esim-Pka_kW"] = 14e6 / h_year                # example: 14 GWh = 14·10^6 kWh : 8760 h = 1598 kW -> 1,6 MW
a["esim-osuus"] = 14e6 / h_year / 5000          # 1598 kW : 5000 kW = 0,32
a["esim-nimellisenergia_GWh"] = 5000 * h_year / 1e6   # check: 5000 kW · 8760 h = 43,8 GWh
a["tuuli-keskiteho_GW"] = 20.2e9 / h_year / 1e6 # wind 2024: 20,2·10^9 kWh : 8760 h = 2,306 GW -> 2,3 GW
a["tuulet-ol3"] = 1600 / 5.0                    # 1600 MW : 5,0 MW = 320 turbines (nominal power)
a["ol3-max_TWh"] = 1600e3 * h_year / 1e9        # OL3 1600 MW = 1600·10^3 kW for 8760 h = 14,0 TWh
a["ol3-osuus"] = 1600e3 * h_year / 1e9 / 79.9 * 100   # 14,0 TWh : 79,9 TWh = 17,5 %
a["tarkistus-2_GWh"] = 1.0e3 * h_year / 1e6     # check 2: 1,0 MW = 1000 kW for 8760 h = 8,76 GWh
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
