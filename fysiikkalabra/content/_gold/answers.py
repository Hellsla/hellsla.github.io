"""Every answer in exercises.json, computed here so the gate can re-run it (python -I answers.py).
Print one JSON object {exercise id: number} as the last line. Keep the physics readable: one line per step."""
import json

a = {}
# fy3-2-L1-01: a = F / m
a["fy3-2-L1-01"] = 12 / 4.0
# fy3-2-L2-01: a = (F - f) / m
a["fy3-2-L2-01"] = (30 - 6) / 12

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
