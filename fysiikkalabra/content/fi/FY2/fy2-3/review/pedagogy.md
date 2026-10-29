VERDICT: PASS
CONTENT-HASH: bbce289c9b4b1f34

## Blocking

## Polish
- inquiry.json simulaatio.model — says the sim powers are "luvun taulukon" values, but the table has LED-lamppu 8 W and no 10 W lamp or toaster — add "lamppu 10 W" and "tosteri 1000 W" to the table or say "pyöristettyjä esimerkkiarvoja"; the exercises use 8 W LED, the sim and prediction 10 W, which may puzzle a student.
- inquiry.json koe-1.intro — "yksi, jossa ne ovat yhtä suuret" means hitting exactly 900 min on a 1–1440 slider; the hint offers arrow keys, which a phone lacks — offer plus/minus buttons or let "lähes yhtä suuret" count (not verified in the sim; no capture).
- inquiry.json tarkistus-2 hint 1 — "jotta tulos on wateissa" — "jotta tulos on watteina".
- inquiry.json hook.question — "Kumpi käyttää enemmän, nopeasti toimiva vai pitkään päällä oleva?" has the answer "kummin vain" — fine as a hook, but pohdi's callback to it is optional; consider keeping pohdi on the core path.
- lesson.md "Tyypillisiä tehoja" — the table omits tosteri, which the figure and the sim use — add the row.

## Checked
- Opening question (why the bill cannot follow from power alone) is answered by Ydinajatus, E = Pt and the example; goals met, no work/force.
- Prediction (15 h) can be refuted by koe-1; wrong options' feedback repairs the misconception; numbers verified (540 kJ, 54 000 s, 15 h).
- Example staged one step per stage; 1,92 € and sanity check agree.
- Misconception paragraph numbers verified (0,15 and 0,24 kWh); unit slip addressed.
- Interpret table consistent (20 kJ per 20 s = 1000 W); source marked as model data.
- Checks test concepts with misconception-based distractors; explain criteria observable.
- Workload one lesson: retrieval, Etsi virhe, koe-2, pohdi, check 5 optional.
- Exit ticket numbers verified (44 vs 37 kWh) and tests the core idea.
- Finnish: case forms after number+unit correct apart from "wateissa".
- Figures: not opened (no captures listed); described adequately in aria-labels.
- Option rebalance (01da3ae6): kertaus, mittari, virhe distractors stay real misconceptions, similar tone; answers not revealed in option text; feedback still teaches. Polish: virhe's correct option is still the longest (it states the corrected result) — drop "ja hinta 0,90 €".
