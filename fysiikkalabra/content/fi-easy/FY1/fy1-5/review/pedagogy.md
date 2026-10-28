VERDICT: PASS
CONTENT-HASH: 57c42b6e7b23df6f

## Blocking
(none left)

## Fixed
- inquiry.json activities[12].solution and [15].solution — Periaate, Kuvaajan lukeminen, Järkevyys were dense Finnish → split into short sentences, all steps kept
- inquiry.json activities[0].question, [4].text, [7].prompt, [9].prompt, [12].prompt, [13].text, [16].prompt, [17].text — long compound sentences → short sentences / separate questions
- inquiry.json feedback [5]c2, [6]c2, [11]c1, [12]mistakes[1], [14]c0–c2, [15]hints[1], [15]mistakes[0] — split, same reasoning kept
- exit-ticket.json [0].q, [0].a, [2].q, [2].a — split into short sentences
- figures.json — Selkeä suomi descriptions added (was empty)

## Polish
- Short labels and simple prompts left as in Finnish (already easy).

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): every learner-facing text; cognitive demand, hints, feedback and options unchanged; correct choice still unambiguous.
- Update 2026-10-28: reviewed experiment intro, column names, word unit and string answers (none in this unit besides level3[0] unit); check_i18n shows no fy1-5 error
