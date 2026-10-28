VERDICT: PASS
CONTENT-HASH: 04c6ee16d8dc975f

## Blocking
(none left; see Fixed)

## Fixed
- lesson.md:21-22, 118, 125 and inquiry.json (contribution, learn[2], data/find-the-error/concept feedback, explain prompt, criteria, model) — "oikeellisuus" was rendered "correctness", which is not an English physics term → "accuracy"/"accurate" throughout (repeatability vs accuracy); the misconception's "tarkka laite" is now "a precise instrument" so it does not clash with the term.
- inquiry.json activities[4].howto — referred to a "*Repeats*" slider; the simulation label is "Repetitions" → "*Repetitions* slider".

## Polish
- The exit-ticket and lesson Polish items of the Finnish review (0.1 vs 0.10 half-ranges) carry over unchanged; not a translation issue.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): every statement of lesson.md (Key idea, three error types, Formula section, Worked example steps, Misconception, Summary), inquiry.json (all activities, choices, feedback, hints, mistakes, solutions), exit-ticket.json, meta.json and figures.json against content/fi; sim labels via i18n.py resolve en (Start, Repetitions, Random error Δt_ran, Systematic error Δt_sys); signs, "at most", sys-error direction, decimal points, \cdot, step labels. check_i18n en: 0 errors.
- Follow-up 2026-10-28 (check_i18n update): experiment intro texts (activities 5–7), column names and the word unit "kertaa"/"times"; slider name *Repetitions*/*Toistoja* matches the sim label; no change needed, re-hashed.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked the lesson text, check-c2 resolution item, changed feedback, figure description and glossary against the new Finnish; same physics, terms, decimals and unambiguous correct choice; no issues found.
