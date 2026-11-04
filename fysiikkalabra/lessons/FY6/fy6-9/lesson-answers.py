"""Numbers of the lesson text and inquiry.json for fy6-9, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Capacity Q = I t (1 Ah = 3600 C), energy W = U Q (1 Wh = 3600 J).
Charging circuit: a charger of constant voltage U_lat with the resistance R of the charger and its leads, and a
battery of source voltage E and internal resistance R_s. Voltage law: U_lat - R I - R_s I - E = 0, so
I = (U_lat - E) / (R + R_s); terminal voltage U = E + R_s I while charging (E - R_s I while discharging).
The simulation's cell: E rises linearly with its charge q from E0 = 3,40 V (empty) to E1 = 4,20 V (full), capacity
2,0 Ah, R_s = 0,10 ohm. With x = U_lat - E: dq/dt = x / Rt and dx/dt = -k dq/dt, k = 0,40 V/Ah, so
x(t) = x0 exp(-k t / Rt). Stored (chemical) energy = integral of E dq; the charger gives U_lat (q - q0).
Prints {id: number} as JSON."""
import json, math

E0, E1, QCAP, RS = 3.40, 4.20, 2.0, 0.10
K = (E1 - E0) / QCAP                                          # 0,40 V per Ah
a = {}


def cell(U, R, start, t):
    """State of the simulated cell after t hours of charging from start (0..1) with charger U and resistance R."""
    Rt = R + RS
    q0 = start * QCAP
    x0 = U - (E0 + K * q0)
    x = x0 * math.exp(-K * t / Rt)
    q = q0 + (x0 - x) / K
    t_full = Rt / K * math.log(x0 / (U - E1)) if x0 > 0 and U > E1 else float("inf")
    if x0 > 0 and q >= QCAP: q, x = QCAP, 0.0                   # full: the charger stops
    if x0 < 0 and q <= 0: q, x = 0.0, 0.0                       # empty: the protection stops the discharge
    E = E0 + K * q
    I = x / Rt
    Wlat = U * (q - q0)                                         # Wh from the charger
    Wkem = E0 * (q - q0) + K / 2 * (q * q - q0 * q0)            # Wh stored chemically
    return dict(I=I, E=E, Uterm=E + RS * I, q=q, soc=q / QCAP * 100, Wlat=Wlat, Wkem=Wkem, Whav=Wlat - Wkem,
                Ws=(Wlat - Wkem) * RS / Rt, eta=Wkem / Wlat * 100 if Wlat > 0 else 0, tfull=t_full)


# --- the simulation on load: U_lat = 4,5 V, R = 0,40 ohm, empty cell, t = 0 ---
s = cell(4.5, 0.40, 0.0, 0.0)
a["sim-I"] = s["I"]                                           # (4,5 V - 3,40 V) : 0,50 ohm = 2,2 A
a["sim-E"] = s["E"]                                           # 3,40 V
a["sim-U"] = s["Uterm"]                                       # 3,40 V + 0,10 ohm · 2,2 A = 3,62 V
a["sim-RI"] = 0.40 * s["I"]                                   # potential drop in R: 0,88 V (Kaava potential graph)
a["sim-RsI"] = RS * s["I"]                                    # in R_s: 0,22 V
a["sim-tfull"] = s["tfull"]                                   # 1,25 h · ln(1,1 : 0,30) = 1,624 h
a["sim-tfull-min"] = s["tfull"] * 60                          # 97 min
f = cell(4.5, 0.40, 0.0, 4.0)                                 # charged to full
a["full-I-end"] = (4.5 - E1) / 0.50                           # current just before the charger stops: 0,60 A
a["full-Wlat"] = f["Wlat"]                                    # 4,5 V · 2,0 Ah = 9,0 Wh (energy-flow figure)
a["full-Wkem"] = f["Wkem"]                                    # mean E 3,80 V · 2,0 Ah = 7,6 Wh
a["full-Whav"] = f["Whav"]                                    # 1,4 Wh
a["full-Ws"] = f["Ws"]                                        # in the cell: 0,28 Wh
a["full-WR"] = f["Whav"] - f["Ws"]                            # in the charger and leads: 1,12 Wh
a["full-eta"] = f["eta"]                                      # 84 %
# hook: at 90 % the current is a third of the start
a["soc90-I"] = (4.5 - (E0 + K * 1.8)) / 0.50                  # (4,5 - 4,12) : 0,50 = 0,76 A

# --- experiment 1: t varied (U_lat 4,5 V, R 0,40 ohm, empty start) ---
for t in (0.0, 0.5, 1.0, 1.5):
    c = cell(4.5, 0.40, 0.0, t)
    a[f"koe1-t{t}-I"] = c["I"]                                # 2,2 / 1,475 / 0,988 / 0,663 A
    a[f"koe1-t{t}-E"] = c["E"]                                # 3,40 / 3,763 / 4,006 / 4,169 V
    a[f"koe1-t{t}-U"] = c["Uterm"]
    a[f"koe1-t{t}-soc"] = c["soc"]                            # 0 / 45 / 76 / 96 %

# --- experiment 2: U_lat varied, cell at 80 % (E = 4,04 V), t = 0 ---
a["koe2-E"] = E0 + K * 1.6                                    # 4,04 V
for U in (3.6, 4.0, 4.2, 4.6):
    a[f"koe2-U{U}-I"] = cell(U, 0.40, 0.8, 0.0)["I"]          # -0,88 / -0,08 / 0,32 / 1,12 A

# --- experiment 3 (optional): U_lat varied, full charge from empty (t = 4,0 h) ---
for U in (4.4, 4.6, 5.0):
    c = cell(U, 0.40, 0.0, 4.0)
    a[f"koe3-U{U}-tfull"] = c["tfull"]                        # 2,01 / 1,37 / 0,866 h
    a[f"koe3-U{U}-Wlat"] = c["Wlat"]                          # 8,8 / 9,2 / 10 Wh
    a[f"koe3-U{U}-eta"] = c["eta"]                            # 86 / 83 / 76 %

# --- Ydinajatus: a phone battery 5000 mAh, 3,85 V; the capacity graph 0,50 A for 4,0 h ---
a["phone-Q-C"] = 5.0 * 3600                                   # 5000 mAh = 5,0 Ah = 18 000 C
a["phone-W"] = 3.85 * 5.0                                     # 19,25 Wh
a["phone-W-kJ"] = 3.85 * 5.0 * 3600 / 1000                    # 69,3 kJ
a["graph-Q"] = 0.50 * 4.0                                     # 2,0 Ah
a["Wh-J"] = 1 * 3600
a["ratio-12-3.7"] = 12 / 3.7                                  # the same Ah at 12 V: 3,24 times the energy of 3,7 V
# misconception: power bank 10 000 mAh at 3,7 V against a laptop battery 4000 mAh at 11,4 V
a["mis-pb"] = 3.7 * 10.0                                      # 37 Wh
a["mis-laptop"] = 11.4 * 4.0                                  # 45,6 Wh                                          # 1 Wh = 3600 J

# --- worked example: E = 3,70 V, R_s = 0,10 ohm, U_lat = 4,20 V, R = 0,15 ohm ---
a["ex-I"] = (4.20 - 3.70) / (0.15 + 0.10)                     # 0,50 V : 0,25 ohm = 2,0 A
a["ex-U"] = 3.70 + 0.10 * a["ex-I"]                           # 3,90 V
a["ex-check"] = 4.20 - 0.15 * a["ex-I"]                       # the same 3,90 V from the charger's side

a["ex-noE"] = 4.20 / 0.25                                     # 16,8 A if E were left out (Järkevyys)
a["ex-noE-ratio"] = a["ex-noE"] / a["ex-I"]                   # 8,4 times too much

# --- error spotting: car battery E = 12,4 V, R_s = 0,050 ohm, charger 14,0 V, R = 0,35 ohm; E left out ---
a["virhe-wrong"] = 14.0 / (0.35 + 0.050)                      # 35 A (wrong)
a["virhe-right"] = (14.0 - 12.4) / (0.35 + 0.050)             # 1,6 V : 0,40 ohm = 4,0 A
a["virhe-noRs"] = (14.0 - 12.4) / 0.35                        # 4,57 A if R_s were left out (a small change)

# --- transfer task: power bank 10 000 mAh at 3,7 V, phone 4000 mAh at 3,85 V, 30 % lost ---
Wpb, Wph = 3.7 * 10.0, 3.85 * 4.0                             # 37 Wh and 15,4 Wh
a["siirto"] = 0.70 * Wpb / Wph                                # 1,68 charges
a["siirto-mAh"] = 10000 / 4000                                # 2,5 (mAh compared, no voltage, no loss)
a["siirto-noloss"] = Wpb / Wph                                # 2,40 (no loss)
a["siirto-mAh-loss"] = 0.70 * 10000 / 4000                    # 1,75 (mAh with the loss)
a["siirto-useful"] = 0.70 * Wpb                               # 25,9 Wh reach the phone

# --- check 2: car battery E = 12,6 V, R_s = 0,050 ohm, charger 14,4 V with R = 0,25 ohm ---
a["tarkistus-2"] = (14.4 - 12.6) / (0.25 + 0.050)             # 1,8 V : 0,30 ohm = 6,0 A
a["tarkistus-2-noE"] = 14.4 / 0.30                            # 48 A (E left out)
a["tarkistus-2-noRs"] = 1.8 / 0.25                            # 7,2 A (R_s left out)
a["tarkistus-2-U"] = 12.6 + 0.050 * a["tarkistus-2"]          # terminal voltage 12,9 V
a["tarkistus-2-U2"] = 14.4 - 0.25 * a["tarkistus-2"]          # the same from the charger's side

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
