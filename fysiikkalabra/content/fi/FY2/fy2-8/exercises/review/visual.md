VERDICT: FAIL
CONTENT-HASH: 5059516b77ef58a8

## Blocking
- [Major] L2-06, L3-04, L3-05 text (contact-7 #74, #81, #83) — the paragraph break (\n\n) before a), b), c) in the task text is lost in the render (scripts/inquiry.py task_text/split_prompt writes one <p>), so the sub-tasks run together in one 80-130 word block, partly or wholly in bold, and the instruction for the answer box ("Vastaa laatikkoon ...") is buried in the middle of it — a student cannot see the parts or which one the box takes — fix: in task_text split the text at blank lines into separate paragraphs (one <p> or list row per a)–d), the closing "Anna/Vastaa ... laatikkoon" sentence last as the bold ask); no content change needed, re-capture afterwards.

## Polish
- [Minor] L1-07 — only the correct option starts with "Esimerkkiväite:"; the label gives it away. Give the same label to all options or none.
- [Minor] L3-05 solution, Sijoitus (contact-7 #84) — the per-source calculations run in prose; set each as its own row.

## Checked
- contact-6, contact-7 triaged (L1-06..08, L2-05..07, L3-04..05)
- #66-#67 (L1-07, L1-08), #72-#73 (L2-05), #74-#76 (L2-06, L2-07), #81-#84 (L3-04, L3-05)
- Tables, MC feedback, subscripts and fractions legible; no clipping; no 360 px exercise capture exists

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 3
