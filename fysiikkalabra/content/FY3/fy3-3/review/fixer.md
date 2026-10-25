VERDICT: DONE

Round 1 fixes for fy3-3. Files edited: exercises.json, solutions.md, lesson.md, exit-ticket.json, meta.json (glossary list only), sim.js, sim-spec.md, tests/sims/fy3-3.json, glossary.json, curriculum.json (fy3-3 glossary slot). No status fields, templates, CSS or review/ files (other than this one) touched.

1. mathematician, significant figures
   - L1-03 data is now "77,4 K" (answer -196 °C, exact -195,75; 3 sf rounding gives -196). L3-03 data is now "20,0 °C" (answer -127 °C, exact -126,575; 3 sf gives -127). solutions.md updated.
   - Checked every task in Python for a student who rounds to the data's sf (and for 273 instead of 273,15): L1-01 (21 °C -> 290, 1,4 %), L1-02, L1-05, L2-03 (-270,9 -> -270, k rounded to 0,28 gives 1,6 %), L3-01 (320 vs 321, 0,3 %) all stay inside 0,02. New tasks listed in item 3 also pass (see there). No other data needed changing.
2. proofreader
   - "Celsiusasteikon" kept; "Celsius-lämpötilan" -> "Celsiuslämpötilan" (capital C because it starts the sentence).
   - solutions.md: "77 astetta" -> "77,4 kelviniä", "muutaman asteen" -> "muutaman kelvinin"; "15 K nousu" disappeared with the rewritten L2-01 ("45 K:n nousu"); L3-02 sanity text replaced with the new task.
   - lesson.md: "Asteikkojen yksi aste on yhtä suuri" -> "Celsiusasteen ja kelvinin suuruus on sama"; SVG aria-label reworded as in the proofreader diff.
   - "päivänpuolen" -> "päiväpuolen" (L2-04, also in the rewritten text). sim-spec.md phrase -> "seinämiin kohdistuvien törmäysten perusteella".
   - Glossary: new entry "paine" in glossary.json (force per area, unit pascal, deeper in a later lesson; lessons fy3-3; see_also tilanmuuttuja); "paine" added to the glossary list in meta.json and to the fy3-3 slot in curriculum.json.
3. educator (blocking) and exercises
   - L3-02 replaced: 150 kPa at 27,0 °C in a sealed rigid container heated to 200 kPa, p proportional to T, find θ. Python: T2 = 300,15 * 200/150 = 400,2 K, θ = 127,05 -> 127 °C (273 gives 127 too; rounding to 2 sf gives 130 = 2,4 % but the data has 3 sf).
   - L2-02 new data: 90,0 kPa at 0 °C, 123 kPa at 100 °C, p at 35 °C: k = 0,33, p = 101,55 -> 102 kPa (101,5 / 101,6 / 101 / 100 are all within 2 %).
   - L2-01 two-step: 288 K plus a rise of 45 K -> 333 K = 59,85 -> 60 °C.
   - L2-04 two-step: -173 °C and 127 °C, how many times greater the day side's kelvin temperature is: 400,15/100,15 = 3,9955 -> 4,0 kertaa (unit "kertaa"; 4 with 273 too).
   - 5/4/3, ids and a solution for each kept; solutions in the usual format.
4. lesson.md additions (no new topics)
   - Words only (no formula): at constant volume and amount of gas the pressure is directly proportional to the kelvin temperature, and so is the mean kinetic energy of the particles; hence temperature ratios are compared in kelvins.
   - One defining sentence for pressure (force per area, pascal, 1 kPa = 1000 Pa, more in a later lesson) in the first paragraph.
   - "ekstrapoloida" explained (extend the fitted line beyond the measured points); display equation p = p₀ + kθ and θ = −p₀/k = −100 kPa / 0,37 kPa/°C ≈ −270 °C (the old display formula was replaced, so each formula still appears once).
   - Misconception paragraph states 293/283 ≈ 1,035 (+3,5 %). "veden kiehumispiste normaalipaineessa". One sentence that real gases liquefy before absolute zero so the extrapolation is only a model/limit.
   - Micro-model paragraph: smaller volume means more frequent collisions but not harder ones; higher temperature at constant volume means both more frequent and harder.
   - exit-ticket.json Q1 replaced with "Miksi suljetun astian kaasun paine kasvaa, kun kaasu lämpenee?" and a short micro-model answer.
5. SVG in lesson.md
   - font-size 24px, axis strokes 3, dashed line stroke 3 (dash 9 7), measured segment 4. "p = 0" label moved to (80, 212), above-left of the dashed line, which no longer crosses it (checked in a 320 px screenshot). Caption under the figure: vertical axis drawn at the left edge, about -300 °C, not at θ = 0; solid line is the measured range, dashed line the extrapolation.
   - U+00A0 inserted between number and unit (°C, K, kPa) in all exercise texts.
6. sim.js and tests/sims/fy3-3.json
   - Thermometer scale labels are right-aligned to the left of the tube (tx - 14); no clipping at 320 px (screenshot checked).
   - Pressure now uses the effective box: Wc = W - 2R, Hc = BOX.h - 2R for the measurement and pRef = N·V_REF²/(2·PX·Hc). To make the effective width exactly proportional to V (otherwise the 0,5 dm³ case would keep a +4 % offset against pTheory = 100·(T/300)/V), the drawn width is now W = PX·V + 2R with PX = 192 (same 200 px at 1,0 dm³; 104 px at 0,5; 392 px at 2,0). Header comment updated. Measured mean of pRel/pTheory over 20 s: 300 K/1,0: 0,994; 300 K/0,5: 0,995; 300 K/2,0: 0,999; 600 K/0,5: 0,986; 100 K/1,0: 0,997; 600 K/1,0: 0,993 (before: 1,03 to 1,07).
   - Note text corrected: faster particles -> more often and harder; smaller box -> more often; plus a line "Mitattu paine vaihtelee hieman teoria-arvon ympärillä."
   - Four assertions added, none existing changed or loosened: theta at 600 K, pTheory = 100·(T/300)/V at 450 K/0,5 dm³, N = 80, readout at 100 K/0,5 dm³ ("T = 100 K = −173 °C", "teoria 67").

Not applied (optional, not requested): L2-03 "Piirrä" wording, exit-ticket Q2 answer wording, extra x-axis tick labels, table CSS and line length (template, not fixable here).

Checks: `python scripts/build.py --all` ok; `python scripts/check_latex.py content/FY3/fy3-3` all LaTeX ok (5 fragments); `test_sims.py fy3-3` PASS three times in a row.

New content hash (`python scripts/gate.py --hash fy3-3`): 3b1b29439e94b105

All reviewers (tester, physics-expert, mathematician, educator, proofreader, editor, web-designer) must run again, because every edit changes the hash.
