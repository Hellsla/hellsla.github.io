"""Every answer in exercises.json for fy5-15, computed from the task data (python -I answers.py).
I = P/A, point source I = P/(4πr²) (even spreading, no reflections or absorption), L = 10 dB · lg(I/I0) with
I0 = 1,0 · 10⁻¹² W/m², I = I0 · 10^(L / 10 dB); independent sources add their intensities.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

I0 = 1.0e-12                                             # hearing threshold, W/m²
lg = math.log10
L = lambda I: 10 * lg(I / I0)
I_of = lambda Ldb: I0 * 10 ** (Ldb / 10)
a = {}
# Level 1: one formula, values given
a["fy5-15-L1-01"] = 3.0e-3 / 1.5                         # window: I = P/A = 3,0 mW : 1,5 m² = 0,0020 W/m²
a["fy5-15-L1-02"] = L(3.2e-5)                            # vacuum cleaner: 10 dB · lg(3,2e7) = 75,05 dB -> 75 dB
a["fy5-15-L1-03"] = I_of(95)                             # motorcycle passing: I = 10⁻¹² · 10^9,5 W/m² = 3,16e-3 -> 0,0032 W/m²
a["fy5-15-L1-04"] = 2.0 / (4 * math.pi * 25 ** 2)        # siren 2,0 W at 25 m: 2,546e-4 W/m² -> 0,00025 W/m²
a["fy5-15-L1-05"] = 10 * lg(100)                         # intensity 100-fold: ΔL = 10 dB · lg 100 = 20 dB
a["fy5-15-L1-08"] = L(1.0)                               # pain threshold 1,0 W/m²: 10 dB · lg(1e12) = 120 dB
# Level 2: two steps, a conversion or a rearrangement
a["fy5-15-L2-01"] = L(0.050 / (4 * math.pi * 3.0 ** 2))  # speaker 0,050 W at 3,0 m: I = 4,42e-4 W/m², L = 86,45 dB -> 86 dB
a["fy5-15-L2-02"] = L(I_of(85) + I_of(88)) - 88          # 85 dB + 88 dB: total 89,76 dB, 1,76 dB above 88 dB -> 1,8 dB
a["fy5-15-L2-03"] = 85 - 10 * lg((12.0 / 3.0) ** 2)     # 85 dB at 3,0 m -> at 12 m: I/16, 85 − 12,04 = 72,96 dB -> 73 dB
a["fy5-15-L2-04"] = 10 ** ((91 - 85) / 10)               # one machine 85 dB, N machines 91 dB: N = 10^0,6 = 3,98 -> 4
a["fy5-15-L2-05"] = (84.2 - 60.1) / 4                    # field data: 1,0 m -> 16 m is 4 doublings, 24,1 dB : 4 = 6,025 -> 6,03 dB (model 6,02 dB)
a["fy5-15-L2-06"] = 71.9 - (86.0 - 10 * lg(8.0 ** 2))    # hall: model 86,0 - 18,06 = 67,94 dB at 8 m, measured 71,9 dB -> 3,96 dB -> 4,0 dB
a["fy5-15-L2-07"] = 10 ** (sum([54.1 - 50, 63.8 - 60, 74.2 - 70, 83.9 - 80]) / 4 / 10)   # phone errors 4,1+3,8+4,2+3,9 = 16,0 dB, mean 4,0 dB -> I ratio 10^0,4 = 2,51 -> 2,5
# Level 3: reasoning or an unfamiliar context
L_crowd = 42 + 10 * lg(12000)                            # 12 000 equal independent voices of 42 dB: 42 + 40,79 = 82,79 dB
a["fy5-15-L3-01"] = L(I_of(L_crowd) + I_of(80))          # plus a PA system alone 80 dB: 10 dB · lg(10^8,279 + 10^8) = 84,63 dB -> 85 dB
a["fy5-15-L3-02"] = 0.50 * math.sqrt(10 ** ((30 - 0) / 10))   # mosquito 30 dB at 0,50 m down to the threshold 0 dB: r = 0,50 m · √1000 = 15,8 m -> 16 m
# level 3 additions
P_est = [I_of(l) * 4 * math.pi * r ** 2 for l, r in [(91.1, 5.0), (84.8, 10.0), (79.3, 20.0), (72.6, 40.0)]]   # P = I·4πr² from each reading: 0,405; 0,380; 0,428; 0,366 W
P_mean = sum(P_est) / 4                                  # mean 0,3945 W
a["fy5-15-L3-04"] = math.sqrt(P_mean / (4 * math.pi * I_of(55)))   # distance where L = 55 dB: sqrt(P / (4π I)) = 315 m
I_amp = 0.20 / (4 * math.pi * 8.0 ** 2)                  # guitar amp 0,20 W at 8,0 m: 2,487e-4 W/m²
I_drum = I_of(90) / (8.0 / 2.0) ** 2                     # drums 90 dB at 2,0 m -> at 8,0 m I/16 = 6,25e-5 W/m²
I_sum = I_amp + I_drum                                   # total 3,112e-4 W/m² (L = 84,93 dB at 8,0 m)
a["fy5-15-L3-05"] = 8.0 * math.sqrt(I_sum / I_of(70))    # I ∝ 1/r²: r = 8,0 m · sqrt(3,112e-4 / 1e-5) = 44,6 m -> 45 m
print(json.dumps({k: round(v, 8) for k, v in a.items()}))
