"""Numbers of the inquiry.json of fy3-1, computed from their data (python -I lesson-answers.py); the exercises' answers
are in answers.py. Prints {id: number} as JSON on the last line."""
import json

g = 9.81                                   # m/s²
a = {}
# kertaus: spring stretch proportional to force, 1,5 cm at 2,0 N
a["kertaus-x"] = 1.5 * 6.0 / 2.0                       # 4,5 cm (mistakes: 1,5 + 4,0 = 5,5; 6,0; 2 * 1,5 = 3,0)
a["kertaus-lisays"] = 1.5 + (6.0 - 2.0)               # 5,5 cm
a["kertaus-kaksinkertainen"] = 2 * 1.5                # 3,0 cm

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
