VERDICT: PASS
CONTENT-HASH: d60f19cf1ffbacf4

## Blocking

## Polish
- content/fi-easy/FY4/fy4-10/exercises/solutions.md (L1 kimmoton with $\Delta E$, L3 car-park and L3 osuus tasks, Kaava) — a capital after a semicolon ("…; Kappaleiden liike-energia …", "…; Liike-energia on …"); a full stop and a new sentence reads right.
- solutions.md (L2 ballistic pendulum Kaava) — "$\tfrac12 (m + M)\,v'^2 + 0$ on sama kuin $0 + (m + M)\,gh$": an equation in words; one formula $\tfrac12 (m + M)\,v'^2 = (m + M)\,gh$ is clearer, and $m$ then cancels symbolically before $h = \dfrac{v'^2}{2g}$.
- solutions.md (L2 analysis tasks A/B, Kaava) — "liikemäärä säilyy, jos $p_\text{ennen} = p_\text{jälkeen}$" mixes the test with the law; "verrataan $p_\text{ennen}$ ja $p_\text{jälkeen}$" says what the step does.
- solutions.md (many Kaava steps) — "joten …, joten …" twice in a sentence; "ja" for the second.
- Earlier L2-10 polish items (häviää; 72 %) still open; not part of this change.

## Checked
- Hash d60f19cf1ffbacf4 at the start and the end; since 062f457c28^ only `**Kaava:**` lines of solutions.md changed (exercises.json, answers.py, numbers, answers, tolerances, ids untouched); the packet's other hunks only split paragraphs, word for word the same.
- Every rewritten Kaava opens with $p_\text{ennen} = p_\text{jälkeen}$ and $p = mv$, then the 1-D form of the brief's lesson, then the asked quantity solved before Sijoitus; rest conditions ($v_2 = 0$, $p_\text{ennen} = 0$ for explosions) stated where used.
- Elastic equal-mass billiard: $v_1 = v_1' + v_2'$ and $v_1^2 = v_1'^2 + v_2'^2$ give $v_1' v_2' = 0$; rejecting $v_2' = 0$ (ball passing through) correct; result $v_1' = 0$, $v_2' = v_1$ as the lesson states.
- Car crash: $\tfrac12 (m_\text{A} + m_\text{B})v'^2 = \mu (m_\text{A} + m_\text{B}) g s$ → $v' = \sqrt{2\mu g s}$, then momentum across the collision only; kinetic energy not used across the inelastic collision.
- Friction-graph task: $\Sigma F = ma$ with $-F_\mu = (m_\text{A} + m_\text{B})a$ → magnitude with $|a|$; consistent with Periaate.
- Astronaut: $0 = Mv_\text{a}' + mv_\text{t}'$, $v = s/t$ → $t = s/v_\text{a}'$; signs consistent with $v_\text{t}' = -4{,}0\,\text{m/s}$.
- Kinetic-energy share and loss defined as $E_\text{k,jälkeen}/E_\text{k,ennen}$ and $E_\text{k,ennen} - E_\text{k,jälkeen}$ with $E_\text{k} = \tfrac12 mv^2$; matches Sijoitus.
- Notation as in the brief's lesson ($v'$, $m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'$).
- Captures: none opened (fi-easy judged from text and the packet).
