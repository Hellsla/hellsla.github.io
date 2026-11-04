VERDICT: PASS
CONTENT-HASH: b8d6bdb7c47a6094
Mode: full
Round: 1

## Blocking
- none

## Fixed
- none needed (English already matches the Finnish).

## Polish
- Source wording: Finnish L1-06 distractor says the atmosphere warms the ground "alhaalta päin" (from below); the English says "from above", which is the physically right direction. Both are wrong options, so no answer is affected; the Finnish could say "ylhäältä päin".

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) in exercises.json and solutions.md against the reviewed Finnish: ids, answers (L1-08 480 kg, L2-05 2.3 ppm/a, L2-06 26 %, L3-04 458 ppm, L3-05 53 %), units, tolerances, correct flags, choice order and feedback, data table cells and every number are equal (scripted number comparison per solution section, decimal comma vs point normalised).
- Recomputed: 40 000 kWh x 12 g/kWh = 480 kg; 34/15 = 2.27; 61 to 45 = 26.2 %; 1.1, 1.6, 2.2 ppm/a and 414 + 44 = 458 ppm (whole-data line 446 ppm); 52 220 t to 24 680 t = 52.7 %, full wind 61.9 %, difference 9.2 points; 820 g x 2.0 = 1640 g = 1.6 kg.
- Decimal point in en JSON and LaTeX; decimal comma in fi-easy as in fi. No Finnish left in en.
- Terms natural English: climate vs weather, emission factor, sinks, percentage points.
- check_i18n.py en: 0 errors for fy2-8 (errors listed are other chapters, fy2-5/fy2-6, being edited by other agents).
