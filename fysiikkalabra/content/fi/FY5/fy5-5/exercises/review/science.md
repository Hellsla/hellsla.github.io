VERDICT: PASS
CONTENT-HASH: 97cb48e5f93cd565

## Blocking

## Polish
- content/fi/FY5/fy5-5/exercises/solutions.md (L2-07) — the Kaava block has `g\,r^2 = \gamma M` and then `p = g\,(R + h)^2`. One word would make the link explicit: $r = R + h$ is the distance from Earth's centre.
- solutions.md (L3-05) — `m g - N = m a_\text{n}` treats $g = 9{,}81\,\text{m/s}^2$ as the pure gravitational field strength, $\gamma M/R^2$. This is a fair simplification at this level (C) and the result is not affected at three figures, so no change is needed.

## Checked
- The hash was the same at the start and the end. I judged only the diff: 15 Kaava steps were rewritten. Sijoitus, answers, units and tolerances are unchanged (the exercises.json and answers.py diffs are empty).
- Every new block starts from Newton's law of gravitation, or from $mg = \gamma Mm/R^2$ (the weight is the gravitational force, as the brief's Tiivistelmä says). Each block then simplifies symbolically to the form Sijoitus uses.
- The algebra is right:
  - the $1/9$ factor
  - $m = r\sqrt{F/\gamma}$
  - $h = \sqrt{\gamma Mm/F} - R$
  - $(R/(R+h))^2$ and the relative change
  - the equal-pull point $x = d/(1 + \sqrt{m_\text{K}/M})$
  - $g = \tfrac43\pi\gamma\rho R$, so $g_\text{p}/g = R_\text{p}/R$
  - the force and field ratios
  - $\gamma = Fr^2/(Mm)$
  - $\rho = M/(\tfrac43\pi R^3)$
  - the rotating-Earth $N = m(g - a_\text{n})$, where the net force points to the centre
- I recomputed every number in one script, and all of them match:
  - 0,40 µN; 2,5 N; 3,70; 3,80 kN; 4,0 µN; 38 kg; 0,815; 15 500 km; 0,344 %
  - 3,46·10⁵ km; 19,6; 177
  - 11,2/9,01/11,2 and 1,25
  - 6,72·10⁻¹¹; 3,99·10¹⁴; 5510 kg/m³; 606 N and 575 N; 315 N; 5,27 kN
- Notation follows the brief: $\gamma$, $r$ between the centres, and $g$ in m/s².
