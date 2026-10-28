"""Numbers of lesson.md and inquiry.json for fy2-6 (python -I lesson-answers.py); prints {id: value} as JSON."""
import json

h_year = 8760                                   # h in a year
a = {}
a["esim-Pka_kW"] = 14e6 / h_year                # example: 14 GWh = 14·10^6 kWh : 8760 h = 1598 kW -> 1,6 MW
a["esim-osuus"] = 14e6 / h_year / 5000          # 1598 kW : 5000 kW = 0,32
a["esim-nimellisenergia_GWh"] = 5000 * h_year / 1e6   # check: 5000 kW · 8760 h = 43,8 GWh
a["tuuli-keskiteho_GW"] = 20.2e9 / h_year / 1e6 # wind 2024: 20,2·10^9 kWh : 8760 h = 2,306 GW -> 2,3 GW
a["data-fi-muut_TWh"] = 79.9 - (31 + 20.2 + 14.1 + 9.5 + 3.4 + 0.9)   # other sources: total minus the listed ones = 0,8 TWh
a["maailma-keskiteho_GW"] = 3.0e4 * 1e3 / h_year   # world ~3·10^4 TWh/yr = 3·10^7 GWh : 8760 h = 3425 GW
a["virhe-suhde"] = 14 * h_year / (3.0e4 * 1e3 / h_year)   # 14 GWh·8760 h = 122 640 "GW" : 3425 GW = 36 ("kymmeniä kertoja")
# example week (invented, rounded; daily mean powers in GW): consumption, nuclear, wind
kul = [11.3, 11.9, 12.6, 13.1, 12.7, 11.4, 10.8]
ydin = [4.3] * 7
tuuli = [6.4, 5.1, 2.2, 0.4, 1.1, 3.6, 5.8]
a["viikko-muut-to_GW"] = kul[3] - ydin[3] - tuuli[3]   # Thursday: 13,1 - 4,3 - 0,4 = 8,4 GW from other sources
a["viikko-muut-ma_GW"] = kul[0] - ydin[0] - tuuli[0]   # Monday: 11,3 - 4,3 - 6,4 = 0,6 GW
a["viikko-tuuli-max-osuus"] = max(tuuli) / 8          # windiest day 6,4 GW of about 8 GW nominal = 0,8
a["viikko-tuuli-min-osuus"] = min(tuuli) / 8          # calmest day 0,4 GW of about 8 GW nominal = 0,05
a["tuulet-ol3"] = 1600 / 5.0                    # 1600 MW : 5,0 MW = 320 turbines (nominal power)
a["ol3-max_TWh"] = 1600e3 * h_year / 1e9        # OL3 1600 MW = 1600·10^3 kW for 8760 h = 14,0 TWh
a["ol3-osuus"] = 1600e3 * h_year / 1e9 / 79.9 * 100   # 14,0 TWh : 79,9 TWh = 17,5 %
a["tarkistus-2_GWh"] = 1.0e3 * h_year / 1e6     # check 2: 1,0 MW = 1000 kW for 8760 h = 8,76 GWh
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
