VERDICT: FAIL
CONTENT-HASH: 982778f9cff7e8e8
## Blocking
- solutions.md:187 fy4-9-L3-04 Kaava — the new sentence "Jäykällä esteellä $I = F_\text{ka}\,\Delta t$, joten $F_\text{ka} = \dfrac{I}{\Delta t}$" uses $\Delta t$ for the rigid obstacle's stopping time ($0{,}025\,\text{s}$), while the same step (in $I = \Delta t \cdot \Sigma F$) and Muunnokset define $\Delta t = 10\,\text{ms}$ as the width of a strip. A student who substitutes the defined $\Delta t$ gets $98\,\text{kN}$, not $39\,\text{kN}$; the symbolic form does not say what Sijoitus computes. Fix: give the stopping time its own symbol (e.g. $F_\text{ka} = \dfrac{I}{\Delta t_\text{e}}$, $\Delta t_\text{e} = 25\,\text{ms}$ the stopping time against the rigid obstacle) or rename the strip width; numbers unchanged.

## Polish
- solutions.md:187 (and L2-07, line ~176, pre-existing) — $\Sigma F$ there means the sum of the tabulated force readings, while the chapter and L3-05 in the same set use $\Sigma F$ for the total force. Fix: write the sum in words or as $\Sigma F_i$ ("sisäpisteiden voimien summa").
- solutions.md Kaava rows of L1 (bat, puck, belt), L2 kick — "…, joten …, joten …" twice in one sentence. Fix: second "joten" → "ja siitä" or a full stop.

## Checked
- Captures opened: fy4-9/review/shots/fy4-9-open-exercises-L3-1280-4.png (rubber/clay ball Kaava renders as the source; $|v - v_0| = 14\,\text{m/s} = v_0 + v_\text{k}$).
- Every rewritten Kaava now starts from $I = \Delta p$, $I = F\,\Delta t$, $p = mv$ (or the area as impulse) before the solved form; each derived form is algebraically right and is the one Sijoitus uses.
- Braking car, bat, puck, belt, kick, bumper: signs consistent with the stated positive direction; magnitude taken where the task asks a size.
- Sled trapezoid and L2-07 strip sum: area = impulse, then $I = \Delta p = m\,\Delta v$; correct.
- L3-05 bouncing ball: $v = v_0 + at$ with $a = -g$ gives $v_1 = -g t$ and $0 = v_2 - g t_\text{nousu}$; $(N_\text{ka} - mg)\Delta t = m(v_2 - v_1)$ right, weight included in the total force.
- Paragraph splits (L1-06, L2-06, L2-09) change no wording, number or claim.
- No number, answer, tolerance, task text or id changed in the diff; answers stand as passed.
- Hash 982778f9cff7e8e8 at the start and at the end.
