"""Every answer in exercises.json for fy7-11, computed from the task data (python -I answers.py).
Snell's law from air (n = 1,000): sin α1 = n sin α2; n = c : v; prism: α2 + α3 = A, δ = α1 + α4 − A;
rainbow (one internal reflection in a drop): θ = 4β − 2α with sin α = n sin β. c = 3,00 · 10⁸ m/s.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

c = 3.00e8
sin = lambda deg: math.sin(math.radians(deg))
asin = lambda x: math.degrees(math.asin(x))
a = {}
# Level 1: one formula, values given
a["fy7-11-L1-01"] = asin(sin(50.0) / 1.332)          # red light air -> water: α2 = 35,11°
a["fy7-11-L1-02"] = c / 1.530 / 1e3                  # violet light in crown glass: v = c / n = 196 078 km/s
a["fy7-11-L1-03"] = sin(45.0) / sin(27.8)            # n = sin α1 / sin α2 = 1,516
a["fy7-11-L1-04"] = 45.0 + 52.0 - 60.0               # prism: δ = α1 + α4 − A = 37,0°
a["fy7-11-L1-05"] = 4 * 38.0 - 2 * 55.0              # drop: θ = 4β − 2α = 42,0°
# Level 2: two steps, a conversion or a rearrangement
L = 5.00e3                                           # 5,00 km of crown glass, n_p = 1,5143, n_v = 1,5302
t_p, t_v = L * 1.5143 / c, L * 1.5302 / c            # t = L / v = L n / c: 25,238 µs and 25,503 µs
a["fy7-11-L2-01"] = (t_v - t_p) * 1e9                # Δt = 265 ns
a2 = asin(sin(40.0) / 1.52)                          # prism A = 60,0°, n = 1,52, α1 = 40,0°: α2 = 25,02°
a["fy7-11-L2-02"] = 60.0 - a2                        # α3 = A − α2 = 34,98°
# figure fy7-11/flint-points: flint glass n at 450 nm read off the graph, 1,6387 (point on the curve)
a["fy7-11-L2-03"] = c / 1.6387 / 1e3                 # v = c / n = 183 072 km/s
b = asin(sin(58.8) / 1.343)                          # violet ray in a drop, α = 58,8°: β = 39,56°
a["fy7-11-L2-04"] = 4 * b - 2 * 58.8 - 25.0          # θ = 4β − 2α = 40,65°; Sun 25,0° high: top at θ − h = 15,65°
# Level 3: reasoning or an unfamiliar context
def delta(n, A, a1):                                 # prism deviation δ = α1 + α4 − A
    a2 = asin(sin(a1) / n); a3 = A - a2; a4 = asin(n * sin(a3)); return a1 + a4 - A
a["fy7-11-L3-01"] = delta(1.5302, 50.0, 45.0) - delta(1.5143, 50.0, 45.0)   # Δδ = 30,80° − 29,84° = 0,966°
b = asin(sin(80.0) / 1.332)                          # red ray at α = 80,0°: β = 47,68°
a["fy7-11-L3-02"] = 4 * b - 2 * 80.0                 # θ = 30,7° < 42,3°: inside the bow
th_p = 4 * asin(sin(59.5) / 1.3315) - 2 * 59.5       # red rainbow ray (lesson table n): 42,30°
th_v = 4 * asin(sin(58.8) / 1.3431) - 2 * 58.8       # violet rainbow ray (lesson table n): 40,63°
a["fy7-11-L3-03"] = th_p - th_v                      # width of the bow 1,665°
# Exercise-bank additions
# L1-06 (words): the correct option is C: the glass n is larger for violet (dispersion) so violet slows more; the frequency does not change
a["fy7-11-L1-07"] = 405 / 1.530                      # λ in glass = λ0 / n (f constant, v = c / n) = 264,7 nm
a["fy7-11-L1-08"] = 42.3 - 30.0                      # red edge 42,3° from the antisolar point, Sun 30,0° high: top at θ − h = 12,3°
# L1-09 is true/false statements (no number): 1 false (violet n larger), 2 true (v = c/n: 1,961 < 1,982 · 10^8 m/s), 3 false (f unchanged),
#   4 true (one colour does not split again), 5 true (violet 40,6° < red 42°), 6 false (Sun 45°: top at 42° - 45° = -3°)
def d_alpha(n_p, n_v):                               # difference of the refraction angles of red and violet at α1 = 60,0°
    return asin(sin(60.0) / n_p) - asin(sin(60.0) / n_v)
a["fy7-11-L2-05"] = d_alpha(1.6150, 1.6498)          # flint glass: 32,43° − 31,66° = 0,765° (crown 0,414°, acrylic 0,461°)
a["fy7-11-L2-06"] = 4 * asin(sin(59.0) / 1.3315) - 2 * 59.0   # error analysis: red at α = 59,0°: θ = 4β − 2α = 42,29° (violet 40,63°)
a["fy7-11-L2-07"] = c / 1.516 / 1e3                  # figure n-graph: n(600 nm) read as 1,516; v = c / n = 197 889 km/s (λ = 600 / 1,516 = 396 nm)
# L3-04: table (α, θ_liquid); β = (θ + 2α) / 4, n = sin α / sin β for each row, mean = 1,400 (data built with n = 1,400, small scatter)
tab = [(40.0, 29.35), (50.0, 32.67), (55.0, 33.26), (58.0, 33.10), (62.0, 32.41), (66.0, 30.91)]
ns = [sin(al) / sin((th + 2 * al) / 4) for al, th in tab]
a["fy7-11-L3-04"] = sum(ns) / len(ns)
# L3-05: flint prism n_p = 1,6150, n_v = 1,6498, α1 = 50,0°, A = 64,0°: Δδ = δ_v − δ_p = 63,82° − 56,40° = 7,42° (A_max for violet 64,98°)
a["fy7-11-L3-05"] = delta(1.6498, 64.0, 50.0) - delta(1.6150, 64.0, 50.0)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
