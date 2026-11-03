"""Every answer in exercises.json for fy5-17, computed from the task data (python -I answers.py).
Echo depth d = v t / 2, wavelength λ = v / f, earthquake distance d = vP vS Δt / (vP − vS), shallow-water wave v = √(g h).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}
# Level 1: one formula, values given
a["fy5-17-L1-01"] = 1540 * 91.0e-6 / 2 * 100          # fetal ultrasound echo after 91,0 µs: d = 1540 m/s · 91,0 µs / 2 = 0,07007 m -> 7,01 cm
a["fy5-17-L1-02"] = 1540 / 7.5e6 * 1e3                # 7,5 MHz in soft tissue: λ = 1540 / 7,5e6 m = 2,053e-4 m -> 0,205 mm
a["fy5-17-L1-03"] = 1480 * 32.0e-3 / 2                # echo sounder on a lake, 32,0 ms in water 1480 m/s: d = 23,68 m -> 23,7 m
a["fy5-17-L1-04"] = 343 * 15e-3 / 2                   # bat, echo from a moth after 15 ms in air: d = 2,5725 m -> 2,6 m
a["fy5-17-L1-05"] = math.sqrt(g * 50)                 # tsunami over a 50 m deep shelf: v = √(9,81 · 50) m/s = 22,15 m/s -> 22 m/s
# Level 2: two steps, a reading or a rearrangement
dt = 30 - 12                                          # figure fy5-17/seismogrammi-ex: P at 12 s, S at 30 s -> Δt = 18 s
a["fy5-17-L2-01"] = 7.0 * 4.0 * dt / (7.0 - 4.0)      # vP = 7,0 and vS = 4,0 km/s: d = vP vS Δt / (vP − vS) = 28 · 18 / 3 km = 168 km
lam_max = 0.30e-3 / 2                                 # resolution taken as 2λ: λ ≤ 0,30 mm / 2 = 0,15 mm
a["fy5-17-L2-02"] = 1540 / lam_max / 1e6              # f = v / λ = 1540 / 0,15e-3 Hz = 10,27 MHz
t_round = 2 * 0.20 / 1540                             # echo from 20 cm: t = 2 d / v = 2,597e-4 s
a["fy5-17-L2-03"] = 1 / t_round / 1e3                 # at most 1 / t = 3850 pulses per second -> 3,85 kHz
d_quake = 6.0 * 3.5 * 14.0 / (6.0 - 3.5)              # Δt = 14,0 s -> d = 117,6 km
a["fy5-17-L2-04"] = d_quake / 6.0                     # P travel time t_P = d / vP = 19,6 s -> 20 s
# Level 3: reasoning or an unfamiliar context
a["fy5-17-L3-01"] = (343 + 10) * 40e-3 / 2            # bat flying at 10 m/s to a wall, echo after 40 ms: 2d − v_b t = v t -> d = (v + v_b) t / 2 = 7,06 m (stationary bat 6,86 m)
t_fat = 2 * 0.040 / 1450                              # two layers: 4,0 cm of fat at 1450 m/s, there and back: 55,17 µs
d_muscle = 1580 * (80.0e-6 - t_fat) / 2               # the rest of 80,0 µs in muscle at 1580 m/s: 0,01962 m
a["fy5-17-L3-02"] = (0.040 + d_muscle) * 100          # depth below the skin 5,96 cm (one speed 1540 m/s would give 6,16 cm)
a["fy5-17-L3-03"] = 200 * math.sqrt(10 / 4000)        # tsunami period constant: λ = vT ∝ √h, 200 km at 4000 m -> 10,0 km at 10 m
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
