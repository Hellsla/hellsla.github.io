VERDICT: PASS
CONTENT-HASH: d8c5f62dda0ab6fa

## Blocking

## Polish
- content/fi-easy/FY7/fy7-16/lesson.md:57 — the paragraph split leaves "Siksi laturin ja puhelimen väli on vain muutamia millimetrejä" right after the sentences about how the figure is drawn, so "Siksi" no longer points at the steep fall of flux (line 55) — move that sentence to the end of the previous paragraph.
- content/fi-easy/FY7/fy7-16/inquiry.json:63 — "kun etäisyys tulee käämin säteen suuruiseksi": the model's half-value is at 8.8 mm, under half the 20 mm radius — "jo käämin sädettä pienemmillä etäisyyksillä" fits the numbers (same in fi).

## Checked
- Every number in lesson.md, inquiry.json, exit-ticket.json and the figures is the same as in the passed fi version (scripted diff); figure geometry identical to fi.
- inquiry.json differs from fi only in 14 fields, all sentence splits; no change of physics, correct options or numbers.
- Added explanations correct: pyörrevirta, tasasuuntaus, oikosuljettu kierros, huippuarvo, vaimennuskerroin.
- Coupling model recomputed independently (Neumann integral): 4.404 / 1.957 / 0.869 / 0.445 V, share 19.74 %, half-value 8.8 mm, R1 optimum at 20 mm 35.4 mm, at 3 mm 20.7 mm, field lines 6 and 1.
- Ravenscraft 47.3 % and mistakes; fibre halving 16.7 km, 1.58 % / 100 km, 4.9 µs/km; worked example 0.0502 mW; check-2 25.1 %; siirto 0.775 mT and its mistakes; exit ticket 20 dB.
- Exactly one correct option per choice item; distractor feedback physics right.
- Sim capture (1280 px): Finnish labels, decimal comma, readouts match the recomputation.
