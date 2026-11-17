"""Numbers of the lesson text and inquiry.json for fy1-8, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Prints {id: number} as JSON on the last line."""
import json

a = {}
# kertaus: five times of a toy car over 1,00 m: mean and half of the range
t = [2.4, 2.6, 2.3, 2.5, 2.4]
a["kertaus-mean"] = sum(t) / len(t)                  # 12,2 / 5 = 2,44 s
a["kertaus-half-range"] = (max(t) - min(t)) / 2      # (2,6 - 2,3) / 2 = 0,15 s
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
