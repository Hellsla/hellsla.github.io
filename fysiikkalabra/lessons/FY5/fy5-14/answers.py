"""Every answer in exercises.json for fy5-14, computed from the task data (python -I answers.py).
Sound in air v = 340 m/s unless the task says otherwise; v = f λ; harmonic series f_n = n f_1; beats f_h = |f1 − f2|;
Doppler, speeds relative to still air: moving source f = f0 v/(v ∓ v_s) (− approaching), moving listener
f = f0 (v ± v_h)/v (+ approaching). Prints {exercise id: number} as JSON on the last line; the lint compares it."""
import json

V = 340.0
a = {}
# Level 1: one formula, values given
a["fy5-14-L1-01"] = 2 * 86.0 / 0.505                      # echo: v = 2d/t = 172,0 m / 0,505 s = 340,6 m/s -> 341 m/s
a["fy5-14-L1-02"] = V / 45.0e3 * 1000                     # bat 45,0 kHz: λ = v/f = 7,556 mm -> 7,56 mm
a["fy5-14-L1-03"] = 4 * 147                               # f4 = 4 f1 = 588 Hz
a["fy5-14-L1-04"] = 415 * V / (V + 15.0)                  # ice-cream van receding: 415 · 340/355 = 397,5 Hz -> 397 Hz
# L1-05 classification (answer in words): 12 Hz infra, 440 Hz audible, 35 kHz ultra, 2,5 MHz ultra
a["fy5-14-L1-08"] = 1 / abs(392 - 398)                    # beats: f_h = 6 Hz, T_h = 1/6 s = 0,167 s
# L1-06, L1-07 multiple choice (answers in words): pitch = frequency; approaching source: constant f > f0
# Level 2: two steps, a conversion or a rearrangement
a["fy5-14-L2-01"] = 262 - 15 / 5.0                        # piano: 15 beats in 5,0 s: f_h = 3,0 Hz; the string is lower: 259 Hz
a["fy5-14-L2-02"] = 1480 / (V / 0.850)                    # f = 340/0,850 = 400 Hz is kept; in water λ = 1480/400 = 3,70 m
a["fy5-14-L2-03"] = 650 * (V + 90.0 / 3.6) / V            # driver 90,0 km/h = 25,0 m/s towards a siren: 697,8 Hz -> 698 Hz
a["fy5-14-L2-04"] = V * (425 / 398 - 1)                   # receding source, f0 = 425 Hz, heard 398 Hz: v_s = 23,07 m/s -> 23 m/s
_fka = (431 + 429 + 432 + 430) / 4                        # horn approaching: mean 430,5 Hz
a["fy5-14-L2-05"] = V * (1 - 392 / _fka)                  # v_s = V (1 - f0/f_ka) = 30,41 m/s -> 30,4 m/s
# L2-06 spectrum peaks 262, 524, 785, 1047, 1309 Hz: f1 = 1309/5 = 261,8 Hz -> 262 Hz
a["fy5-14-L2-06"] = round(1309 / 5)
a["fy5-14-L2-07"] = 500 * V / (V - 30.0)                  # source approaching (not the listener formula): 548,4 Hz -> 548 Hz
# Level 3: reasoning or an unfamiliar context
# L3-01 siren 476 Hz approaching and 404 Hz receding: f1/f2 = (v + v_s)/(v − v_s) -> v_s = v (f1 − f2)/(f1 + f2)
a["fy5-14-L3-01"] = V * (476 - 404) / (476 + 404)         # 27,82 m/s -> 28 m/s
# L3-02 beats 4 Hz with 440 Hz; tightening raises f and the beats speed up to 6 Hz -> the string was above: 444 Hz
a["fy5-14-L3-02"] = 440 + 4
# L3-03 spectrum 147, 441, 735, 1029 Hz: only odd multiples of 147 Hz (answer in words)
# L3-04 blood flow: f = f0 (v + vb)/(v - vb) -> vb = v df/(2 f0 + df), v = 1540 m/s, f0 = 4,00 MHz, df = 2470 Hz
a["fy5-14-L3-04"] = 1540.0 * 2470 / (2 * 4.00e6 + 2470)   # 0,4753 m/s -> 0,475 m/s
# L3-05 plucked string: peaks 196, 392, ... 1176 Hz -> f1 = 1176/6 = 196 Hz; v = 2 L f1, L = 0,650 m
a["fy5-14-L3-05"] = 2 * 0.650 * (1176 / 6)            # 254,8 m/s -> 255 m/s
# L1-10 figure fy5-14/spektri-tehtava: peaks at 200, 400, ... 1000 Hz, strongest at 400 Hz; fundamental = lowest = spacing = 200 Hz
a["fy5-14-L1-10"] = 200
# L2-08 figure fy5-14/huojunta-tehtava: loud moments 0,25 s apart -> f_beat = 1 / 0,25 s = 4 Hz; asked quantity is the beat frequency itself
a["fy5-14-L2-08"] = 1 / 0.25
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
