VERDICT: PASS
CONTENT-HASH: bde30bba307db58e

## Blocking
(none)

## Polish
1. exercises/solutions.md:403 (two-surface slope-and-flat task, Formula) and :435 (height from the speed table) — these two Formula paragraphs are now about 120 and 110 tokens; split each after the first derived result (e.g. after $L = \dfrac{\mu_2 d}{\sin\alpha - \mu_1\cos\alpha}$, and after $h = \sum\dots$) so no paragraph nears the 120-word limit.
2. exercises/solutions.md:193 (chute with three parts, Formula) — the sentence "On a slope $N = mg\cos\alpha$ and the horizontal part is $x = s\cos\alpha$ …" is the key idea of the task; give it its own sentence in the Principle rather than the middle of the Formula.
3. exercises/solutions.md (Formula rows with "Zero level at …") — "$E_\text{initial}$ / $E_\text{final}$" are introduced in each row but not defined for a first-time reader; one clause in the first such solution ("initial = at the start, final = at the end") suffices.

## Checked
- Delta: the Kaava rewrite plus paragraph splits only; numbers, answers, ids, tasks and tolerances unchanged (exercises.json: presentation only).
- Force solutions start from $\Sigma F = ma$ with the positive direction named (up for the lift, down for the descent, $\Sigma F = 0$ for constant speed on the slope and with the rope); then $N$ or $a$ is solved in symbols.
- Energy solutions start from $E_\text{initial} = E_\text{final} (+ W)$, with $E_\text{k} = \tfrac12 mv^2$, $E_\text{p} = mgh$, $F_\mu = \mu N$ and the normal force on each surface derived, then the combined expression; the substitution rows are untouched and still use the last symbolic form.
- Signs and directions checked in the new rows (friction work as $-F_\mu s$, $E_\text{final} = E_\text{k}$ at the foot, $|\Delta E_\text{mech}|$ for the loss, $W = Th$ and $P = W/t$ for constant speed).
- Paragraph splits (Principle, Model answers, Reasonableness) give one idea per paragraph.
- Captures: none opened (derivation/presentation rewrite judged from the diff).
