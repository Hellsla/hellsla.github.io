VERDICT: PASS
CONTENT-HASH: f1b67e3925bfc7d6
Mode: delta (Kaava steps rewritten as aligned derivations from Newton II and a_n = v²/r; paragraph splits)
Round 1

## Blocking
(none)

## Polish
- solutions.md:143 (L3-02) — the derivation goes from $a_\text{n} = v^2/r$ straight to $v = \sqrt{Tr/m}$, so the combined row $T = m\,v^2/r$ is left out — add that row before the root.
- solutions.md:285 (L3-04) — the old text gave the axis for each row ("alhaalla $y$ ylös", "ylhäällä $y$ alas kohti keskipistettä"), and the new $\Sigma F_1$, $\Sigma F_2$ rows do not. The force-diagram text implies the directions, so this is not an error, but a short note such as "(positiivinen kohti keskipistettä)" would make the sign of $N_2 + mg$ explicit.

## Checked
- Every rewritten Kaava block starts from the basic equation ($\Sigma F = m a_\text{n}$ in the stated direction, or $\Sigma F_y = 0$ for the vertical balance), uses $a_\text{n} = v^2/r$, and is simplified symbolically to the form the unchanged Sijoitus substitutes into.
- The signs are right in every task. Hill crest: $\Sigma F_y = -m a_\text{n}$ with $y$ up. Dip: $+m a_\text{n}$. Loop top: $N_2 + mg = m a_2$ toward the centre, so $N_2 = 0$ gives $a_2 = g$ and $v_\text{min} = \sqrt{gr}$.
- In the friction tasks, $F_\mu = \mu_0 N$ is used only at the limit (maximum speed, minimum radius, measured skid limits), as the guardrails require. $F_\mu \le 0{,}25\,mg$ gives $r \ge v^2/(0{,}25\,g)$ in the right direction.
- Banked curve (L3-05): $\Sigma F_y = N\cos\alpha - mg = 0$ and $\Sigma F_x = N\sin\alpha = m v_0^2/r$ give $\tan\alpha = v_0^2/(gr)$. With friction, the component equations are unchanged in content.
- Plug data (L2-02): $F = (m/r)\,v^2$, so slope $= m/r$ and $m = kr$. This is correct and matches the graph reading.
- Recomputed all affected answers in one script: 6.667 N, 7.906 m/s, 1104.8 N, 6012 N, 2064 N, 27.62 km/h, 1.407 Hz, 201.4 m, 24.98 g, μ₀ = 0.551, 3672 N, 75 m, r = 13.91/13.90 m, N = 257.4 N / 3780.6 N, v_min = 11.7 m/s, μ₀ = 0.680. All agree with the solutions.
- Sijoitus, answers and tolerances are unchanged. The paragraph splits (L1-05 b, L1-06, L2-02, L2-08, L3-04) change no physics.
