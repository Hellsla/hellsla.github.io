VERDICT: PASS
CONTENT-HASH: f5b4bdd7b0b1cd9b

## Blocking
(none)

## Polish
1. inquiry.json:233 (johtopaatos) — `after` lists koe-1, koe-2 and koe-3, but the prompt, model answer and four criteria cover only koe-1 and koe-2. Goal 3 ("tunnistamaan, milloin lineaarinen malli ei sovi") then has no self-assessment line in the conclusion — add a criterion and a sentence: "Aineistossa 3 poikkeamat muodostivat kuvion (päissä suoran yläpuolella, keskellä alapuolella), joten suora ei sovi, vaikka $d$ oli pieni verrattuna muutokseen."
2. lesson.md:31,33 — the "Lineaarinen malli" paragraph introduces fysikaalinen, graafinen, matemaattinen and kvantitatiivinen malli in one sentence, and the next paragraph holds proportionality, interpolation, extrapolation and curvature. Split into one idea per paragraph (e.g. a short ### "Mallin pätevyysalue" for interpolointi, ekstrapolointi and kaareutuminen).
3. lesson.md:36 — the pysähdy item "Jännitettä mitattiin välillä $x = 2\ldots 10$" has no unit and does not say that $x$ is the voltage. Fix: "Jännitettä $U$ mitattiin välillä $2\ldots 10\,\text{V}$. Kummassa arvossa tulos on luotettavampi, kun $U = 6\,\text{V}$ vai kun $U = 30\,\text{V}$?" and adjust the answer.
4. inquiry.json:393 (check-c2) — "Suoran piirtäminen" repeats ennuste-1, kertaus, virhe and tarkistus-3 (polyline vs fit, origin line). The core path allows 1–2 checks; make it `optional`. Correct options are mostly the longest and most qualified in the choice items (kertaus, ennuste-1, virhe, check-c2). Shorten them or lengthen the distractors.
5. inquiry.json:94 (ennuste-2, third option's feedback) — "kuin Kokeessa 2" should be "kuin kokeessa 2" (lowercase mid-sentence).

## Checked
- Learning path: the opening question is answered by the theory (random error, fit through the middle) and by the experiments; goals 1–3 are covered and nothing goes beyond FY1.
- Prediction data recomputed: the best fit through the origin is k≈0.49 m/s (d≈0.12 m), the 0.60 m/s line gives 0.44 m, the polyline slopes are 0.2/0.8/0.5/0.3/0.5. Prediction 2 gives b≈61 g (d≈1.2 g), and the b=0 line d≈61 g.
- Koe 3 recomputed with b=80 locked: minimum d≈5.8 °C and the residuals are + at the ends and − in the middle, as the question says. The simulation fits the topic and its numbers are called model values.
- Worked example: the kettle data fit T=8,0·t+20 (3 points above, 3 below, max 0,8 °C). k, b and t=2,5 min are correct, and the 7 stages each hold one step.
- Etsi virhe, Lue kulmakerroin, Sovella uuteen tilanteeseen, tarkistus-2 and exit ticket: all numbers and distractor values recomputed and correct; hints are progressive and each common-mistake feedback repairs a named misconception.
- The interpret figure was checked against its aria-label: the line starts at 5 km and passes (1 h; 20 km) and (3 h; 50 km).
- Solutions follow the 7-step form, symbolic first, and the plausibility checks are real checks.
- Captures at 390 and 1280 px (contact-1, lab-1280): nothing clipped, the sim controls and readout are understandable, figures sit next to their paragraphs.
- Finnish: glossary terms (kuvaaja, kulmakerroin, suoran sovitus, lineaarinen malli) are used consistently, the units after numbers are fine and the case endings are fine; no speaker names and no option referred to by letter.
- Workload is acceptable because of the optional items (kertaus, pohdi, siirto, tarkistus-3), though it is at the upper end of one lesson.
