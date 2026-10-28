"""Numbers of the inquiry.json of fy3-9, computed from their data (python -I lesson-answers.py); the exercises' answers
are in answers.py. Prints {id: number} as JSON on the last line."""
import json

a = {}
# check-c2: a rigid bottle of air warms from 7 °C to 35 °C: p2/p1 = T2/T1 (kelvins)
T1, T2 = 7 + 273.15, 35 + 273.15                          # 280,15 K and 308,15 K
a["inq-c2-suhde"] = T2 / T1                               # 1,0999 -> about 10 %
a["inq-c2-prosentti"] = (T2 / T1 - 1) * 100               # 9,99 %
a["inq-c2-celsius-suhde"] = 35 / 7                        # mistake: ratio of the Celsius values = 5
a["inq-c2-28"] = (T2 - T1) / T1 * 100                     # mistake 28 % from 28 degrees: the true relative change is 9,99 %

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
