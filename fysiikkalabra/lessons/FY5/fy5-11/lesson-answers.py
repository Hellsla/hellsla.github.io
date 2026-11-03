"""Numbers of lesson.md and inquiry.json of fy5-11, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. The simulation's model (assets/sims/fy5/fy5-11/sim.js) is repeated here so that
the experiments' model values in the feedback come from the same computation. Prints {id: number} as JSON on the last line."""
import cmath, json, math

a = {}


def sources(w, lam):                       # Huygens point sources λ/8 apart (at most) over a gap of width w (sim.js sources)
    N = max(2, math.ceil(w / (lam / 8)))
    return [-w / 2 + w * (j + 0.5) / N for j in range(N)], w / N


def theta_half(b, lam):                    # far-field angle where the gap's amplitude falls to half, 0,1° steps (sim.js thetaHalf)
    ys, _ = sources(b, lam); k = 2 * math.pi / lam
    amp = lambda th: abs(sum(cmath.exp(-1j * k * y * math.sin(th)) for y in ys))
    A0 = amp(0)
    for i in range(901):
        if amp(math.radians(i / 10)) < 0.5 * A0: return i / 10
    return 90.0


def obstacle_AP(b, lam, D=8.0):            # amplitude 8,0 cm behind an obstacle of width b, % of the free wave (Babinet, sim.js obstacleAP)
    ys, dy = sources(b, lam); k = 2 * math.pi / lam
    U = sum(cmath.exp(1j * (k * math.hypot(D, y) - math.pi / 4)) / math.sqrt(lam * math.hypot(D, y)) * dy for y in ys)
    return 100 * abs(cmath.exp(1j * k * D) - U)


# ennuste-1 / koe-1: the ray makes 30° with the wall's surface, so the angle of incidence from the normal is 90° − 30°
a["ennuste1-alpha"] = 90 - 30                                   # 60°
a["ennuste1-beta"] = math.degrees(math.asin(math.sin(math.radians(a["ennuste1-alpha"]))))   # sim: sin β = r1/d = sin α -> 60°
a["koe1-pinta-30"] = 90 - 30                                    # at α = 30° the reflected ray makes 60° with the surface
# koe-2: the rope pulse, A = 3,0 cm; the fixed end inverts it, the free end does not (sim.js image pulse)
A, L, S0, V, SIG = 3.0, 5.0, 1.0, 2.0, 0.2
g = lambda u: math.exp(-u * u / (2 * SIG * SIG))
y = lambda s, t, sgn: A * (g(s - S0 - V * t) + sgn * g(2 * L - s - S0 - V * t))
a["koe2-kiintea-yh"] = y(2 * L - S0 - V * 3.0, 3.0, -1)        # −3,0 cm
a["koe2-vapaa-yh"] = y(2 * L - S0 - V * 3.0, 3.0, +1)          # +3,0 cm
a["koe2-vapaa-paa-max"] = y(L, (L - S0) / V, +1)                # the free end swings to 2A = 6,0 cm as the pulse turns
a["koe2-kesto"] = 2 * (L - S0) / V                              # the pulse is back at 1,0 m after 4,0 s
# koe-3: λ = 2,0 cm, gap b varied: the spreading angle θ
for b in (1.0, 2.0, 4.0, 8.0):
    a[f"koe3-theta-b{b:g}"] = theta_half(b, 2.0)               # 90; 37,4; 17,6; 8,7 degrees
# koe-4: gap b = 3,0 cm, λ varied: θ depends on b/λ
for lam in (1.0, 2.0, 3.0):
    a[f"koe4-theta-l{lam:g}"] = theta_half(3.0, lam)           # 11,7; 23,8; 37,4 degrees
a["koe4-sama-suhde"] = theta_half(6.0, 2.0)                     # b/λ = 3 again: 11,7° as with b = 3,0 cm, λ = 1,0 cm
# the obstacle (free exploration, model text): amplitude at P 8,0 cm behind it, λ = 2,0 cm
for b in (1.0, 2.0, 8.0):
    a[f"este-AP-b{b:g}"] = obstacle_AP(b, 2.0)                  # 84 %, 71 %, 30 %
# Esimerkki: wavefronts at 50° to the breakwater: α = 50°, β = 50°, reflected ray at 90° − 50° = 40° to the surface
a["esim-alpha"] = 50
a["esim-beta"] = 50
a["esim-pinta"] = 90 - 50
# siirto: two walls at a right angle; the ray reflected from wall 1 (α1 = 35°) meets wall 2 at α2 = 90° − α1
a["siirto-alpha2"] = 90 - 35                                    # 55°
# tarkistus-2: tank wave f = 6,0 Hz, v = 0,18 m/s; gap 4,5 cm: λ = v/f, b/λ
lam_t = 0.18 / 6.0                                              # 0,030 m = 3,0 cm
a["tarkistus2-lambda-cm"] = lam_t * 100
a["tarkistus2-suhde"] = 0.045 / lam_t                           # 1,5
a["tarkistus2-virhe-f"] = 0.045 / (6.0 / 0.18)                  # mistake λ = f/v = 33,3 m: b/λ = 0,00135
a["tarkistus2-theta"] = theta_half(4.5, 3.0)                    # Järkevyys: the model spreads b/λ = 1,5 over θ ≈ 24°
a["tarkistus2-virhe-cm"] = 4.5 / (0.18 / 6.0)                   # mistake: b in cm, λ in m: 150
# kertaus: f doubled at the same v halves λ = v/f
a["kertaus-lambda"] = 0.20 / 10                                 # 0,20 m/s at 10 Hz: 0,020 m = 2,0 cm
a["kertaus-lambda-2"] = 0.20 / 20                               # at 20 Hz: 1,0 cm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
