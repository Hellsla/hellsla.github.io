VERDICT: PASS
CONTENT-HASH: d848741bf171d6aa

## Blocking

## Polish
- lesson.md:51 — "Mitä suurempi on taitekertoimien ero, sitä enemmän säde taittuu" still holds in general only for the ratio n₂ : n₁, not the difference (2,00 → 2,42 differs more than 1,00 → 1,33 but bends less) — write "mitä suurempi on taitekertoimien suhde". (B, minor; carried from round 1)
- lessons/FY7/fy7-10/lesson-answers.py:54 — comment says 0,674; 1 : 1,4895 = 0,671 (the inquiry.json value 0,671 is right). (carried from round 1)

## Checked
- Delta: tarkistus-3 prompt now "katsotaan vinosti ylhäältä veden pinnan läpi"; this resolves my round-1 polish item: the viewing path crosses only the water surface, so the model answer (one refraction, water → air, away from the normal, back-extended rays meet higher) and all four criteria fit the situation exactly.
- The prompt agrees with lesson.md:57 ("vinosti ylhäältä vedenpinnan läpi", raised part also seen displaced sideways) and with the apparent-depth figure.
- Criteria ask only what the prompt gives and asks; no new numbers or symbols in the diff.
- Content hash d848741bf171d6aa identical at start and end.
- Rest of the lesson as passed in round 1 (hash 8627fcebb3296c19).
