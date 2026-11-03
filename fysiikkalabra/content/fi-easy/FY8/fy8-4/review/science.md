VERDICT: PASS
CONTENT-HASH: a39da44d46850279

## Blocking

## Polish
- inquiry.json activities[4].model — "Haalea aalto näyttää todennäköisyysaallon" reads as if the drawn rings were the probability wave itself; the source's "havainnollistaa todennäköisyysaaltoa" keeps it schematic (C, optional).

## Checked
- Round-1 blocker fixed: kertaus now defines intensity as "teho pinta-alaa kohti … energiaa sekunnissa yhtä pinta-alayksikköä kohti", consistent with siirto (W/m²). Round-1 polish items applied ("tietyn taajuuden valon energian pienin erä"; "sironnut = muuttanut suuntaansa osuessaan aineeseen").
- Full text diff against content/fi (lesson.md prose, all SVG aria-labels, figures.json, inquiry.json string by string, exit-ticket.json): no number, formula, unit or condition lost; drawings identical; all non-text inquiry values (correct flags, answers, tolerances, mistakes, experiment initial/locked/vary/measure) identical.
- Added glosses correct at this level: matkaero, kvanttiolio, diffraktio, lepomassa, intensiteetti.
- Conditions kept after sentence splits: "keskimäärin alle yksi fotoni", "lähes vapaa elektroni", "tyhjiössä", "vektorisuureena", ball-model proviso "jos lähde lähettää yhtä monta kvanttia sekunnissa yhtä kauan", "kun osumia on yhteensä yhtä monta".
- Recomputed in one script with own formulas: worked example 3.138e-19 J, 3.187e5 1/s, 940.8 m, 0.0013 photons, 1 mW pointer 3.2e15 1/s, dimming 1e10; p(500 nm) 1.33e-27, p(0.0711 nm) 9.32e-24, ratio 7032; Compton table 0.0711/0.0718/0.0735/0.0752/0.0760 nm; virhe 1.27e-36 vs 1.27e-27; tarkistus-2 794.9 eV (20.7 keV, 3.8 %), hc/Δλ mistake 5.17e5 eV; siirto 290.5 µN, absorbed 145 µN, no-area 9.08 µN, 29.6 mg; exit ticket 700:450 ≈ 1.6. All match lesson-answers.py and the text.
- Simulation model re-implemented independently (cos²·sinc², 480 bins, Park–Miller seed 12345): x0 = 1,0 mm gives 43/1000 one slit or path measured, 3/1000 both slits — the numbers in every feedback and model answer; window probabilities 4.27 % and 0.27 %.
- Exactly one correct option in kertaus, ennuste-1, ennuste-2, compton-data, virhe, tarkistus-1; reworded compton option "Mitä suurempi sirontakulma on, sitä enemmän se luovuttaa" agrees with the table; distractor feedback physics unchanged.
- Experiments koe-1/koe-2 isolate raot and reitti respectively, with hiukkanen and x0 locked; simState gives N, n, osuus (capture koe-1 checked).
- Duality text keeps "ei vaihda muotoaan", "koejärjestely ratkaisee", probability interpretation; scope respected (no de Broglie wavelength).
