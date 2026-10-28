VERDICT: PASS
CONTENT-HASH: 901e18a6fefc4a77

Round 2: re-check of round-1 Blocking items against the fix diff.

## Blocking

## Polish
- inquiry.json:481 — check-2 solution writes "pV = NkT" with a Boltzmann constant k the chapter never introduces; "p ∝ NT/V (tilanyhtälöstä, kun n ∝ N)" says the same with the chapter's symbols.
- lesson.md:230 — "kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan": correct for the point-particle model as written, but the guardrail wording is "etenemisliikkeen keskimääräiseen liike-energiaan"; using it avoids a clash for the diatomic/CO₂ gases discussed in the same chapter.
- inquiry.json:389 — "2{,}0\,\text{l}" here vs \textsf{l} elsewhere (typography only).

## Checked
- Round-1 Blocking resolved: lesson.md:38 now says the masses are "esimerkkipunnituksessa (keksityt arvot, joissa on punnituksen hajontaa)" and lesson.md:233 "Esimerkkipunnituksesta saadaan luku…"; theory now agrees with inquiry.json "punnitus" (source simulated) and the johtopäätös model answer. The changed sentences are grammatical; numbers unchanged.
- The diff touches only these two lesson.md lines; nothing else in the lesson, inquiry, figures or sim changed.
- From round 1, still valid: worked example 0,2073 → 0,21 mol, 0,83 g; R from example data 8,32 ≈ 8,3 (helium row 8,302, mistakes correct); hot-air balloon 2645 → 2,64·10³ kg; virhe 0,083 mol; check-2 3,0; exp-2 N = 50; exit ticket 0,601 mol.
- Simulation table pV/(NT) values match the model; sim.js wall-impulse pressure, v ∝ √T, no particle collisions (stated).
- Figures to scale; every choice item has exactly one correct option with correct distractor feedback.
- Hash identical at start and end.
