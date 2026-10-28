"""Numbers of the lesson text and inquiry.json for fy1-1, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
import json, math

a = {}
# Inquiry numbers (inquiry.json), not exercises
a["inq-exp1-dn"] = -10 - (-15)                       # hydrogen atom 10⁻¹⁰ m, its nucleus (a proton) 10⁻¹⁵ m: Δn = 5
a["inq-exp1-ratio"] = 1.1e-10 / 1.7e-15              # mistake: the factor 6,5·10⁴ is not the number of powers
a["inq-exp2-dn"] = 21 - 13                           # Neptune's orbit 10¹³ m (4,5·10¹² m radius, 9,0·10¹² m across), Milky Way 10²¹ m: Δn = 8
a["inq-exp3-mid"] = (-35 + 27) / 2                   # midpoint of the exponents: −4
a["inq-siirto"] = 360 / 7.2 * 800 / math.pi          # Earth's diameter: C = (360° / 7,2°) · 800 km = 40 000 km, d = C / π = 12 700 km
a["inq-siirto-c"] = 360 / 7.2 * 800                  # mistake: the circumference 40 000 km
a["inq-siirto-r"] = 360 / 7.2 * 800 / math.pi / 2    # mistake: the radius 6370 km
a["inq-siirto-1deg"] = 800 / 7.2                     # mistake: the length of one degree 111 km
a["inq-check2"] = 1.39e9 / 2.4e4                     # Sun / neutron star diameters: k = 1,39·10⁹ m / 2,4·10⁴ m = 5,79·10⁴
a["inq-check2-inv"] = 2.4e4 / 1.39e9                 # mistake: divided the wrong way round, 1,73·10⁻⁵
a["inq-example-k"] = 1.1e-10 / 1.7e-15               # example: k = 1,1·10⁻¹⁰ / 1,7·10⁻¹⁵ = 6,5·10⁴
a["inq-example-dn"] = -10 - (-15)                    # example: Δn = 5
print(json.dumps(a))
