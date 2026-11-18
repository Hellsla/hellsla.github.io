"""Numbers of the inquiry.json of fy3-3, computed from their data (python -I lesson-answers.py); the exercises' answers
are in answers.py. Prints {id: number} as JSON on the last line."""
import json

g = 9.81                                   # m/s²
a = {}
# kertaus: tyre air -6 °C -> 14 °C
a["kertaus-dT"] = 14 - (-6)                           # 20 °C (mistakes: 14 - 6 = 8)
a["kertaus-virhe"] = 14 - 6                           # 8

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
