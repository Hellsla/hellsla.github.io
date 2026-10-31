"""Numbers of the lesson text and inquiry.json for fy4-10, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Velocities are signed: positive to the right (or in the stated direction).
Prints {id: number} as JSON."""
import json, math

a = {}
# The simulation's model (assets/sims/fy4/fy4-10/sim.js): two gliders 0,20 m long on a level 2,0 m air track, friction
# and air resistance neglected, the weight and the track's normal force cancel. In contact (overlap d = L − (x2 − x1) > 0)
# they push each other with equal and opposite forces F (on 2) and −F (on 1): F = max(0, k d + c (v1 − v2)).
# kimmoisa: spring bumper, c = 0; kimmoton: c = 3,0 N·s/m; tarra (täysin kimmoton): critical damping
# c = 2√(k μ), μ = m1 m2/(m1 + m2), and the gliders stick when v1 − v2 ≤ 0; rajahdys: a spring compressed 4,0 cm
# (k = 300 N/m, 0,24 J) between gliders at rest. Velocity Verlet steps of 0,2 ms of simulated time (model.js uses RK4 with the same step). The "after" values
# are taken when the contact ends (or when they stick).
L, K, C_IN, KR, D0, DT = 0.20, 300.0, 3.0, 300.0, 0.04, 0.0002
def run(m1, m2, v1, v2, typ):
    if typ == "rajahdys": x1, x2, w1, w2 = 1.0 - (L - D0) / 2, 1.0 + (L - D0) / 2, 0.0, 0.0
    else: x1, x2, w1, w2 = 0.40, 1.20, v1, v2
    stuck = contact = False; after = None; t = 0.0
    def force(x1, x2, w1, w2):
        d = L - (x2 - x1)
        if d <= 0: return 0.0
        k = KR if typ == "rajahdys" else K
        c = {"kimmoisa": 0.0, "kimmoton": C_IN, "tarra": 2 * math.sqrt(K * m1 * m2 / (m1 + m2)), "rajahdys": 0.0}[typ]
        return max(0.0, k * d + c * (w1 - w2))
    F = force(x1, x2, w1, w2)
    while t < 12:
        if stuck: x1 += w1 * DT; x2 += w2 * DT
        else:
            w1h, w2h = w1 - F / m1 * DT / 2, w2 + F / m2 * DT / 2
            x1 += w1h * DT; x2 += w2h * DT
            F = force(x1, x2, w1h, w2h)
            w1, w2 = w1h - F / m1 * DT / 2, w2h + F / m2 * DT / 2
            d = L - (x2 - x1)
            if d > 0: contact = True
            if typ == "tarra" and contact and w1 - w2 <= 0:
                V = (m1 * w1 + m2 * w2) / (m1 + m2); w1 = w2 = V; stuck = True; after = (w1, w2)
            elif contact and after is None and d <= 0: after = (w1, w2)
        t += DT
        if x1 - L / 2 <= 0 or x2 + L / 2 >= 2.0: break
    u1, u2 = after
    return {"u1": u1, "u2": u2, "p0": m1 * (0 if typ == "rajahdys" else v1) + m2 * (0 if typ == "rajahdys" else v2),
            "pJ": m1 * u1 + m2 * u2, "Ek0": 0.5 * m1 * v1 ** 2 + 0.5 * m2 * v2 ** 2 if typ != "rajahdys" else 0.0,
            "EkJ": 0.5 * m1 * u1 ** 2 + 0.5 * m2 * u2 ** 2}
# Experiments 1-3: glider 1 0,40 kg at 0,60 m/s, glider 2 at rest; the mass of glider 2 varied
for typ in ("tarra", "kimmoisa", "rajahdys", "kimmoton"):
    for m2 in (0.20, 0.40, 0.60):
        r = run(0.40, m2, 0.60, 0.0, typ)
        for key in ("u1", "u2", "pJ", "EkJ"): a[f"sim-{typ}-{m2:.2f}-{key}"] = r[key]
a["sim-p0"] = 0.40 * 0.60                                   # 0,24 kg·m/s before every collision
a["sim-Ek0"] = 0.5 * 0.40 * 0.60 ** 2                       # 0,072 J before every collision
a["sim-tarra-0.40-Ek-ratio"] = a["sim-tarra-0.40-EkJ"] / a["sim-Ek0"]   # one half of E_k left
a["sim-rajahdys-E"] = 0.5 * KR * D0 ** 2                    # the spring's energy 0,24 J
# prediction 1 distractor: E_k conserved with the gliders stuck together: v' = v/√2
a["pred1-mist-energy"] = 0.60 / math.sqrt(2)               # 0,424 m/s
# Figure "tarra": equal masses, v = 0,60 m/s → v' = 0,30 m/s, p the same (sim-tarra-0.40)
# Kaava: the inline example of a perfectly inelastic collision (the same numbers as the figure and experiment 1)
a["kaava-v"] = 0.40 * 0.60 / (0.40 + 0.40)                  # 0,30 m/s
a["kaava-Ek1"] = 0.5 * 0.80 * a["kaava-v"] ** 2              # 0,036 J
# Worked example: railway wagons, A 32 000 kg at 1,5 m/s catches up with B 18 000 kg at 0,50 m/s, they couple
mA, vA, mB, vB = 32000, 1.5, 18000, 0.50
a["ex-pA"] = mA * vA                                        # 48 000 kg·m/s
a["ex-pB"] = mB * vB                                        # 9000 kg·m/s
a["ex-v"] = (mA * vA + mB * vB) / (mA + mB)                 # 1,14 m/s
a["ex-Ek0"] = 0.5 * mA * vA ** 2 + 0.5 * mB * vB ** 2       # 38 250 J
a["ex-Ek1"] = 0.5 * (mA + mB) * a["ex-v"] ** 2              # 32 490 J
a["ex-dEk"] = a["ex-Ek0"] - a["ex-Ek1"]                     # 5760 J
a["ex-dEk-pct"] = 100 * a["ex-dEk"] / a["ex-Ek0"]           # 15 %
# Ydinajatus: billiards, equal masses, v = 2,0 m/s (illustration only): v1' + v2' = v and v1'^2 + v2'^2 = v^2
# Retrieval (kertaus): impulse 3,0 N for 0,10 s
a["kertaus"] = 3.0 * 0.10                                   # Δp = F Δt = 0,30 kg·m/s
# Error-spotting: gliders 0,50 kg at +0,40 m/s and 0,30 kg at −0,60 m/s stick together
a["virhe-right"] = (0.50 * 0.40 + 0.30 * -0.60) / 0.80      # +0,025 m/s
a["virhe-wrong"] = (0.50 * 0.40 + 0.30 * 0.60) / 0.80       # 0,475 m/s without the sign
# Transfer task (siirto): a 50 kg boy jumps from a 120 kg rowing boat at rest at 2,4 m/s
a["siirto"] = 50 * 2.4 / 120                                # 1,0 m/s
a["siirto-mist-same"] = 2.4
a["siirto-mist-total"] = 50 * 2.4 / 170                     # 0,706: the boy's mass added to the boat
a["siirto-mist-inverse"] = 120 * 2.4 / 50                   # 5,76: the ratio upside down
# Check 2: 0,60 kg at +0,50 m/s and 0,20 kg at −0,90 m/s stick together
a["check-2"] = (0.60 * 0.50 + 0.20 * -0.90) / 0.80          # 0,15 m/s
a["check-2-mist-nosign"] = (0.60 * 0.50 + 0.20 * 0.90) / 0.80   # 0,60
a["check-2-mist-onemass"] = (0.60 * 0.50 + 0.20 * -0.90) / 0.60  # 0,20
print(json.dumps(a))
