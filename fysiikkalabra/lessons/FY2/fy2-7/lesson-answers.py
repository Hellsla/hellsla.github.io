"""Numbers of the lesson text and inquiry.json for fy2-7, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
import json

a = {}
# Worked example (lesson.md): 245 MWh sent, loss 9,0 %
a["example-perille"] = 245 * (1 - 0.090)              # delivered = 0,910 · 245 MWh = 222,95 MWh -> 223 MWh
a["example-havio"] = 245 - 245 * (1 - 0.090)          # loss = 245 MWh - 222,95 MWh = 22,05 MWh -> 22,1 MWh
a["example-tarkistus"] = 0.09 * 245                   # check: 0,090 · 245 MWh = 22,05 MWh
# Inquiry: Energiateollisuus 2024 (district heat procured 36,0 TWh, used 32,7 TWh; electricity 83 TWh with 4 % losses)
a["inq-kl-havio"] = 36.0 - 32.7                       # district heat loss = 3,3 TWh
a["inq-kl-prosentti"] = (36.0 - 32.7) / 36.0 * 100    # 3,3 / 36,0 = 9,17 % -> 9,2 %
a["inq-kl-vaarin"] = (36.0 - 32.7) / 32.7 * 100       # mistake: divided by the delivered 32,7 TWh: 10,1 %
a["inq-kl-erotus"] = 36.0 - 32.7                      # mistake: the loss in TWh, not a percentage
a["inq-sahko-havio"] = 83 * 0.04                      # electricity: 4 % of 83 TWh = 3,32 TWh
# Inquiry: the voltage table (invented example, 100 MW, loss 8,0 / 0,26 / 0,020 MW)
a["inq-jannite-20"] = 8.0 / 100 * 100                 # 20 kV: 8,0 MW of 100 MW = 8,0 %
a["inq-jannite-400"] = 0.020 / 100 * 100              # 400 kV: 0,020 %
a["inq-jannite-vaarin"] = 8.0 / 0.020                 # mistake: the ratio of losses 400, not a percentage
# Etsi virhe: sent 500 MWh, loss 4 %
a["inq-virhe-oikea"] = 500 * (1 - 0.04)               # 480 MWh
a["inq-virhe-vaarin"] = 500 - 4                       # mistake: subtracted 4 MWh, 496 MWh
a["inq-virhe-havio"] = 500 * 0.04                     # loss = 20 MWh
# Transfer: battery, 12,0 kWh charged, 10,2 kWh discharged
a["inq-siirto"] = (12.0 - 10.2) / 12.0 * 100          # loss share = 1,8 / 12,0 = 15 %
a["inq-siirto-hyoty"] = 10.2 / 12.0 * 100             # mistake: the efficiency 85 %
a["inq-siirto-vaarin"] = (12.0 - 10.2) / 10.2 * 100   # mistake: divided by 10,2 kWh, 17,6 %
# Check 2: delivered 455 MWh, eta 91 %
a["inq-check2"] = 455 / 0.91                          # sent = 500 MWh
a["inq-check2-vaarin"] = 455 * 0.91                   # mistake: multiplied, 414 MWh
a["inq-check2-lisays"] = 455 * 1.09                   # mistake: added 9 %, 496 MWh
# Exit ticket
a["exit-1"] = 800 * (1 - 0.040)                       # 768 MWh
a["exit-3"] = 2.0 * 24                                # 48 kWh
print(json.dumps(a))
