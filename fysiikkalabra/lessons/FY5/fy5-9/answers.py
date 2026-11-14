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

# Added batch (L1-06..08 are multiple choice, no number)
a["fy5-9-L2-05"] = 4 * pi ** 2 / 4.04                     # (l, T²) line through the origin and (1,00 m; 4,04 s²): slope 4,04 s²/m, g = 4π²/slope = 9,772 m/s² -> 9,77 m/s²
a["fy5-9-L2-06"] = 4 * pi ** 2 / 1.96                     # (m, T²) line through the origin and (0,500 kg; 0,98 s²): slope 1,96 s²/kg, k = 4π²/slope = 20,14 N/m -> 20,1 N/m
T0_27 = 2 * pi * math.sqrt(1.000 / g)                     # pendulum 1,000 m: T0 = 2,0061 s
a["fy5-9-L2-07"] = (21.5 / 10 / T0_27 - 1) * 100          # 60° start: T = 2,15 s, (T − T0)/T0 = 7,17 % -> 7,2 %
slope34 = (0.504 - 0.033) / 0.300                         # fitted (m, T²) line through (0; 0,033 s²) and (0,300 kg; 0,504 s²): 1,570 s²/kg
a["fy5-9-L3-04"] = 4 * pi ** 2 / slope34                  # k = 4π²/slope = 25,14 N/m -> 25,1 N/m (m0 = 0,033/1,570 = 0,0210 kg; k from 50 g alone 17,69 N/m, −29,6 %)
l35, al35 = 1.20, math.radians(10.0)                      # pendulum 1,20 m released from 10,0°
a["fy5-9-L3-05"] = math.sqrt(2 * g * l35 * (1 - math.cos(al35)))  # ½mv² = mgh, h = l(1 − cos α) = 0,01823 m: v = 0,5981 m/s -> 0,598 m/s (harmonic model l·α·√(g/l) = 0,5988 m/s, 0,13 % more)
# L2-08 is multiple choice with a reason (Moon): pendulum T = 1,00 s · √(9,81/1,62) = 2,461 s, spring T stays 1,00 s; no number
# Added batch (teacher 2026-11-12): figure tasks (kuvaaja-k: A = 3,0 cm, T = 0,40 s) and a MAFY table task
a["fy5-9-L1-09"] = 2 * pi * math.sqrt(1.00 / 3.72)        # MAFY: g_Mars = 3,72 m/s², l = 1,00 m: T = 2π√(1,00/3,72) s = 3,2577 s -> 3,26 s
a["fy5-9-L1-10"] = 0.5 * 120 * 0.030 ** 2                 # figure: A = 3,0 cm; E = ½kA² = ½ · 120 N/m · (0,030 m)² = 0,054 J
a["fy5-9-L2-09"] = 2 * pi * 0.030 / 0.40                  # figure: A = 3,0 cm, T = 0,40 s; v_max = 2πA/T = 0,1885 / 0,40 = 0,471 m/s -> 0,47 m/s
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
