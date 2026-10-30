"""Numbers of the lesson text and inquiry.json for fy4-14, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Positive direction: down for a falling body (the simulation's too), up for a rising
one, down the slope on the slope; g = 9,81 m/s². Prints {id: number} as JSON."""
import json, math

g = 9.81
a = {}
# The simulation's model (assets/sims/fy4/fy4-14/sim.js): F_v = k v², k = 0,26 kg/m belly down, 0,10 kg/m head down,
# 30 kg/m with the canopy open; the canopy opens at 20 s over 3,0 s (k = k0 + (k1 − k0) s²); Euler steps of 2 ms, 40 s.
K = {"vatsa": 0.26, "paa": 0.10}
def run(m, asento, varjo, tend=40.0, dt=0.002):
    t = v = 0.0; Fmax = 0.0
    def k_at(t):
        k0 = K[asento]
        if varjo != "auki" or t < 20: return k0
        s = min(1.0, (t - 20) / 3.0); return k0 + (30 - k0) * s * s
    while t < tend - 1e-9:
        h = min(dt, tend - t)
        acc = (m * g - k_at(t) * v * v) / m
        v += acc * h; t += h
        Fmax = max(Fmax, k_at(t) * v * v)
    return v, Fmax
for m in (60, 80, 100):
    a[f"sim-vT-{m}"] = run(m, "vatsa", "ei")[0]      # terminal speed belly down: 47,6 / 54,9 / 61,4 m/s (√(mg/k))
    a[f"sim-G-{m}"] = m * g                          # G = mg = 588,6 / 784,8 / 981,0 N, equal to F_v at the end
a["sim-vT-80-paa"] = run(80, "paa", "ei")[0]          # head down: 88,6 m/s
v80, F80 = run(80, "vatsa", "auki")
a["sim-vT-80-varjo"] = v80                            # under the canopy: 5,1 m/s
a["sim-FvMax-80-varjo"] = F80                         # the largest air resistance while the canopy opens: about 3,9 kN
a["sim-FvMax-ratio"] = F80 / (80 * g)                 # about 5 times the weight
a["sim-amax-80-varjo"] = (F80 - 80 * g) / 80          # the largest upward acceleration: about 39 m/s² (4 g)
# Figure "vt" (the same model): the speed after 5 s and 10 s for 60 kg and 100 kg (belly down)
for m in (60, 100):
    for T in (5, 10):
        a[f"fig-v-{m}-{T}"] = run(m, "vatsa", "ei", tend=T)[0]
a["fig-v-free-5"] = g * 5                             # without air resistance: 49,1 m/s after 5 s
# Worked example: the canopy opens, m = 85,0 kg, F_v = 2,40 kN at that moment, the jumper moves down
m, Fv = 85.0, 2400.0
a["ex-G"] = m * g                                     # G = mg = 833,85 N
a["ex-sumF"] = m * g - Fv                             # ΣF = G − F_v = −1566,15 N (up)
a["ex-a"] = (m * g - Fv) / m                          # a = (mg − F_v)/m = −18,43 m/s²: 18,4 m/s² up
a["ex-ratio"] = Fv / (m * g)                          # Järkevyys: F_v is about 2,9 times G
a["ex-check"] = Fv / m - g                            # Järkevyys: F_v/m − g = 28,24 − 9,81 = 18,43 m/s²
# siirto: snowboarder at constant velocity down a 30,0° slope, m = 75,0 kg, snow friction 64,0 N
m, al, Fmu = 75.0, math.radians(30.0), 64.0
a["siirto-Gx"] = m * g * math.sin(al)                 # G along the slope: 367,9 N
a["siirto"] = m * g * math.sin(al) - Fmu              # F_v = mg sin α − F_μ = 303,9 N
a["siirto-nofric"] = m * g * math.sin(al)             # mistake: friction forgotten, 368 N
a["siirto-cos"] = m * g * math.cos(al) - Fmu          # mistake: cos instead of sin, 573 N
a["siirto-mg"] = m * g - Fmu                          # mistake: whole weight along the slope, 672 N
# check-2: jumper under the canopy at a constant 5,5 m/s, m = 64,0 kg
a["check2"] = 64.0 * g                                # F_v = mg = 627,8 N
a["check2-mv"] = 64.0 * 5.5                           # mistake: m·v = 352
# check-3 model figure: a ball thrown down faster than its terminal speed slows down: F_v > G (no numbers in the task)
# Exit ticket and the theory: rising ball, |a| = g + F_v/m > g; falling ball, |a| = g − F_v/m < g (no numbers)
print(json.dumps(a))
