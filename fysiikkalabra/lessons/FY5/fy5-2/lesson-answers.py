"""The numbers of lesson.md and inquiry.json for fy5-2 (python -I lesson-answers.py); prints {id: value} as JSON.
Rigid-body equilibrium: ΣF = 0 and ΣM = 0 about any point (anticlockwise positive), g = 9,81 m/s²."""
import json

g = 9.81
r = {}
# --- worked example: log 4,00 m, 60,0 kg carried by A at the front end and B 1,00 m from the rear end
G = 60.0 * g                                     # 588,6 N
r["esim-G"] = G
r["esim-NB"] = G * 2.00 / 3.00                   # moments about A: N_B · 3,00 m = G · 2,00 m -> 392,4 N
r["esim-NA"] = G - r["esim-NB"]                  # ΣF = 0: N_A = G − N_B = 196,2 N

# --- simulation model: plank 4,0 m, 20 kg (CoM at 2,0 m); supports at x1 < x2; box m_k at x_k (positions from the left end)
def plank(x1, x2, xk, mk, mL=20.0, xL=2.0):
    GL, Gk = mL * g, mk * g
    N2 = (GL * (xL - x1) + Gk * (xk - x1)) / (x2 - x1)   # moments about support 1
    N1 = GL + Gk - N2                                    # ΣF = 0
    xpp = (mL * xL + mk * xk) / (mL + mk)                # common centre of mass
    return N1, N2, xpp
# koe-1: no box, x1 = 0,5 m, x2 varied
for x2 in (3.5, 3.0, 2.5):
    N1, N2, _ = plank(0.5, x2, 2.0, 0)
    r[f"koe1-x2={x2}-N1"], r[f"koe1-x2={x2}-N2"] = N1, N2   # 98,1/98,1; 78,48/117,72; 49,05/147,15
# koe-2: box 40 kg, x1 = 0,5 m, x2 = 3,0 m, x_k varied; tips when x_pp > 3,0 m <=> x_k > 3,5 m
for xk in (3.0, 3.2, 3.4, 3.5, 3.6):
    N1, N2, xpp = plank(0.5, 3.0, xk, 40)
    r[f"koe2-xk={xk}-N1"], r[f"koe2-xk={xk}-N2"], r[f"koe2-xk={xk}-xpp"] = N1, N2, xpp
r["koe2-raja-xk"] = (3.0 * 60 - 20 * 2.0) / 40   # x_pp = 3,0 m: x_k = (3,0 · 60 − 20 · 2,0) / 40 = 3,5 m
r["koe2-Gtot"] = 60 * g                          # 588,6 N

# --- siirto: diving board 4,00 m, 30,0 kg (CoM 2,00 m from the bolt), bolt at the rear end, support 1,50 m, diver 60,0 kg at the front end
Gl, Gh = 30.0 * g, 60.0 * g                      # 294,3 N and 588,6 N
r["siirto-N"] = (Gl * 2.00 + Gh * 4.00) / 1.50   # moments about the bolt: N · 1,50 m = Gl · 2,00 m + Gh · 4,00 m -> 1962 N
r["siirto-Fp"] = r["siirto-N"] - Gl - Gh         # ΣF = 0 (up positive): N − Gl − Gh − F_p = 0 -> 1079,1 N
r["siirto-check"] = (Gh * 2.50 + Gl * 0.50) / 1.50   # the same from moments about the support: 1079,1 N
r["siirto-virhe-ei-lautaa"] = Gh * 2.50 / 1.50       # board weight forgotten: 981 N
r["siirto-virhe-merkki"] = (Gh * 2.50 - Gl * 0.50) / 1.50   # board moment with the wrong sign: 882,9 N

# --- check 2: seesaw pivoted at its middle, child 24,0 kg at 1,50 m; the adult presses down at 1,20 m on the other side
r["check2-F"] = 24.0 * g * 1.50 / 1.20           # 294,3 N
r["check2-virhe-varret"] = 24.0 * g * 1.20 / 1.50    # arms swapped: 188,4 N
r["check2-G"] = 24.0 * g                         # 235,4 N (forgot the arms)

# --- error task: plank 4,0 m, 20 kg, supports 0,5 m and 3,0 m (as in the sim): correct N1 and N2
N1, N2, _ = plank(0.5, 3.0, 2.0, 0)
r["virhe-N1"], r["virhe-N2"] = N1, N2            # 78,48 N and 117,72 N, not 98,1 N each

# --- tipping boxes on a 30° slope (Ydinajatus figure): tips when tan θ > b/h
import math
r["kaatuu-tan30"] = math.tan(math.radians(30))   # 0,577
r["kaatuu-matala"] = 0.60 / 0.60                 # b/h = 1,0 > 0,577: stays
r["kaatuu-korkea"] = 0.30 / 0.80                 # b/h = 0,375 < 0,577: tips
print(json.dumps({k: round(v, 6) for k, v in r.items()}))
