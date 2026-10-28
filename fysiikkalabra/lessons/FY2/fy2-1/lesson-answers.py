"""Numbers of the lesson text and inquiry.json for fy2-1, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. The skateboarder model is the one of the simulation (assets/sims/fy2/fy2-1/sim.js):
a 50 kg point on a parabolic half-pipe (rims 3,0 m high, 9,0 m apart), RK4 with a 2 ms step, friction force mu m g.
Prints {id: number} as JSON on the last line."""
import json, math

g, M, HR, LR = 9.81, 50.0, 3.0, 4.5
A = 2 * HR / LR ** 2
DT, T = 0.002, 16.0
N = round(T / DT)


def run(h0, mu):
    """The whole run: x, u = dx/dt and the thermal energy at every step (as sim.js computes them)."""
    def accel(x, u, sg):
        hp = A * x
        return -(g * hp + hp * A * u * u + mu * g * sg * math.sqrt(1 + hp * hp)) / (1 + hp * hp)
    x, u, eth, stuck = -LR * math.sqrt(h0 / HR), 0.0, 0.0, False
    X, U, E = [x], [u], [eth]
    for _ in range(N):
        if not stuck:
            sg = 1 if u > 0 else -1 if u < 0 else 0
            if sg == 0:
                hp = A * x; sn = hp / math.sqrt(1 + hp * hp)
                if abs(sn) <= mu: stuck = True
                else: sg = -1 if sn > 0 else 1
            if not stuck:
                f = lambda xx, uu: (uu, accel(xx, uu, sg))
                k1 = f(x, u); k2 = f(x + DT / 2 * k1[0], u + DT / 2 * k1[1]); k3 = f(x + DT / 2 * k2[0], u + DT / 2 * k2[1]); k4 = f(x + DT * k3[0], u + DT * k3[1])
                xn = x + DT / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); un = u + DT / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
                if u != 0 and un * u < 0:
                    hp = A * xn
                    if abs(hp / math.sqrt(1 + hp * hp)) <= mu: un = 0.0
                v0 = abs(u) * math.sqrt(1 + (A * x) ** 2); v1 = abs(un) * math.sqrt(1 + (A * xn) ** 2)
                eth += mu * M * g * (v0 + v1) / 2 * DT
                x, u = xn, un
        X.append(x); U.append(0.0 if stuck else u); E.append(eth)
    return X, U, E


def energies(r, t):
    """E_p, E_k, E_lämpö in joules at time t."""
    X, U, E = r
    i = max(0, min(N, round(t / DT)))
    h = HR * X[i] ** 2 / LR ** 2; v = abs(U[i]) * math.sqrt(1 + (A * X[i]) ** 2)
    return M * g * h, 0.5 * M * v * v, E[i]


a = {}
# Simulation, start height 2,0 m: the total energy is m g h0 = 50 kg · 9,81 m/s² · 2,0 m
a["inq-sim-total"] = M * g * 2.0                       # 981 J
free = run(2.0, 0.0)
for t in (1.0, 2.0, 3.0):                              # experiment 1, no friction
    ep, ek, el = energies(free, t)
    a[f"inq-exp1-t{t:g}-Ep"], a[f"inq-exp1-t{t:g}-Ek"], a[f"inq-exp1-t{t:g}-Eth"] = ep, ek, el
    a[f"inq-exp1-t{t:g}-sum"] = ep + ek + el
small = run(2.0, 0.04)
for t in (0.0, 8.0, 16.0):                             # experiment 2, small friction
    ep, ek, el = energies(small, t)
    a[f"inq-exp2-t{t:g}-Ep"], a[f"inq-exp2-t{t:g}-Ek"], a[f"inq-exp2-t{t:g}-Eth"] = ep, ek, el
    a[f"inq-exp2-t{t:g}-mech"] = ep + ek
    a[f"inq-exp2-t{t:g}-sum"] = ep + ek + el
big = run(2.0, 0.10)
ep, ek, el = energies(big, 16.0)                       # large friction, end of the run
a["inq-big-Ep"], a["inq-big-Ek"], a["inq-big-Eth"] = ep, ek, el
# Inquiry data table: the bouncing ball (invented example): mechanical energy 0,60 J, 0,48 J, 0,38 J, 0,31 J after bounces 0 … 3
a["inq-data"] = 0.60 - 0.31                            # converted to thermal energy in three bounces: 0,29 J
# Transfer task: cyclist climbing at constant speed: 420 kJ of chemical energy, 85 kJ of potential energy gained
a["inq-siirto"] = 420 - 85                             # 335 kJ of thermal energy
# Check 2: a bulb takes 2,5 kJ of electrical energy and gives 0,12 kJ of visible light
a["inq-check2"] = (2.5 - 0.12) * 1000                  # 2380 J of thermal energy -> 2,4 · 10^3 J (two significant figures)
# Worked example: potential energy 840 J at the rim, kinetic energy 0,72 kJ = 720 J at the bottom
a["inq-example"] = 840 - 0.72 * 1000                   # 120 J of thermal energy
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
