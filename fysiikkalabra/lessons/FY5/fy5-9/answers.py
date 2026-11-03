"""Every answer in exercises.json for fy5-9, computed from the task data (python -I answers.py).
Harmonic oscillation: spring oscillator T = 2π√(m/k), mathematical pendulum T = 2π√(l/g) for small swings, f = 1/T,
energy E = ½kA² = ½mv² + ½kx²; g = 9,81 m/s² (Mars 3,71 m/s²). Prints {exercise id: number} as JSON on the last line."""
import json, math

g, g_mars = 9.81, 3.71
pi = math.pi
a = {}
# Level 1: one formula, values given
a["fy5-9-L1-01"] = 2 * pi * math.sqrt(0.80 / 50)          # spring: m = 0,80 kg, k = 50 N/m: T = 2π√0,016 s = 0,7948 s -> 0,79 s
a["fy5-9-L1-02"] = 2 * pi * math.sqrt(0.600 / g)          # pendulum l = 0,600 m: T = 2π√(0,600/9,81) s = 1,5539 s -> 1,55 s
T_13 = 2 * pi * math.sqrt(0.20 / 80)                      # spring m = 0,20 kg, k = 80 N/m: T = 2π√0,0025 s = 0,31416 s
a["fy5-9-L1-03"] = 1 / T_13                               # f = 1/T = 3,1831 Hz -> 3,2 Hz
a["fy5-9-L1-04"] = 0.5 * 120 * 0.050 ** 2                 # E = ½kA² = ½ · 120 N/m · (0,050 m)² = 0,15 J
a["fy5-9-L1-05"] = 4 * 0.030                              # one period: A out, A back, A to the other side, A back = 4A = 0,12 m
# Level 2: two steps, a conversion or a rearrangement
a["fy5-9-L2-01"] = g * 1.50 ** 2 / (4 * pi ** 2)          # T = 1,50 s: l = gT²/(4π²) = 9,81 · 2,25 / 39,478 m = 0,5591 m -> 0,559 m
a["fy5-9-L2-02"] = 4 * 0.30 - 0.30                        # T doubles when m is four times: 1,20 kg in all, add 0,90 kg
a["fy5-9-L2-03"] = 0.080 * math.sqrt(25 / 0.40)           # ½kA² = ½mv² -> v = A√(k/m) = 0,080 m · 7,906 1/s = 0,6325 m/s -> 0,63 m/s
a["fy5-9-L2-04"] = 2.00 * math.sqrt(g / g_mars)           # T ∝ 1/√g: T_Mars = 2,00 s · √(9,81/3,71) = 3,2522 s -> 3,25 s
# Level 3: reasoning, two ideas or an unfamiliar context
k31, m31, A31, x31 = 200, 0.50, 0.100, 0.0500
a["fy5-9-L3-01"] = math.sqrt(k31 / m31 * (A31 ** 2 - x31 ** 2))   # ½kA² = ½mv² + ½kx² -> v = √(k/m (A² − x²)) = √(400 · 0,0075) = 1,7321 m/s
k32 = 80 * g / 0.030                                      # car sinks 3,0 cm under an 80 kg passenger: k = mg/Δx = 26 160 N/m
a["fy5-9-L3-02"] = 2 * pi * math.sqrt((1200 + 80) / k32)  # T = 2π√(1280 kg / 26 160 N/m) = 1,3898 s -> 1,4 s
l33, dl33 = 0.994, 0.50e-3                                # clock pendulum 0,994 m lengthens by 0,50 mm in the summer heat
ratio = math.sqrt((l33 + dl33) / l33)                     # T'/T = √(l'/l) = 1,0002515
a["fy5-9-L3-03"] = 86400 * (1 - 1 / ratio)                # the clock counts 86 400 s / T' swings of T each: it loses 86 400 s (1 − T/T') = 21,73 s -> 22 s
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
