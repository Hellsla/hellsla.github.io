"""Numbers of the inquiry.json of fy3-7, computed from their data (python -I lesson-answers.py); the exercises' answers
are in answers.py. Prints {id: number} as JSON on the last line."""
import json

g = 9.81                                   # m/s²
a = {}
# kertaus: 0,40 kg water warms 10 K at 800 W, c = 4190 J/(kg K)
c = 4190
Q = c * 0.40 * 10                                    # 16 760 J
a["kertaus-Q"] = Q
a["kertaus-t"] = Q / 800                              # 20,95 s -> 21 s
a["kertaus-kaanteinen"] = 800 / Q                     # mistake: 0,048 s

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
