"""Numbers of the lesson text and inquiry.json for fy2-2, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Prints {id: number} as JSON on the last line."""
import json

a = {}
# Worked example (lesson.md): banana 0,45 MJ, motion 110 kJ
a["esim-lampo"] = 0.45 * 1000 - 110                # 0,45 MJ = 450 kJ; 450 kJ − 110 kJ = 340 kJ of heat
# Prediction 1 and experiment 1: a litre of petrol against a day's food
a["inq-bensiini-ruoka"] = 32 / 10                  # 32 MJ : 10 MJ = 3,2 times as much
# Prediction 2: sunlight on the Earth for one hour against humankind's use in a year
sun_s = 1361 * 3.14159265 * 6.371e6 ** 2           # J every second (solar constant 1361 W/m², Earth's cross-section)
a["inq-aurinko-tunti"] = sun_s * 3600              # about 6,2 · 10^20 J, the same as humankind's 620 EJ in 2023
# Chain table (interpret): 100 MJ in, 40 MJ electricity at the plant, 2 MJ lost in the grid, 34 MJ into the water
a["inq-ketju-lampo"] = 100 - 34                    # 66 MJ has become heat before the water: 60 + 2 + 4
# Transfer task: wind power
a["inq-siirto"] = 360 - 9 - 0.30 * 1000            # 360 GJ − 9 GJ − 0,30 TJ (300 GJ) = 51 GJ
# Check 2: lightning against a day's food
a["inq-tarkistus-2"] = (1.0 * 1000) / 10           # 1,0 GJ = 1000 MJ; 1000 MJ : 10 MJ = 100
# Error-spotting item: 2,5 kJ
a["inq-virhe-oikea"] = 2.5 * 1000                  # 2,5 kJ = 2,5 · 1000 J = 2500 J
print(json.dumps(a))
