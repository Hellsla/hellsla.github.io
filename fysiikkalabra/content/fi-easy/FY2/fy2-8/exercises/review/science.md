VERDICT: PASS
CONTENT-HASH: d84745408ad2e7e1
Mode: full
Round: 1

## Blocking
- none

## Fixed
- none needed (plain Finnish (selkosuomi) already matches the Finnish).

## Polish
- Source wording: Finnish L1-06 distractor says the atmosphere warms the ground "alhaalta päin" (from below); fi-easy copies it. Both are wrong options, so no answer is affected; the Finnish could say "ylhäältä päin".

## Checked
- All 8 new exercises (L1-06..08, L2-05..07, L3-04..05) in exercises.json and solutions.md against the reviewed Finnish: ids, answers (L1-08 480 kg, L2-05 2.3 ppm/a, L2-06 26 %, L3-04 458 ppm, L3-05 53 %), units, tolerances, correct flags, choice order and feedback, data table cells and every number are equal (scripted number comparison per solution section, decimal comma vs point normalised).
- Recomputed: 40 000 kWh x 12 g/kWh = 480 kg; 34/15 = 2.27; 61 to 45 = 26.2 %; 1.1, 1.6, 2.2 ppm/a and 414 + 44 = 458 ppm (whole-data line 446 ppm); 52 220 t to 24 680 t = 52.7 %, full wind 61.9 %, difference 9.2 points; 820 g x 2.0 = 1640 g = 1.6 kg.
- Decimal point in en JSON and LaTeX; decimal comma in fi-easy as in fi. No Finnish left in en.
- Selkosuomi: short sentences, terms (päästökerroin, nielu, kulmakerroin, säätövoima) used as in the lesson.
- check_i18n.py fi-easy: 0 errors for fy2-8 (errors listed are other chapters, fy2-5/fy2-6, being edited by other agents).

## Follow-up (2026-11-04, teacher's edit of L1-06: exercises.json:69, solutions.md:125)
- **Blocking [B]** exercises.json:69 and solutions.md:125 (L1-06): "Yksinkertainen säteilytasapainomalli antaa Maan lämpötilaksi vain noin −18 °C." Unlike fi, en and the fi-easy lesson (which defines **efektiivinen säteilylämpötila** in bold), this calls −18 °C simply "Maan lämpötila", and "vain" sets it against the surface temperature as if it were the same quantity, i.e. the surface temperature without greenhouse gases. That is exactly the reading the lesson rules out ("ei ole tarkka ennuste pinnan lämpötilasta ilman kasvihuonekaasuja"). Internal consistency (6) and NOTES §12.1 (same physics). Fix: replace "antaa Maan lämpötilaksi vain noin" with "antaa Maan efektiiviseksi säteilylämpötilaksi noin" in both places.
- Recomputed: $+15-(-18)=33$, and a temperature difference is the same in °C and K, so $33\,\text{K}$ is right; −18 °C ≈ 255 K is the textbook effective radiating temperature (σT⁴ = S(1−α)/4 with α ≈ 0,3), +15 °C ≈ 288 K the mean surface temperature.
- Otherwise correct: +15 °C named as the mean surface temperature; correct option and distractors unchanged.
- Scope: only these two sentences; the rest of this report stands from the earlier round.

## Follow-up 2 (2026-11-04, fix re-check)
- Fix applied in exercises.json:69 and solutions.md:125: "antaa Maan efektiiviseksi säteilylämpötilaksi noin $-18\,{}^\circ\text{C}$", without "vain". It now matches the lesson, fi and en. The Blocking item above is resolved. The physics and the 33 K value are still right.
