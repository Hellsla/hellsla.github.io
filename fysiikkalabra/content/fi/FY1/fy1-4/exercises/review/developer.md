VERDICT: DONE

Round 2, fix mode. Only fy1-4-L2-08 changed.

exercises.json (fy1-4-L2-08 `text`):
- Major (visual): Rivi 1-4 now each in their own paragraph (blank line between rows, "\n\n" in JSON).
- Polish (science): dropped "Täsmälleen yhdellä rivillä on virhe."; the stem now says "Laskussa voi olla virhe." The option "Laskussa ei ole virhettä" is kept.

solutions.md, answers.py: unchanged (no answer or solution affected).

Checks: lint_lesson.py fy1-4 0 errors (6 warnings, all carried over); check_solutions.py fy1-4 ok; check_lesson.py fy1-4 all ok (lint, latex, build, sims, inquiry, answer positions, layout 360/768/1280).
