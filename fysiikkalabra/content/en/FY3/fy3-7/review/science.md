VERDICT: PASS
CONTENT-HASH: d2094534394d5a6a

## Blocking
- none

## Polish
- none

## Checked
- delta review 2026-11-07 (teacher's proofread replacement texts): opening question and reflect prompt now say boiling water stays at about 100 °C at normal atmospheric pressure while energy flows in: correct condition (pure water, constant pressure) per guardrail; no other change. English text carries the same meaning as fi.
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json, exit-ticket.json, figures.json (each value translates its own key). Science: every statement, number, unit, formula, sign and causal claim compared against the Finnish; chapter references against courses.json; decimal point and \cdot; sim labels (Heat/Reset/melts/boils) against lang/en.json sims.
- Update 2026-10-28: figure or sim labels shortened so they fit at 360 px (layout check): air pressure, bottom pressure, column's weight, line through origin, path, heat radiation, Object's/Water's initial temperature; re-hashed.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked lesson.md, inquiry.json (incl. the new check-c2 item, wording of the particle-model explanations, math-wrapped units), exit-ticket.json (now two questions), figures.json (new melting-curve text).

## Delta review (2026-11-01)
- Fixed: "0-degree ice into 0-degree water" (check item prompt) reworded to "ice at zero degrees into water at zero degrees", which is natural English with the same physics.
- Checked: inquiry.json prose temperatures ("at zero degrees", "100 degrees", "130-degree steam", "100-degree steam/water") match the Finnish 0-asteinen/100-asteinen/130-asteinen: same values, same physics, no unit typed as text beside maths; maths formulas unchanged, so parity with the Finnish holds. Time-axis label shift is visual only.

## Delta review (lesson.md, 2026-11-01)
- Checked: two sentences changed since bd71b55: "100-degree steam burns worse than 100-degree water" and "ice at zero degrees and water at zero degrees". Both mirror the Finnish 100-asteinen / 0-asteista; same values and physics, no unit typed as text beside maths (the maths-wrapped $100\,{}^\circ\text{C}$ elsewhere is unchanged). No blocking issues.
