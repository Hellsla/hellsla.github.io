"""Numbers of the lesson text and inquiry.json for fy6-7, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Electrical energy E = P t; in kilowatts and hours it comes out in kWh,
1 kWh = 1000 W · 3600 s = 3,6 MJ. Mains 230 V (the effective value of the AC voltage), P = U I. Devices run at their
rated power for the time given; cost = price per kWh · E + fixed fees. Prints {id: number} as JSON."""
import json

a = {}
# --- Ydinajatus: equal energies, kettle 2,0 kW for 6 min and TV 100 W for 2,0 h (the (t, P) figure) ---
a["kettle-6min-kWh"] = 2.0 * 6 / 60                           # 2,0 kW · 0,10 h = 0,20 kWh
a["tv-2h-kWh"] = 0.100 * 2.0                                  # 0,100 kW · 2,0 h = 0,20 kWh
a["kWh-J"] = 1000 * 3600                                      # 1 kWh = 1000 W · 3600 s = 3 600 000 J = 3,6 MJ
a["kettle-I"] = 2000 / 230                                    # I = P : U = 2000 W : 230 V = 8,70 A
a["standby-1W-year-kWh"] = 0.001 * 24 * 365                   # 1 W all year: 0,001 kW · 8760 h = 8,76 kWh
a["sauna-once-kWh"] = 6.0 * 1.5                               # 6,0 kW · 1,5 h = 9,0 kWh

# --- worked example: floor heating 0,80 kW, 6 h 15 min a day, 30 days, 18 snt/kWh ---
t_ex = (6 + 15 / 60) * 30                                     # 6,25 h · 30 = 187,5 h
a["ex-t"] = t_ex
a["ex-E"] = 0.80 * t_ex                                       # 150 kWh
a["ex-cost"] = 0.18 * 0.80 * t_ex                             # 0,18 EUR/kWh · 150 kWh = 27,0 EUR
a["ex-check-day"] = 0.80 * 6.25                               # 5,0 kWh a day

# --- retrieval: lamp on 230 V takes 0,26 A ---
a["kertaus-P"] = 230 * 0.26                                   # 59,8 W, about 60 W
a["kertaus-wrong"] = 230 / 0.26                               # 885 W (divided): wrong option

# --- prediction 1 and the device table (one day) ---
devices = {"kettle": (2000, 12 / 60), "fridge": (100, 8.0), "tv": (100, 3.0), "led": (40, 5.0), "charger": (5, 2.0)}
for k, (P, t) in devices.items():
    a[f"day-{k}-kWh"] = P / 1000 * t                          # kettle 0,40; fridge 0,80; tv 0,30; led 0,20; charger 0,010 kWh
a["laitteet"] = a["day-kettle-kWh"]                           # the table's numeric question: 0,40 kWh

# --- prediction 2 and the saving table (one year) ---
a["save-standby-kWh"] = 0.0030 * 21 * 365                     # TV and set-top box 3,0 W, 21 h a day: 23,0 kWh
a["save-kettle-kWh"] = 2.0 * 10 / 60 * 365                     # kettle 2,0 kW, 10 min less a day: 121,7 kWh
a["save-led-kWh"] = 5 * (0.040 - 0.0050) * 3.0 * 365          # five 40 W -> 5,0 W, 3,0 h a day: 191,6 kWh
a["save-sauna-kWh"] = 6.0 * 1.5 * 52                          # one sauna fewer a week, 6,0 kW 1,5 h: 468 kWh
a["saastot"] = a["save-led-kWh"]                              # the table's numeric question: 190 kWh
for k in ("standby", "kettle", "led", "sauna"):
    a[f"save-{k}-EUR"] = 0.18 * a[f"save-{k}-kWh"]            # at 18 snt/kWh: 4,1 / 22 / 34 / 84 EUR

# --- error spotting: 2000 W · 15 min taken as kWh ---
a["virhe-wrong"] = 2000 * 15                                  # 30 000 (W · min, not kWh)
a["virhe-right"] = 2.0 * 15 / 60                              # 2,0 kW · 0,25 h = 0,50 kWh

# --- transfer: the bill from two meter readings ---
E_bill = 15589 - 15362                                        # 227 kWh
a["siirto-E"] = E_bill
a["siirto"] = (0.120 + 0.060) * E_bill + 9.00                 # 0,180 EUR/kWh · 227 kWh + 9,00 EUR = 49,86 EUR
a["siirto-mistake-fixed"] = 0.180 * E_bill                    # fixed fees forgotten: 40,86 EUR
a["siirto-mistake-transfer"] = 0.120 * E_bill + 9.00          # transfer price forgotten: 36,24 EUR

# --- check 2: hair dryer 1800 W, 10 min a day, 30 days ---
a["tarkistus-2"] = 1.8 * 10 / 60 * 30                         # 9,0 kWh
a["tarkistus-2-mistake-min"] = 1.8 * 0.10 * 30                # 10 min taken as 0,10 h: 5,4 kWh
a["tarkistus-2-mistake-W"] = 1800 * 10 / 60 * 30              # watts not turned into kilowatts: 9000

# --- exit ticket ---
a["exit-1"] = 2.0 * 3.6                                       # 2,0 kWh = 7,2 MJ
a["exit-2"] = 0.010 * 100                                     # 10 W · 100 h = 1,0 kWh
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
