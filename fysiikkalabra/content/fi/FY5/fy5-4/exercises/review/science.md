VERDICT: PASS
CONTENT-HASH: eeef02e000ff63e5

## Blocking

## Polish
- content/fi/FY5/fy5-4/exercises/solutions.md:300 (L3-05) — the step from `\tan\alpha = \dfrac{N\sin\alpha}{N\cos\alpha}` to `\dfrac{v_0^2}{g r}` skips the division $\dfrac{m v_0^2/r}{mg}$. The result is correct; showing that one row would make the step explicit.
- solutions.md:302 (L3-05, Kitkan kanssa) — unlike the frictionless block above it, these two rows have no $\Sigma F_x$ / $\Sigma F_y$ labels. — For consistency, start them from $\Sigma F_x = m a_\text{n}$ and $\Sigma F_y = 0$.
- solutions.md:163 (L3-03) and :125 (L3-01) — this is the same note as before, on lines the diff did not touch. Both answers are limit values rounded to the unsafe side. In L3-03, $r \ge 201\,\text{m}$ is given as $2{,}0\cdot10^2\,\text{m}$; in L3-01, $v \le 27{,}6\,\text{km/h}$ is given as $28\,\text{km/h}$. Fixing them changes answers, so they need their own change.

## Checked
- The hash was the same at the start and the end. I judged only the diff:
  - 17 Kaava steps were rewritten as aligned blocks.
  - Some paragraphs were split.
  - The Sijoitus rows, answers, units and tolerances are unchanged.
- The previous Blocking item is fixed. In L3-05 the friction rows now read `N\cos\alpha - \mu_0 N\sin\alpha = mg` and `N\sin\alpha + \mu_0 N\cos\alpha = m v^2/r`, which is correct.
- Every block starts from $\Sigma F = m a_\text{n}$ with $a_\text{n} = v^2/r$, or from the force components, and is simplified to the form that Sijoitus uses.
- The signs are right:
  - L2-01: the dip, with $+m a_\text{n}$.
  - L2-03: the crest, with $-m a_\text{n}$ and $y$ up.
  - L3-04: the bottom ($N_1 - mg = m a_1$) and the top ($N_2 + mg = m a_2$), and $N_2 = 0 \Rightarrow v_\text{min} = \sqrt{g r}$.
- The friction rows use $F_\mu = \mu_0 N$ only at the limit the task asks for: L3-01, L2-06 and L3-06. L3-03 keeps the inequality $F_\mu \le 0{,}25\,mg$, and $r \ge$ follows from it.
- In L3-02, $T$ is named as the string's jännitysvoima in the Periaate, so `\Sigma F_x = T` is defined.
- L2-05 derives $F = (m/r)v^2$, so the slope is $k = m/r$ and $m = kr$. This is right for a line through the origin.
- I recomputed in one script: 6,667; 7,906; 1104,8; 6012; 2064; 27,62 km/h; 1,407 Hz; 201,4; 24,98 g; 3672; 75; 0,6796. All of them match the Sijoitus values. The L3-04 and L3-05 values are as in my previous report, and their Sijoitus rows are unchanged.
