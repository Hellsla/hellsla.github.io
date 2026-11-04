VERDICT: PASS
CONTENT-HASH: c1bb42f3585103cf
ROUND: 2

## Blocking

## Polish
- solutions.md:178 (L3-04): "taajuus f on rullan ja käämin pyörimistaajuus" describes a device that does not exist. In a real pullodynamo the magnet turns with the roller inside a fixed coil, and it is often multipole. Fix: "f on rullan ja magneetin pyörimistaajuus; käämin vuo vaihtelee kuten pyörivässä käämissä (kaksinapainen malli)". Or use "opetusgeneraattori".
- lessons/FY7/fy7-7/answers.py:36: the comment still says "napadynamo". Fix: "pullodynamo".
- exercises.json:47 (L1-06): the correct option "tuottaa saman tehon kuin tasajännite" does not say which DC voltage. Fix: "tuottaa vastukseen saman keskimääräisen tehon kuin yhtä suuri tasajännite".
- exercises.json:125 (L2-05): still open from round 1. `graph` was dropped, but the plan's follow-up (three rotation rates → NBA) was not made. That is for pedagogy and the plan.

## Checked
- Round-1 Blocking item L3-04 is resolved: the device is now a pullodynamo in the text, the caption and the solution. At 5–30 r/s, a roller of about 2,5 cm gives about 1–9 km/h, which is realistic for a lab measurement. The single-coil model was kept as a stated simplification.
- L2-06 c) uncertainty is now right: ±0,2 V for the prediction plus ±0,1 V gives ±0,3 V, and the 0,2 V difference is smaller. "Eroa verrannollisuudesta ei voida osoittaa" follows the guardrail.
- L3-04: c = −0,11 V is now "todennäköisesti" a measurement error. The two-point check (9,1 − 1,4)/25 = 0,308 V/Hz is right.
- L2-05 reading: "hetkellä 12 ms (−0,1 V)" now matches the table.
- L1-06: exactly one option is correct. The new distractor "tehollinen arvo, koska huippuarvo on pienempi" is really wrong, and its feedback is right.
- I recomputed all new answers in one script: L1-07 20 ms, L1-08 12,02 V, L2-05 5,94 V, L2-06 2,44 %, L2-07 0,261 A, L3-04 k 0,308, c −0,107, B 0,3404 T, and 22 Hz → 6,67/6,78 V, L3-05 56,85 W. All equal answers.py and exercises.json.
- Hash unchanged at start and end.
