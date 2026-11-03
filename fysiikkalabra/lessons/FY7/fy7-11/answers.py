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
a["fy7-11-L1-01"] = asin(sin(50.0) / 1.331)          # red light air -> water: α2 = 35,14°
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
b = asin(sin(80.0) / 1.331)                          # red ray at α = 80,0°: β = 47,72°
a["fy7-11-L3-02"] = 4 * b - 2 * 80.0                 # θ = 30,9° < 42,4°: inside the bow
th_p = 4 * asin(sin(59.5) / 1.331) - 2 * 59.5        # red rainbow ray: 42,37°
th_v = 4 * asin(sin(58.8) / 1.343) - 2 * 58.8        # violet rainbow ray: 40,64°
a["fy7-11-L3-03"] = th_p - th_v                      # width of the bow 1,73°
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
