"""Numbers of the lesson text and inquiry.json for fy1-7, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Prints {id: number} as JSON on the last line."""
import json

a = {}
# kertaus: cube side 4,0 cm; V = a³ = (4,0·10⁻² m)³
a["kertaus-V"] = (4.0e-2) ** 3                       # 6,4·10⁻⁵ m³ (mistakes: 64, 0,64 and 6,4·10⁻⁴)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
