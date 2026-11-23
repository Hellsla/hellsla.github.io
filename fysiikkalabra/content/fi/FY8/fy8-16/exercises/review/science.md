VERDICT: PASS
CONTENT-HASH: 5512292a4a3afd87

## Blocking

## Polish
- solutions.md (several Kaava steps, e.g. L2-01, L2-03, L3-03) — the lead-in now uses inline `\frac` ($z = \frac{\lambda - \lambda_0}{\lambda_0}$), where the rest of the file uses `\dfrac`. This is typography only.

## Checked
- The hash was 5512292a4a3afd87 at the start and the end. Scope: delta on solutions.md since the version I passed (commit c9c77c41ba).
- A script removed the Kaava steps, collapsed whitespace and compared the rest of the file: it is identical. The changed Järkevyys and Mallivastaus lines (L2-03, conceptual MCQs, L3-04) are only paragraph splits. exercises.json and answers.py are unchanged.
- Each Kaava step now starts from the basic laws:
  - L1-05 and L2-03: $E = hf$ and $f = c/\lambda$. The L2-03 stretch $\lambda = \lambda_\text{nyt}/1100$ is unchanged.
  - L2-01, L3-03, L2-06, L2-09: $z$, then $v = cz$ and $v = H_0 d$, then $d = v/H_0 = cz/H_0$. The condition $z < 0{,}1$ is still stated in the tasks.
  - L2-02: $t = d/v$ with $v = H_0 d$ gives $t = 1/H_0$. Correct.
  - L2-04: $H_0$ is equal for A and B, giving $d_\text{B} = d_\text{A} v_\text{B}/v_\text{A}$.
  - L3-01: $Y = m_\text{He}/m_\text{yht} = 2n/(n+p)$. This is correct with equal nucleon masses, as answers.py states.
  - L3-02: $Q = \Delta m c^2$, $\Delta m = 3m_\text{He} - m_\text{C}$. Atomic masses are fine, because the electrons balance.
  - L3-05: $k = 1 + z$ and $T = (1+z)T_\text{nyt}$. This is the correct scaling of the background temperature.
  - L2-05: slope and least-squares fit through the origin, $\sum dv/\sum d^2$.
  - L3-06: $d = 0{,}10c/H_0$.
- I recomputed L2-02 $14{,}5 \cdot 10^9\,\text{a}$, L2-04 $160{,}9\,\text{Mpc}$, L3-02 $7{,}274\,\text{MeV}$, L3-05 $10{,}9\,\text{K}$ and L3-06 $416{,}4\,\text{Mpc}$. All match answers.py.
- Every step ends in the symbolic form substituted in Sijoitus. Notation is as in the brief.
