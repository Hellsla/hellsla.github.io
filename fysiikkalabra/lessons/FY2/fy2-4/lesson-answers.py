"""Numbers of the lesson text and inquiry.json for fy2-4, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model as there. Prints {id: number} as JSON on the last line."""
import json

a = {}
# Lesson text: the filament lamp of the Sankey figure (100 J in, eta = 5 %), the lamp pair of the second figure
a["fig1-Ea"] = 0.05 * 100                                  # useful light energy from 100 J: 5 J
a["fig1-Eh"] = 100 - 0.05 * 100                            # heat: 95 J
a["fig2-led-Po"] = 3.0 / 0.30                              # LED lamp giving 3,0 W of light: 3,0 W / 0,30 = 10 W
a["fig2-bulb-Po"] = 3.0 / 0.05                             # filament lamp giving 3,0 W of light: 60 W
a["fig2-bulb-Ph"] = 60 - 3.0                               # 57 W
a["fig2-led-Ph"] = 10 - 3.0                                # 7,0 W
# Worked example: kettle, P_o = 2,0 kW, t = 3,0 min, eta = 90 %
Eo = (2.0 * 1000) * (3.0 * 60)                             # 2000 W · 180 s = 360 000 J
Ea = 0.90 * Eo                                             # 324 000 J
a["ex-Eo"] = Eo
a["ex-Ea"] = Ea
a["ex-Eh"] = Eo - Ea                                       # 36 000 J = 36 kJ
# Inquiry: retrieval, experiments (model values of the simulation), transfer and checks
a["inq-kertaus"] = 40 * 30                                 # E = P t = 40 W · 30 s = 1200 J
a["inq-koe1-Eo-10s"] = 60000 * 10                         # engine locked at P_o = 60 kW, t = 10 s: E_o = 600 000 J
a["inq-koe1-Ea-10s"] = 0.25 * 60000 * 10                  # E_a = 150 000 J
a["inq-koe1-Eh-10s"] = 60000 * 10 - 0.25 * 60000 * 10     # E_h = 450 000 J
a["inq-koe1-eta"] = 150000 / 600000 * 100                  # eta = E_a / E_o = 25 %
a["inq-koe1-Eo-20s"] = 60000 * 20                         # conclusion: t = 20 s: E_o = 1 200 000 J = 1200 kJ
a["inq-koe1-Ea-20s"] = 0.25 * 60000 * 20                  # E_a = 300 000 J = 300 kJ
a["inq-koe1-Pa"] = 0.25 * 60000                            # P_a = 15 kW, P_h = 45 kW (ennuste-1 feedback)
a["inq-koe1-Ph"] = 60000 - 15000                           # 45 kW lost at 60 kW in
a["inq-koe2-Eo-20s"] = 40 * 20                             # bulb 40 W, 20 s: E_o = 800 J
a["inq-koe2-Ea-20s"] = 0.05 * 40 * 20                      # E_a = 40 J
a["inq-siirto"] = 0.20 * 4.5e6 / 3600                      # panel: E_a = 0,20 · 4,5 MJ = 0,90 MJ; P_a = 900 000 J / 3600 s = 250 W
a["inq-siirto-ilman-hyotysuhdetta"] = 4.5e6 / 3600         # mistake: eta forgotten: 1250 W
a["inq-siirto-minuutti"] = 0.20 * 4.5e6 / 60               # mistake: 1 h taken as 60 s: 15 000 W
a["inq-tarkistus-2"] = (2.5 - 0.50) / 2.5 * 100            # motor: E_a = 2,5 kJ − 0,50 kJ = 2,0 kJ; eta = 80 %
a["inq-tarkistus-2-haviot"] = 0.50 / 2.5 * 100             # mistake: E_h / E_o = 20 %
a["inq-tarkistus-2-kaanteinen"] = 2.5 / 2.0 * 100          # mistake: E_o / E_a = 125 %
a["inq-virhe"] = 2.4 / 8.0 * 100                           # error-spotting: correct eta = 30 %; the student's 8,0/2,4 = 3,33 = 333 %
a["inq-virhe-vaara"] = 8.0 / 2.4 * 100
a["inq-tulkinta-eta"] = 1.5 / 6.0 * 100                    # interpret: Sankey bands 6,0 cm and 1,5 cm: eta = 25 %
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
