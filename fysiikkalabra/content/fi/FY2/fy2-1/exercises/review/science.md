VERDICT: FAIL
CONTENT-HASH: dc9ac2fa1d6708f1
Mode: full
Round: 1

## Blocking
- content/fi/FY2/fy2-1/exercises/exercises.json:131 — (A, causality) L1-09 statement 1 feedback says "osa pallon potentiaalienergiasta muuttui törmäyksessä ... lämpöenergiaksi". At the collision the ball is at the floor (E_p = 0); what turns into thermal energy and sound there is its kinetic energy (via deformation), and statement 5's feedback and the model answer rightly say "liike-energian kautta". The feedback gives a wrong mechanism. — Fix: "osa pallon mekaanisesta energiasta muuttui törmäyksessä ja ilmanvastuksen takia lämpöenergiaksi ja ääneksi, joten $E_\text{p} + E_\text{k}$ pieneni."

## Polish
- content/fi/FY2/fy2-1/exercises/exercises.json:149 — statement 5 says the energy is "ympäristössä", but its feedback and the model answer put it in the ball, the floor and the air (the ball is not its own surroundings). Write "on lämpöenergiana pallossa, lattiassa ja ilmassa" so the three agree.
- content/fi/FY2/fy2-1/exercises/exercises.json:141 — statement 3 feedback says "likimain eristetyn" while the task states the system is assumed isolated; "oletettu eristetty systeemi" matches the task. (The Earth's role in E_p is left out as in the lesson's skater example: a fair C simplification.)
- solutions.md L3-04 c) and exercises.json L1-07 third option: the round-3 Polish items (constant total presented as caused by conservation; "Ympäristö kuuluu systeemiin") are still open.

## Checked
- Hash dc9ac2fa1d6708f1 at start and end; the only change since the PASS set is L1-09 (exercises.json, solutions.md), as in commit 18b454cd1.
- L1-09 key recomputed from the model (isolated system, mechanical energy dissipated in each bounce): 1 true, 2 false, 3 true, 4 false, 5 true; matches `answer`, the `true` flags and solutions.md.
- Each false statement is wrong for the reason its feedback gives (energy not used up; thermal energy and sound count in the total).
- Type 8 rules met: 5 statements, both truth values present, a reason in every feedback.
- Scope: FY2 energy forms and E_alussa = E_lopussa only, no expressions; notation E_p, E_k as in the lesson.
- No number in L1-09, so answers.py needs no line; the other tasks are unchanged from the PASS set.
