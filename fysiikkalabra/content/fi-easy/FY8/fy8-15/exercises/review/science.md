VERDICT: PASS
CONTENT-HASH: d6490d7f746bd076
SCOPE: delta added-exercise from d9f79207147a8ef9 base 1bdc56f920e4

## Blocking

## Polish
- exercises.json fy8-15-L1-10 — "Jokainen ruutu on yksi hiukkanen" while the box $W^\pm$ holds two (a particle and its antiparticle) and $g$ stands for eight colour states; the count of boxes asked is unaffected (C-level simplification). Optional: "Jokainen ruutu on yksi hiukkaslaji".
- solutions.md fy8-15-L2-08 — c) could add that $t \to W^+ + b$ is by far the most common decay; not needed by the task, which asks only what charge allows.

## Checked
- Delta only: the two added exercises fy8-15-L1-10 and fy8-15-L2-08 with their solutions and answers.py lines; nothing else re-reviewed.
- Figure fy8-15/taulukko (figures.py): 17 boxes, every box shows its charge: u, c, t $+2e/3$; d, s, b $-e/3$; $e^-$, $\mu^-$, $\tau^-$ $-e$; three neutrinos, $g$, $\gamma$, $Z^0$, $H$ $0$; $W^\pm$ $\pm e$. Matches the standard model; the description gives the same values in words.
- L1-10 recomputed independently: neutral boxes 3 + 3 + 1 = 7 (a), of them leptons 3 neutrinos (b); 10 charged + 7 = 17. answers.py 7 agrees; integer answer, tolerance 0,02 fine.
- L2-08 recomputed: charge conservation $q_X = q_t - q_W = \tfrac{2}{3}e - e = -\tfrac{1}{3}e$; candidates with $-\tfrac13 e$ and $B = \tfrac13$: d, s, b. answers.py −0,333333 agrees; −0,333 and −0,33 both inside the 2 % tolerance.
- L2-08 physics: $t \to W^+ + q$ ($q$ = b, s or d) is the real weak decay of the top quark; energetically allowed ($m_t \approx 173$, $m_W \approx 80{,}4$, $m_b \approx 4{,}2\,\text{GeV}/c^2$). The antiquark check ($+\tfrac13 e$ or $-\tfrac23 e$, not $-\tfrac13 e$) is right.
- $B_X = \tfrac13$ for a single quark follows the brief's definition $B = (n_\text{q} - n_{\bar{\text{q}}})/3$; the task gives it, so the student needs no new rule.
- Both solutions: given/asked, principle, symbolic formula before numbers, no conversions, substitution, answer with its precision reason, a real check (box total 17; $q_W + q_X = q_t$). Graph reading shown.
- Scope: hiukkasfysiikan standardimalli, charge conservation as taught in the brief; notation ($q$, $e$, $W^+$, $\bar{\nu}$) as in the lesson.
- Neither the figure nor its description gives the answers away beyond the reading the tasks ask.
- Hash d6490d7f746bd076 (--lang fi-easy) the same at the start and the end.
