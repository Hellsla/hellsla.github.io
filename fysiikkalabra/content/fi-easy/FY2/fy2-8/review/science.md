VERDICT: PASS
CONTENT-HASH: 0820bc39ae57687e

Follow-up review of the fix commit 2c31ff041 (delta from 7c190a2fcc2fb406). Changes: ennuste-1 correct-option feedback, tarkistus-3 criterion 2, and Ydinajatus now defines **säteilytasapainomalli** (Maa lähettää avaruuteen yhtä paljon energiaa kuin saa Auringolta) and **efektiivinen säteilylämpötila**.

## Blocking

None.

## Polish
- lesson.md:136 — "Ilman sitä merien vesi olisi jäässä" (C); "olisi todennäköisesti jäässä" would match the caveat.
- inquiry.json:71, :410 — "nostaa lämpötilaa noin $33\,\text{K}$" could become "ero, noin $33\,\text{K}$, …" (C).

## Checked
- Both earlier blocking items resolved: inquiry.json:63 ("Maan yksinkertainen säteilytasapainomalli antaa efektiiviseksi säteilylämpötilaksi noin $-18\,{}^\circ\text{C}$. Maanpinnan keskilämpötila on kuitenkin noin $+15\,{}^\circ\text{C}$. Ero on noin $33\,\text{K}$ …") and :497 criterion now matching its model answer (:501). Physically right.
- New Ydinajatus definition is right: in balance the energy sent to space (reflected plus emitted) equals what the Earth receives; with albedo ≈ 0,3 that gives $\approx 255\,\text{K}$.
- Consistency: grep of "-18" — Ydinajatus, misconception (:328), Tiivistelmä (:331), sim model box (:112), koe-1 (:154), ennuste-1, tarkistus-3 all say the same.
- GISTEMP 2025 anomaly map caption (base 1951–1980, grey = no data, not a photo) correct; numbers unchanged.
- Hash same at start and end.

## Shared issues
- Outside this hash: exercises/exercises.json:69 and solutions.md:125 keep the older wording.

## Follow-up (uncommitted edit, hash 70f1856a80c78f26 → 0820bc39ae57687e)
- Changes: ennuste-1 correct-option feedback (inquiry.json:63) and the simulaatio `model` parenthesis (:112) now explain *säteilytasapainomalli* (Maa lähettää avaruuteen yhtä paljon energiaa kuin se saa Auringolta) and *efektiivinen säteilylämpötila* (the temperature the model gives).
- Physics right and the same as Ydinajatus (lesson.md:136): "sent to space" covers reflected plus emitted, so the balance gives $\approx 255\,\text{K}$ with albedo ≈ 0,3. The hedge stays ("ei tarkka ennuste"; "Maanpinnan keskilämpötila on kuitenkin noin $+15\,{}^\circ\text{C}$"). Values −18 °C, +15 °C, 33 K unchanged; no new number, formula or step, so §12 rule 1 holds.
- Polish (C): "yhtä paljon energiaa" is strictly a rate (energy per unit time); fine at this level.
- Blocking: none. Hash 0820bc39ae57687e at start and end.
