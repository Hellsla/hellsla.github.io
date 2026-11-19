VERDICT: PASS
CONTENT-HASH: 9b74a742cd52d2d6
## Blocking

## Polish

## Checked
- Captures opened: none (text and formula changes only; judged from the files and the packet).
- L3-03 (ramp): energy balance $E_\text{mech,1} = E_\text{mech,2} + E_\text{other}$ with only kinetic energy at the foot ($h = 0$, the stated zero level) and only potential energy at the top ($v = 0$) gives $E_\text{other} = \tfrac12 mv^2 - mgh$; the Principle's "internal energy" wording follows the guardrail.
- $(v^2, E_\text{k})$ graph: from $E_\text{k} = \tfrac12 mv^2$ the slope is $\tfrac12 m$, $m = 2k$, correct.
- Bouncing ball: $E_\text{mech} = E_\text{k} + E_\text{p}$ with $E_\text{k} = 0$ at the top, so $E_\text{mech} = mgh$ and $\Delta E = mg(h_0 - h_4)$; the share from the height ratio is justified.
- Roller-coaster data: $E_\text{mech} = \tfrac12 mv^2 + mgh$ and the balance $E_\text{mech,1} = E_\text{mech,5} + \Delta E$, correct.
- Stopping distance: uniform motion in the reaction time, $s_\text{r} = v_0 t_\text{r}$; $t_\text{b} = -v_0/a$, $s_\text{b} = -v_0^2/(2a)$ (with $a < 0$), $s = s_\text{r} + s_\text{b}$, unchanged.
- Every rewritten Formula step starts from a basic equation (energy balance, $E_\text{k}$, $E_\text{mech} = E_\text{k} + E_\text{p}$, $x = vt$) and solves symbolically before the unchanged substitution.
- Paragraph splits in Principle, Model answer and Reasonableness change no wording, number or claim.
- answers.py run: every numeric answer agrees with exercises.json; answers, units and tolerances identical to content/fi; git diff origin/main touches no task text, answer, unit, tolerance, id or answers.py.
