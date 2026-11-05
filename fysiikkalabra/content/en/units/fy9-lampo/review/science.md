VERDICT: PASS
CONTENT-HASH: 73381a386f867cdd

Science review, round 3, of the English translation of fy9-lampo (source content/fi/units/fy9-lampo/, reviewed). `check_i18n.py` en: 0 errors; `units.py check` and `practice.py check` give "OK en/units/fy9-lampo: 6 tasks, 95 points", so answers, units, tolerances, correct options, sections and formulas match the source. The numbers recomputed in earlier rounds (c of ice 2083 J/(kg·K), 13.79 kg, 2.027 kg, 180 mm, 0.886 K, 3.88 kg, 21.9 GJ / 17.4 h, 81.6 K / 1667 W / 35.8 %, r = 2.26 MJ/kg and 2.54 MJ/kg, 371 / 333 kJ/kg, 31.5 K / 133.7 K / 40.2 %) are unchanged. Decimal point throughout. The concept map now shows the correct English branch headings (heating, change of state, thermal expansion, heat transfer) over physically correct formulas.

## Blocking
None.

## Polish
1. s3 d: the en text matches the source at both places: tasks.json criterion "about 12 %" (fi "noin 12 %") and solutions.md model answer "600 : 530 ≈ 1.13 … about 13 %" (fi "noin 13 %"). The mismatch is in the Finnish source itself. Changing the en model answer to 12 % was tried and check_i18n rejects it ("solutions.md fy9-lampo-s3 d): formulas differ from Finnish"), so it was reverted. Fix in fi first (e.g. "about 12–13 %" in both, or criterion 13 %), then carry over.
