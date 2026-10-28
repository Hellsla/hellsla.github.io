"""Numbers of the inquiry.json of fy3-11, computed from their data (python -I lesson-answers.py); the exercises' answers
are in answers.py. Prints {id: number} as JSON on the last line."""
import json

a = {}
# check-c2, heat pump: E_s = 1,0 kWh electricity, Q_sisälle = 3,0 kWh delivered indoors
a["inq-c2-Q-ulko"] = 3.0 - 1.0                            # Q_ulko = Q_sisälle − E_s = 2,0 kWh taken from the outdoor air
a["inq-c2-epsilon"] = 3.0 / 1.0                           # ε = Q_sisälle/E_s = 3,0

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
