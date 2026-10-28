VERDICT: PASS
CONTENT-HASH: 3a4e8d0c78b56cee

## Blocking
(none left)

## Fixed
- inquiry.json activities[11].choices[3].feedback — "The distance and the time are proportional, not the position when the initial position is not zero." (ambiguous) → "When the initial position is not zero, the distance is proportional to time, but the position is not."
- inquiry.json activities[4].howto — *Speed (playback)* did not match the sim button "Speed (replay)" → *Speed (replay)*

## Polish
- Natural, consistent register for 16–18-year-olds; terms match terms.md (uniform motion, slope, initial position, direct proportionality, Given/Find/Principle… labels).

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): every learner-facing string in lesson.md, inquiry.json, exit-ticket.json and figures.json; sim labels (Start/Pause/Reset/Moment/Speed (playback)) as named in howto; correct choices still unambiguous and feedback matches each option.
- Update 2026-10-28: reviewed experiment intro, column names, word unit and string answers (none in this unit besides level3[0] unit); check_i18n shows no fy1-5 error
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked lesson text, inquiry.json (units in math, new check-c2 choice item with feedback, renumbered checks, one-question exit ticket and its answer), exit-ticket.json and figures.json (new line-read figure description); correct option still unambiguous, feedback matches its option, figure label short, en decimal point.
