"""Numbers of the lesson text and inquiry.json for fy3-16, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
import json

c_vesi, c_jaa, c_kivi, c_neste = 4190, 2100, 800, 3500   # J/(kg·K): water, ice, sauna stones, glycol-water coolant (given in the tasks)
s, r = 334e3, 2260e3                                      # J/kg: melting and vaporization of water
a = {}
# Inquiry numerics
P_tut = 0.90 * 28                                         # tutki graph: U A = 0,90 W/K, ΔT = 28 K -> P = 25,2 W, plateau t = 334 000 / 25,2 = 13 254 s = 3,68 h
a["tutki-energia"] = 25 * 3.7 * 3600 / 1e3                # E = P t = 25 W · 13 320 s = 333 000 J -> 333 kJ
a["tutki-loyly"] = r * 0.25 / (0.25 * (c_vesi * 90 + r)) * 100   # löyly 0,25 kg, 10 -> 100 °C: 94 275 J + 565 000 J; vaporization share 565 000 / 659 275 = 85,7 % -> 86 %
a["siirto"] = 0.15 * (c_vesi * 80 + r) / 6000             # 0,15 kg löyly, 6,0 kW: t = 0,15 (335 200 + 2 260 000) / 6000 = 64,9 s -> 65 s
a["siirto-virhe-ei-hoyrystysta"] = 0.15 * c_vesi * 80 / 6000   # 8,4 s: vaporization forgotten
a["siirto-virhe-ei-lammitysta"] = 0.15 * r / 6000          # 56,5 s: warming 20 -> 100 °C forgotten
a["check-2"] = (c_jaa * 0.60 * 10 + s * 0.60) / 1e3       # ice pack -10 °C -> water 0 °C: 12 600 + 200 400 = 213 000 J -> 210 kJ
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
