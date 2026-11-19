VERDICT: PASS
CONTENT-HASH: 0e7961781cc75498
## Blocking

## Polish
- solutions.md (bus not reached, $s_\text{min} = 4{,}0\,\text{m}$) Kaava — "Sijoitetaan tämä välimatkaan ja sievennetään" jumps straight to $s_\text{min} = -x_{0\text{R}} - \dfrac{v^2}{2a}$. Fix: show the one middle row $\tfrac12 a (v/a)^2 - x_{0\text{R}} - v^2/a$ so the student can follow the simplification.
- solutions.md (graph task, $t = 5{,}0\,\text{s}$) Kaava — ends without a full stop after "leikkauspisteen vaakakoordinaattina"; several other Kaava rows lack it as well.

## Checked
- Captures: none opened (judged from text; the diff is text-only).
- Every rewritten Kaava now starts from $x = x_0 + v\,t$ or $x = x_0 + v_0 t + \tfrac12 a t^2$ (the brief's MAFY forms), writes each body's position, sets $x_\text{A} = x_\text{B}$ and solves symbolically; each solved form is right and is the one substituted.
- Sign handling: where $v_\text{B}$ is negative the substitution now reads $v_\text{A} - (-v)$, consistent with the general form ($t = 4{,}0$, $5{,}0$, $3{,}75$, $9{,}0$, $7{,}0\,\text{s}$ unchanged).
- Trains and scooter: $v_2$, $v$ named as speeds with $x = D - v\,t$; correct.
- Bus: first meeting the smaller root $(v - \sqrt{v^2 + 2 a x_{0\text{R}}})/a = 2{,}0\,\text{s}$; no-meeting case: $s_\text{min} = -x_{0\text{R}} - v^2/(2a) = 20 - 16 = 4{,}0\,\text{m}$, recomputed.
- Gap of $10\,\text{m}$: $(v_\text{A} - v_\text{B})t = x_{0\text{B}} - s$ gives $3{,}75\,\text{s}$; right.
- Largest gap: $t = v_\text{A}/a_\text{B} = 6{,}0\,\text{s}$, $\tfrac12 a_\text{B} t^2 = \tfrac12 v_\text{A} t$, so $36\,\text{m}$; right.
- Overtaking and delayed-start car: $x_\text{h} - x_\text{k} = \tfrac12 a t^2$; $\tau$ substitution right.
- exercises.json: only the "esimerkkiaineisto" marker removed from captions (teacher 2026-11-15/16); no value, answer, tolerance or id changed.
- Hash 0e7961781cc75498 at the start and at the end.
