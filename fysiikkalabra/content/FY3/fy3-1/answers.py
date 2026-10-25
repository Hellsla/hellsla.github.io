"""Every answer in exercises.json for fy3-1, computed from the task data (python -I answers.py).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

g = {"Maa": 9.81, "Kuu": 1.62, "Mars": 3.71, "Jupiter": 24.8}   # N/kg, the lesson's table
a = {}
# Level 1: G = m g, and the stretch of a spring is proportional to the force
a["fy3-1-L1-01"] = 4.0 * g["Maa"]                 # 39,24 N -> 39 N
a["fy3-1-L1-02"] = 2.0 * 12 / 4.0                 # 6,0 cm
a["fy3-1-L1-03"] = 30 * g["Kuu"]                  # 48,6 N -> 49 N
a["fy3-1-L1-04"] = 5.0 * 3.0 / 2.0                # force proportional to stretch: 7,5 N
a["fy3-1-L1-05"] = 2.5 * g["Jupiter"]             # 62 N
# Level 2: one rearrangement or one conversion
a["fy3-1-L2-01"] = 49 / g["Maa"]                  # m = G / g = 4,99 kg -> 5,0 kg
a["fy3-1-L2-02"] = 0.060 * g["Maa"]               # 60 g = 0,060 kg -> 0,589 N -> 0,59 N
a["fy3-1-L2-03"] = 145 * (g["Maa"] - g["Kuu"])    # 1187,55 N -> 1190 N
a["fy3-1-L2-04"] = 0.20 * g["Maa"] * 4.5 / 1.5    # force proportional to stretch: 1,962 N * 3 = 5,886 N -> 5,9 N
# Level 3: reasoning
a["fy3-1-L3-01"] = 18 / g["Maa"] * g["Mars"]      # same mass, weight scales with g: 6,81 N -> 6,8 N
a["fy3-1-L3-02"] = 22.0 * g["Maa"] / g["Kuu"]     # same force, m = F / g: 133,2 kg -> 133 kg
a["fy3-1-L3-03"] = 6.0 * g["Kuu"] / g["Maa"]      # scale shows G / 9,81: 0,991 kg -> 0,99 kg
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
