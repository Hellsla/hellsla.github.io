VERDICT: PASS
CONTENT-HASH: 4afdc6bfe3a42eeb
Mode: light (teacher 2026-11-07, "kevyt katselmointi"): the FY2 targeted-fix diff (git diff origin/main...HEAD) only

## Blocking
- none

## Polish
- [Minor] inquiry.json koe intro — the list "esiteollinen, 2020-luvun alun ja kaksinkertainen hiilidioksidi" leaves the genitive "2020-luvun alun" without its noun; readable, but "2020-luvun alun määrä" would match the menu label exactly.

## Checked
- Diff of content/fi/FY2/fy2-8/inquiry.json in context: sim model, koe intro, values.co2.420, correct-option feedback; lang/fi.json taso_nyt; sim-spec.md and tests/sims/fy2-8.json option string match the new label.
- "Tämä lämpötila ei ole vielä asettunut" and "Simulaatio alkaa 2020-luvun alun tilanteesta" read naturally; "jo nykyisellä määrällä" left later in the model refers to the real present atmosphere and stays correct.
- Rendered preview/fy2-8.html at 390 px (Playwright): menu shows "2020-luvun alun määrä", no clipping, readout "Kasvihuonekaasut: 2020-luvun alun määrä, CO2-pitoisuus 420 ppm" wraps cleanly, no horizontal overflow (scrollWidth 390).
- Note: the fi-easy feedback still says "Nykyisellä pitoisuudella" (reported in that part).
- Content hash recomputed: 4afdc6bfe3a42eeb (matches brief).
