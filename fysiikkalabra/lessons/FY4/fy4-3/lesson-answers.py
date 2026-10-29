"""Numbers of the lesson text and inquiry.json for fy4-3, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Prints {id: number} as JSON on the last line."""
import json, math

g = 9.81
a = {}
# Worked example: two jet engines, each pushes the gases back with 48 kN; level flight at constant velocity
a["ex-Fv-kN"] = 2 * 48                                  # third law: thrust 48 kN per engine; first law: F_v = 2 F_1 = 96 kN
# Simulation (model values): a 10 kg box pushed over 0,50 m to v0, then sliding; constant friction per surface
m, d, v0 = 10.0, 0.50, 3.0
fr = {"matto": 40.0, "puu": 20.0, "jaa": 10.0, "kitkaton": 0.0}
a["sim-G"] = m * g                                      # G = mg = 98,1 N
a["sim-push-a"] = v0 ** 2 / (2 * d)                     # push: v0² = 2 a d → 9,0 m/s²
for k, F in fr.items():
    a[f"sim-push-F-{k}"] = m * a["sim-push-a"] + F      # the hand's force while pushing: 90 N + F_μ (130, 110, 100, 90 N)
    if F > 0:
        dec = F / m                                     # slowing down after release: 4, 2, 1 m/s²
        a[f"sim-s-{k}"] = v0 ** 2 / (2 * dec)           # sliding distance: 1,125 m, 2,25 m, 4,5 m
        a[f"sim-t-{k}"] = v0 / dec                      # sliding time: 0,75 s, 1,5 s, 3,0 s
a["sim-s-kitkaton"] = 12.0                              # no friction: the box reaches the end of the 12 m lane
a["sim-t-kitkaton"] = 12.0 / v0                         # in 4,0 s, still at 3,0 m/s
# Collision graph (example data, figures.py): the largest force between the carts and the contact time
a["data-peak"] = 4.0                                    # N, both sensors (equal and opposite)
a["data-contact"] = 0.15 - 0.05                         # s, 0,10 s
# siirto: a trailer at constant velocity, air resistance 420 N and rolling resistance 260 N
a["inq-siirto"] = 420 + 260                             # first law on the trailer: hitch pulls 680 N forward; third law: trailer pulls the car 680 N back
a["inq-siirto-diff"] = 420 - 260                        # mistake: 160 N
print(json.dumps(a))
