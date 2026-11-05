"""Every answer in exercises.json for fy5-16, computed from the task data (python -I answers.py).
Rules from the lesson: equal sources add intensities (L = L1 + 10 dB · lg N), a point source in free field loses
6 dB per doubling of distance (I ∝ 1/r², 10 dB · lg 4 = 6,02 dB, rounded to 6 dB as in the chapter Äänen voimakkuus),
and the allowed daily exposure is t = 8 h / 2^n with n = (L − 85 dB)/(3 dB) (equal-energy rule of thumb).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math


def t_allowed(L):                                          # hours: 85 dB -> 8 h, every +3 dB halves the time
    return 8.0 / 2 ** ((L - 85) / 3)


a = {}
# Level 1: one formula or one rule, values given
a["fy5-16-L1-01"] = t_allowed(91)                          # drill at 91 dB: n = 6 dB / 3 dB = 2, t = 8 h / 4 = 2,0 h
a["fy5-16-L1-02"] = 70 + 3                                 # two equal fans: intensity doubles, +3 dB -> 73 dB (10 lg 2 = 3,01)
a["fy5-16-L1-03"] = 88 - 6                                 # 4,0 m -> 8,0 m doubles the distance: -6 dB -> 82 dB
a["fy5-16-L1-04"] = 106 - 23                               # jackhammer 106 dB, protectors attenuate 23 dB -> 83 dB at the ear
# L1-05: source, path, receiver of four measures: answered in words
# L1-06: which measure shortens the reverberation time (multiple choice): answered in words
a["fy5-16-L1-07"] = 68 - 41                                 # outside 68 dB, inside 41 dB: the wall and windows attenuate 27 dB
# L1-08: how a loudspeaker produces sound (multiple choice): answered in words
# Level 2: two steps, a conversion or a rearrangement
a["fy5-16-L2-01"] = t_allowed(85 + 3)                      # two machines of 85 dB: 88 dB, then t = 8 h / 2 = 4,0 h
a["fy5-16-L2-02"] = 1.5 / t_allowed(94) * 100              # earbuds 94 dB for 1,5 h: allowed 1,0 h, dose 1,5 h : 1,0 h = 150 %
a["fy5-16-L2-03"] = 2.0 * 2 ** ((78 - 60) / 6)             # lawnmower 78 dB at 2,0 m, wanted 60 dB: 18 dB = three doublings, r = 2,0 m · 8 = 16 m
a["fy5-16-L2-04"] = 0.45 * 60 / (92 - 62)                  # decay 30 dB in 0,45 s at a steady rate: T = 0,45 s · 60/30 = 0,90 s
dT1 = 90.3 - 74.4                                           # level drop before the panels in 0,40 s: 15,9 dB
dT2 = 90.2 - 50.1                                           # level drop after the panels in 0,40 s: 40,1 dB
a["fy5-16-L2-05"] = (1 - dT1 / dT2) * 100                   # T = 60/dL * 0,40 s: 1,51 s and 0,599 s; shortened by 60,3 %
a["fy5-16-L2-06"] = (60.3 - 35.1) - (68.4 - 55.0)   # attenuation 25,2 dB at 4000 Hz minus 13,4 dB at 500 Hz = 11,8 dB
a["fy5-16-L2-07"] = round(t_allowed(109) * 60, 1)       # 109 dB: n = 24 dB / 3 dB = 8, t = 480 min / 2^8 = 1,875 min = 1,9 min (student: 8 h / 8 = 1,0 h)
# Level 3: reasoning or an unfamiliar context
a["fy5-16-L3-01"] = (4.0 / t_allowed(88) + 4.0 / t_allowed(82)) * 100   # 4 h at 88 dB (1/1 of 4 h) + 4 h at 82 dB (allowed 16 h): 100 % + 25 % = 125 %
L_one = 55 - 6 * math.log2(12 / 3.0)                      # one heat pump 55 dB at 3,0 m, window at 12 m: two doublings, -12 dB -> 43 dB
a["fy5-16-L3-02"] = L_one + 3                               # two equal units: intensity doubles, +3 dB -> 46 dB
D_shop = 1.0 / t_allowed(97) + 2.0 / t_allowed(91) + 3.0 / t_allowed(85)   # sawing 2,0 + planing 1,0 + assembling 0,375 = 3,375 (dose 340 %)
a["fy5-16-L3-04"] = 3 * math.log2(D_shop)                   # protectors divide the dose by 2^(dL/3 dB) -> dL >= 3 dB · log2 3,375 = 5,3 dB
L_fest = 112 - 6 * math.log2(8.0 / 2.0)                     # speaker 112 dB at 2,0 m, listener at 8,0 m: two doublings -> 100 dB
a["fy5-16-L3-05"] = t_allowed(L_fest - 8)                   # earplugs 8 dB -> 92 dB: n = 7/3, t = 8 h / 2^(7/3) = 1,59 h (3,0 h = 190 %; at 16 m 86 dB: 6,35 h, 47 %)
# L3-03: why active noise cancellation works best at low frequencies: answered in words
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
