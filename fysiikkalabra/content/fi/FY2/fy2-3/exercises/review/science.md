VERDICT: PASS
CONTENT-HASH: 633302ba5d59bc16

## Blocking

## Polish
- solutions.md fy2-3-L2-09 a) — "Silloin sähköä tuottava joutuu maksamaan siitä, että sähkö otetaan verkosta" goes a step beyond the article (which says only that the price can fall below zero when production exceeds consumption). It is true for a seller at a negative price; "artikkelin mukaan" should not cover it (C).
- Earlier item: L1-09 "hp" for metric horsepower (C) is still open.

## Checked
- Delta review: hash 633302ba5d59bc16 at the start and the end; I judged only the added L2-09 (exercises.json, solutions.md, answers.py).
- Source values checked against docs/audits/2026-11-16-fy2-aineistot.md: Yle 74-20045312, 16.8.2023; Vaasan sähkö 0,41, Oomi 0,25, Vattenfall 0,50 snt/kWh; Vaasan sähkö treats a negative hour as zero, Oomi and Vattenfall credit it; Fingrid's area price excludes taxes and transmission. All agree.
- Recomputed in my own script: E = 2,0 kW · 4 h = 8,0 kWh; C = −5,0 · 8,0 = −40 snt (answers.py −40, tolerance 0,02); +15 snt/kWh → 120 snt, difference 160 snt; margin 0,41 · 8,0 = 3,28 ≈ 3,3 snt.
- C = hPΔt is solved in symbols before substitution; kW·h = kWh needs no conversion; two significant figures from 2,0 kW and −5,0 snt/kWh with the four hours exact (CLAUDE.md, 2026-11-16).
- The packet shows the b) chain flattened onto one line ("8,0 kWh C = …"); on disk it is an aligned display block, so no error.
- d): storage losses as internal energy transferred as heat is correct; the limits (capacity, hourly contract) are stated.
- Stays inside FY2 (E = Pt, kWh, energy price; storage and timing as energy-system reasoning).
