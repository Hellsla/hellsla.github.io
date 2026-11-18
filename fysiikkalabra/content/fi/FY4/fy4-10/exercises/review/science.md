VERDICT: FAIL
CONTENT-HASH: 504b94a242b0ab65
## Blocking
- solutions.md:65 (ice-hockey players, $\Delta E = 717\,\text{J}$) Kaava — the new text says "Liike-energian muutos on $\Delta E = E_\text{k,ennen} - E_\text{k,jälkeen}$". A change is final minus initial; the kinetic energy's change here is $-717\,\text{J}$, and what the task asks (energy turned into other forms) is its decrease. Fix: "Liike-energian pieneneminen on $\Delta E = E_\text{k,ennen} - E_\text{k,jälkeen}$", as fy4-10-L2-10 already writes; numbers unchanged.

## Polish
- solutions.md:65 — "…; Liike-energian" capital after a semicolon. Fix: lower case or a full stop.
- solutions.md:97 (ballistic pendulum) — "$E_\text{k,alku} + E_\text{p,alku}$ on sama kuin $E_\text{k,loppu} + E_\text{p,loppu}$" and "$\tfrac12 (m + M)\,v'^2 + 0$ on sama kuin $0 + (m + M)\,gh$": an equation written half in words. Fix: write them with "$=$"; also the general $E_\text{k} = \tfrac12 mv^2$ reuses $m$, $v$, which in this task are the bullet's mass and speed (say "kappaleen" or use the bound form directly).
- Kaava rows of many tasks — "…, joten …, joten …" twice in one sentence. Fix: second "joten" → "ja".
- solutions.md L2-10 c) (context, unchanged) — "$-0{,}26\,\text{kg}\cdot\text{m/s} E_\text{k}' = …$" lacks a separator between the two results.

## Checked
- Captures: none opened (judged from text; the diff is text-only).
- Every rewritten Kaava starts from $p_\text{ennen} = p_\text{jälkeen}$ and $p = mv$ (sum of parts), then the task's form, then the unknown solved symbolically; each solved form is algebraically right and is the one Sijoitus uses.
- Explosions (skaters, rifle, ball throw, astronaut): $p_\text{ennen} = 0$, signs consistent with the chosen direction; astronaut $t = s/v_\text{a}'$ from $v = s/t$.
- Elastic equal masses: from $v_1 = v_1' + v_2'$ and $v_1^2 = v_1'^2 + v_2'^2$ follows $v_1' v_2' = 0$; rejecting $v_2' = 0$ (passing through) is correct.
- Car crash: $\tfrac12 (m_\text{A}+m_\text{B})v'^2 = \mu (m_\text{A}+m_\text{B}) g s$ then momentum across the collision only; order of the two stages right.
- L2-08 friction: $\Sigma F = ma$ with friction alone gives $-F_\mu = (m_\text{A}+m_\text{B})a$; correct.
- Rocket: $Mv = m_1 v_1' + m_2 v_2'$ with non-zero initial momentum; right.
- Line 67 Sijoitus is now an aligned block (commit b55e7a6714): same numbers, signs and units in the same order.
- Paragraph splits change no wording or number; no answer, tolerance, task or id changed.
- Hash 504b94a242b0ab65 at the start and at the end.
