"""Numbers of the lesson text and inquiry.json for fy6-2, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. A multimeter's error limit (valmistajan ilmoittama virheraja)
±(p % of the reading + n digits) is Δx = p · x + n · r, r the resolution of the range; the relative limit is Δx : x.
The simulation: an ideal battery of N cells of 1,5 V, a lamp 15 Ω and a resistor 30 Ω in series; the meter's own
resistance is 10 MΩ on the voltage ranges, 1,0 Ω on 200 mA and 0,010 Ω on 10 A. Prints {id: number} as JSON."""
import json

RL, RR, RV, RA_mA, RA_A = 15.0, 30.0, 10e6, 1.0, 0.010
par = lambda a, b: a * b / (a + b)
limit = lambda x, pct, digits, res: pct / 100 * x + digits * res      # error limit Δx = p·x + n·r
a = {}

# --- simulation, three cells U0 = 4,5 V ---
U0 = 3 * 1.5
a["sim-I-mA200"] = U0 / (RL + RR + RA_mA) * 1000          # ammeter 200 mA in either gap: 97,83 mA -> 97,8 on the display
a["sim-I-A10"] = U0 / (RL + RR + RA_A)                    # ammeter 10 A: 0,09998 A -> 0,10
a["sim-I-nometer"] = U0 / (RL + RR) * 1000                # without a meter in series: 100 mA
a["sim-UL"] = U0 * par(RL, RV) / (par(RL, RV) + RR)       # voltmeter across the lamp: 1,500 V
a["sim-UR"] = U0 * par(RR, RV) / (par(RR, RV) + RL)       # across the resistor: 3,000 V (OL on the 2 V range)
a["sim-V-series"] = U0 * RV / (RV + RL + RR)              # voltmeter in series: 4,49998 V -> 4,50 on 20 V
a["sim-I-V-series-uA"] = U0 / (RV + RL + RR) * 1e6        # the current then: 0,45 µA, the lamp is out
Rp = par(RL, RA_mA); I = U0 / (Rp + RR)
a["sim-lamp-short-mA"] = I * Rp / RA_mA * 1000            # ammeter 200 mA across the lamp: 136,4 mA through the meter
a["sim-lamp-short-IL-mA"] = I * Rp / RL * 1000            # the lamp's own current then 9,09 mA (power 1,2 mW: dark)
Rp = par(RR, RA_mA); I = U0 / (Rp + RL)
a["sim-res-short-mA"] = I * Rp / RA_mA * 1000             # ammeter 200 mA across the resistor: 272,7 mA > 199,9 mA: fuse
a["sim-bat-short-A"] = U0 / RA_mA                         # ammeter 200 mA across the battery: 4,5 A: fuse
a["sim-PL-nom"] = (U0 / (RL + RR)) ** 2 * RL              # the lamp's power without a meter: 0,150 W

# --- Kaava: the same lamp voltage on two ranges (worked example and the figure error-bands) ---
a["ex-d20"] = limit(1.50, 0.5, 2, 0.01)                   # 20 V range, 1,50 V: 0,0075 + 0,02 = 0,0275 V -> 0,028 V
a["ex-d2"] = limit(1.500, 0.5, 2, 0.001)                  # 2 V range, 1,500 V: 0,0075 + 0,002 = 0,0095 V
a["ex-rel20"] = a["ex-d20"] / 1.50 * 100                  # 1,83 %
a["ex-rel2"] = a["ex-d2"] / 1.500 * 100                   # 0,633 %
a["ex-ratio"] = a["ex-d20"] / a["ex-d2"]                  # 2,9: the smaller range is about three times as exact
a["ex-check"] = 0.005 * 1.5                               # the percentage part alone 0,0075 V on both ranges

# --- inquiry ---
a["siirto-d"] = limit(0.02, 2.0, 3, 0.01)                 # LED 0,02 A on the 10 A range: 0,0004 + 0,03 = 0,0304 A
a["siirto"] = a["siirto-d"] / 0.02 * 100                  # 152 % of the reading
a["siirto-m-pct"] = 2.0                                   # mistake: the percentage part only
a["siirto-m-digit"] = limit(0.02, 2.0, 3, 0.001) / 0.02 * 100   # mistake: digit 0,001 A: 17 %
a["siirto-mA200-d"] = limit(18.6, 1.0, 2, 0.1)            # the same LED on 200 mA: 0,186 + 0,2 = 0,386 mA
a["siirto-mA200-rel"] = a["siirto-mA200-d"] / 18.6 * 100  # 2,1 %
a["tark2"] = limit(0.846, 0.5, 2, 0.001) * 1000           # 2 V range 0,846 V: 4,23 mV + 2 mV = 6,23 mV
a["tark2-m-pct"] = 0.005 * 0.846 * 1000                   # mistake: the percentage part only, 4,23 mV
a["tark2-m-20V"] = limit(0.846, 0.5, 2, 0.01) * 1000      # mistake: the 20 V range's digit, 24,2 mV
a["virhe-wrong"] = 0.005 * 6.00 + 2                       # error spotting: 2 V instead of 2 digits: 2,03 V
a["virhe-right"] = limit(6.00, 0.5, 2, 0.01)              # 0,03 + 0,02 = 0,050 V
a["exit-d"] = limit(3.00, 0.5, 2, 0.01)                   # exit ticket: 3,00 V on 20 V: 0,035 V
print(json.dumps({k: round(v, 8) for k, v in a.items()}))
