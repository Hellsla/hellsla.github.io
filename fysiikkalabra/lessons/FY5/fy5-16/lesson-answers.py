"""Numbers of the lesson text and inquiry.json for fy5-16, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Exposure rule: t = 8 h / 2^n, n = (L − 85 dB)/(3 dB). Prints {id: number} as JSON."""
import json, math


def t_allowed(L):
    return 8.0 / 2 ** ((L - 85) / 3)


a = {}
a["kertaus-L"] = 90 + 10 * math.log10(2)                   # two equal loudspeakers of 90 dB: 93,0 dB
a["ennuste-1-t"] = t_allowed(94)                           # 94 dB: n = 3, t = 1,0 h
a["ennuste-1-I"] = 2 ** 3                                  # 9 dB = three doublings of intensity: 8-fold
for L in (85, 88, 91, 94, 97, 100):                        # table of the interpret activity and the Kaava graph
    a[f"table-{L}"] = t_allowed(L)                         # 8, 4, 2, 1, 0,5, 0,25 h
a["taulukko-103-min"] = t_allowed(103) * 60                # 103 dB: n = 6, t = 8 h / 64 = 0,125 h = 7,5 min
a["taulukko-100-min"] = t_allowed(100) * 60                # 100 dB: 15 min (mistake feedback)
# interpret 2, invented example data: free field loses 6 dB per doubling: 82, 76, 70, 64 dB at 1, 2, 4, 8 m
a["kentta-8m"] = 82 - 6 * 3
a["luokka-pudotus"] = 82 - 75                              # classroom 82 -> 75 dB over the same 1 -> 8 m: only 7 dB
# worked example: drummer at 100 dB for 2,0 h. 2^n = 8 h / 2,0 h = 4 -> n = 2 -> L_sall = 85 dB + 2 · 3 dB = 91 dB
n_ex = math.log2(8 / 2.0)
a["esim-Lsall"] = 85 + 3 * n_ex                            # 91 dB
a["esim-vaimennus"] = 100 - a["esim-Lsall"]                # 9 dB
a["esim-check-t"] = t_allowed(100 - 9)                     # with the protectors 91 dB: 2,0 h, the rehearsal fits
# transfer: saw 100 dB at 1,0 m, helper at 4,0 m: two doublings, -12 dB -> 88 dB -> 4,0 h
a["siirto-L"] = 100 - 6 * math.log2(4.0 / 1.0)
a["siirto"] = t_allowed(a["siirto-L"])
a["siirto-mistake-nodist"] = t_allowed(100)                # 0,25 h
a["siirto-mistake-one"] = t_allowed(94)                    # 1,0 h: only one doubling (or −3 dB per doubling)
# check 2: concert 106 dB, earplugs attenuate 15 dB -> 91 dB -> 2,0 h
a["tarkistus-2"] = t_allowed(106 - 15)
a["tarkistus-2-mistake-noplug"] = t_allowed(106)           # 106 dB unprotected: 8 h / 2^7 = 0,0625 h = 3,75 min
a["tarkistus-2-mistake-88"] = t_allowed(88)               # 4,0 h: one step only
# decay figure: from 90 dB, T = 1,2 s (bare room) and 0,6 s (panels): 60 dB per T
a["decay-rate-bare"] = 60 / 1.2                            # 50 dB/s
a["decay-rate-panel"] = 60 / 0.6                           # 100 dB/s
# exit ticket: 85 -> 95 dB is 10 dB = tenfold intensity; equal energy: 8 h / 10 = 48 min; by the 3 dB rule 47,6 min
a["exit-I"] = 10 ** (10 / 10)
a["exit-t-min"] = 8 * 60 / 10
a["exit-t-rule-min"] = t_allowed(95) * 60
# loudspeaker: 1 % of 50 W electric power becomes sound power: 0,5 W
a["kaiutin-P"] = 0.01 * 50
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
