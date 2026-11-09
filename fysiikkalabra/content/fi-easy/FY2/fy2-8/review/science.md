VERDICT: PASS
CONTENT-HASH: 322b65f689539151
Mode: light (teacher 2026-11-07, "kevyt katselmointi"): the FY2 targeted-fix diff (git diff origin/main...HEAD) only
Round: 2

## Blocking
- none

## Polish
- The changed sentence pairs "2020-luvun alussa / in the early 2020s" with the 2011–2020 warming (1.1 °C). For the early 2020s the warming is about 1.2–1.3 °C, and +14 + 1.2 still rounds to about +15 °C, so nothing is wrong. Saying that the 1.1 °C is the 2010s decade mean would make the time base clearer. Optional.
- lessons/FY2/fy2-8/sim-spec.md (not shown to students) still says "+16 °C asettuneena nykyisellä pitoisuudella (mitattu nykyarvo ...)" right after the renamed slider label. Use "2020-luvun alun pitoisuudella" there too, to keep it consistent.

## Checked
- Round 2: commit b01e11571 changes only line 154 of the feedback, "Nykyisellä" to "2020-luvun alun pitoisuudella", so it now matches fi, en and the sim label. The round-1 blocking item is resolved. The sentence reads naturally.
- Hashes recomputed with scripts/reviews.py at start and end; all six match the brief.
- 420 ppm as "the early-2020s amount": global annual-mean CO2 was about 414.7 ppm (2021), 417 (2022), 419 (2023) and 423 (2024) (NOAA), so a rounded 420 ppm fits the early 2020s, and "present" (2025 ≈ 425.6 ppm) is no longer claimed. As instructed, 420 and the temperatures (−18/+14/+15→+16/+17 °C) are unchanged. I rechecked them against the text: 14 + 1.1 ≈ 15; 560 ppm = 2 × 280 ppm; ECS 3 °C (2.5–4) → ≈ +17 °C.
- "This temperature has not yet settled", and the sim starts from the early-2020s situation at +15 °C. This agrees with the sim behaviour stated in the model and spec (it approaches +16 °C).
- The unchanged sentence "the atmosphere already absorbs most of the thermal radiation ... at the present amount" is true at today's concentration, so it needs no change.
- The experiment intro, the values label, lang sims.fy2-8.taso_nyt, the tests/sims expected option string and the sim-spec label all match the new label.
- Correct option feedback of the experiment: physics unchanged and consistent with the model.
- fi-easy model and intro: the new phrases ("2020-luvun alussa", "Tämä lämpötila", "2020-luvun alun tilanteesta") are short and clear (NOTES §12).
