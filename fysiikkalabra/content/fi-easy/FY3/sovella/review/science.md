VERDICT: PASS
CONTENT-HASH: 51c86aaf9a3b697c

## Blocking
None.

## Polish
- fy3-s3 c) Kaava: $p_1$ and $p_2$ now mean the tank pressures, while in a) and b) of the same task $p_1$ is the pressure at depth and $p_2$ the surface pressure. Subscripts such as $p_\text{s,1}$ and $p_\text{s,2}$ would avoid the clash. The physics is right.
- fy3-s3 c): the litre is $\textsf{l}$ in the tank volume and the volumes, but the consumption unit stays $\text{l/min}$ (Annettu, Sijoitus, Vastaus, and s3 d). Not a physics issue.
- fy3-s3 c) Kaava: the chain still ends in two formulas. It could finish with $t = \dfrac{\Delta p_\text{s} V_\text{s}}{p\,q}$ (carried over from round 1).
- Round 1 polish items for s1 c), s1 d) and s3 a) still apply. None of them blocks.

## Checked
- s3 c) fix: the Kaava now starts from the two tank states, $p_1 V_\text{s} = n_1 RT$ and $p_2 V_\text{s} = n_2 RT$. It subtracts them to get $\Delta p_\text{s} V_\text{s} = \Delta n\,RT$ and equates that with the used air at depth, $pV = \Delta n\,RT$. Then it solves $V = \Delta p_\text{s} V_\text{s} / p$ and $t = V/q$. Each row is algebraically correct. Equating them is valid because $T$ is the same by the task's stated assumption, and Periaate says so. The round 1 polish point about $n$ vs $\Delta n$ is fixed. Using the gauge-pressure difference is justified because atmospheric pressure cancels. The high-pressure non-ideality is noted in d) as beyond the level (C).
- Recomputed from the task text with my own script: $p = 248{,}15\,\text{kPa}$, $V = 725\,\textsf{l}$, $t = 36{,}3\,\text{min} \to 36\,\text{min}$, $89\,\text{min}$ at the surface. Also a) $10{,}3\,\text{cm}^3$ and b) $14{,}7\,\textsf{l}$. All agree with answers.py and the solutions. Tolerances hold.
- Rubric s3 c) still matches: Boyle/assumption, why the difference of gauge pressures works, about $725\,\textsf{l}$, a reasonableness check of about 2,5 times, and $36\,\text{min}$. That is 5 points, as stated.
- The litre is changed to $\textsf{l}$ in the tasks and solutions. No number or unit meaning changed.
- Hash at start and end: 51c86aaf9a3b697c.
