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
print(json.dumps(a))
