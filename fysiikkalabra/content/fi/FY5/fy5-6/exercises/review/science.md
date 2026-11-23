VERDICT: PASS
CONTENT-HASH: 6686402cbc67b037

## Blocking

## Polish
- content/fi/FY5/fy5-6/exercises/solutions.md (L1-03), Kaava: the block goes from `\gamma\dfrac{Mm}{r^2} = m\dfrac{v^2}{r}` straight to `a_\text{n} = \dfrac{\gamma M}{r^2}`. The step $a_\text{n} = \tfrac{v^2}{r}$ is not shown. Either write the second row as `= m a_\text{n}` or add that row.
- solutions.md (L3-02), Kaava: the block ends with the separate rows $v_1$ and $v_2$ and stops short of the combined form. The rule is to simplify to the end, so add `\Delta v = \sqrt{\gamma M/(R+h_2)} - \sqrt{\gamma M/(R+h_1)}` as the last row (the old text had it).

## Checked
- The hash was the same at the start and the end. I judged only the diff: 19 Kaava steps were rewritten. Sijoitus, answers, units and tolerances are unchanged (the diffs of exercises.json and answers.py are empty).
- Every new block starts from $\Sigma F = m a_\text{n}$ with gravitation as the only force, as the lesson's Kaava says. Each solves for the asked quantity in symbols, with $r = R + h$ wherever a height is given.
- The algebra is right:
  - $r^3 = \gamma M T^2/(4\pi^2)$ and $T = 2\pi\sqrt{r^3/(\gamma M)}$
  - $M = \tfrac{4\pi^2}{\gamma}\tfrac{r^3}{T^2}$
  - $v = \sqrt{gR}$
  - the ratio $\sqrt{r_2/r_1}$
  - the synodic $t = T_\text{A}T_\text{B}/(T_\text{B} - T_\text{A})$
  - $T^2 \propto r^3$ for d)
- L2-08 (Halley): the circular-orbit ratio is what the task asks for ("ympyräradan ratanopeuksien suhde näillä säteillä"). The Vastaus says the real orbit is an ellipse that the model does not describe, so the new circular-motion derivation leaves no wrong picture.
- L1-10: $a = \gamma M/r^2$ uses the mean distance, and the figure supports the near-circle assumption.
- I recomputed every number in one script. All of them match:
  - 7,44 km/s; 12,0 h; 0,224; 1,02; 1,63
  - 9570 km; 3,36; 1,68; 650 N
  - 1,70·10⁴ km; 1,13 m/s; 84,4 min; 17,3; 29,79
  - 7,45 and 3,87 kN; 5,93 mm/s²; 1,45; 7,72; 687,1 d
  - 92,4 / 105,0 min and 12,9 h
