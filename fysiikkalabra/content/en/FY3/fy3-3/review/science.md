VERDICT: PASS
CONTENT-HASH: 5b30dec7dd62b914

## Blocking
(none left; list what you fixed under Fixed)

## Fixed
- Update 2026-10-28: translate_kit apply had reset the Finnish glossary words in meta.json; restored the English glossary.
- meta.json glossary — three terms left in Finnish (systeemi, tilanmuuttuja, paine) → system, state variable, pressure

## Polish
- Sim readout (lessons/FY3/fy3-3/sim.js, tx()) writes values with a decimal comma {,} in every language; outside this unit's files, not changed.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md (key idea, micro model, Kelvin formula, worked example steps and numbers, misconception, summary), inquiry.json (contribution, goals, prior knowledge, phenomenon, all predictions with options and feedback, sim text/model/calc, experiment intros and labels, conclusion model answer, find-the-error, apply problem with hints/mistakes/solution, check-your-understanding items), exit-ticket.json, meta.json, figures.json (every value translates its own key). Physics meaning, sign/direction words, proportionality to kelvin temperature, decimal points, \cdot, units and chapter reference (*Changes of state of a gas and Boyle's law*) all match. check_i18n en: 0 errors.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked lesson.md (new Limits-of-the-model section, dilute-gas wording, LaTeX temperatures, extrapolation wording), inquiry.json (new check-c2 item with options and feedback, renumbered titles, LaTeX temperatures, explain model answer, exit intro), exit-ticket.json (trimmed to 1 question) and the new figure description; check_i18n and the page checks pass.
