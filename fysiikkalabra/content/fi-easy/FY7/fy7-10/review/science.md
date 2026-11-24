VERDICT: PASS
CONTENT-HASH: 39c930b50e38683d

## Blocking

## Polish
- Polish items of round 1 (sim.js reflected beam at R ≈ 0, lesson-answers.py comment 0,674 → 0,6714, stray "." after display blocks in hints, "ero" → "suhde") were outside this diff and were not re-checked; carry them if still open.

## Checked
- Delta: the `selita-pilli` prompt (inquiry.json:445) now says the glass is viewed obliquely from above *through the water surface* instead of "sivulta vinosti ylhäältä". The new wording is more exact. It names the geometry where refraction at the water–air surface causes the apparent break, and it rules out the side view through the glass wall, where the curved wall's lens effect would be a different mechanism.
- The prompt agrees with the model answer (rays from water to air bend away from the normal, backward extensions meet higher, the break is at the surface) and with all four criteria. No criterion asks for anything the prompt does not give.
- The prompt agrees with the theory text (lesson.md:87, "kun lasia katsotaan vinosti ylhäältä vedenpinnan läpi") and with the hero illustration's Miksi question (lesson.md:3).
- No numbers, symbols or options changed. Recomputation is not needed: the round-1 values stand.
- Content hash 39c930b50e38683d at the start and at the end (`reviews.py hash fy7-10 --lang fi-easy`).
