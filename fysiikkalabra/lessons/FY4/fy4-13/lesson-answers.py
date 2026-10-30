"""Numbers of the lesson text and inquiry.json for fy4-13, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. A cart m1 on a smooth table (or a second hanging body) and a hanging body m2, light string,
light frictionless pulley, no air resistance; each body's positive direction is its direction of motion; g = 9,81 m/s². Prints {id: number} as JSON."""
import json, math

g = 9.81
a = {}


def cart(m1, m2):
    """Cart on the table + hanging body: returns a, T."""
    acc = m2 * g / (m1 + m2)                 # cart T = m1 a; body m2 g − T = m2 a  →  a = m2 g/(m1 + m2)
    return acc, m1 * acc


def hang(m1, m2):
    """Two hanging bodies, m2 > m1: returns a, T."""
    return (m2 - m1) * g / (m1 + m2), 2 * m1 * m2 * g / (m1 + m2)     # T − m1 g = m1 a; m2 g − T = m2 a


# Ydinajatus figure and pred-1 (cart 1,0 kg, body 0,50 kg)
acc, T = cart(1.0, 0.50)
a["fig-a"] = acc                              # 3,27 m/s²
a["fig-T"] = T                                # 3,27 N
a["fig-G2"] = 0.50 * g                        # 4,905 N
a["fig-sum2"] = 0.50 * g - T                  # body's net force 1,635 N = m2 a
# exp-1: m2 = 0,50 kg, m1 = 0,50 / 1,0 / 1,5 kg
for m1 in (0.50, 1.0, 1.5):
    acc, T = cart(m1, 0.50)
    a[f"exp1-a-{m1}"] = acc                   # 4,905 / 3,27 / 2,4525 m/s²
    a[f"exp1-T-{m1}"] = T                     # 2,4525 / 3,27 / 3,67875 N
a["exp1-question"] = 0.50 * g - cart(1.0, 0.50)[1]     # net force on the 0,50 kg body at m1 = 1,0 kg: 1,635 N
a["exp1-question-T"] = cart(1.0, 0.50)[1]              # mistake: the tension itself 3,27 N
a["exp1-question-G2"] = 0.50 * g                       # mistake: the weight 4,9 N
# pred-2 / exp-2: hanging 0,30 / 0,50 kg (m2 = 0,50 kg fixed)
acc, T = hang(0.30, 0.50)
a["exp2-a"] = acc                             # 2,4525 m/s²
a["exp2-T"] = T                               # 3,679 N
a["exp2-G1"] = 0.30 * g                       # 2,943 N
a["exp2-G2"] = 0.50 * g                       # 4,905 N
a["exp2-sum"] = T - 0.30 * g                  # net force on the rising body 0,736 N = m1 a
a["exp2-sum-check"] = 0.30 * acc
a["pred2-sumG"] = 0.30 * g + 0.50 * g         # mistake: T = sum of the weights 7,85 N
a["exp2-a-1.0"], a["exp2-T-1.0"] = hang(0.50, 1.0)        # m1 = 1,0 kg is the heavier body: 3,27 m/s², 6,54 N
a["exp2-a-0.5"], a["exp2-T-0.5"] = hang(0.50, 0.50)        # equal masses: 0, 4,905 N
# aineisto: cart 1,0 kg, body 0,50 kg, s = 0,80 m, t = 0,70 s from rest
s, t, m1 = 0.80, 0.70, 1.0
a["data-a"] = 2 * s / t**2                    # s = ½ a t² → a = 2s/t² = 3,265 m/s²
a["data-T"] = m1 * a["data-a"]                # cart: T = m1 a = 3,265 N
a["data-T-noTwo"] = m1 * s / t**2             # mistake: a = s/t² → 1,63 N
a["data-G2"] = 0.50 * g                       # mistake: T = m2 g = 4,9 N
# Esimerkki: cart 1,5 kg, body 0,60 kg
acc, T = cart(1.5, 0.60)
a["ex-a"] = acc                               # 2,803 m/s²
a["ex-T"] = T                                 # 4,204 N
a["ex-G2"] = 0.60 * g                         # 5,886 N
a["ex-sum2"] = 0.60 * g - T                   # 1,682 N
a["ex-sum2-check"] = 0.60 * acc               # = m2 a = 1,682 N
# siirto: cart 1,2 kg, measured a = 2,0 m/s² → m2 = m1 a/(g − a)
a["siirto"] = 1.2 * 2.0 / (g - 2.0)           # 0,3073 kg
a["siirto-T"] = 1.2 * 2.0                     # T = m1 a = 2,4 N
a["siirto-mistake-T"] = 1.2 * 2.0 / g         # mistake: T = m2 g → 0,2446 kg
a["siirto-mistake-plus"] = 1.2 * 2.0 / (g + 2.0)   # mistake: g + a → 0,2032 kg
a["siirto-check-a"] = 0.3073 * g / (1.2 + 0.3073)   # check with the formula: 2,0 m/s²
# check-1: 2,0 kg and 4,0 kg
a["check1-a"] = hang(2.0, 4.0)[0]             # 3,27 m/s²
# check-2: cart 0,60 kg + body 0,80 kg
acc, T = cart(0.60, 0.80)
a["check2"] = T                               # 3,363 N
a["check2-a"] = acc                           # mistake: a 5,61 m/s²
a["check2-G2"] = 0.80 * g                     # mistake: T = m2 g 7,85 N
a["check2-m2a"] = 0.80 * acc                  # mistake: T = m2 a 4,48 N
# check-3 model: 0,40 kg and 0,80 kg
acc, T = hang(0.40, 0.80)
a["check3-a"] = acc                           # 3,27 m/s²
a["check3-T"] = T                             # 5,232 N
a["check3-G1"] = 0.40 * g                     # 3,924 N
a["check3-G2"] = 0.80 * g                     # 7,848 N
print(json.dumps(a))
