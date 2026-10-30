"""Numbers of the lesson text and inquiry.json for fy4-12, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
import json, math

a = {}
# Lesson text: head-on meeting of the figure (A from 0 m at 3,0 m/s, B from 60 m at −2,0 m/s)
a["lesson-tilanne-t"] = 60 / (3.0 + 2.0)             # 12 s
a["lesson-tilanne-x"] = 3.0 * a["lesson-tilanne-t"]  # 36 m
# Lesson text: car from rest (a = 2,0 m/s²) and cyclist (6,0 m/s) from the same place
a["lesson-kaava-t"] = 2 * 6.0 / 2.0                  # t = 2 v / a = 6,0 s
a["lesson-kaava-x"] = 6.0 * a["lesson-kaava-t"]      # 36 m
a["lesson-kaava-vauto"] = 2.0 * a["lesson-kaava-t"]  # a t = 12 m/s = 2 v
a["lesson-kaava-eroaika"] = 6.0 / 2.0                # speeds equal at t = v / a = 3,0 s
a["lesson-kaava-ero"] = 6.0 * 3.0 - 0.5 * 2.0 * 3.0 ** 2   # greatest gap 9,0 m
# Worked example: cyclist 16 m ahead
d, v, acc = 16.0, 6.0, 2.0
a["inq-example-t"] = (v + math.sqrt(v ** 2 + 2 * acc * d)) / acc      # 8,0 s
a["inq-example-x"] = 0.5 * acc * a["inq-example-t"] ** 2              # 64 m
a["inq-example-xB"] = d + v * a["inq-example-t"]                      # check: 64 m
a["inq-example-vA"] = acc * a["inq-example-t"]                        # 16 m/s
a["inq-example-t-neg"] = (v - math.sqrt(v ** 2 + 2 * acc * d)) / acc  # −2,0 s: before the start
a["inq-example-eroaika"] = v / acc                                     # largest gap at t = 3,0 s
a["inq-example-ero"] = d + v * 3.0 - 0.5 * acc * 3.0 ** 2             # 25 m
# Simulation case 1: A from 10 m at 4,0 m/s, B from 70 m at −2,0 m/s
a["inq-case1-t"] = (70 - 10) / (4.0 + 2.0)           # 10 s
a["inq-case1-x"] = 10 + 4.0 * a["inq-case1-t"]       # 50 m
a["inq-case1-sA"] = 4.0 * a["inq-case1-t"]           # A has gone 40 m
a["inq-case1-sB"] = 2.0 * a["inq-case1-t"]           # B has gone 20 m
a["inq-case1-puoliva"] = (10 + 70) / 2               # halfway: 40 m (the wrong answer of the prediction)
# Case 4: A from 0 at 3,0 m/s, B from 20 m at 5,0 m/s: x_A = x_B at t = −10 s
a["inq-case4-t"] = (20 - 0) / (3.0 - 5.0)            # −10 s
# Case 5: bus from rest a = 1,0 m/s² at 0, runner from −5,0 m at 4,0 m/s
a["inq-case5-t1"] = 4 - math.sqrt(6)                 # 1,55 s
a["inq-case5-t2"] = 4 + math.sqrt(6)                 # 6,45 s
# Transfer task: motorcycle a = 3,0 m/s² from rest, lorry 12 m/s from the same place
a["inq-siirto-t"] = 2 * 12.0 / 3.0                   # 8,0 s
a["inq-siirto-x"] = 12.0 * a["inq-siirto-t"]         # 96 m
a["inq-siirto-v"] = 3.0 * a["inq-siirto-t"]          # 24 m/s
a["inq-siirto-v-virhe"] = 12.0 / 3.0 * 3.0           # mistake: speeds set equal: t = 4,0 s, v = 12 m/s
# Checks
a["inq-check2"] = 30 / (2.0 + 3.0)                   # A from 0 at 2,0 m/s, B from 30 m at −3,0 m/s: 6,0 s
a["inq-check2-virhe1"] = 30 / 2.0                    # mistake: only A's speed, 15 s
a["inq-check2-virhe2"] = 30 / (3.0 - 2.0)            # mistake: speeds subtracted, 30 s
print(json.dumps(a))
