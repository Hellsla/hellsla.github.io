VERDICT: PASS
CONTENT-HASH: 8577b79765a947c4

## Blocking

## Polish
- lesson.md (bouncing-ball photo, end of "Kaava: Vapaan pudotuksen nopeus", after the last pysahdy) — the photo shows the spacing of a falling ball growing, which is what the Ydinajatus figure "free-fall" shows; it sits a screen away from that paragraph and after a question box — move it beside the free-fall figure or the paragraph on the growing intervals.
- inquiry.json exp-1 (and pred-1/exp-1 pair) — in a vacuum the sim only evaluates v = g t, so exp-1 confirms the arithmetic. The conclusion's model answer already says so, which is honest; to make the physics emerge, consider asking the student in exp-1 to compare the three readings with the dashed line before computing the slope.
- inquiry.json simulaatio.calc — "rajanopeus" appears unexplained in a closed box for S2 students; add: "suurin nopeus, jota pallo ei ylitä, kun ilma jarruttaa yhtä paljon kuin Maa vetää".
- lesson.md "Kaava" paragraph — "keskikiihtyvyys" is the MAFY name but the sentence under the formula gives no gloss for S2 readers; "keskikiihtyvyys eli nopeuden muutos sekunnissa" would match the Selkeä suomi rule.
- inquiry.json exp-3 — the balls are the same size, so lighter means slower; a reader may take this as "mass matters in air". The Selitystehtävä model answer fixes it with "leveä", but one sentence in exp-3's correct feedback saying that a heavier ball of the same size has a larger weight against the same drag would close the gap.

## Checked
- Path: Miksi (Moon hammer/feather) → hook → retrieval s = v t → two predictions → sim/exp 1–3 → johtopäätös → theory → example → exercises → three checks → exit ticket; goals of the slot covered, nothing beyond FY1 scope.
- Predictions: committed before evidence; option feedback repairs each misconception and no answer is disclosed before commit; correct options are not always the first.
- Numbers verified: 9,81·1,5 = 14,7 m/s = 53 km/h; 108 km/h → 3,06 s; 7,4/2,0·3,0 = 11,1 m/s; data slope 9,8; exit ticket 4,9 m/s and ratio 6,06; sim air values 10,5 and 37,5 m/s at 4 s match the drag model in sim-spec.
- Worked example: seven stages, one step each, symbols first, unit conversion explained (1 m/s = 3,6 km/h), reasonableness check present; does not repeat any task.
- Solutions in the inquiry follow the seven-step form and are followable by a weak student.
- Finnish: case after number+unit correct ("1,0 s:n kuluttua"), glossary terms (putoamiskiihtyvyys, vapaa pudotus, kiihtyvyys) used consistently.
- Captures: nothing clipped at 390 px; sim controls and readout legible; figures sit beside their paragraphs; exp panels read in order (Alkutila / Vakiona / Muutetaan).
- Optional items (data, reflect, Etsi virhe) keep the core path to one lesson.
- check_lesson.py was not run per the packet; not repeated here.
