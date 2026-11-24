VERDICT: PASS
CONTENT-HASH: 238e593134987e6b
SCOPE: delta numbers,teacher-figure from dc09b0ce9519b96f base 146d1b7

## Blocking

## Polish
- solutions.md:186 (L3-04, Sijoitus): the Kaava chain now solves $\alpha_1 = \arctan(h'\tan\alpha_2/d)$, but Sijoitus still begins with $\tan\alpha_1 = \dots$. Write it as $\alpha_1 = \arctan\dfrac{44{,}9\cdot\tan 10{,}0^\circ}{60{,}0} = 7{,}517^\circ$ so that it substitutes into the last symbolic form.
- solutions.md:186 (L3-04, Sijoitus): $n = \sin 10{,}0^\circ / \sin 7{,}517^\circ$ leaves out $n_2 = 1{,}00$, which the Kaava chain keeps. The number is the same.
- lessons/FY7/fy7-10/answers.py:51–52: the dead slope line from my earlier report is still there (carried).

## Checked
- Delta: the L3-04 Kaava line was rewritten as an aligned chain. No number, answer, Muunnokset or Sijoitus changed. The protractor picture and drawing are teacher-approved (teacher-figure). The hash was the same at the start and the end.
- Geometry: the ray meets the surface at horizontal offset $x = d\tan\alpha_1$ (true depth) and $x = h'\tan\alpha_2$ (image straight above the object, as Periaate states). Setting them equal gives $\alpha_1 = \arctan(h'\tan\alpha_2/d)$, which is correct.
- Snell at the water–air surface: $n\sin\alpha_1 = n_2\sin\alpha_2 \Rightarrow n = n_2\sin\alpha_2/\sin\alpha_1$ is correct. $\alpha_1$ is the angle in water and $\alpha_2$ the angle in air.
- Recomputed with $d = 60{,}0\,\text{cm}$: $\alpha_1 = 7{,}517^\circ;\ 14{,}880^\circ;\ 22{,}006^\circ;\ 28{,}978^\circ$ and $n = 1{,}3274;\ 1{,}3319;\ 1{,}3344;\ 1{,}3268$. These match the solution.
- The mean is $1{,}3301$. This matches the solution and answers.py ($1{,}330124$). The answer $1{,}33$ with three significant figures is justified.
