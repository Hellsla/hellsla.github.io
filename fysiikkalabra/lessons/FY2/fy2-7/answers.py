"""Every answer in exercises.json for fy2-7, computed from the task data (python -I answers.py).
Loss share p of the energy sent, delivered E_perille = eta E_lahto with eta = 1 - p, E_havio = E_lahto - E_perille, P = E : t.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy2-7-L1-01"] = 500 * (1 - 0.040)                  # sent 500 MWh, loss 4,0 %: delivered = 0,960 · 500 MWh = 480 MWh
a["fy2-7-L1-02"] = 0.09 * 360                         # loss share 9 % read off fy2-7/sankey; 0,09 · 360 MWh = 32,4 MWh (about 32 MWh)
a["fy2-7-L1-03"] = 76.8 / 80.0 * 100                  # sent 80,0 MWh, delivered 76,8 MWh: eta = 0,960 = 96,0 %
a["fy2-7-L1-04"] = 125 * (1 - 0.040)                  # power sent 125 MW, loss 4,0 %: delivered 120,0 MW
a["fy2-7-L1-05"] = 2.5 * 24                           # loss power 2,5 kW for 24 h: E = P t = 60 kWh
# Level 2: a conversion, two steps or a rearrangement
E_sent = 600 / (1 - 0.20)                             # delivered 600 MWh, loss 20 % of sent: sent = 600 / 0,80 = 750 MWh
a["fy2-7-L2-01"] = E_sent - 600                       # loss = 750 MWh - 600 MWh = 150 MWh (wrong base: 0,20 · 600 = 120 MWh)
a["fy2-7-L2-02"] = 1.20 / 0.80 * 1000                 # delivered 1,20 GWh = 1200 MWh, eta 80 %: sent = 1500 MWh (wrong: 1,2 · 1200 = 1440 MWh)
E_loss = 2.40 * 1e6 * 0.040                           # 2,40 TWh = 2 400 000 MWh sent, loss 4,0 %: 96 000 MWh in a year
a["fy2-7-L2-03"] = round(E_loss / 8760, 0)            # mean loss power = 96 000 MWh : 8760 h = 10,96 MW -> 11 MW
P_send = 40.0 / 0.80                                  # building needs 40,0 kW, loss 20 % of sent: P_sent = 50,0 kW
a["fy2-7-L2-04"] = P_send * 24                        # E = P t = 50,0 kW · 24 h = 1200 kWh (wrong: 1,2 · 40,0 · 24 = 1152 kWh)
# Level 3: reasoning and combining ideas
a["fy2-7-L3-01"] = round(600 / 0.91 - 600 / 0.94)     # needs 600 MWh; loss 9,0 % vs 6,0 %: 659,3 - 638,3 = 21,0 MWh saved
a["fy2-7-L3-02"] = 500 * 0.910 - 520 * 0.850          # A: 500 MWh at 91,0 % -> 455,0; B: 520 MWh at 85,0 % -> 442,0; A delivers 13,0 MWh more
a["fy2-7-L3-03"] = round(150 * 8760 / 1000 / 20)      # loss 150 kW for 8760 h = 1314 MWh; one house 20 MWh/year: 65,7 -> 66 houses
# Exercise bank additions (L1-06 and L2-07 are multiple choice: no number)
a["fy2-7-L1-07"] = (250 - 238) / 250 * 100            # sent 250 MWh, delivered 238 MWh: loss 12 MWh = 4,8 %
a["fy2-7-L1-08"] = 800 - 728                          # power sent 800 kW, delivered 728 kW: loss power 72 kW
a["fy2-7-L2-05"] = (2650 - 2395) / 2650 * 100         # sent 820+760+640+430 = 2650 MWh, delivered 745+692+577+381 = 2395 MWh: 255/2650 = 9,62 %
a["fy2-7-L2-06"] = 0.25 / 4                           # loss power quarters when voltage doubles (16, 4,0, 1,0, 0,25 MW): 320 kV -> 0,0625 MW
E_house = 0.50 * 2.4 * 5000                           # option A: walls 2,4 kW cut 50 % = 1,2 kW for 5000 h = 6000 kWh (B 3600, C 4500)
a["fy2-7-L3-04"] = E_house / 0.910 / 1000             # plant must send 6,0 MWh : 0,910 = 6,593 MWh less
E_in = 7 * 18 + 5 * 42 + 7 * 50 + 5 * 66              # energy sent in a day: 126 + 210 + 350 + 330 = 1016 MWh
E_lo = 0.015 * 7 * 18 + 0.035 * 5 * 42 + 0.042 * 7 * 50 + 0.055 * 5 * 66   # losses 1,89 + 7,35 + 14,70 + 18,15 = 42,09 MWh
a["fy2-7-L3-05"] = E_lo / E_in * 100                  # 42,09 / 1016 = 4,14 %
print(json.dumps(a))
