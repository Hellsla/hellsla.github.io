VERDICT: PASS
CONTENT-HASH: 719006f25019fc2b
none

## Blocking

## Polish
- solutions.md s3 d: the task says to use the added mass from part c's graph (14 g), but Annettu/Sijoitus use $m_\text{j}/3 = 15$ g as the main path and give 14 g only under Hyväksytään myös. Both give 0.43 m/s (recomputed 0.433 and 0.434 m/s), so no score changes.
- solutions.md s3 d Kaava: the chain goes from $E_\text{k,max} = E_\text{p,max}$ straight to $v_\text{max} = A\sqrt{k/m_\text{eff}}$. The row $\tfrac{1}{2}m_\text{eff}v_\text{max}^2 = \tfrac{1}{2}kA^2$ is missing, although the rubric's equation detail shows it.
- solutions.md s3 Hyväksytään myös: the condition for the two points of the massless-spring path ("Opiskelijan pitää kertoa … perustella oletus") now stands in its own paragraph after "Tuloksen piste edellyttää …". It is detached from the bullet it qualifies, which makes it slightly ambiguous for a grader.

## Checked
- Full review of the rewritten Kaava steps. Every chain starts from its basic law and is simplified in symbols before the numbers go in: s1 a/b ($M = Fr$, $F = mg$ → $\Sigma M$ → solved for $r$ and $m$), s1 e (component equations → $\tan\theta = v^2/(rg)$), s2 b/c ($\gamma Mm/r^2 = mv^2/r$ → $M = k/\gamma$, $r^3 = \gamma MT^2/4\pi^2$), s3 b ($T = 2\pi\sqrt{m/k}$ → $k = 4\pi^2/\text{kulmakerroin}$), s4 b/c/d ($v = f\lambda$, $L = \lambda/2$; $f' = v'/2L$; $I \propto 1/r^2$ → $\Delta L$ → $n$ → $t_\text{v}$). The chains match the en and fi physics, their Sijoitus rows and the rubric details.
- I recomputed every number with my own formulas in one script: s1 21 m, 2579 kg, 412/608 kNm, 1.92 t, 3.06 t, 1.466 m/s, 0.598°, 0.157 m; s2 the v, 1/r and v² table, fitted slope 1.271e17, M 1.90e27 kg, r 1.602e8 m, height 88 700 km; s3 the T² values, slope 1.982, intercept 0.0278, residuals ≤ 0.0047 s², k 19.9, static k 20.02, 14.1 g, origin-forced k 18.89, v_max 0.433/0.446 m/s; s4 0.686 m, 244.75 Hz, Δf 5.25 Hz, 94.0 dB, n 3.01, t_ref 0.995 h, P 0.127 W. All agree with answers.py and the text, and every answer lies inside its tolerance.
- s4 d adds "ilman heijastuksia" to the task, which agrees with the free-field assumption of the solution and with e. The FBD has only G and S, with a_n drawn separately, and no centrifugal force. The action values are 80 and 85 dB. Everything is in FY5 scope, with no angular quantities. The rubric points add up and the accepted alternatives are valid.
