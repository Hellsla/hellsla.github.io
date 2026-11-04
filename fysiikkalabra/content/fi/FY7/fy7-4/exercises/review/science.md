VERDICT: PASS
CONTENT-HASH: e1d566ce1d59da9e

## Blocking
- (none)

## Polish
- solutions.md fy7-4-L3-04 Periaate (B) — "tanko lähtee liikkeelle vasta, kun IlB > μmg": starting is set by static friction, not the sliding coefficient μ the task fits — "liikkuvan tangon kiihtyvyys on positiivinen vain, kun IlB > μmg".
- docs/exercise-bank/FY7.md fy7-4 Taso 3 — the plan's terminal-velocity/energy rail task and the commutator + torque task were replaced by L3-04 (rail with friction, data) and L3-05 (levitating wire); the substitution is sound (torque is not in the lesson brief), so record it in the plan.
- solutions.md fy7-4-L2-07 Järkevyys — "lähellä luvussa esitetyn kaiutinkelan kierroslukua 60" relies on an assumed 1,2 cm radius; say "jos säde on sama kuin luvun esimerkissä (1,3 cm), noin 65 kierrosta".
- Deterministic checks show "FAIL layout 360 px" for fy7-4; not a science matter, but the visual/developer reviewers should confirm it is not in the exercise set.

## Checked
- Recomputed all 19 numeric answers in one script with my own formulas; all equal answers.py: new ones 0,30 N, 0,09397 N, 0,08513 T (half range 0,0018 T), 0,04055 T (student's 0,0169 T reproduced), 5,27 m (LSQ through origin 5,795 N/A; free intercept −0,007), 0,351 T and μ = 0,200 (LSQ slope 0,935, intercept −1,96), 54,25 A.
- L1-06: I east × B north = up; one correct option; every distractor's feedback right.
- L1-07 F ∝ 1/r and L1-08 F ∝ sin α (not α) correctly reasoned.
- L2-05: half range called a scatter estimate, not the uncertainty of the mean (guardrail met).
- L2-06: error is exactly the plan's (whole length instead of the part in the field); ratio 2,5 : 6,0 explains the student's value.
- L3-04: N2L model a = (lB/m)I − μg; negative intercept explained by friction; data consistent with B = 0,35 T, μ = 0,20.
- L3-05: repulsion needs opposite currents (natural in series); F = μ₀I²l/(2πr) = mg; vertical stability argument (F ∝ 1/r) correct; lateral question not asked.
- Levels 8/7/5; scope FY7 + FY4 dynamics; notation matches the brief; every new solution complete, symbolic first.
- Rendered L3-04/L3-05 at 1280 px: formulas render, no overflow.
