"""FY2 Esimerkkikoe: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json; `python scripts/practice.py check FY2/koe` compares them."""
import json

out = {}
# fy2-k1: Osa 1 items with numbers
out["k1-c"] = 15 * 3600                     # J in 15 Wh
out["k1-d"] = (5 * 10, 60 * 1)              # Wh: LED 10 h, incandescent 1 h
out["k1-e"] = 100 * (400 - 120) / 400       # %
out["k1-i"] = 0.025 * 500                   # MW
# fy2-k2: charging an electric car
cap, P2, eta2, price = 64.0, 11.0, 0.90, 0.12
E_bat = cap * (0.80 - 0.20); E_grid = E_bat / eta2
out["fy2-k2-a-bat"] = round(E_bat, 1); out["fy2-k2-a-grid"] = round(E_grid, 1)
out["fy2-k2-b"] = round(E_grid / P2, 2); out["k2-b-min"] = round((E_grid / P2 % 1) * 60)
out["fy2-k2-c"] = round(E_grid * price, 2)
out["k2-d-loss"] = round(E_grid - E_bat, 1)
# fy2-k3: pellets and oil
need = 18000.0                              # kWh delivered to the house in a year
Hp, Ho, ep, eo = 17e6, 42.7e6, 0.85, 0.90   # J/kg
kWh = 3.6e6
out["fy2-k3-a"] = round(need / ep * kWh / Hp, 0)
out["fy2-k3-b"] = round(need / eo * kWh / Ho, 0)
out["k3-fuel-energy"] = (round(need / ep), round(need / eo))
# fy2-k4: solar panels
M4 = [40, 150, 420, 680, 870, 880, 860, 700, 440, 210, 60, 15]   # kWh per month
out["fy2-k4-b-E"] = sum(M4); out["fy2-k4-b-share"] = round(100 * sum(M4) / 15000, 1)
out["fy2-k4-c-P"] = round(sum(M4) / 8760, 2); out["fy2-k4-c-f"] = round(100 * sum(M4) / 8760 / 6.0, 1)
out["k4-winter"] = sum(M4[i] for i in (0, 1, 10, 11))
# fy2-k5: data centre
P5, rec, home = 20.0, 0.70, 15000.0
E5 = P5 * 8760 / 1000                        # GWh
out["fy2-k5-a"] = round(E5, 1)
out["fy2-k5-c"] = round(rec * E5 * 1e6 / home, -2)
# fy2-k6: a winter day
prod = {"03": (4400, 5600, 1300, 2400), "09": (4400, 2100, 2600, 3200), "18": (4400, 900, 2900, 3400)}
use = {"03": 10200, "09": 12800, "18": 13500}
for k, p in prod.items(): out[f"k6-net-import-{k}"] = use[k] - sum(p)
out["fy2-k6-a-03"] = round(100 * 5600 / sum(prod["03"]), 1); out["fy2-k6-a-18"] = round(100 * 900 / sum(prod["18"]), 1)
out["fy2-k6-b"] = round(2900 * 24 / 1000, 1)  # GWh
out["k6-b-homes"] = round(2900 * 24 * 1000 / 15000)
out["fy2-k6-d-wind"] = round(9000 * 0.30 * 8760 / 1e6, 1); out["fy2-k6-d-nuc"] = round(4400 * 0.90 * 8760 / 1e6, 1)   # TWh
# fy2-k7: cyclist and e-bike
Pm, t7, eta7, banana = 150.0, 3600.0, 0.25, 0.45e6
E_food = Pm * t7 / eta7
out["fy2-k7-b"] = round(E_food / 1e6, 2); out["k7-b-bananas"] = round(E_food / banana, 1)
out["fy2-k7-c"] = round(500 * 0.80 / 150, 2)
print(json.dumps(out))
