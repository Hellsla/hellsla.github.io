VERDICT: PASS
CONTENT-HASH: 9d4d47952b34a428
## Blocking
(none)
## Polish
- exercises.json L2-01 — an unrounded 1,617 or 1,62 is also rejected though correct physics; the task text asks to round up, so acceptable, but the wrong-answer feedback should say "round up to two figures" if it does not.
## Checked
- Delta: tolerance 0,04 on L2-01 (answer 1,7; exact 1,617) and L3-03 (answer 1,6; exact 1,511). Rounded-down 1,6 / 1,5 are now rejected, as the tasks say "round up"; 1,7 / 1,6 pass. Judged from the diff.
- Judged from the diff and the previous PASS; captures not opened.
