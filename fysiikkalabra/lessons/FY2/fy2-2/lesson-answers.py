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
a["inq-aurinko-EJ"] = sun_s * 3600 / 1e18          # the same in EJ (1 EJ = 10^18 J): about 620 EJ (koe-2)
# Prediction 2, option "a thousand years": 1000 × 6 · 10^20 J of use comes from the Sun in about 1000 h
a["inq-tuhat-vuotta-vrk"] = 1000 * 6.2e20 / (sun_s * 3600) / 24   # hours of sunlight : 24 h = about 41 days, "noin 40"
# Kaava figure (sailyminen, an example): porridge 800 kJ, motion 200 kJ
a["fig-sailyminen-lampo"] = 800 - 200              # 600 kJ of heat
# Common mistake: 1,5 MJ + 300 kJ = 1500 kJ + 300 kJ
a["virhekasitys-summa"] = 1.5 * 1000 + 300         # 1800 kJ (the wrong sum 1,5 + 300 = 301,5)
# Kaava: 1 MJ = 1000 · 1000 J
a["kaava-MJ"] = 1000 * 1000                        # 1 000 000 J
# Chain table (interpret): 100 MJ in, 40 MJ electricity at the plant, 2 MJ lost in the grid, 34 MJ into the water
a["inq-ketju-lampo"] = 100 - 34                    # 66 MJ has become heat before the water: 60 + 2 + 4
# Transfer task: a wind farm (0,300 TJ = 300 GJ, all data to the gigajoule)
a["inq-siirto"] = 360 - 9 - 0.30 * 1000            # 360 GJ − 9 GJ − 0,30 TJ (300 GJ) = 51 GJ
# Check 2: lightning against a day's food
a["inq-tarkistus-2"] = (1.0 * 1000) / 10           # 1,0 GJ = 1000 MJ; 1000 MJ : 10 MJ = 100
# Error-spotting item: 2,5 kJ
a["inq-virhe-oikea"] = 2.5 * 1000                  # 2,5 kJ = 2,5 · 1000 J = 2500 J
print(json.dumps(a))
