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
- None.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json (all prompts, choices, feedback, hints, mistakes, solutions, experiment intros/names, howto/model), exit-ticket.json, meta.json and figures.json against the Finnish; sim labels sims.fy3-8 resolved in the language. Compared register, term consistency with terms.md and lang labels, and that each question, hint and feedback still matches its option.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked the changed lesson texts (unit formatting, interactions wording, water/liquid caveat), the new check-c2 hole item, the trimmed exit ticket, the new activity titles and the figure description against the new Finnish.
- Update 2026-10-29 (sim LaTeX PR #132): pred-3 is now revealed after the theory section (reveal after theory, min 1) and exp-1 says "Test prediction 1", both matching the Finnish; the waiting note lang/en.json inquiry.pending_theory ("Your prediction is saved. Feedback appears when you have read the theory section.") is clear and consistent with the existing pending note. Sim labels (KaTeX) and the rest of the translation re-compared with the current Finnish: complete and faithful.
