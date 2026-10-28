VERDICT: PASS
CONTENT-HASH: 5b30dec7dd62b914

## Blocking
(none left; list what you fixed under Fixed)

## Fixed
- inquiry.json activities[5].text — "Try freely what temperature and volume do…" (unidiomatic) → "Explore freely what temperature and volume do…"
- inquiry.json activities[6].intro — "kelvin temperatures" → "temperatures in kelvins" (consistent with the rest of the lesson)
- figures.json hero — "on a summer heat day" → "in the summer heat" (figure redrawn)

## Polish
- en exercises.json uses plain spaces between number and unit where the Finnish has no-break spaces; harmless.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): natural English for 16–18-year-olds, terms per terms.md (state variable, surroundings, absolute zero, slope, extrapolation, micro model), step labels (**Given:** … **Reasonableness:**, Rearranged formula, Unit conversions), sim control names (*Speed*, *measured*, *theory*) against the en sim labels, every option still unambiguous and its feedback matching it, hints and model answers complete.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked lesson.md (new Limits-of-the-model section, dilute-gas wording, LaTeX temperatures, extrapolation wording), inquiry.json (new check-c2 item with options and feedback, renumbered titles, LaTeX temperatures, explain model answer, exit intro), exit-ticket.json (trimmed to 1 question) and the new figure description; check_i18n and the page checks pass.
