VERDICT: PASS
CONTENT-HASH: f1b54f3657d64f1b

## Blocking
(none)

## Polish
1. exercises/solutions.md (skydiver, speed-vs-time table task, Reasonableness) — "the model of the chapter's graph … than the skydivers of the graph" is still the wording of my earlier polish; "the chapter's example skydiver (belly down)" places it for a student.
2. exercises/solutions.md (Formula rows of the terminal-speed tasks) — "$\Sigma F = G - F_\text{v} = mg - F_\text{v} = 0$" strings three equalities; the middle step $G = mg$ could be dropped or put in its own clause, as the other rows do.
3. exercises/solutions.md (the 1500 m drop, part b) — the Formula row now carries two sub-derivations; start part b with "b)" on a new line as a separate paragraph so a) and b) can be found.

## Checked
- Delta: the Kaava rewrite plus paragraph splits only; numbers, answers, ids, tasks and tolerances unchanged (exercises.json: presentation only).
- Every force solution starts from $\Sigma F = ma$ (with $a = 0$ for constant speed), writes $\Sigma F$ from the forces with its positive direction named, then solves in symbols before the Substitution.
- Directions are right in the new rows: down positive for falling and for up/down throws (weight and air resistance both down on the way up), forwards positive for the cyclist, and $\Sigma F = -mg - F_\text{v}$ with up-positive for the rising object.
- The half-resistance task first shows $F_\text{v} = mg$ at constant speed, then $a = g/2$; the free-fall check derives $a = g$ and $v^2 = 2gh$ from uniform acceleration.
- Paragraph splits (Principle, Free-body diagram, Model answers, Reasonableness) put one idea per paragraph with blank lines between them.
- Captures: none opened (derivation/presentation rewrite judged from the diff).
