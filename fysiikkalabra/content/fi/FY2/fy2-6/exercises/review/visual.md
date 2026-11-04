VERDICT: FAIL
CONTENT-HASH: db6b0a8bbd9663c1

## Blocking
- [Major] L2-06, L2-07, L3-04, L3-05 text (open-exercises-L2-1280-7/-8..., L3-1280-4, -6; contact-5 #57-#59, contact-6 #64, #66) — the paragraph break (\n\n) before a), b), c) in the task text is lost in the render (scripts/inquiry.py task_text/split_prompt writes one <p>), so the sub-tasks run together in one 80-130 word block, partly or wholly in bold, and the instruction for the answer box ("Vastaa laatikkoon ...") is buried in the middle of it — a student cannot see the parts or which one the box takes — fix: in task_text split the text at blank lines into separate paragraphs (one <p> or list row per a)–d), the closing "Anna/Vastaa ... laatikkoon" sentence last as the bold ask); no content change needed, re-capture afterwards.

## Polish
- [Minor] L3-05 solution, Sijoitus (contact-6 #67-#68) — a), b), c) calculations for two plants are rows inside prose chains; set each plant's step as its own aligned row.
- [Minor] L2-05 text — "Vastaa muutoksella." is a clipped sentence; "Anna vastaus muutoksena prosenttiyksikköinä."
- [Minor] L2-06 text — the student's claim is in straight quotes "..."; use Finnish ”...” both ends.

## Checked
- contact-5, contact-6 (all new tasks triaged: L1-06..08, L2-05..07, L3-04..05)
- open-exercises-1280-x via contact-5 #49-#52 (L1-06..08), #56-#60 (L2-05..07), #61-#68 (L3-04, L3-05)
- Tables (decimal comma, units in headers), MC feedback blocks, solution rows and fractions legible; no clipping; no 360 px exercise capture exists

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 3
