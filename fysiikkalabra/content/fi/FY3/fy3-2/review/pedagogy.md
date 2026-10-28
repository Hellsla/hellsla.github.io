VERDICT: PASS
CONTENT-HASH: f1306d3bece1b9c4
## Blocking

## Polish
- exit-ticket.json q2 and inquiry.json solution of task "2. Kuvaaja ja laskeminen" — ranges are half converted ("0–$0{,}50\,\text{m}$", "4,0–$8{,}0\,\text{m}$"); the plain-text first number sits beside a LaTeX second one. Write the whole range in one math span, e.g. $0\ldots 0{,}50\,\text{m}$ or "välillä $0$–$0{,}50\,\text{m}$".
- inquiry.json (several prompts, e.g. "60 N:n voimalla", "98 N painoista", "48 N:n voimalla") — some N values stay plain while neighbouring m, s, W values are LaTeX; page shows two number styles side by side. Convert for consistency.
## Checked
- Delta judged in context: all changes are unit-in-LaTeX conversions plus two content edits; sentences stay grammatical (case endings after math spans: `$10\,\text{kg}$:n`, `$120\,\text{W}$:sta` are correct Finnish).
- Kiuas sentence (lesson.md): "6000 joulea sähköenergiaa sisäenergiaksi, joka siirtyy lämpönä kiviin ja ilmaan" reads well, is one idea, correct terms.
- Joule feedback: "ero on joka rivillä samansuuntainen" is true of the table (194<196, 389<392, 583<588) and the hedge "luultavasti" fits a student's evidence; the correct option still has exactly one right answer.
- Choice items (kertaa, ennuste 1-3): each still has one correct option; no feedback leaks changed.
- Worked example result "Tulos" stage still one step, sig-figure rationale intact.
