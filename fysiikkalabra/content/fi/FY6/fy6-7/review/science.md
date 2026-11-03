VERDICT: FAIL
CONTENT-HASH: cf58bdca542b734b

## Blocking
- glossary.json:1938 (term "sähköenergia", listed for this lesson) — A: "käytössä takaisin esimerkiksi lämmöksi, valoksi tai liikkeeksi" teaches electrical energy turning *into heat*; heat is energy in transfer (guardrails "Energy, heat and efficiency"; FY6 thread rule: never "muuttuu lämmöksi"). — Fix: "…ja käytössä esimerkiksi sisäenergiaksi, joka siirtyy lämpönä, valoksi tai liike-energiaksi" (the entry is shared with fy2-7, so fix it once there).
- inquiry.json:326 (tarkistus-3, criterion 3) — A (assessment): the prompt asks only why heating, the water heater and the sauna stove dominate the bill; the criterion demands the energy conversion to internal energy, which the prompt does not ask, so a complete answer fails it. — Fix: drop the criterion, or add to the prompt "…ja mihin sähköenergia niissä päätyy".

## Polish
- lesson.md:306 — the summary says "laitteen virta on I = P : U" for every device; the theory (lesson.md:172) correctly limits P = UI with the effective 230 V to heating (resistive) devices. Write "lämmittävän laitteen virta" in the summary too.
- lesson.md:119, inquiry.json:18 — "Sähkölaskussa maksetaan energiasta, ei tehosta" / "Siinä ei lue yhtään wattia": several Finnish network companies now bill a power fee (kW). C at this level; "yleensä" or "pääosin" would keep it true.
- inquiry.json:259 — a bill of 49,86 € rounded to "49,9 €" by significant figures is odd for money; say the sum is 49,86 € ≈ 50 € or justify the rounding.
- lessons/FY6/fy6-7/answers.py:15 — comment names the figure "fy6-7/pesukone"; its id is `fy6-7/washer`.

## Checked
- All lesson and inquiry numbers recomputed in one script (lesson-answers.py, numeric answers, mistakes, feedback numbers): all agree (0,40; 191,6; 49,86; 9,0; 468; 23; 0,88; 150 kWh/27 €; exit 7,2 MJ and 1,0 kWh).
- Power–time figure is to scale (154 px/h, 94,5 px/kW): both rectangles 0,20 kWh.
- E = Pt stated with its condition (constant power) in theory, formula and example; 1 kWh = 3,6 MJ derived by substituting units.
- Energy wording in lesson.md:174 and tarkistus-3 model: "sisäenergiaksi, joka siirtyy lämpönä" — correct.
- Every choice item has exactly one correct option; each distractor's feedback names the right reason (ennuste-1, ennuste-2, kertaus, virhe, tarkistus-1).
- Worked example: symbolic first, 6 h 15 min converted to 6,25 h, rounding justified, check is independent (per-day route).
- Notation: energy E, power P, price a, K_perus consistent across lesson, inquiry and exit ticket.
