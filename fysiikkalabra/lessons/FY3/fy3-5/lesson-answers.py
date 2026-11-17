"""Numbers of the inquiry.json of fy3-5, computed from their data (python -I lesson-answers.py); the exercises' answers
are in answers.py. Prints {id: number} as JSON on the last line."""
import json

g = 9.81                                   # m/s²
a = {}
# kertaus: work of the pump handle, F = 90 N, s = 0,10 m
a["kertaus-W"] = 90 * 0.10                            # 9,0 J (mistakes: 900 = F / s, 90, 90,1 = F + s)
a["kertaus-jako"] = 90 / 0.10
a["kertaus-summa"] = 90 + 0.10

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
