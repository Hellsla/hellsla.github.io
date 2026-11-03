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
# Level 2: two steps, a conversion or a rearrangement
a["fy5-15-L2-01"] = L(0.050 / (4 * math.pi * 3.0 ** 2))  # speaker 0,050 W at 3,0 m: I = 4,42e-4 W/m², L = 86,45 dB -> 86 dB
a["fy5-15-L2-02"] = L(I_of(85) + I_of(88)) - 88          # 85 dB + 88 dB: total 89,76 dB, 1,76 dB above 88 dB -> 1,8 dB
a["fy5-15-L2-03"] = 90 - 10 * lg((8.0 / 2.0) ** 2)       # 90 dB at 2,0 m -> at 8,0 m: I/16, 90 − 12,04 = 77,96 dB -> 78 dB
a["fy5-15-L2-04"] = 10 ** ((91 - 85) / 10)               # one machine 85 dB, N machines 91 dB: N = 10^0,6 = 3,98 -> 4
# Level 3: reasoning or an unfamiliar context
a["fy5-15-L3-01"] = 42 + 10 * lg(12000)                  # 12 000 equal independent voices of 42 dB: 42 + 40,79 = 82,79 dB -> 83 dB
a["fy5-15-L3-02"] = 0.50 * math.sqrt(10 ** ((30 - 0) / 10))   # mosquito 30 dB at 0,50 m down to the threshold 0 dB: r = 0,50 m · √1000 = 15,8 m -> 16 m
print(json.dumps({k: round(v, 8) for k, v in a.items()}))
