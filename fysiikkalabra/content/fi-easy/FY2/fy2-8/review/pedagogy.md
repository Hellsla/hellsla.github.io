VERDICT: PASS
CONTENT-HASH: 322b65f689539151
Mode: light (teacher 2026-11-07, "kevyt katselmointi"): the FY2 targeted-fix diff (git diff origin/main...HEAD) only
Round: 2

## Blocking
- none

## Polish
- Correct-option feedback (line 154) now begins a sentence with a numeral: "2020-luvun alun pitoisuudella maapallo on ...". Finnish style avoids that; "Kun pitoisuus on 2020-luvun alun tasolla, maapallo on ..." reads more smoothly.

## Checked
- git show b01e11571: the correct-option feedback "Nykyisellä pitoisuudella" -> "2020-luvun alun pitoisuudella"; hash 322b65f689539151 verified with scripts/reviews.py.
- Correction to my round-1 report: I wrote that the fi-easy feedback never used "nykyinen". That was wrong. My search missed this line, and the science and visual reviewers found it.
- The level label is now consistent in fi-easy: select (lang/fi-easy.json), experiment values, koe intro, model text and feedback; grep finds no "nykyinen/nykyisellä" naming the level. The remaining "jo nykyisellä määrällä" in the model is generic wording about absorption and does not conflict.
- The feedback still explains the warming lag (about +15 °C now, still warming towards +16 °C); substance agrees with fi and en; short, clear sentences (NOTES §12).
