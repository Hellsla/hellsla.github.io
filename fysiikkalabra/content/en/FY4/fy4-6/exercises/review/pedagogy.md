VERDICT: PASS
CONTENT-HASH: 1ace0703ffbec0e1

## Blocking
None.

## Polish
- solutions.md, Moon-and-Earth ramp task Formula — one line carries the law, the components, the Earth expression for mu and the Moon comparison (about 90 words of symbols). It is correct, but a student who could not solve the task would follow it better with the Moon step on its own line.
- solutions.md, the limit-angle task Formula ($\mu_0 = \tan\alpha_0$) — $N$ appears in "$mg\sin\alpha_0 = \mu_0 N$" before it is defined; write "$y$: $N = mg\cos\alpha_0$" first, or insert "where $N$ is the normal force".
- solutions.md, the task with a downhill and a horizontal braking case — the line is long; split the horizontal and the downhill parts into two sentences-with-formula rows.

## Checked
- Round 1, delta (work queue 8g): no number, answer, tolerance, task or id changed. I compared every removed line with the added text: all paragraph splits are lossless and in the same order; only the Formula lines and one Substitution differ.
- Every Formula now opens with $\Sigma\overline{F} = m\overline{a}$ (or the equilibrium case $\overline{a} = \overline{0}$), then the components, then $F_\mu = \mu N$ with $N$ solved, and the mass is shown cancelling; each result (mu = F/(mg), mu = (g sin a - a)/(g cos a), a = g(sin a + mu cos a), a = g(mu cos a - sin a), a = mu g) is correct, including the sign choice for the downhill braking case.
- The Substitution of the slope-margin task now shows $56.3\,\text{N} - 48.2\,\text{N} = 8.1\,\text{N}$ (same answer, one step more).
- Static-friction wording (maximum static friction, sliding friction) unchanged and consistent with the glossary.
- Tasks, levels, counts and figures unchanged.
- Captures not opened: text-structure change only.
