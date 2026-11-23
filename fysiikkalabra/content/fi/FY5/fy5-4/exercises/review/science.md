VERDICT: FAIL
CONTENT-HASH: b5df027644f73b9c

## Blocking
- content/fi/FY5/fy5-4/exercises/solutions.md:302 (L3-05, "Kitkan kanssa") — A (error introduced by the diff). The block sets `\Sigma F_y = N\cos\alpha - \mu_0 N\sin\alpha` and then `\Sigma F_y = mg`. The car does not accelerate vertically, so $\Sigma F_y = N\cos\alpha - \mu_0 N\sin\alpha - mg = 0$, not $mg$. As written it says the vertical net force equals the weight. The frictionless part two rows above does it right (`\Sigma F_y = N\cos\alpha - mg = 0`). The old text was the correct `y: N\cos\alpha - \mu_0 N\sin\alpha = mg`. — Fix: `\Sigma F_y &= N\cos\alpha - \mu_0 N\sin\alpha - mg = 0 \\ N\cos\alpha - \mu_0 N\sin\alpha &= mg`.

## Polish
- solutions.md:300 (L3-05) — the row `\tan\alpha = \dfrac{N\sin\alpha}{N\cos\alpha}` jumps to `\dfrac{v_0^2}{g r}` without showing the division $\dfrac{m v_0^2/r}{mg}$. This is correct; one row would make it explicit.
- solutions.md:163 (L3-03) and :125 (L3-01) — these lines were not changed by the diff, so this is a note for later. Both are limit values rounded to the unsafe side. In L3-03, $r \ge 201\,\text{m}$ is given as $2{,}0\cdot10^2\,\text{m}$; the house rule rounds an "at least" value up, to $210\,\text{m}$. In L3-01, $v \le 27{,}6\,\text{km/h}$ is given as $28\,\text{km/h}$; an "at most" value is rounded down, to $27\,\text{km/h}$. Fixing this would change answers, so it needs its own change.

## Checked
- The hash was the same at the start and the end. I judged only the diff: 16 Kaava steps were rewritten and the friction part of L3-05 was split into paragraphs. The Sijoitus rows, answers, units and tolerances are unchanged.
- Every new block starts from $\Sigma F = m a_\text{n}$ with $a_\text{n} = v^2/r$, or from the force components, and ends in the form that Sijoitus uses.
- The signs are right in L2-01 (dip, $y$ up, $+ma_\text{n}$) and L2-03 (crest, $-ma_\text{n}$). In L3-04 the bottom ($N_1 - mg$) and the top ($N_2 + mg$, toward the centre) are right, and $N_2 = 0 \Rightarrow v_\text{min} = \sqrt{gr}$.
- The friction rows use the lepokitka limit $F_\mu = \mu_0 N$ only where the task asks for the limit (L3-01, L2-06, L3-06). L3-03 uses $F_\mu \le 0{,}25\,mg$, as the lesson does.
- I recomputed every number in one script: 6,7; 7,9; 1105; 4,74; 6012; 2064; 27,6 km/h; 1,41; 201; μ = 0,55/0,54/0,56/0,54; 3672; 75; 3781/257; 97,3 and 48,2 km/h; 0,68. All of them match the answers.
