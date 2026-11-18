VERDICT: PASS
CONTENT-HASH: 36a3fdd60977dd35
## Blocking

## Polish
- solutions.md:65 — "…; Liike-energian pieneneminen" capital after a semicolon. Fix: lower case or a full stop (carried over).
- solutions.md:97 (ballistic pendulum) — "… on sama kuin …": an equation written half in words; write it with "$=$"; the general $E_\text{k} = \tfrac12 mv^2$ reuses $m$, $v$, which here are the bullet's (carried over).
- Kaava rows of many tasks — "…, joten …, joten …" twice in one sentence (line 65 too). Fix: second "joten" → "ja" (carried over).
- solutions.md L2-10 c) (unchanged) — "$-0{,}26\,\text{kg}\cdot\text{m/s} E_\text{k}' = …$" lacks a separator between the two results (carried over).

## Checked
- Round-1 Blocking fixed: line 65 now reads "Liike-energian pieneneminen on $\Delta E = E_\text{k,ennen} - E_\text{k,jälkeen}$", so the positive $\Delta E = 717\,\text{J}$ is named as the decrease the task asks, as L2-10 writes; no longer called a change (final minus initial).
- The rest of the step unchanged: $p_\text{ennen} = p_\text{jälkeen}$, $v' = m_1 v_1/(m_1 + m_2)$, $\Delta E = \tfrac12 m_1 v_1^2 - \tfrac12 (m_1 + m_2)v'^2$; numbers and answer unchanged.
- No other change since round 1 (git diff d97ccea596..HEAD on the set: line 65 only); no task, answer, tolerance or id changed.
- Captures: none opened (one-word text fix, judged from the source).
- Hash 36a3fdd60977dd35 at start and end.
