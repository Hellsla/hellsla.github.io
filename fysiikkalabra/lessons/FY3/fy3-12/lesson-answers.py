"""Numbers of the inquiry.json of fy3-12, computed from their data (python -I lesson-answers.py); the exercises' answers
are in answers.py. Prints {id: number} as JSON on the last line."""
import json

g = 9.81                                   # m/s²
a = {}
# kertaus: layer gives 4,0 kJ and receives 1,0 kJ of heat, W = 0
a["kertaus-dU"] = (1.0 - 4.0) + 0                    # -3,0 kJ

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
