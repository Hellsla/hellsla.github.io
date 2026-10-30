"""Numbers of the lesson text and inquiry.json for fy4-9, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. The positive direction is the direction of the first motion unless a line says
otherwise; momentum p = m v, impulse I = F Δt, impulse principle Δp = I. Prints {id: number} as JSON."""
import json, math

a = {}
# The simulation's model (assets/sims/fy4/fy4-9/sim.js): a cart of mass m moves to the right (+x) at v1 on a level
# track without friction and hits a bumper of spring constant k at the wall. While the bumper is pressed by x, its
# force on the cart is F = k x to the left. "pysahtyy": a crushable bumper that does not spring back, so the cart stops
# when its velocity reaches 0; "kimpoaa": a spring bumper that pushes the cart back until it leaves the bumper.
# RK4 steps of 0,1 ms of simulated time; the impulse I is the area under the recorded force (trapezoids), with the
# minus sign of a force pointing to the left; Δt from the first contact to the end of the contact.
K = {"kova": 1600.0, "keski": 400.0, "pehmea": 100.0}
def run(m, v1, k, tyyppi, dt=1e-4):
    x, v, t, area, F_prev, Fmax = 0.0, v1, 0.0, 0.0, 0.0, 0.0
    acc = lambda xx: -k * max(xx, 0.0) / m
    while True:
        k1x, k1v = v, acc(x); k2x, k2v = v + dt / 2 * k1v, acc(x + dt / 2 * k1x)
        k3x, k3v = v + dt / 2 * k2v, acc(x + dt / 2 * k2x); k4x, k4v = v + dt * k3v, acc(x + dt * k3x)
        xn, vn = x + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x), v + dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        if tyyppi == "pysahtyy" and vn <= 0:                     # stops: interpolate the moment v = 0
            f = v / (v - vn); xs = x + f * (xn - x); Fs = k * xs
            area += (F_prev + Fs) / 2 * f * dt; t += f * dt; Fmax = max(Fmax, Fs); v2 = 0.0; break
        if tyyppi == "kimpoaa" and xn <= 0 and vn < 0:           # leaves the bumper: interpolate the moment x = 0
            f = x / (x - xn); area += F_prev / 2 * f * dt; t += f * dt; v2 = v + f * (vn - v); break
        Fn = k * xn; area += (F_prev + Fn) / 2 * dt; F_prev = Fn; Fmax = max(Fmax, Fn); x, v, t = xn, vn, t + dt
    I = -area
    return {"dt": t, "Fmax": Fmax, "I": I, "v2": v2, "dp": m * v2 - m * v1, "Fka": area / t}

# prediction 1 / experiment 1: m = 1,0 kg, v1 = 2,0 m/s, the cart stops; bumper hard, medium, soft
for b in K:
    r = run(1.0, 2.0, K[b], "pysahtyy")
    a[f"exp1-{b}-dt"] = r["dt"]          # kova 0,0393 s, keski 0,0785 s, pehmea 0,157 s (π/2 · √(m/k))
    a[f"exp1-{b}-Fmax"] = r["Fmax"]      # 80,0 N, 40,0 N, 20,0 N (v1 · √(m k))
    a[f"exp1-{b}-I"] = r["I"]            # −2,00 N·s in every case
    a[f"exp1-{b}-Fka"] = r["Fka"]        # mean force |I| / Δt: 50,9 N, 25,5 N, 12,7 N
a["exp1-dp"] = 1.0 * 0 - 1.0 * 2.0       # Δp = m v2 − m v1 = −2,00 kg·m/s
# prediction 2 / experiment 2: m = 1,0 kg, v1 = 2,0 m/s, medium bumper; stops or bounces back
for ty in ("pysahtyy", "kimpoaa"):
    r = run(1.0, 2.0, K["keski"], ty)
    a[f"exp2-{ty}-I"] = r["I"]           # −2,00 N·s and −4,00 N·s
    a[f"exp2-{ty}-dt"] = r["dt"]         # 0,0785 s and 0,157 s
    a[f"exp2-{ty}-Fmax"] = r["Fmax"]     # 40,0 N in both
    a[f"exp2-{ty}-v2"] = r["v2"]         # 0 and −2,00 m/s
# experiment 3 (optional): medium bumper, the cart stops, v1 = 2,0 m/s, mass 0,50 / 1,0 / 2,0 kg
for m in (0.5, 1.0, 2.0):
    r = run(m, 2.0, K["keski"], "pysahtyy")
    a[f"exp3-{m}-I"] = r["I"]            # −1,00, −2,00, −4,00 N·s
    a[f"exp3-{m}-Fmax"] = r["Fmax"]      # 28,3 N, 40,0 N, 56,6 N
    a[f"exp3-{m}-dt"] = r["dt"]          # 0,0555 s, 0,0785 s, 0,111 s
# the largest compression in the model (m = 2,0 kg, v1 = 2,0 m/s, soft bumper): v1 √(m/k) = 0,283 m < 0,32 m bumper
a["sim-xmax"] = 2.0 * math.sqrt(2.0 / 100.0)
a["sim-dt-longest"] = math.pi * math.sqrt(2.0 / 100.0)   # the longest contact: 0,444 s, inside the graph's 0,5 s
a["sim-Fmax-largest"] = 2.0 * math.sqrt(2.0 * 1600.0)    # the largest force: 113 N, inside the graph's 120 N

# Ydinajatus figure: a football 0,45 kg at 20 m/s and a bowling ball 6,0 kg at 1,5 m/s have equal momenta
a["fig-p-pallo"] = 0.45 * 20             # 9,0 kg·m/s
a["fig-p-keila"] = 6.0 * 1.5             # 9,0 kg·m/s
a["fig-p-vasen"] = 0.45 * -10            # the football to the left at 10 m/s: −4,5 kg·m/s
# Kaava: the units: 1 N·s = 1 kg·m/s² · s = 1 kg·m/s (no number)
# Kaava text: a constant force 4,0 N for 0,50 s on a 2,0 kg cart: I = 2,0 N·s, Δv = 1,0 m/s
a["kaava-I"] = 4.0 * 0.50
a["kaava-dv"] = 4.0 * 0.50 / 2.0
# Kaava figure: a ball of 0,50 kg hits a wall at 4,0 m/s and bounces back at 4,0 m/s: Δp = −4,0 kg·m/s
a["fig-kimpo-p1"] = 0.50 * 4.0
a["fig-kimpo-dp"] = 0.50 * (-4.0) - 0.50 * 4.0

# Worked example: a tennis ball 58 g arrives at 25 m/s and leaves the racket at 35 m/s the other way in 4,0 ms;
# the positive direction is the direction after the hit, so v1 = −25 m/s and v2 = +35 m/s
m, v1, v2, dt = 0.058, -25.0, 35.0, 4.0e-3
a["ex-dp"] = m * v2 - m * v1             # 3,48 kg·m/s
a["ex-F"] = (m * v2 - m * v1) / dt       # 870 N
a["ex-G"] = m * 9.81                     # the ball's weight 0,569 N: about 1/1500 of the force
a["ex-ratio"] = a["ex-F"] / a["ex-G"]    # 1529
a["ex-wrong"] = m * (35.0 - 25.0) / dt   # the sign error: 145 N
a["ex-Gimp"] = m * 9.81 * dt             # the weight's impulse during the contact 0,0023 N·s ≪ 3,48 N·s

# Retrieval: 2,0 kg cart, net force 6,0 N for 0,50 s: a = 3,0 m/s², Δv = a Δt = 1,5 m/s
a["kertaus-dv"] = 6.0 / 2.0 * 0.50
# Etsi virhe: a 0,40 kg ball hits a wall at 5,0 m/s and bounces back at 5,0 m/s
a["virhe-oikea"] = 0.40 * (-5.0) - 0.40 * 5.0   # Δp = −4,0 kg·m/s; the student's 0 is the sign error
# Transfer (siirto): a pesäpallo of 0,16 kg at 25 m/s stopped in the glove in 0,050 s
a["siirto"] = 0.16 * 25 / 0.050          # 80 N
a["siirto-dp"] = 0.16 * 25               # mistake: Δp only, 4,0
a["siirto-kerto"] = 0.16 * 25 * 0.050    # mistake: Δp · Δt = 0,20
a["siirto-ms"] = 0.16 * 25 / 0.0050      # mistake: Δt as 0,0050 s: 800 N
a["siirto-jaykka"] = 0.16 * 25 / 0.010   # a stiff hand that stops the ball in 0,010 s: 400 N
a["siirto-kg"] = 80 / 9.81                # the force equals the weight of about 8 kg
# Check 2: a football 0,45 kg from rest, a triangular force graph with a peak 900 N and a duration 12 ms
a["check2-I"] = 0.5 * 900 * 0.012        # 5,4 N·s
a["check2"] = 0.5 * 900 * 0.012 / 0.45   # 12,0 m/s
a["check2-peak"] = 900 * 0.012 / 0.45    # mistake: the rectangle peak × time: 24 m/s
a["check2-I-only"] = 0.5 * 900 * 0.012   # mistake: the impulse 5,4 as the speed
a["check2-kmh"] = a["check2"] * 3.6       # 43 km/h
a["check2-Fka"] = a["check2-I"] / 0.012  # mean force 450 N, half the peak
a["check2-ms"] = 0.5 * 900 * 12 / 0.45  # mistake: 12 ms used as 12 s: 12 000 m/s
# Check 1: two skaters of 60 kg each at 2,0 m/s in opposite directions: p = +120 and −120 kg·m/s
a["check1-p"] = 60 * 2.0
# Hook: a high jumper of 70 kg falls from 1,8 m (the centre of mass about 1,0 m lower: no number in the text)
print(json.dumps(a))
