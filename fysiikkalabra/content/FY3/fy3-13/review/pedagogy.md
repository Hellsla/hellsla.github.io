VERDICT: FAIL
CONTENT-HASH: f9bbdacd430c964b

## Blocking
- inquiry.json activities `ennuste-1` and `ennuste-2` (choices[].feedback) — the predictions have no `reveal`, so the feedback appears the moment the student presses Vastaa, before any data has been seen. It quotes "aineisto" the student has not met and discloses results that Tutki then asks them to compute: k ≈ 0,37 kPa/°C, "−260 °C ja −292 °C", "−276 ± 16 °C" (answers of `suora` −276 and `epavarmuus` 15,7). An answer is disclosed before the student acts. Fix: rewrite every option's feedback of both predictions conceptually, with no figures from the data (for example "Tutki aineistoa ja palaa tähän: onko muutos yhtä suuri jokaista astetta kohti?"), and let the numbers appear only in `pohdi` or in the later tasks.
- solutions.md, `fy3-13-L2-03` Järkevyys — "Ylipaineen nolla olisi noin 9 °C:ssa" is wrong. The gauge pressure is 9,0 kPa at 30 °C and the slope is 0,3667 kPa/°C, so the gauge reads zero at about 5,5 °C (30 − 9/0,3667). The point of the remark is right, the number is not. Fix: "noin 5,5 °C:ssa".

## Polish
- inquiry.json `ennuste-1` prompt — "mittauspisteet merkitään kuvaajaan", but no graph or table is shown in Ennusta. Show the table (or one small graph) in the prompt, so the prediction can be argued from data, or drop the sentence.
- Tutki figures (`suora`, `epavarmuus`) end at θ = 0 °C, so the central idea, the extension to zero pressure, is first seen in the Kaava figure after Tutki. Use the wide-range figure (as in the Kaava section) in `suora`, or add a second view there, so the student sees what the answer −276 °C means.
- lesson.md:193 — "tulos pyöristetään samaan kymmenen asteen tarkkuuteen" does not match "−276 ± 16 °C" (unit-degree accuracy). Fix: "tulos pyöristetään samaan asteen tarkkuuteen kuin epävarmuus".
- The student only computes from given lines and never judges them. Add a short choice, for example "Kulkeeko tämä suora kaikkien epävarmuusjanojen kautta?", so that drawing the extreme lines (the Täsmennys of the slot) is practised. Also the worked example reads the point (0 °C; 101,3 kPa) from the line, outside the measured range 10–100 °C; one sentence on that would help.
- exercises.json `fy3-13-L2-04` — the question is hard to parse. Better: "Kuinka monta prosenttia lämpötilan epävarmuuden aiheuttama paineen muutos on paineen epävarmuudesta?" Also the correct option of each prediction is the longest and most hedged, so it can be guessed.

## Checked
- Learning path: prior (kelvin proportionality), hook, model, example, transfer and checks follow one another; the slot's goals (straight line, extrapolation, uncertainty) are covered, nothing extra.
- Worked example: 5 stages, one step each, symbolic first, then substitution; the numbers recomputed (k 0,367, −276,0, −260,3, −291,7, 15,7).
- Hints, mistake values and answers in `suora`, `siirto`, `virhe`, `tarkistus-2` recomputed: correct (−276, −277, −316 → −276, −283).
- Exercises: counts 5/4/3, answers recomputed, none repeats the example; L3 asks for reasoning, but only the number is checked.
- Figures 390 px: the gas thermometer is recognisable (gauge, thermometer, flask, heat arrows) and its LaTeX labels are legible; the data figures are uncluttered, and the dashed extreme lines are told apart by labels, not colour alone. At 1280 px the figure sits beside its paragraph.
- Exit ticket tests the core idea (why the line misses points, slope, agreement with −273,15 °C).
- Finnish: glossary terms used correctly, no lesson ids in student text (chapter name only), decimal commas, number+unit forms fine.
- Workload is about one lesson; no simulation, which fits (data, graph, model).
