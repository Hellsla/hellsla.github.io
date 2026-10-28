VERDICT: PASS
CONTENT-HASH: a906e94302d67010

## Blocking

## Polish
- inquiry.json exp-1 solution — "Annettu" lists $v_1 = 9{,}81\,\text{m/s}$, but the sim readout rounds to one decimal ($9{,}8\,\text{m/s}$); the student's table shows 9,8 and 29,4 — quote the values as the table shows them (result 9,8 m/s² unchanged).
- inquiry.json data solution — "Mittauspisteet poikkeavat suorasta noin 0,1 m/s": the residuals from the fitted line ($v = 9{,}81\,t$) are at most 0,04 m/s; "alle 0,1 m/s" would be accurate (the ~0,2 m/s² slope estimate stays a fair rough bound).
- lesson.md:46 — "se otetaan koetulokseksi, jonka tutkit itse": the vacuum experiments run on a model that already assumes v = gt (the johtopäätös model answer says so correctly). Consider "jonka tulos on mitattu (esim. Apollo 15) ja jonka mallia tutkit simulaatiolla" so the lesson does not call model values experimental evidence.
- inquiry.json simulaatio.model — air model also neglects buoyancy (about 5 % of the weight for the 0,1 kg, 0,20 m ball); one clause "nosteen vaikutus jätetään huomiotta" would complete the assumptions (C, not a finding).
- lesson.md:137 — "nopeus kasvaa sekunnissa 9,81 m/s myös silloin, kun kappale ei lähtenyt levosta" is right for the downward velocity as defined (v alaspäin); for an object thrown upward the speed decreases. Fine as C at FY1; optional "kun se liikkuu alaspäin".

## Checked
- One-script recomputation: worked example 14,715 m/s → 15 m/s, 52,97 km/h → 53 km/h; exp-1 9,81 (9,8) m/s²; data slope 4,9/0,50 = 9,8 m/s², mistake 0,102; siirto g = 3,7 m/s², 11,1 → 11 m/s, mistakes 29,4/22,2/3,7; check-2 30,0 m/s, 3,058 → 3,06 s, mistakes 11,0/0,327/30. All match lesson-answers.py and the texts; tolerances accept the rounded answers.
- Sim drag model: K = ½·1,2·0,47·π·0,10²; v_T = √(mg/K), v = v_T tanh(gt/v_T), fall ln cosh — correct; at 4,0 s: 0,1 kg → 10,5 m/s, 1 kg → 27,5, 10 kg → 37,5 m/s (< gt = 39,2), matching the johtopäätös model answer.
- Exp setups: exp-1 locks environment and masses, varies t; exp-2/3 lock t and m_A, vary m_B; simState gives vA, vB; slider steps reach the suggested values.
- Predictions, exp questions, virhe, check-1: exactly one correct option each, every distractor wrong and its feedback right; exp-3 correct option holds for same-size balls.
- Figures: free-fall positions (6,2 px/m: 4,9/19,6/44 m) and arrow lengths 1:2:3 to scale; same-fall heights equal; vt-graph and data-graph points and fitted line (slope 9,81) match the stated values.
- Definitions (vapaa pudotus, kiihtyvyys, g as rate of change of speed, m/s²) consistent with glossary and summary; v = gt stated with "levosta" and "ilmanvastusta ei ole" wherever used.
- Mass/air explanation ("eron aiheuttaa ilma, ei massa sellaisenaan") consistent across theory, misconception, check-3, exit ticket; within FY1 scope (forces deferred).
- Hook facts (Apollo 15, 1971, David Scott, hammer and falcon feather) correct.
- Hash identical at start and end.
