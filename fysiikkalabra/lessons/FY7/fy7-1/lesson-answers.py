"""Numbers of the lesson text and inquiry.json for fy7-1, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Fields in µT. Perpendicular fields add as B = sqrt(B1² + B2²); the compass needle
settles along the total horizontal field, θ from north with tan θ = B_east : B_north; Earth's field with the inclination I
has B_h = B cos I and B_v = B sin I. Simulation: two poles 4 cm from the magnet's centre (field ∝ 1/d² each), scaled to
B_m = 30,0 µT on the axis 10 cm from the centre; Earth's horizontal component 14 µT. Prints {id: number} as JSON."""
import json, math

deg = math.degrees
rad = math.radians
a = {}
# Kaava: Earth's field in southern Finland B = 52 µT, I = 74° (WMM2025, rounded)
a["kaava-Bh"] = 52 * math.cos(rad(74))            # 14,3 µT -> about 14 µT
a["kaava-Bv"] = 52 * math.sin(rad(74))            # 50,0 µT
# Kaava figure: B_h = 14 µT north, B_m = 20 µT east
a["fig-B"] = math.hypot(14, 20)                   # 24,4 µT
a["fig-theta"] = deg(math.atan2(20, 14))          # 55,0°
# Tesla table: MRI 3 T against Earth's 50 µT
a["mri-ratio"] = 3 / 50e-6                        # 60 000 (used only in an exercise; kept here for the table's sentence)
# Worked example: B_h = 14 µT, needle turned 52° east, magnet's field east
a["ex-Bm"] = 14 * math.tan(rad(52))               # 17,9 µT -> 18 µT
a["ex-B"] = math.hypot(14, 14 * math.tan(rad(52)))   # Järkevyys: total 22,7 µT = B_h / cos θ
a["ex-B2"] = 14 / math.cos(rad(52))               # the same
a["ex-45"] = 14 * math.tan(rad(45))               # at 45° B_m = B_h

# Simulation model (assets/sims/fy7/fy7-1/sim.js)
A = 0.04
C = 30e-6 / (1 / (0.10 - A) ** 2 - 1 / (0.10 + A) ** 2)
def field(r_cm, phi, s=1, earth=True):
    x, y = r_cm / 100 * math.cos(rad(phi)), r_cm / 100 * math.sin(rad(phi))
    bx = by = 0.0
    for px, q in ((s * A, 1), (-s * A, -1)):
        dx, dy = x - px, y; d3 = math.hypot(dx, dy) ** 3
        bx += q * C * dx / d3; by += q * C * dy / d3
    bx, by = bx * 1e6, by * 1e6
    Bm = math.hypot(bx, by); ty = by + (14 if earth else 0)
    return Bm, math.hypot(bx, ty), deg(math.atan2(bx, ty))
# exp-1: on the axis (φ = 0), N pole east, Earth's field on: B_m and θ by distance
for r in (10, 12, 14, 16, 20, 24):
    Bm, B, th = field(r, 0)
    a[f"exp1-Bm-{r}"] = Bm                       # B_m by distance, printed by the script
    a[f"exp1-th-{r}"] = th                       # 65,0°; 47,9°; 33,2°; 22,9°; 11,6°; 6,2°
a["exp1-question"] = field(10, 0)[0] / field(20, 0)[0]          # B_m(10 cm) : B_m(20 cm) = 10,4
a["exp1-q-readout"] = 30.0 / 2.9                                 # from the readout's rounded values: 10,3
a["exp1-mistake-half"] = 2                                        # "half": ratio 2
a["exp1-mistake-quarter"] = 4                                     # inverse square: ratio 4
a["pred1-half"] = 30.0 / 2                                        # 15 µT
a["pred1-quarter"] = 30.0 / 4                                     # 7,5 µT
# exp-2: r = 14 cm, Earth's field off, N pole east: needle direction around the magnet
for phi in (0, 45, 90, 135, 180, 270):
    Bm, B, th = field(14, phi, earth=False)
    a[f"exp2-th-{phi}"] = th                      # needle directions around the magnet: printed
    a[f"exp2-Bm-{phi}"] = Bm                      # 9,15 µT on the axis, 3,43 µT beside the middle
a["exp2-axis-side-ratio"] = field(14, 0, earth=False)[0] / field(14, 90, earth=False)[0]
# flipped magnet (N pole west), on the axis east, Earth on
a["flip-th-10"] = field(10, 0, s=-1)[2]            # −65,0°
# virhe: B_h 14 µT north, B_m 18 µT east; the student added 14 + 18
a["virhe-wrong"] = 14 + 18                        # 32 µT
a["virhe-right"] = math.hypot(14, 18)             # 22,8 µT
a["virhe-angle"] = deg(math.atan2(18, 14))        # 52,1°
# siirto: A 20 µT east, B 12 µT north, Earth 14 µT north
a["siirto-north"] = 12 + 14                       # 26 µT
a["siirto"] = deg(math.atan2(20, 26))             # 37,6° east of north
a["siirto-B"] = math.hypot(20, 26)                # 32,8 µT
a["siirto-noB"] = deg(math.atan2(20, 14))         # mistake: magnet B left out, 55,0°
a["siirto-noEarth"] = deg(math.atan2(20, 12))     # mistake: Earth left out, 59,0°
a["siirto-inverted"] = deg(math.atan2(26, 20))    # mistake: tan θ inverted, 52,4°
# exit ticket: fridge magnet 5 mT in µT and against Earth's 52 µT
a["exit-uT"] = 5e-3 / 1e-6                         # 5000 µT
a["exit-ratio"] = 5000 / 52                        # about 96, i.e. about a hundred times
print(json.dumps(a))
