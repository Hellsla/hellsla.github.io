VERDICT: PASS
CONTENT-HASH: 2b5836b87ab1a81b

## Blocking

## Polish
- inquiry.json:118 (simulaatio calc) — "avoimessa päässä suurin" still holds only at the eigenfrequencies (the model box now says so); add "ominaistaajuuksilla" here too, or say "poikkeaman muutos on nolla".
- inquiry.json:103 (ennuste-2, 150 Hz feedback) — now correct, but "kokonaislukukertoja … parittomia kertoja" says the same thing twice; keep only "parittomia kertoja".

## Checked
- Round 1 blocking items fixed: ennuste-2's 150 Hz feedback now says an odd number of quarter wavelengths and odd multiples, which agrees with the correct option and the theory. The worked example's check is now real: λ1 = 2L = 1,30 m, f1·λ1 = 143 m/s.
- Polish applied: lesson.md:297 "samalla kireydellä"; the model box limits the 1,0 mm drive amplitude to the string and the open-end antinode to the eigenfrequencies.
- Recomputed in one script (round 1, numbers unchanged): worked example 143 m/s, 0,433 m; Etsi virhe 200/100 Hz; siirto 170 Hz with mistakes 113, 227 and 56,7 Hz; tarkistus-2 0,80 m with mistakes 0,40 and 2,4 m.
- Sim model reproduced: string peaks of 16,7 mm at 100/200/300 Hz with 2/3/4 nodes; closed pipe peaks at 100/300/500 Hz, 1,0 mm at 200/400 Hz, 1,41 mm at 150 Hz; open pipe peaks at 200/400 Hz. Every number quoted in feedback and model answers matches.
- Boundary conditions and eigenfrequencies come from the model and are not entered; 340 m/s is used throughout the chapter.
- Superposition, string and pipe figures: node and antinode positions and amplitudes are right.
- Exactly one correct option in each choice item; experiments isolate f; the exit ticket is correct.
