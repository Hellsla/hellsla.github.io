"""Numbers of the inquiry.json of fy3-4, computed from their data (python -I lesson-answers.py); the exercises' answers
are in answers.py. Prints {id: number} as JSON on the last line."""
import json

g = 9.81                                   # m/s²
a = {}
# kertaus: weight of a 3000 kg water column
a["kertaus-G"] = 3000 * g                             # 29 430 N -> about 29 kN
a["kertaus-jako"] = 3000 / g                          # mistake: 305,8 -> 306 N

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
