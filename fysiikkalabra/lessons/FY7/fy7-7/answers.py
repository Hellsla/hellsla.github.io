"""Every answer in exercises.json for fy7-7, computed from the task data (python -I answers.py).
Generator: e(t) = e0 sin(2πft), e0 = N B A · 2πf; effective values U = U0 / √2, I = I0 / √2; mean power P = U I.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

r2 = math.sqrt(2)
a = {}
# Level 1: one formula, values given
a["fy7-7-L1-01"] = 300 * 0.15 * 0.0030 * 2 * math.pi * 10          # e0 = N B A 2πf = 300 · 0,15 T · 0,0030 m² · 2π · 10 Hz = 8,482 V -> 8,5 V
a["fy7-7-L1-02"] = 115 * r2                                         # aircraft mains 115 V (effective), peak U0 = U √2 = 162,6 V -> 163 V
a["fy7-7-L1-03"] = 8.5 / r2                                         # kettle current peak 8,5 A: I = I0 / √2 = 6,010 A -> 6,0 A
a["fy7-7-L1-04"] = 1500 / 60                                        # 1500 turns per minute: f = 1500 / 60 s = 25 Hz
a["fy7-7-L1-05"] = 230 * 4.35 / 1000                                # heater, effective values: P = U I = 230 V · 4,35 A = 1000,5 W = 1,0005 kW -> 1,00 kW
# Level 2: two steps, a conversion or a rearrangement
f2 = 1200 / 60                                                      # 1200 r/min = 20 Hz
A2 = 6.0 * 0.01 * 8.0 * 0.01                                        # 6,0 cm · 8,0 cm = 0,0048 m²
a["fy7-7-L2-01"] = 150 * 0.25 * A2 * 2 * math.pi * f2               # e0 = 150 · 0,25 T · 0,0048 m² · 2π · 20 Hz = 22,62 V -> 23 V
e0_fig, T_fig = 12.0, 40e-3                                         # figure fy7-7/trace: peak 12 V, period 40 ms (read off the graph)
a["fy7-7-L2-02"] = e0_fig / (200 * 30 * 1e-4 * 2 * math.pi / T_fig)  # B = e0 / (N A 2πf), f = 1/T = 25 Hz: 12 V / (200 · 0,0030 m² · 2π · 25 Hz) = 0,1273 T -> 0,13 T
e0_3 = 12 * r2                                                      # wanted effective 12 V -> peak 16,97 V
a["fy7-7-L2-03"] = e0_3 / (200 * 0.30 * 0.0050 * 2 * math.pi)       # f = e0 / (N B A 2π) = 16,97 V / 1,885 V·s = 9,003 Hz -> 9,0 Hz
P_mean = 19.8e12 / (366 * 24)                                       # Finland's wind power 2024 (leap year, 8784 h): 19,8 TWh / 8784 h = 2,254 GW
a["fy7-7-L2-04"] = P_mean / 8358e6 * 100                            # as a share of the year-end capacity 8358 MW: 26,97 % -> 27 %
# Level 3: reasoning or an unfamiliar context
a["fy7-7-L3-01"] = 20.0 * math.sin(math.radians(30))                # coil turned 30° from the position of the largest flux: e = e0 sin 30° = 10,0 V
U3 = 40 / r2                                                        # generator peak 40 V on a 40 Ω resistor: U = 28,28 V
a["fy7-7-L3-02"] = U3 ** 2 / 40                                     # P = U I = U² / R = 800 V² / 40 Ω = 20 W (half of the peak power 40 W)
a["fy7-7-L3-03"] = 690 * 9.0 / 15                                   # permanent-magnet generator, U ∝ e0 ∝ f ∝ rotation rate: 690 V · 9,0 / 15 = 414 V
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
