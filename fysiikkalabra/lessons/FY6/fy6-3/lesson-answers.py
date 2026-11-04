"""Numbers of the lesson text and inquiry.json for fy6-3, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. The simulation's models (assets/sims/fy6/fy6-3/sim.js) are repeated here:
resistor R = 10 Ω; lamp R(U) = R_k + (R_n − R_k)(U/U_n)^0,6 with R_k = 1,0 Ω, R_n = 12,0 Ω, U_n = 3,0 V;
constantan wire R = ρ l / A with ρ = 5,0·10⁻⁷ Ω·m. Prints {id: number} as JSON on the last line."""
import json

R_RES, RK, RN, UN, RHO_K = 10.0, 1.0, 12.0, 3.0, 5.0e-7


def lamp_R(U):                                        # the lamp model: the filament's resistance grows as it heats
    return RK + (RN - RK) * (U / UN) ** 0.6


def wire_R(l, A_mm2):                                 # R = ρ l / A, A in mm² = A · 10⁻⁶ m²
    return RHO_K * l / (A_mm2 * 1e-6)


a = {}
# koe 1 (resistor): I = U / R at 0,5 … 3,0 V, U : I always 10 Ω
a["koe1-I-0.5"] = 0.5 / R_RES                         # 0,050 A
a["koe1-I-1.5"] = 1.5 / R_RES                         # 0,150 A
a["koe1-I-3.0"] = 3.0 / R_RES                         # 0,300 A
a["koe1-R"] = 1.5 / (1.5 / R_RES)                     # koe 1 question: R = U : I = 1,50 V : 0,150 A = 10,0 Ω
a["koe1-R-mistake-IU"] = (1.5 / R_RES) / 1.5          # mistake: I : U = 0,10 (1/Ω)
# koe 2 (lamp) and prediction 1: U 1,5 V -> 3,0 V
a["lamp-R-0.5"] = lamp_R(0.5); a["lamp-I-0.5"] = 0.5 / lamp_R(0.5)     # 4,75 Ω, 0,105 A
a["lamp-R-1.0"] = lamp_R(1.0); a["lamp-I-1.0"] = 1.0 / lamp_R(1.0)     # 6,69 Ω, 0,149 A
a["lamp-R-1.5"] = lamp_R(1.5); a["lamp-I-1.5"] = 1.5 / lamp_R(1.5)     # 8,26 Ω, 0,182 A
a["lamp-R-3.0"] = lamp_R(3.0); a["lamp-I-3.0"] = 3.0 / lamp_R(3.0)     # 12,0 Ω, 0,250 A
a["lamp-ratio"] = a["lamp-I-3.0"] / a["lamp-I-1.5"]   # the current grows 1,38-fold when U doubles
# where the lamp and the 10 Ω resistor carry the same current: lamp_R(U) = 10 Ω
a["cross-U"] = UN * ((R_RES - RK) / (RN - RK)) ** (1 / 0.6)            # 2,15 V
a["cross-I"] = a["cross-U"] / R_RES                                      # 0,215 A
# the error-spotting item: the tangent's slope at 3,0 V is dU/dI, not U : I
dRdU = (RN - RK) * 0.6 * (3.0 / UN) ** (-0.4) / UN    # dR/dU = 2,2 Ω/V
dIdU = (lamp_R(3.0) - 3.0 * dRdU) / lamp_R(3.0) ** 2  # dI/dU = (R − U R') / R² = 0,0375 1/Ω
a["virhe-tangent"] = 1 / dIdU                         # 26,7 Ω: the student's wrong 27 Ω
a["virhe-R"] = 3.0 / 0.25                             # correct: U : I = 3,0 V : 0,250 A = 12 Ω
# koe 3 (wire length, U = 1,5 V, A = 0,20 mm²) and prediction 2
for l in (0.5, 1.0, 1.5, 2.0):
    a[f"koe3-R-{l}"] = wire_R(l, 0.20); a[f"koe3-I-{l}"] = 1.5 / wire_R(l, 0.20)    # 1,25/2,50/3,75/5,00 Ω; 1,20/0,600/0,400/0,300 A
# koe 4 (wire cross-section, U = 1,5 V, l = 1,00 m)
for A in (0.1, 0.2, 0.4):
    a[f"koe4-R-{A}"] = wire_R(1.0, A); a[f"koe4-I-{A}"] = 1.5 / wire_R(1.0, A)      # 5,00/2,50/1,25 Ω; 0,300/0,600/1,20 A
# sim on load: resistor at 1,5 V
a["load-I"] = 1.5 / R_RES
# worked example: constantan wire for a 12 Ω resistor, A = 0,20 mm²: l = R A / ρ
a["ex-l"] = 12 * 0.20e-6 / RHO_K                      # 4,8 m
a["ex-check-I"] = 6.0 / 12                            # check: at 6,0 V the current is 0,50 A
a["ex-check-1m"] = RHO_K * 1.0 / 0.20e-6              # 1 m of the wire is 2,5 Ω, so 12 Ω needs 4,8 m
# transfer task: copper wiring, 2 · 18 m, 1,5 mm², ρ = 1,7·10⁻⁸ Ω·m
RHO_CU = 1.7e-8
a["siirto"] = RHO_CU * 36 / 1.5e-6                    # 0,408 Ω
a["siirto-one"] = RHO_CU * 18 / 1.5e-6                # mistake: one conductor only, 0,204 Ω
a["siirto-mm2-1e3"] = RHO_CU * 36 / 1.5e-3            # mistake: mm² = 10⁻³ m², 4,08·10⁻⁴ Ω
a["siirto-check-U"] = a["siirto"] * 10                # reasonableness: at 10 A the wiring takes 4,1 V of the 230 V
# check 2: the measured points of figure resistor-points, fitted line through (0,100 A; 2,20 V)
a["tark2"] = 2.20 / 0.100                             # 22 Ω
a["tark2-inv"] = 0.100 / 2.20                         # mistake: I : U = 0,045
# check 1: doubling U through a resistor at constant temperature: R stays 10 Ω, I doubles
a["tark1-I"] = 2 * a["koe1-I-1.5"]
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
