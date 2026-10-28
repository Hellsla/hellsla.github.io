"""Every answer in exercises.json for fy2-7, computed from the task data (python -I answers.py).
Loss share p of the energy sent, delivered E_perille = eta E_lahto with eta = 1 - p, E_havio = E_lahto - E_perille, P = E : t.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy2-7-L1-01"] = 500 * (1 - 0.040)                  # sent 500 MWh, loss 4,0 %: delivered = 0,960 · 500 MWh = 480 MWh
a["fy2-7-L1-02"] = 360 - 327                          # district heat sent 360 MWh, delivered 327 MWh: loss = 33 MWh
a["fy2-7-L1-03"] = 76.8 / 80.0 * 100                  # sent 80,0 MWh, delivered 76,8 MWh: eta = 0,960 = 96,0 %
a["fy2-7-L1-04"] = 125 * (1 - 0.040)                  # power sent 125 MW, loss 4,0 %: delivered 120,0 MW
a["fy2-7-L1-05"] = 2.5 * 24                           # loss power 2,5 kW for 24 h: E = P t = 60 kWh
# Level 2: a conversion, two steps or a rearrangement
a["fy2-7-L2-01"] = 960 / (1 - 0.040)                  # delivered 960 MWh, loss 4,0 % of sent: sent = 960 / 0,960 = 1000 MWh
a["fy2-7-L2-02"] = 1.82 / 0.91 * 1000                 # delivered 1,82 GWh, eta 91 %: sent = 2,00 GWh = 2000 MWh
a["fy2-7-L2-03"] = 83 * 0.04                          # 83 TWh consumption, losses 4 % of it: 3,32 TWh -> 3,3 TWh
P_send = 40.0 / 0.910                                 # building needs 40,0 kW, loss 9,0 % of sent: P_sent = 43,96 kW
a["fy2-7-L2-04"] = round(P_send * 24, -1)             # E = P t = 43,96 kW · 24 h = 1055 kWh -> 1050 kWh (three figures)
# Level 3: reasoning and combining ideas
a["fy2-7-L3-01"] = round(600 / 0.91 - 600 / 0.94)     # needs 600 MWh; loss 9,0 % vs 6,0 %: 659,3 - 638,3 = 21,0 MWh saved
a["fy2-7-L3-02"] = (10 + 30) / 1000 * 100             # 1,00 GW = 1000 MW sent; losses 10 MW + 30 MW = 40 MW: 4,0 % of the energy sent
a["fy2-7-L3-03"] = round(150 * 7 * 24 / 1000, 1)      # loss power 150 kW for a week (168 h): 25 200 kWh = 25,2 MWh
print(json.dumps(a))
