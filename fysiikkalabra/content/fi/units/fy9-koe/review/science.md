VERDICT: PASS
CONTENT-HASH: b2f0b8b8cd894742

Delta review of the editorial correction 48d1f30a / 57b67249 (teacher's narrow correction round): one sentence added in unit.md "Sähköinen koe" after "Yhteensä kokeesta saa enintään 120 pistettä": "Tämä on kokeen yleinen rakenne: tehtävien kysymysmuodot ja Osan I kohtien määrä vaihtelevat kokeesta toiseen, joten tarkista ajantasainen rakenne ylioppilastutkintolautakunnan ohjeista." Nothing else in the unit changed (`git diff origin/main`).

## Blocking

None.

## Polish

1. (Carried over) inquiry.json testi-20 third distractor: optional "…jos käämissä kulkisi tasavirta paristosta".

## Checked

- Exam facts: the new sentence makes no new factual claim; it hedges the existing list (11 tasks, Osa I compulsory 20 p, Osa II 4 of 7 × 15 p, Osa III 2 of 3 × 20 p, 120 p), which agrees with the YTL physics exam's current general structure and already says "yleensä 11 tehtävää". Saying that question formats and the number of Osa I items vary between sittings is true and points the student to YTL's current instructions. No false claim about the YTL exam.
- Consistency: the sentence does not contradict "Osa I … yksi tehtävä, 20 pistettä", the time budget (360 − 50 = 310 = 60 + 4 · 35 + 2 · 55 min) or teacher.md.
- No number, formula or task changed; the earlier recomputation stands.

## Follow-up (4.11.2026, hash 4ff9fa1cddf8ae89)

Delta: one bullet deleted from teacher.md "Kertaustestin käyttö" ("FY7:n luvut eivät ole vielä sivustolla …"; Lauri, commit b6de518c4). No physics, number, formula, option or feedback changed.

- Blocking: none. The deleted sentence made no physics claim; the remaining teacher.md and unit.md make no claim about FY7 chapters being missing (grep "FY7": only inquiry.json and developer.md hit).
- Polish (for pedagogy, not physics): FY7 chapters now exist (fy7-4 *Voima virtajohtimeen*, fy7-5 *Sähkömagneettinen induktio*, fy7-10 *Valon heijastuminen ja taittuminen*), yet the 8 feedbacks of testi-19/20/21 still end "Kertaa tämä moduulissa FY7." without a chapter link, unlike FY1–FY6 and FY8. The physics of those feedbacks is unchanged and correct; the linked chapters match their topics (testi-19 refraction → fy7-10, testi-20 induction → fy7-5, testi-21 $F = IlB$ → fy7-4).

## Follow-up 2 (4.11.2026, hash b2f0b8b8cd894742)

Delta: the 8 FY7 feedbacks in inquiry.json now end "Kertaa luvussa [*…*](fy7-N.html)."; developer.md line 17 updated. Feedback physics unchanged.

- Blocking: none. Targets match topic and meta.json titles: testi-19 refraction → fy7-10 *Valon heijastuminen ja taittuminen*; testi-20 induction → fy7-5 *Sähkömagneettinen induktio*; testi-21 $F = IlB$ → fy7-4 *Voima virtajohtimeen: sähkömoottori ja kaiutin*. The pages exist in site/. The Polish item from Follow-up 1 is resolved.
