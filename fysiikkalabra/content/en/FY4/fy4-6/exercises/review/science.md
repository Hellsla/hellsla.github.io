VERDICT: PASS
CONTENT-HASH: 1ace0703ffbec0e1
## Blocking

## Polish
- content/en/FY4/fy4-6/exercises/solutions.md:211 — the slide up the slope: $x$ is used with the down-slope direction positive ($mg\sin\alpha + F_\mu = ma$, $a$ the deceleration) but the step does not say so, while the downhill-braking task states its axis; add "$x$ down the slope positive".

## Checked
- Captures opened: none (text and formula changes only; judged from the files and the packet).
- Every rewritten Formula step opens with $\Sigma\overline{F} = m\overline{a}$ (overline as the course requires), then $y$: $N = mg$ or $N = mg\cos\alpha$, then the friction law, and only then the combined formula; nothing opens with the combined equation any more.
- Friction terms follow the guardrail: sliding friction $F_\mu = \mu N$; static friction "at most $\mu_0 N$", its greatest value called maximum static friction; the block at rest under $20\,\text{N}$ still has friction $20\,\text{N}$, not $\mu_0 N$.
- Incline with acceleration: $mg\sin\alpha - \mu mg\cos\alpha = ma$, mass cancels, $\mu = (g\sin\alpha - a)/(g\cos\alpha)$; Earth/Moon: the bracket $(\sin\alpha - \mu\cos\alpha)$ is the same, so $a_\text{Moon} = a_\text{Earth}\,g_\text{Moon}/g$.
- Limit angle: $mg\sin\alpha_0 = \mu_0 mg\cos\alpha_0 \Rightarrow \mu_0 = \tan\alpha_0$, correct.
- Downhill braking: up the slope positive, $F_\mu - mg\sin\alpha = ma$, $a = g(\mu\cos\alpha - \sin\alpha)$, $s = v_0^2/(2a)$; slide up: $a = g(\sin\alpha + \mu\cos\alpha)$; slide from rest: $s = v_0t + \tfrac12 at^2$ with $v_0 = 0$.
- Incline at $35^\circ$: $G_x - F_\text{max} = 56.3\,\text{N} - 48.2\,\text{N} = 8.1\,\text{N}$, the new intermediate row agrees.
- $(N, F_\mu)$ slope and the peak/steady sensor task: $\mu_0 = F_\text{peak}/N$, $\mu = F_\text{steady}/N$ derived from the force balance, correct.
- Paragraph splits in Principle and Model answer change no wording, number or claim.
- answers.py run: every numeric answer agrees with exercises.json within rounding; answers, units and tolerances identical to content/fi; git diff origin/main touches no task text, answer, unit, tolerance, id or answers.py.
