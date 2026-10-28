"""Numbers of the lesson text and inquiry.json for fy2-8, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Prints {id: number} as JSON on the last line."""
import json

a = {}
# Lesson text
a["ratio-coal-nuclear"] = 820 / 12                    # coal / nuclear and wind (12 g/kWh): about 68, "noin 70-kertainen"
a["example-m-g"] = 490 * 4800                         # example: m = 490 g/kWh · 4800 kWh = 2 352 000 g
a["example-m-t"] = 490 * 4800 / 1e6                   # = 2,352 t -> 2,4 t
a["example-check"] = 500 * 5000 / 1e6                 # rounded check: 2,5 t
a["example-wind-kg"] = 12 * 4800 / 1e3                # same electricity by wind: 57,6 kg -> 58 kg
a["example-gas-wind"] = 490 / 12                      # gas / wind = 40,8 -> 41
a["kwh-in-mj"] = 1000 * 3600 / 1e6                    # 1 kWh = 1000 W · 3600 s = 3,6 MJ
# Inquiry numbers
a["inq-aineisto-kg"] = 820 * 1000 / 1e3               # 1000 kWh by coal: 820 000 g = 820 kg
a["inq-virhe-g"] = 12 * 3600                          # error-spotting: m = 12 g/kWh · 3600 kWh = 43 200 g
a["inq-virhe-wrong"] = 3600 / 12                      # the student's E : e = 300
a["inq-siirto-t"] = 490 * 100e6 / 1e6                 # 100 GWh = 100·10^6 kWh by gas: 4,9·10^10 g = 49 000 t
a["inq-siirto-wind-t"] = 12 * 100e6 / 1e6             # the same by wind: 1200 t (model answer of perustele)
a["inq-siirto-ratio"] = 490 / 12                      # 41
a["inq-trip-l"] = 120 / 100 * 6.0                     # 120 km: 7,2 l
a["inq-trip-mj"] = 7.2 * 32                           # 230,4 MJ
a["inq-trip-kg"] = 7.2 * 32 * 69 / 1e3                # 15 898 g = 15,9 kg -> 16 kg
a["inq-trip-kg-per-l"] = 32 * 69 / 1e3              # check: one litre 2208 g = 2,2 kg
a["inq-trip-check-kg"] = 7.2 * 2.2                   # 7,2 l · 2,2 kg = 15,84 kg -> 16 kg
a["inq-siirto-gwh-slip-t"] = 490 * 100 / 1e6         # mistake: GWh kept: 49 000 g = 0,049 t
a["inq-hake-ratio"] = 400 / 50                        # transport: 400 km vs 50 km, eight times the distance
a["inq-trip-100km-kg"] = 6.0 * 32 * 69 / 1e3          # mistake: only 100 km, 13,2 kg
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
