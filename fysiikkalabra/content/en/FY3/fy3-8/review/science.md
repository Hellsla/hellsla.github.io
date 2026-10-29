VERDICT: PASS
CONTENT-HASH: d5db061908d14fdc

## Blocking
(none left; see Fixed)

## Fixed
- lesson.md:16 — "the **average distance grows** between more strongly vibrating particles" was awkward and could be read as a distance between the particles that vibrate → "for more strongly vibrating particles the **average distance grows**".
- inquiry.json:75,92,93,143 — "material" mixed with "substance" (aine) used elsewhere → "substance" throughout the lesson texts.
- lang/en.json sims.fy3-8 — "Material" (label and status text) and "microscopic model" did not match the lesson/experiment column ("substance", "micro model") → "Substance", "micro model"; inquiry.json howto "other materials" → "other substances".
- figures.json — checked that all values translate their own key (none shifted); no change needed.

## Polish
- lessons/FY3/fy3-8/sim.js (shared code, not a translation file) — `tx` hard-codes the decimal comma inside the LaTeX (`{,}`), so the English canvas and readout show decimal numbers with a comma while the English text uses a point (lang/en.json format.decimal "."); have the sim take the decimal sign from the page's format block. Same pattern in the other FY3 sims. Not a meaning error.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json (all prompts, choices, feedback, hints, mistakes, solutions, experiment intros/names, howto/model), exit-ticket.json, meta.json and figures.json against the Finnish; sim labels sims.fy3-8 resolved in the language. Compared physics statements, signs, 'at least/at most', quantities, units, symbols in prose, chapter titles from courses.json, decimal sign, step labels.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked the changed lesson texts (unit formatting, interactions wording, water/liquid caveat), the new check-c2 hole item, the trimmed exit ticket, the new activity titles and the figure description against the new Finnish.
- Update 2026-10-29 (sim LaTeX PR #132): pred-3 reveal {after: theory, min: 1} and exp-1 intro "Test prediction 1." match the Finnish source exactly; pred-3 still has Bea alone correct and all four feedbacks translate the Finnish physics (asymmetric vibration, particles keep their size, heat is transferred energy); no other text still refers to prediction 3 being tested in experiment 1. lang/en.json inquiry.pending_theory "Your prediction is saved. Feedback appears when you have read the theory section." says the same as the Finnish and the built page carries it. The Finnish source and this translation changed only in these lines since the last PASS; check_i18n 0 errors; test_sims fy3-8 PASS in this language.
