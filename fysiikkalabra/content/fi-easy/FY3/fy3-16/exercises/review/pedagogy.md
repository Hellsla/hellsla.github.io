VERDICT: PASS
CONTENT-HASH: c5435cd354b04553
## Blocking
(none)
## Polish
- exercises.json L3-03 (tolerance 0.07) — the accepted band 1,49–1,71 kg now also takes 1,5 from a student who left out both the drinks and the warming of the freezer ice (486 kJ / 334 kJ/kg = 1,46 → 1,5), and 1,6–1,7 from one who left out only the ice warming (1,605; 1,6 was accepted before too). Unavoidable once the rounded-down value is accepted (teacher 2026-11-15); the solution shows all three energy terms, so no fix needed unless the teacher wants the check narrower.
- exercises.json L2-01, L3-03 — a rounded-down answer gets a plain "correct" although the task says to round up; the solution's answer line explains why 1,7 / 1,6 is the safe value, so the student who opens it is repaired. A feedback note for the lower value would be nicer if the schema allows it.
## Checked
- Delta: tolerance 0,04 → 0,07 on L2-01 (answer 1,7; exact 1,617) and L3-03 (answer 1,6; exact 1,511); nothing else in the diff.
- Tolerance is relative in the page check (max of 2 %, tolerance × answer, half a last-digit unit): L2-01 accepts 1,581–1,819, so 1,6, 1,62 and 1,7 pass; L3-03 accepts 1,488–1,712, so 1,5, 1,51 and 1,6 pass. Matches the teacher's decision; the earlier Polish (unrounded value rejected) is thereby closed.
- Both exact values recomputed from the task data (540 kJ / 334 kJ/kg; 536,3 kJ / 355 kJ/kg).
- L2-01: no plausible wrong method lands in the widened band.
- Task texts still ask to round up and the model answers and solutions still round up with the reason given (solutions.md lines 58, 125–126); text, check and solution do not contradict each other.
- Levels, contexts, solutions and language unchanged since the previous PASS; captures not opened (no visible change).
- Hash identical at start and end.
