VERDICT: PASS
CONTENT-HASH: 04842bd55c702318

## Blocking
(none)

## Polish
- lesson.md, Ydinajatus (kettle photo `steaming-kettle.webp`, caption "Näkyvä huuru on tiivistyneitä vesipisaroita") — Minor — the photo and its caption (condensation) do not serve the paragraph's idea (c, Q = cm dT) and split it from the water-sand figure that does. Move the photo or give a caption about heating water.
- lesson.md, last `data-fig="scene"` (sauna stove), after Tiivistelmä — Minor — a figure after the summary that explains no paragraph (the rule: no figure after a block it does not explain). Attach it to the text it illustrates or drop it.
- inquiry.json koe-2 `intro` "esimerkiksi 0,20, 0,50 ja 0,80 kg. Millä massalla tulos on keskiarvo?" — Minor — the suggested masses contain the answer (0,50 kg) before the student acts. List only 0,20 and 0,80 or ask the student to find the mass.
- inquiry.json koe-1 `measure` "C (J/K)" and ennuste-1 feedback — Minor — C = cm is read and used before Teoria introduces it (only in the closed "Laskennan selitys" box). Add one clause in koe-1 `intro` ("C = cm, lämpökapasiteetti, kertoo J/K") or ask for C after the experiment.
- lesson.md, Yleinen virhekäsitys — Minor — "Viimeisen ryhmän ensimmäisellä rivillä yhtälö on jaettu puolittain kilogrammalla..." is hard to follow, and the division is written ": 4,0 kg" followed by a stray full stop after `$$`. Say "jaetaan puolittain luvulla $c$ ja kilogrammoilla" and write a fraction. Also inquiry.json siirto: `answer` 29.1 but solution gives 29,09 → "29 kg, kaksi merkitsevää numeroa"; align the answer line.

## Checked
- Path: prerequisites (heat = energy transfer, conservation) retrieved through the beach scene; the opening question is answered in the theory and reflect (the surface-layer point appears only in text and the optional reflect; Minor).
- Predictions are refutable (equal-effect and the "mean" misconception); the wrong options repair them; model numbers verified by hand (26,8; 44,0; 40,0; 63,1 °C).
- Goal "kalorimetrinen mittaus": the student only varies the substance or mass in an ideal sim; no experiment determines an unknown c from data or meets heat losses. Major (not blocking: the example and check 3 carry the skill), suggested secondary experiment: unknown block, determine c, compare with a table.
- Worked example: seven stages, principle first, symbolic then numeric, units, sensible sig figs, check. Etsi virhe and its algebra verified (6,6 vs 30,0 °C); excellent task for the multi-term goal.
- Transfer task and checks: hints progressive, mistake values (220; 21,3; 768; 501) correct and diagnostic; distractors misconception-based.
- Exit ticket tests the core idea (Q = cm dT, comparison of c); Finnish and case endings correct.
- Phone: layout tests pass; I judged from text/JSON only, no captures opened.

## Scores
- 2 Conceptual clarity: 4 — c vs C vs Q vs T separated well; C used before it is defined (Minor).
- 3 Pedagogical effectiveness: 4 — strong predict/test/explain; two decorative figures, an experiment suggestion that leaks.
- 4 Exercise quality (lesson tasks): 4 — varied, diagnostic feedback; check 3 close to the example.
- 5 YO readiness: 4 — symbolic first, sig figs, error analysis, unit care.
- 6 Experimental reasoning: 3 — a purely ideal model, no measurement, uncertainty or loss analysis in the student's own investigation (Major).
