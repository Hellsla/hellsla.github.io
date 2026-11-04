VERDICT: FAIL
CONTENT-HASH: dca6b1359dc2ef02

## Blocking
- [Major] L2-05, L2-06, L3-04, L3-05 text (contact-5 #61-#63; contact-6 #64, #70-#72) — the paragraph break (\n\n) before a), b), c) in the task text is lost in the render (scripts/inquiry.py task_text/split_prompt writes one <p>), so the sub-tasks run together in one 80-130 word block, partly or wholly in bold, and the instruction for the answer box ("Vastaa laatikkoon ...") is buried in the middle of it — a student cannot see the parts or which one the box takes — fix: in task_text split the text at blank lines into separate paragraphs (one <p> or list row per a)–d), the closing "Anna/Vastaa ... laatikkoon" sentence last as the bold ask); no content change needed, re-capture afterwards.

## Polish
- [Minor] L3-05 solution, Sijoitus (open-exercises-L3-1280-7) — eight calculations in one prose paragraph, broken mid-chain at "0,015 ·"; give each period its own row (aligned).

## Checked
- contact-5, contact-6, contact-7 triaged (L1-06..08, L2-05..07, L3-04..05)
- open-exercises-L3-1280-7 and -8 at full size (L3-05 table, solution, Vastaus, Järkevyys)
- MC feedback (L1-06, L2-07), tables, fractions legible; no clipping; no 360 px exercise capture exists

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 3
