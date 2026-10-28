VERDICT: PASS
CONTENT-HASH: 57c42b6e7b23df6f

## Blocking
(none left)

## Fixed
- figures.json — was empty {} (figures fell back to dense Finnish) → all three figure texts written in Selkeä suomi, figures redrawn (figures.py fy1-5 --lang fi-easy)

## Polish
- (none)

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json, exit-ticket.json, meta.json, figures.json. Every simplified sentence keeps the same physics (only distance Δs ∝ t when s₀ ≠ 0; slope = speed; model value vs measurement), numbers, decimal commas and every $…$. check_i18n fi-easy: 0 errors.
- Update 2026-10-28: reviewed experiment intro, column names, word unit and string answers (none in this unit besides level3[0] unit); check_i18n shows no fy1-5 error
