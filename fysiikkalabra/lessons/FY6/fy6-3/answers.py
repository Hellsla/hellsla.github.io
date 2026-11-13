"""Every answer in exercises.json for fy6-3, computed from the task data (python -I answers.py).
R = U / I (Ohm's law U = R I when R is constant), R = ρ l / A with A in m² (1 mm² = (10⁻³ m)² = 10⁻⁶ m²).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

RHO_CU, RHO_K, RHO_NI = 1.7e-8, 5.0e-7, 1.1e-6        # Ω·m: copper, constantan, nichrome (lesson table)
a = {}
# Level 1: one formula, values given
a["fy6-3-L1-01"] = 230 / 8.7                           # kettle: R = U / I = 230 V / 8,7 A = 26,4 Ω -> 26 Ω
a["fy6-3-L1-02"] = 220 * 15e-3                         # resistor: U = R I = 220 Ω · 0,015 A = 3,3 V
a["fy6-3-L1-03"] = 12 / 1.2                            # rear-window heater: I = U / R = 12 V / 1,2 Ω = 10 A
a["fy6-3-L1-04"] = RHO_CU * 25 / 2.5e-6                # copper cable: R = ρ l / A = 1,7·10⁻⁸ · 25 / 2,5·10⁻⁶ = 0,17 Ω
a["fy6-3-L1-05"] = 5.0 / 2.0e-3 / 1000                 # moisture sensor: R = 5,0 V / 0,0020 A = 2500 Ω = 2,5 kΩ
# Level 2: two steps, a conversion or a rearrangement
R_l2_1 = 6.0 / 0.25                                    # resistor: R = 6,0 V / 0,25 A = 24 Ω, constant at the same temperature
a["fy6-3-L2-01"] = 9.0 / R_l2_1                        # I = 9,0 V / 24 Ω = 0,375 A -> 0,38 A
a["fy6-3-L2-02"] = 1.0 / 0.15                          # figure fy6-3/lamp-curve: at U = 1,0 V the curve is at I = 0,15 A: R = 6,7 Ω
a["fy6-3-L2-03"] = RHO_CU * 50 / 0.50 * 1e6            # copper, 50 m, R ≤ 0,50 Ω: A = ρ l / R = 1,7·10⁻⁶ m² = 1,7 mm²
A_l2_4 = math.pi * (0.40e-3 / 2) ** 2                  # constantan, diameter 0,40 mm: A = π r² = 1,257·10⁻⁷ m²
a["fy6-3-L2-04"] = RHO_K * 2.0 / A_l2_4                # R = 5,0·10⁻⁷ · 2,0 / 1,257·10⁻⁷ = 7,96 Ω -> 8,0 Ω
# Level 3: reasoning or an unfamiliar context
a["fy6-3-L3-01"] = 0.80 * 2 * 2                        # wire drawn to twice its length, volume kept: l doubles, A halves: R = 4 · 0,80 Ω = 3,2 Ω
ls = [0.40, 0.80, 1.20, 1.60]                          # nichrome wire, A = 0,20 mm², U = 2,00 V
Is = [0.91, 0.46, 0.30, 0.23]                          # measured currents (A)
Rs = [2.00 / I for I in Is]                            # R = U / I: 2,198; 4,348; 6,667; 8,696 Ω
k = sum(l * R for l, R in zip(ls, Rs)) / sum(l * l for l in ls)   # least-squares slope through the origin, R / l = 5,47 Ω/m
a["fy6-3-L3-02"] = k * 0.20e-6 * 1e6                   # ρ = (R / l) · A = 5,47 Ω/m · 0,20·10⁻⁶ m² = 1,09·10⁻⁶ Ω·m -> 1,1 µΩ·m
a["fy6-3-L3-03"] = 3.0 / 1.0                           # lamp switched on cold: I = U / R_cold = 3,0 V / 1,0 Ω = 3,0 A (12 times the running 0,25 A)
# Exercise bank additions (teacher 2026-11-04): L1-06 and L1-07 are multiple choice (no number)
a["fy6-3-L1-08"] = 4.5 / (2 * (4.5 / 0.60))            # copper wire twice as long: R2 = 2 R1 = 2 · 7,5 Ω = 15 Ω, I2 = 4,5 V / 15 Ω = 0,30 A
U5 = [1, 2, 3, 4, 5, 6, 7, 8]; I5 = [6.6, 13.5, 19.8, 26.9, 33.1, 40.2, 46.3, 53.6]   # mA, resistor U-I table
a["fy6-3-L2-05"] = sum(u * i * 1e-3 for u, i in zip(U5, I5)) / sum((i * 1e-3) ** 2 for i in I5)   # slope through the origin (least squares) 150,0 Ω
Ul = [1, 2, 3, 4, 5]; Il = [0.098, 0.146, 0.187, 0.221, 0.248]      # lamp, A
a["fy6-3-L2-06"] = (Ul[-1] / Il[-1]) / (Ul[0] / Il[0])              # R(5,0 V) / R(1,0 V) = 20,2 Ω / 10,2 Ω = 1,98 -> 2,0
Re = [u / i for u, i in zip([1.0, 2.0, 3.0, 4.0], [0.20, 0.41, 0.61, 0.81])]   # 5,00; 4,88; 4,92; 4,94 Ω (0 V point excluded: 0 : 0)
a["fy6-3-L2-07"] = sum(Re) / len(Re)                                 # sum 19,74 Ω, mean 4,93 Ω -> 4,9 Ω
a["fy6-3-L3-04"] = 1.5 / 2.5e-3                                      # diode C at U = 1,5 V, I = 2,5 mA: R = 600 Ω (lamp B 1,5 V / 57 mA = 26 Ω, resistor A 75 Ω)
Rt = [1.00 / i for i in (0.500, 0.442, 0.398, 0.362)]                # iron wire R = U / I at 20, 40, 60, 80 °C
a["fy6-3-L3-05"] = (Rt[-1] / Rt[0] - 1) * 100                        # increase 20 -> 80 °C: 2,762 / 2,000 - 1 = 38,1 %
# MAFY table task (docs/mafy-arvot.tsv): copper resistivity 1,678·10⁻⁸ Ω·m from the table "Resistiivisyyksiä"
a["fy6-3-L1-10"] = 1.678e-8 * 40 / 1.5e-6              # R = ρ l / A = 1,678·10⁻⁸ · 40 / 1,5·10⁻⁶ = 0,4475 Ω -> 0,45 Ω
print(json.dumps({k_: round(v, 6) for k_, v in a.items()}))
