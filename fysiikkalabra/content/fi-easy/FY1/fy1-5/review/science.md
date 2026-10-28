VERDICT: PASS
CONTENT-HASH: efb3a6e30bd90cf7

## Blocking
(none left)

## Fixed
- figures.json — was empty {} (figures fell back to dense Finnish) → all three figure texts written in Selkeä suomi, figures redrawn (figures.py fy1-5 --lang fi-easy)

## Polish
- (none)

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json, exit-ticket.json, meta.json, figures.json. Every simplified sentence keeps the same physics (only distance Δs ∝ t when s₀ ≠ 0; slope = speed; model value vs measurement), numbers, decimal commas and every $…$. check_i18n fi-easy: 0 errors.
- Update 2026-10-28: reviewed experiment intro, column names, word unit and string answers (none in this unit besides level3[0] unit); check_i18n shows no fy1-5 error
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked lesson text, inquiry.json (units in math, new check-c2 choice item with feedback, renumbered checks, one-question exit ticket and its answer), exit-ticket.json and figures.json (new line-read figure description); correct option still unambiguous, feedback matches its option, figure label short, en decimal point.
