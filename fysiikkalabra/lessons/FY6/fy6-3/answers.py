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
k = sum(l * R for l, R in zip(ls, Rs)) / sum(l * l for l in ls)   # least-squares slope through the origin, R / l = 5,45 Ω/m
a["fy6-3-L3-02"] = k * 0.20e-6 * 1e6                   # ρ = (R / l) · A = 5,45 Ω/m · 0,20·10⁻⁶ m² = 1,09·10⁻⁶ Ω·m -> 1,1 µΩ·m
a["fy6-3-L3-03"] = 3.0 / 1.0                           # lamp switched on cold: I = U / R_cold = 3,0 V / 1,0 Ω = 3,0 A (12 times the running 0,25 A)
print(json.dumps({k_: round(v, 6) for k_, v in a.items()}))
