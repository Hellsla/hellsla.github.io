"""Numbers of lesson.md and inquiry.json for fy2-5 (python -I lesson-answers.py): one commented line per step."""
import json

a = {}
H_puu, H_bens, H_hiili, H_turve, H_pel, H_kaasu = 15, 43, 26, 10, 17, 49     # MJ/kg, lesson table
a["bensiini_puu_suhde"] = H_bens / H_puu                  # 43 : 15 = 2,87 (kertaa)
a["esimerkki_E_MJ"] = H_puu * 6.0                         # 15 MJ/kg · 6,0 kg = 90 MJ (worked example)
a["esimerkki_E_kWh"] = a["esimerkki_E_MJ"] / 3.6          # 1 kWh = 3,6 MJ: 90 : 3,6 = 25 kWh
a["suklaa_H"] = 2.2 / 0.100                               # 2200 kJ = 2,2 MJ per 100 g = 0,100 kg: 22 MJ/kg
a["suklaa_vs_puu_100g_kJ"] = H_puu * 0.100 * 1000         # 100 g wood: 15 · 0,100 = 1,5 MJ = 1500 kJ (chocolate 2200 kJ)
a["ruisleipa_H"] = 1.0 / 0.100                            # 1000 kJ per 100 g -> 10 MJ/kg
a["voi_H"] = 3.0 / 0.100                                  # 3000 kJ per 100 g -> 30 MJ/kg
a["peruna_H"] = 0.3 / 0.100                               # 300 kJ per 100 g -> 3 MJ/kg
# data table of the inquiry: wood masses and released energies
a["puu_1kg"] = H_puu * 1.0                                # 15 MJ
a["puu_2kg"] = H_puu * 2.0                                # 30 MJ
a["puu_4kg"] = H_puu * 4.0                                # 60 MJ
a["puu_8kg"] = H_puu * 8.0                                # 120 MJ
# misconception: wet wood
a["tiivistelma_sakki_puu"] = H_puu * 10                   # 10 kg wood = 150 MJ
a["tiivistelma_sakki_bensiini"] = H_bens * 10             # 10 kg petrol = 430 MJ
# error-spotting: 250 g of wood
a["virhe_oikea_E"] = H_puu * 0.250                        # 15 · 0,250 = 3,75 MJ
a["virhe_vaara_E"] = H_puu * 250                          # 3750 MJ (forgot g -> kg)
# transfer task: LPG cartridge 0,230 kg, H = 46 MJ/kg, eta 60 %
a["siirto_E"] = 46 * 0.230                                # 10,58 MJ
a["siirto_hyoty"] = 0.60 * a["siirto_E"]                  # 6,348 MJ -> 6,3 MJ
a["siirto_mistake_ilman_eta"] = a["siirto_E"]             # 10,6 MJ (forgot eta)
a["siirto_mistake_g"] = 46 * 230 * 0.60                   # 6 348 MJ (forgot g -> kg)
# check 2: 1,0 kg petrol in kWh
a["tark2_kWh"] = H_bens / 3.6                             # 43 : 3,6 = 11,94 kWh -> 12 kWh
a["tark2_mistake_kWh"] = H_bens * 3.6                     # 154,8 (multiplied instead of divided)
# one litre of petrol (about 0,74 kg) in food terms etc. are not used
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
