VERDICT: PASS
CONTENT-HASH: 99d9cf49a3fb1eb9

Science review of the Selkeä suomi (fi-easy) translation of fy9-moderni. The source content/fi/units/fy9-moderni (hash b942c369bb9ab315) passed all three reviews.

Method: `check_i18n.py` reports no error for fy9-moderni, and `practice.py check` gives "OK fi-easy/units/fy9-moderni: 6 tasks, 95 points". Every `$…$` and display formula in unit.md, teacher.md, sovella/solutions.md, inquiry.json, exit-ticket.json and sovella/tasks.json was compared as a multiset with the source. They are identical, apart from one added `$E = hf$` in the key concept *fotoni*, which NOTES.md §12 allows. The plain-text numbers are also identical. Answers, units, tolerances, correct flags, points and criteria keys are unchanged. Each changed string in the JSON files and each changed paragraph of the Markdown was read side by side with the source.

## Blocking
None.

## Polish
1. sovella/tasks.json, fy9-moderni-s1 text: "laskeumaa eli radioaktiivista pölyä". Fallout came down mostly with rain, as radioactive substances, so "pölyä" is a slight simplification. Suggestion: "laskeumaa eli radioaktiivisia aineita, jotka laskeutuivat maahan".
2. inquiry.json activities[19].solution, Järkevyys: "Lähteessä on satojatuhansia becquerelejä" treats activity as an amount of something inside the source. Suggestion: "Lähteen aktiivisuus on satojatuhansia becquerelejä, mutta siinä on vain kymmeniä nanogrammoja cesiumia."
3. sovella/solutions.md, s2 Yleisiä virheitä c): "Sama on kuitenkin vain suhteellinen muutos" no longer says clearly that it is the relative change, not the shift in nanometres, that is the same for both lines. Suggestion: "Viivoilla on kuitenkin sama suhteellinen muutos, ei sama muutos nanometreinä."

## Checked and correct
- unit.json key_concepts (fotoni, energiatila, puoliintumisaika, sidosenergia, ionisoiva säteily): the physics is correct. The *sidosenergia* sentence ("kun sidosenergia nukleonia kohti kasvaa reaktiossa, energiaa vapautuu") is right because the nucleon number is conserved.
- The added explanations are correct: ionisaatioenergia, perustila, kynnysjännite, annosnopeus, viitearvo, alipaine, virittynyt ydin "jolla on ylimääräistä energiaa" and massavaje. The model answers keep every step and every condition of the source (point source, large set of nuclei, one photon to one electron, background subtraction).
- figures.json translates every description and keeps the numbers.
