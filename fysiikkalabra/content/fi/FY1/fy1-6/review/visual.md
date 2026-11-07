VERDICT: PASS
CONTENT-HASH: 8df0fe9533bdd32b
Mode: light (teacher 2026-11-07, "kevyt katselmointi": round-2 diff since edb368de4 only)

## Blocking
- none

## Polish
- [Minor] sim.js — pallo B ja sen nopeusnuoli ovat lähes samaa sinistä, ja pallo A:n nuoli on sininen vaikka pallo on oranssi; ehkä selitteeseen rivi 'sininen nuoli = nopeus' jos sitä ei ole.

## Checked
- fy1-6 sim.js (COL/VEL, arrow-kutsu), lesson.md, exit-ticket.json (6,06); kuvien osalta lähdekoodi/SVG (ei kuvakaappauksia, kevyt katselmointi)
- Nopeusnuolet ovat sim.js:ssä nyt nopeuden sinisiä (VEL #1971c2), pallot erotetaan toisistaan sijainnillaan ja pallon, jälkipisteiden, kuvaajan ja selitteen värillä (A oranssi, B sininen); koodista ei näy vaaraa, että pallon B tunnusväri ja nopeuden väri sekoittuisivat pahasti: B-pallo (38,110,214) ja nuoli (25,113,194) ovat lähes samaa sinistä, mutta nuolet ovat aina pallon vieressä ja selite kertoo asian. 'metriä sekunnissa toiseen' on selkeä ja luonteva.
