VERDICT: PASS
CONTENT-HASH: 7709ad5454f5a266

## Blocking
(none left; see Fixed)

## Fixed
- inquiry.json:83 — activity title 'Weigh the balloons' (the object is a glass flask, as the activity text says) → 'Weigh the flasks'
- inquiry.json:189,227 — experiment column name 'particle number N' → 'number of particles N' (the simulation label is 'Number of particles N')
- meta.json:14-19 — glossary terms left in Finnish (ideaalikaasu, mooli, moolimassa) → 'ideal gas', 'mole', 'molar mass'

## Polish
- en: hint text says "experiment 1" lower-case while other texts say "Experiment 1"; worked-example Result sentence about limiting figures is a little clumsy.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json (all activities, feedback, hints, solutions, experiment texts and names, source_note), exit-ticket.json, meta.json and figures.json (each value translates its own key) compared with the reviewed Finnish; sim labels checked with i18n.py resolve (Reset measurement, Speed, Number of particles, Temperature, Volume); terms.md terms and chapter title 'Changes of state of a gas and Boyle's law' match.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked the changed lesson text, inquiry (prior, units as math, simulation-pressure wording, new check-c2 item, renumbered check items, one-question exit ticket), exit ticket and the new figure description against the new Finnish.
