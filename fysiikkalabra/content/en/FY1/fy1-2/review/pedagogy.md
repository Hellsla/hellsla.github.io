VERDICT: PASS
CONTENT-HASH: d2cd6b8493fbdd36

## Blocking
(none left; list what you fixed under Fixed)

## Fixed
- inquiry.json activities[5].names.n — "power of ten of distance n" → "power of ten of the distance n"
- inquiry.json activities[4].howto — field named *Voyager 2 date* but the sim label (sims fy1-2.voyager_paiva) reads "Voyager 2 day" → *Voyager 2 day*
- meta.json glossary — "suure", "etuliite" left in Finnish (extract skipped one-word strings as ids) → "quantity", "prefix"
- lesson.md:112, :127 — awkward "For light, one AU is…" → "Light travels one AU in…"

## Polish
- "Given and unknown." in the worked example is fine; terms match terms.md and sim labels (Travel at the speed of light, Speed, Reset).

## Checked
- Update 2026-10-28: meta.json glossary terms restored to English (the update tool had reverted them to Finnish); pages unchanged.
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): Readability for 16–18-year-olds, terms vs terms.md, step labels, button/label names vs `python3 scripts/i18n.py resolve assets/sims/fy1/fy1-2/sim.js en`, choices still unambiguous and feedback matching its option.
- Update 2026-10-28: reviewed the newly translated fields intro, source_note, names, word units (pcs, million km) and string answers; button names in *asterisks* match the sim labels and lang exp_record; check_i18n shows no fy1-2 error.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked lesson, inquiry (check-c2 item, renumbered titles, exit ticket trimmed to two questions), figures.json (ruler-read description) and prefix sentence.
