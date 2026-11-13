"""Every answer in exercises.json for fy3-1, computed from the task data (python -I answers.py).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

g = {"Maa": 9.81, "Kuu": 1.62, "Mars": 3.71, "Jupiter": 24.8}   # m/s², the lesson's table
a = {}
# Level 1: G = m g, and the stretch of a spring is proportional to the force
a["fy3-1-L1-01"] = 4.0 * g["Maa"]                 # 39,24 N -> 39 N
a["fy3-1-L1-02"] = 2.0 * 12 / 4.0                 # 6,0 cm
a["fy3-1-L1-03"] = 30 * g["Kuu"]                  # 48,6 N -> 49 N
a["fy3-1-L1-04"] = 3.5 / (1 / 2)                 # figure fy3-1/spring-points: points (2 N; 1 cm) ... (10 N; 5 cm), x/F = 0,5 cm/N, so F = 3,5 cm / 0,5 cm/N = 7,0 N
a["fy3-1-L1-05"] = 2.5 * g["Jupiter"]             # 62 N
# Level 2: one rearrangement or one conversion
a["fy3-1-L2-01"] = 49 / g["Maa"]                  # m = G / g = 4,99 kg -> 5,0 kg
a["fy3-1-L2-02"] = 0.060 * g["Maa"]               # 60 g = 0,060 kg -> 0,589 N -> 0,59 N
a["fy3-1-L2-03"] = 145 * (g["Maa"] - g["Kuu"])    # 1187,55 N -> 1190 N
a["fy3-1-L2-04"] = 0.20 * g["Maa"] * 4.5 / 1.5    # force proportional to stretch: 1,962 N * 3 = 5,886 N -> 5,9 N
# Level 3: reasoning
a["fy3-1-L3-01"] = 18 / g["Maa"] * g["Mars"]      # same mass, weight scales with g: 6,81 N -> 6,8 N
a["fy3-1-L3-02"] = 22.0 * g["Maa"] / g["Kuu"]     # same force, m = F / g: 133,2 kg -> 133 kg
a["fy3-1-L3-03"] = 26 * g["Maa"] / g["Mars"]      # scale shows G / 9,81, so G = 26 kg · 9,81 m/s² and m = G / g_Mars: 68,75 kg -> 69 kg
# Added exercises (bank P1): levels 1-3
a["fy3-1-L1-08"] = 0.18 * 1000 * g["Mars"]                # 667,8 N -> 670 N
a["fy3-1-L2-05"] = 4.90 / 0.50                    # slope of the fitted line through the origin, read at (0,50 kg; 4,90 N): 9,8 m/s²
a["fy3-1-L2-06"] = g["Maa"] * 2.8 / 7.4           # m = 7,4 N / g_Maa, g_Mars = 2,8 N / m: 3,71 -> 3,7 m/s²
a["fy3-1-L2-07"] = 4.9 / g["Maa"]                 # m = G / g = 0,4995 kg -> 0,50 kg
a["fy3-1-L3-04"] = g["Maa"] * (1.9 / 0.50) / (sum([1.1, 2.1, 3.2, 4.1, 5.2, 6.1]) / sum([0.1, 0.2, 0.3, 0.4, 0.5, 0.6]))  # x/m ratio of the spring on Earth 10,38 cm/kg, on X 3,8 cm/kg: 3,59 m/s² -> 3,6
a["fy3-1-L3-05"] = 6000 / g["Mars"] - (520 + 180 + 95 + 140)  # max total mass 1617 kg minus 935 kg = 682 kg
a["fy3-1-L1-10"] = 85.0 * 3.72                      # MAFY (Aurinkokunta): Marsin g = 3,72 m/s², G = m g = 316,2 N -> 316 N
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
