"""Every answer in exercises.json for fy7-5, computed from the task data (python -I answers.py).
Magnetic flux Φ = B A (field perpendicular to the area), the induction law e = −N ΔΦ / Δt (magnitudes here), the
voltage of a moving rod e = v B l. Prints {exercise id: number} as JSON on the last line; the lint and the gate compare
it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy7-5-L1-01"] = 0.35 * 0.12 ** 2 * 1e3                    # Φ = B A = 0,35 T · (0,12 m)² = 5,04 · 10⁻³ Wb = 5,04 mWb -> 5,0 mWb
a["fy7-5-L1-02"] = 400 * 1.5e-3 / 0.20                       # e = N ΔΦ / Δt = 400 · 1,5 · 10⁻³ Wb / 0,20 s = 3,0 V
a["fy7-5-L1-03"] = 2.0 * 0.40 * 0.25                         # e = v B l = 2,0 m/s · 0,40 T · 0,25 m = 0,20 V
a["fy7-5-L1-04"] = 0.45 * 0.12 / 150 * 1e3                   # ΔΦ = e Δt / N = 0,45 V · 0,12 s / 150 = 3,6 · 10⁻⁴ Wb = 0,36 mWb
a["fy7-5-L1-05"] = 12e-3 / (0.080 * 0.30)                    # v = e / (B l) = 0,012 V / (0,080 T · 0,30 m) = 0,50 m/s
# Level 2: two steps, one conversion or one rearrangement
a["fy7-5-L2-01"] = 0.80 * (200e-4 - 50e-4) / 0.25 * 1e3      # ΔΦ = B ΔA = 0,80 T · 0,0150 m² = 0,012 Wb; e = ΔΦ / Δt = 0,048 V = 48 mV
# figure fy7-5/flux-task: N = 50, Φ rises 0 -> 4,0 mWb in 0–0,20 s, stays 0,20–0,50 s, falls 4,0 -> 0 mWb in 0,50–0,60 s
e_rise = 50 * 4.0e-3 / 0.20                                  # 1,0 V while rising
e_fall = 50 * 4.0e-3 / 0.10                                  # 2,0 V while falling: the steepest part of the graph
a["fy7-5-L2-02"] = max(e_rise, e_fall)                       # largest magnitude 2,0 V
e_rod = 3.0 * 0.50 * 0.40                                    # rod on rails: e = v B l = 0,60 V
a["fy7-5-L2-03"] = e_rod / 2.0                               # I = e / R = 0,60 V / 2,0 Ω = 0,30 A
a["fy7-5-L2-04"] = 20 * 0.30 * 0.050 * 0.25 * 1e3            # coil entering a field: e = N B l v = 20 · 0,30 T · 0,050 m · 0,25 m/s = 0,075 V = 75 mV
# Level 3: reasoning or an unfamiliar context
v_train = 200 / 3.6                                          # 200 km/h = 55,56 m/s
a["fy7-5-L3-01"] = v_train * 50e-6 * 1.524 * 1e3             # axle 1,524 m (Finnish gauge 1524 mm) across the vertical component 50 µT: e = v B l = 4,23 mV -> 4,2 mV
a["fy7-5-L3-02"] = 2.0e-3 * 0.10 / (2 * 100 * 0.020) * 1e6   # flip coil: ΔΦ = 2 B A, e = N · 2 B A / Δt, so B = e Δt / (2 N A) = 5,0 · 10⁻⁵ T = 50 µT
area = 0.5 * 0.90 * 0.040                                    # first pulse, about a triangle: e Δt summed = ½ · 0,90 V · 0,040 s = 0,018 V·s = N ΔΦ
a["fy7-5-L3-03"] = area / 300 * 1e3                          # Φ_max = 0,018 V·s / 300 = 6,0 · 10⁻⁵ Wb = 0,060 mWb
# Exercise-bank additions: L1-06 and L2-07 are multiple-choice (answer text, not computed here)
a["fy7-5-L1-07"] = 300 / 120 * 0.90                 # e is proportional to N: e2 = (N2 / N1) e1 = 2,5 · 0,90 V = 2,25 V
a["fy7-5-L1-08"] = 18e-3 / (0.60 * 0.50)                     # B = e / (v l) = 0,018 V / (0,60 m/s · 0,50 m) = 0,060 T
# L2-05 data: N = 120, Φ (mWb) at 0,10 s steps; steepest part 0,40–0,60 s
phi = [0.00, 0.98, 2.03, 3.00, 3.01, 1.80, 0.60]
a["fy7-5-L2-05"] = 120 * (3.01 - 0.60) * 1e-3 / 0.20         # use the whole falling part: 1,446 V ≈ 1,45 V
# L2-06 data: slope k of (v, e) through the origin, B = k / l
v = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60]
e = [3.1, 5.8, 9.2, 11.9, 15.2, 17.8]                        # mV
k = sum(x * y for x, y in zip(v, e)) / sum(x * x for x in v) # least squares through the origin: 29,97 mV/(m/s)
a["fy7-5-L2-06"] = k * 1e-3 / 0.20                           # B = k / l = 0,030 V·s/m / 0,20 m = 0,15 T
# L3-04 data: e = a B l t, so a = k / (B l), k from the (t, e) fit through the origin
t = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
ev = [32, 65, 98, 133, 163, 198]                             # mV
k3 = sum(x * y for x, y in zip(t, ev)) / sum(x * x for x in t) * 1e-3   # 0,1643 V/s
a["fy7-5-L3-04"] = k3 / (0.25 * 0.40)                        # a = k / (B l) = 1,64 m/s² -> 1,6 m/s²
# L3-05 data: N = 250, trapezoid area of the first pulse 0–24 ms (step 4 ms) = N Φ
u = [-0.02, 0.09, 0.63, 1.77, 1.77, 0.60, 0.03]
area1 = 0.004 * (sum(u) - (u[0] + u[-1]) / 2)                # 0,01946 V·s
a["fy7-5-L3-05"] = area1 / 250 * 1e3                         # Φ = 0,0778 mWb -> 0,078 mWb
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
