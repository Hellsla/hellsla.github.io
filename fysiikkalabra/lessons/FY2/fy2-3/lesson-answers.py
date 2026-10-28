"""Numbers of the lesson text and inquiry.json for fy2-3, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Prints {id: number} as JSON on the last line."""
import json

KWH = 1000 * 3600
YEAR_H = 365 * 24
PRICE = 0.20
a = {}
# Prediction: hair dryer 1800 W for 5,0 min against a lamp 10 W for 24 h
a["inq-kuivain-MJ"] = 1800 * 300 / 1e6                # 540 000 J = 0,54 MJ
a["inq-lamppu-MJ"] = 10 * 86400 / 1e6                 # 864 000 J = 0,864 MJ
a["inq-lamppu-tunnit"] = 1800 * 300 / 10 / 3600        # t = E : P = 540 000 J : 10 W = 54 000 s = 15 h
# Table of the meter readings (kJ at 60 s): kettle 2000 W, toaster 1000 W, television 80 W
a["inq-vedenkeitin-60s-kJ"] = 2000 * 60 / 1000        # 120 kJ
a["inq-tosteri-60s-kJ"] = 1000 * 60 / 1000            # 60 kJ
a["inq-tv-60s-kJ"] = 80 * 60 / 1000                   # 4,8 kJ
a["inq-tosteri-teho"] = (60e3 - 20e3) / (60 - 20)     # 40 000 J : 40 s = 1000 W
# Worked example: television 80 W, 4,0 h per day for 30 days, 20 snt/kWh
t_h = 4.0 * 30                                        # 120 h
e_kwh = 0.080 * t_h                                   # 9,6 kWh
a["esim-aika-h"] = t_h
a["esim-energia-kWh"] = e_kwh
a["esim-hinta-eur"] = e_kwh * PRICE                   # 1,92 EUR
a["esim-energia-J"] = 80 * t_h * 3600                 # 34 560 000 J = 34,56 MJ
a["kWh-J"] = 1000 * 3600                              # 1 kWh = 3 600 000 J
# Transfer: standby 2,5 W for a year
a["inq-siirto"] = 2.5 / 1000 * YEAR_H                 # 0,0025 kW · 8760 h = 21,9 kWh
a["inq-siirto-ilman-muunnosta"] = 2.5 * YEAR_H        # mistake: W not converted to kW = 21 900
a["inq-siirto-hinta"] = 2.5 / 1000 * YEAR_H * PRICE   # 4,38 EUR
a["inq-siirto-365h"] = 2.5 / 1000 * 365               # mistake: 365 h instead of 365 d = 0,9125
# Check 2: washing machine 1,2 kWh in 90 min
a["inq-check2"] = 1.2 * KWH / (90 * 60)               # 4 320 000 J : 5400 s = 800 W
a["inq-check2-ilman-muunnosta"] = 1.2 / 90            # mistake: 1,2 kWh : 90 min
# Lamp comparison used in the text: 10 W 24 h in kWh
a["text-lamppu-kWh"] = 0.010 * 24                     # 0,24 kWh
a["text-kuivain-kWh"] = 1.8 * 5 / 60                  # 0,15 kWh
# Power plant against a kettle: Olkiluoto 3, 1600 MW, in kettles of 2000 W
a["text-ol3-keittimet"] = 1600e6 / 2000               # 800 000 kettles
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
