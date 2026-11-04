"""Numbers of the lesson text and inquiry.json for fy6-14, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. A series circuit of a source U, a resistor R and a diode or LED: Kirchhoff's loop
U = U_R + U_D, so I = (U - U_D) / R and R = (U - U_D) / I. A solar cell or panel is a DC source; its power P = U I.
The simulation (assets/sims/fy6/fy6-14) uses the same models:
- diode / LED (forward): I = I_s (exp(U_D / m) - 1), I_s chosen so that I = 10 mA at U_ref; the operating point solves
  U = U_D + R I by bisection. Reverse: I = 0 (leakage ignored), U_D = -U.
- solar panel (10 cells in series): I = I_L - I_0 (exp(U / m) - 1), I_L = 0,200 A · G / (1000 W/m^2), I_0 such that the
  open-circuit voltage is 6,0 V at 1000 W/m^2; with a load R the point solves U = R I.
Prints {id: number} as JSON."""
import json
from math import exp, log

COMP = {"piidiodi": (0.70, 0.040), "punainen": (1.90, 0.050), "sininen": (2.90, 0.060)}   # U at 10 mA (V), m (V)
M_PV, ISC, UOC = 0.40, 0.200, 6.0                                                          # panel: m (V), I_k (A), U_t (V) at 1000 W/m^2
I0 = ISC / (exp(UOC / M_PV) - 1)
AREA = 60e-4                                                                               # panel area 60 cm^2 in m^2
a = {}


def led(U, R, c, forward=True):
    """Operating point (U_D in V, I in mA) of source U, resistor R and component c."""
    if not forward: return -U, 0.0
    ur, m = COMP[c]; Is = 0.010 / (exp(ur / m) - 1)
    lo, hi = 0.0, U
    for _ in range(200):
        mid = (lo + hi) / 2
        if mid + R * Is * (exp(mid / m) - 1) > U: hi = mid
        else: lo = mid
    ud = (lo + hi) / 2
    return ud, (U - ud) / R * 1000


def panel(G, R):
    """Operating point (U in V, I in A) of the panel at G (W/m^2) with load R (ohm)."""
    IL = ISC * G / 1000
    if G <= 0: return 0.0, 0.0
    if R <= 0: return 0.0, IL
    lo, hi = 0.0, M_PV * log(IL / I0 + 1)
    for _ in range(200):
        mid = (lo + hi) / 2
        if IL - I0 * (exp(mid / M_PV) - 1) - mid / R > 0: lo = mid
        else: hi = mid
    U = (lo + hi) / 2
    return U, U / R


def u_t(G): return M_PV * log(ISC * G / 1000 / I0 + 1)                                   # open-circuit voltage


# --- the lesson text: thresholds of the components at 10 mA (the (U, I) figure) ---
for c, (ur, m) in COMP.items():
    a[f"kynnys-{c}"] = ur                                                                  # 0,70 / 1,90 / 2,90 V at 10 mA
    Is = 0.010 / (exp(ur / m) - 1)
    a[f"kynnys-{c}-1mA"] = m * log(0.001 / Is + 1)                                         # U at 1 mA: 0,61 / 1,78 / 2,76 V
    a[f"kynnys-{c}-20mA"] = m * log(0.020 / Is + 1)                                        # U at 20 mA: 0,73 / 1,93 / 2,94 V
# --- Kaava: the series resistor; the worked example: 6,0 V, LED 2,0 V, 20 mA ---
U, UD, I = 6.0, 2.0, 0.020
a["esim-UR"] = U - UD                                                                      # U_R = 6,0 V - 2,0 V = 4,0 V
a["esim-R"] = (U - UD) / I                                                                 # R = 4,0 V : 0,020 A = 200 ohm
a["esim-PR"] = (U - UD) * I                                                                # P_R = 4,0 V · 0,020 A = 0,080 W
a["esim-PD"] = UD * I                                                                      # P_D = 2,0 V · 0,020 A = 0,040 W
a["esim-I220"] = (U - UD) / 220 * 1000                                                     # with 220 ohm: 18,2 mA
# --- Ydinajatus: the solar panel of the figure and the sim (G = 1000 and 500 W/m^2) ---
a["kenno-Ik-1000"] = ISC                                                                   # 0,200 A
a["kenno-Ut-1000"] = u_t(1000)                                                             # 6,0 V
a["kenno-Ik-500"] = ISC * 0.5                                                              # 0,100 A: half the light, half the current
a["kenno-Ut-500"] = u_t(500)                                                               # 5,72 V: the voltage falls only 5 %
best = max(range(0, 301), key=lambda R: panel(1000, R)[0] * panel(1000, R)[1])
Ub, Ib = panel(1000, best)
a["mpp-R"] = best                                                                          # 27 ohm (whole ohms)
a["mpp-U"] = Ub                                                                            # 4,98 V
a["mpp-I"] = Ib                                                                            # 0,184 A
a["mpp-P"] = Ub * Ib                                                                       # 0,918 W
a["mpp-Pvalo"] = 1000 * AREA                                                               # light on the panel 1000 W/m^2 · 0,0060 m^2 = 6,0 W
a["mpp-eta"] = Ub * Ib / (1000 * AREA) * 100                                               # efficiency 15 %
a["mpp-500-R"] = max(range(0, 301), key=lambda R: panel(500, R)[0] * panel(500, R)[1])    # 51 ohm at half the light

# --- the simulation on load: LED circuit 5,0 V, 330 ohm, red LED forward; panel 1000 W/m^2, 50 ohm ---
ud, i = led(5.0, 330, "punainen")
a["sim-UD"] = ud                                                                           # 1,897 V
a["sim-I"] = i                                                                             # 9,40 mA
a["sim-UR"] = 5.0 - ud                                                                     # 3,10 V
u, ip = panel(1000, 50)
a["sim-pv-U"] = u                                                                          # 5,67 V
a["sim-pv-I"] = ip * 1000                                                                  # 113 mA
a["sim-pv-P"] = u * ip                                                                     # 0,642 W

# --- koe 1: red LED, R = 330 ohm, U varied ---
for U in (2.0, 3.0, 5.0, 7.0, 9.0):
    ud, i = led(U, 330, "punainen")
    a[f"koe1-U{U}-UD"] = ud                                                                # 1,77 / 1,85 / 1,90 / 1,92 / 1,94 V
    a[f"koe1-U{U}-I"] = i                                                                  # 0,70 / 3,49 / 9,40 / 15,4 / 21,4 mA
    a[f"koe1-U{U}-UR"] = U - ud                                                            # the rest of the voltage over R
a["koe1-I-ratio"] = led(6.0, 330, "punainen")[1] / led(3.0, 330, "punainen")[1]            # 3,55: double U, 3,5 x the current (ennuste-1)
a["koe1-UD-3"] = led(3.0, 330, "punainen")[0]                                              # 1,85 V
a["koe1-UD-6"] = led(6.0, 330, "punainen")[0]                                              # 1,91 V: the LED's voltage barely changes
a["koe1-I-3"] = led(3.0, 330, "punainen")[1]                                               # 3,5 mA
a["koe1-I-6"] = led(6.0, 330, "punainen")[1]                                               # 12,4 mA
# --- koe 2: 5,0 V, 330 ohm, red LED, the direction varied ---
a["koe2-esto-I"] = 0.0                                                                     # reverse: no current
a["koe2-esto-UD"] = -5.0                                                                   # the whole source voltage over the LED
a["koe2-esto-UR"] = 0.0                                                                    # U_R = R I = 0
# --- koe 3: 5,0 V, 330 ohm, the component varied ---
for c in COMP:
    ud, i = led(5.0, 330, c)
    a[f"koe3-{c}-UD"] = ud                                                                 # 0,710 / 1,897 / 2,874 V
    a[f"koe3-{c}-I"] = i                                                                   # 13,0 / 9,40 / 6,44 mA
# --- koe 4: panel at 1000 W/m^2, the load R varied ---
for R in (0, 10, 20, 27, 30, 50, 100, 300):
    u, ip = panel(1000, R)
    a[f"koe4-R{R}-U"] = u                                                                  # 0 / 2,0 / 3,98 / 4,98 / 5,20 / 5,67 / 5,86 / 5,96 V
    a[f"koe4-R{R}-I"] = ip * 1000                                                          # 200 / 200 / 199 / 184 / 173 / 113 / 59 / 20 mA
    a[f"koe4-R{R}-P"] = u * ip                                                             # 0 / 0,40 / 0,79 / 0,92 / 0,90 / 0,64 / 0,34 / 0,12 W
# --- koe 5: the light varied (I_k and U_t shown for every G) ---
for G in (200, 500, 1000):
    a[f"koe5-G{G}-Ik"] = ISC * G / 1000 * 1000                                             # 40 / 100 / 200 mA
    a[f"koe5-G{G}-Ut"] = u_t(G)                                                            # 5,36 / 5,72 / 6,00 V

# --- inquiry: retrieval R = U : I ---
a["kertaus-R"] = 3.0 / 0.015                                                               # 200 ohm
# --- inquiry: Etsi virhe: 9,0 V, LED 2,0 V, 20 mA ---
a["virhe-vaara"] = 9.0 / 0.020                                                             # 450 ohm (the LED's voltage forgotten)
a["virhe-oikea"] = (9.0 - 2.0) / 0.020                                                     # 350 ohm
a["virhe-I-vaara"] = (9.0 - 2.0) / 450 * 1000                                              # with 450 ohm only 15,6 mA
# --- inquiry: siirto, a cabin panel charging a 12 V battery directly ---
Pmpp, Pakku = 18.0 * 5.5, 12.8 * 5.8
a["siirto-Pmpp"] = Pmpp                                                                    # 99 W
a["siirto-Pakku"] = Pakku                                                                  # 74,24 W
a["siirto"] = Pmpp - Pakku                                                                 # 24,76 W lost compared with the maximum
a["siirto-osuus"] = (Pmpp - Pakku) / Pmpp * 100                                            # 25 % of the maximum
# --- inquiry: tarkistus-3, a 4,5 V battery straight to a red LED (1 ohm of internal resistance and wires) ---
a["tark3-I"] = (4.5 - 2.0) / 1.0                                                           # about 2,5 A, over a hundred times 20 mA
# --- exit ticket: I_k 5,0 A and U_t 21 V do not occur together ---
a["exit-tulo"] = 5.0 * 21                                                                  # 105 W is not reached
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
