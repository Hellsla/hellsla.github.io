VERDICT: PASS
CONTENT-HASH: 63ff7bc3c9a8481e

Science review of the Selkeä suomi (fi-easy) translation of fy9-liike, against content/fi/units/fy9-liike/ (source already PASS).

Method: `check_i18n.py` (fi-easy: 0 errors), `practice.py check` (fi-easy/units/fy9-liike: 6 tasks, 95 points, OK), `units.py check` clean. All 169 changed strings of the JSON files (translate_kit extract: source.json vs strings.json) and every changed paragraph or line of unit.md, teacher.md and sovella/solutions.md read side by side with the Finnish. Every number recomputed in one Python call: tram 450 m and 7,5 m/s; scooter 22,5 m; moose 46,8 m; dog 8,0 s; ball -1,81 m/s; lift 16 m; cyclist 30 km/h; exit ticket 15 m/s and -2,0 m/s²; s1 12,0 s, 1,25 m/s², 6,0 s, 17,5 m, 15,4 s, 307 m, 77 m; s2 8,84 m, 0,625 s, 7,08 m, 5,87 / -6,13 m/s, Moon 8,7 m; s3 -0,645 m/s², 481 m; s4 81,8 km/h, 135 s, 4,5 s, about 18 km/h; s5 0,94 (0,74–1,22) m/s²; s6 9,77 m/s², 8,92 m/s², difference 0,93 m/s². All match the translation.

## Blocking
None.

## Polish
1. No changed physics anywhere: every formula, value, unit, rounding argument, correct option and answer is the source's. The S2 additions are correct definitions, not new physics: tangent "sivuaa eli koskettaa käyrää yhdessä pisteessä", lakipiste "radan korkein kohta", "suoraan verrannollinen: kun aika kaksinkertaistuu, myös paikka kaksinkertaistuu" (unit.md, Tasainen liike), kehäpäätelmä "olettaa sen, mikä pitäisi osoittaa", ekstrapolointi, ääriarvo. No new numbers, so no extra calculations were needed.
2. Sign and direction wording stays exact where the source is careful: "Kun kiihtyvyys on samaan suuntaan kuin nopeus, vauhti kasvaa" (activities.4.choices.2.feedback), "Etumerkki on vastakkainen kuin nopeudella" (exit-ticket 1.a), and $ downwards at the top of the flight (activities.5, s2 a).
3. unit.json key_concepts: all five definitions are correct. *kiihtyvyys* "Jos $ ja $ ovat samansuuntaiset, vauhti kasvaa" is right; optional: add "Jos ne ovat vastakkaissuuntaiset, vauhti pienenee" so the card does not suggest that a negative $ always means slowing down (the misconception in Ennusta 4).
4. figures.json: the four figure descriptions are the same as the source, sentence by sentence (values 10 s, 48,5 s, −2,3 km/h per s and the colours are kept); the axis words are unchanged physics terms.
