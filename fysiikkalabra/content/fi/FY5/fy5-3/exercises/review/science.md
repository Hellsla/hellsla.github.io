VERDICT: PASS
CONTENT-HASH: a87d1199dc24605e

## Blocking

## Polish
- content/fi/FY5/fy5-3/exercises/solutions.md:65 (L2-02) — the Kaava block ends with `r = d/2` after `T = 2\pi r/v`, so the symbolic form is not simplified to the end (rule: substitute into the last symbolic form). Either put `r = d/2` first and end with `T = \dfrac{\pi d}{v}`, or keep it as it is. Sijoitus substitutes $r = 20\,\text{m}$ correctly either way.
- solutions.md L2-07 and L2-01 — `v = 2\pi r/T`, `T = 1/f`, `v = 2\pi r f`: the middle row is the definition $f = 1/T$ written the other way round. This is correct; it is a matter of taste.

## Checked
- The hash was the same at the start and at the end. I judged only the diff: the 13 Kaava steps were rewritten. Sijoitus, answers, units and tolerances are unchanged (the diffs of exercises.json and answers.py are empty).
- Each new block starts from the basic equation and ends in the form that Sijoitus substitutes into:
  - $v = 2\pi r/T$ with $f = 1/T$
  - $v_1, v_2$ at the same $T$ (L2-04) or the same time $t$ on the half-circle arcs (L3-01)
  - the chain speed $v_\text{k} = 2\pi r_\text{e} f_\text{e} = 2\pi r_\text{t} f_\text{t}$ (L3-03, no slipping)
  - $r = R\cos\varphi$ (L3-04)
  - $v_\text{A}, v_\text{B}$ at the same $f$ (L2-08)
- L1-04: the tangent path $s = vt$ and $d^2 = r^2 + s^2$ are right, because the string breaks and the body moves along the tangent, perpendicular to the radius.
- L3-02: $|\Delta\overline{v}|^2 = v^2 + v^2$ is right for a quarter turn, where the velocities are perpendicular.
- I recomputed every number in one script. Everything matches the Sijoitus values: 2,618; 18,85; 0,25; 6,185; 7676; 0,4006; 5,98 min; 4523; 25,0; 7,710; 14,14; 19,23 km/h; 0,020; 0,2094 mm/s; 2,262; 463/408/213 m/s.
- Notation follows the brief: $T$, $f$ in $\tfrac{1}{\text{s}}$, and no angular quantities, as the scope notes require.
