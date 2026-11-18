VERDICT: PASS
CONTENT-HASH: 1672c605e0f0a0e0
SCOPE: delta added-exercise from b01d8774ea628a16 base 1bdc56f920e4

## Blocking

## Polish
- solutions.md fy8-15-L1-10 Periaate — "jokaisella rivillä on sama varaus" holds for the three generation columns only; in the mediator column the rows differ ($g$, $\gamma$, $Z^0$ neutral, $W^\pm$ charged), which the Kuvaajan lukeminen line handles correctly — write "jokaisen sukupolvirivin hiukkasilla on sama varaus" or similar.

## Checked
- Recomputed in one script from the figure's boxes: 17 boxes, neutral $\nu_e$, $\nu_\mu$, $\nu_\tau$, $g$, $\gamma$, $Z^0$, $H$ = 7 (answers.py 7, json 7); neutral leptons 3 (b-part, solution 3).
- L2-08: $q_X = q_t - q_W = \tfrac{2}{3} - 1 = -\tfrac{1}{3}$; answers.py −0,333333, json −0,3333 e. Candidates of charge $-\tfrac{1}{3}e$ in the figure: $d$, $s$, $b$, as the solution says.
- Physics of L2-08: $t \to W^+ + q$ with $q = d, s, b$ is the real decay (all three allowed by the weak interaction; $b$ dominates), so "varaus ei yksin valitse niistä yhtä" is right and no option is wrongly excluded. $B_X = \tfrac{1}{3}$ follows from the lesson's $B = (n_\text{q} - n_{\bar{\text{q}}})/3$ and is given in the task; the antiquark exclusion ($+\tfrac{1}{3}e$ or $-\tfrac{2}{3}e$) is correct.
- Figure fy8-15/taulukko: $t$ in the top quark row, column III, label $+2e/3$; $W^\pm$ label $\pm e$; every value the two tasks need is drawn, and the description gives the same charges in words without giving the counts.
- One $W^\pm$ box with "antihiukkasia ei lasketa" is consistent: the box is charged either way, the count of 17 and 7 is unaffected.
- Tolerance 0,02: L1-10 an exact integer (6 or 8 fall outside); L2-08 −0,333 and −0,33 accepted (0,1 % and 1 %), −0,3 rejected (10 %), matching an exact fraction.
- Units: L1-10 dimensionless count, L2-08 in $e$, as the lesson's convention (charges as multiples of $e$).
- Both solutions complete: given/asked, principle, figure reading, symbolic form before substitution, no conversions stated, rounding reason, real reasonableness checks (10 + 7 = 17; $q_W + q_X = q_t$).
- Scope: standard model particles and charge conservation, inside FY8 "hiukkasfysiikan standardimalli" and the lesson's Kaava section.
- Hash the same at the start and the end.
