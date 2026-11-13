"""Numbers of the inquiry.json of fy3-11, computed from their data (python -I lesson-answers.py); the exercises' answers
are in answers.py. Prints {id: number} as JSON on the last line."""
import json

a = {}
# check-c2, heat pump: W = 1,0 kWh electricity, Q₁ = 3,0 kWh delivered indoors
a["inq-c2-Q-ulko"] = 3.0 - 1.0                            # Q₂ = Q₁ − W = 2,0 kWh taken from the outdoor air
a["inq-c2-epsilon"] = 3.0 / 1.0                           # ε = Q₁/W = 3,0

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
