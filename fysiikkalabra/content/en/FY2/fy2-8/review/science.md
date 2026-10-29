VERDICT: PASS
CONTENT-HASH: a66673b866cebfa2

## Blocking
- none left (fixes listed under Fixed)

## Fixed
- lesson.md:19 — biomass carbon "bound into plants only over a few decades" (lost the sense of *vasta*, "only recently") → "only during the last few decades"
- inquiry.json activities[17].model — "escapes more and more slowly" (suggested a progressive slowdown) → "more slowly than before" (= *entistä hitaammin*)
- inquiry.json activities[3].choices[1].feedback, lesson.md:30 — "per mass" → "per unit mass"
- meta.json glossary[3] — left in Finnish ("ilmastonmuutos") → "climate change"

## Polish
- inquiry.json activities[5].values.co2 (the experiment table's level names) are still Finnish in en. check_i18n refuses a translated `values` ("only texts are translated"), so they cannot be fixed inside the unit. `values` should be added to the text keys, using the sim labels sims.taso_* ("no greenhouse gases", "pre-industrial amount", "present amount", "double carbon dioxide").

## Checked
- Update 2026-10-28: meta.json glossary terms restored to English (the update tool had reverted them to Finnish); pages unchanged.
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md (all sections except SVG bodies), figures.json, inquiry.json including the new sim/experiment texts (howto, model, calc, intro, names, measure label, question and feedback), exit-ticket.json and meta.json, compared sentence by sentence for physics, numbers, units, decimal points, \cdot, sign/direction words and chapter titles against content/en/courses.json; sim labels via i18n.py resolve en. check_i18n en: 0 errors.
- Update 2026-10-28: experiment option words (`values`) translated to match the English sim labels; re-hashed.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked the lesson text, inquiry texts (fossil-fuel wording, check items, feedback, model answer) and criteria
