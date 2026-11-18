VERDICT: PASS
CONTENT-HASH: 310dab2b8cd66f1a
## Blocking

## Polish
- solutions.md:308 (hailstone, $171{,}55\,\text{m/s}$) Kaava b) — the reason $a = g$ ("Ilman ilmanvastusta $\Sigma F = G = mg$ ja $\Sigma F = ma$, joten $a = g$") comes after $v = \sqrt{2gh}$ is already reached. Fix: put it first, then $v^2 = v_0^2 + 2as$ with $a = g$.
- solutions.md fy4-14-L2-08 Vastaus (carried over, unchanged) — "kolme merkitsevää numeroa kuten massassa" overstates it; the graph reading ($\Delta v = 6{,}0\,\text{m/s}$) limits to two. Fix: $F_\text{v} \approx 6{,}2 \cdot 10^2\,\text{N}$.
- solutions.md fy4-14-L2-08 Järkevyys (carried over) — "koska tämä hyppääjä putoaa leveämmässä asennossa" states one cause as fact. Fix: "esimerkiksi koska".

## Checked
- Captures: none opened (judged from text; the diff is text-only).
- Every rewritten Kaava now starts from $\Sigma F = ma$ (with $a = 0$ where the motion is steady), names $\Sigma F$ from the force diagram ($G - F_\text{v}$, $-G - F_\text{v}$, $F - F_\text{v} - F_\text{r}$), then solves symbolically; signs agree with each task's positive direction and diagram.
- Rising ball: $-mg - F_\text{v} = ma$ gives $-14{,}196\,\text{m/s}^2$; rise/fall difference with positive down: $a_1 - a_2 = 2F_\text{v}/m = 6{,}00\,\text{m/s}^2$; right.
- Halved drag: $F_\text{v} = mg$ before, $a = g/2$ after; right.
- Parachute opening: $\Sigma F = mg - F_\text{v} = -911{,}4\,\text{N}$ (positive down), magnitude asked; right.
- L3-04: $a = -17{,}5\,\text{m/s}^2$ with positive down gives $F_\text{v} = m(g + 17{,}5) = 2239\,\text{N}$, $2{,}78\,mg$; at the end $\Sigma F = 0$; right.
- Car coasting: $a = -(F_\text{v} + F_\text{r})/m = -0{,}525\,\text{m/s}^2$ right.
- exercises.json: presentation only; paragraph splits change no wording or number; no answer, tolerance or id changed.
- Hash 310dab2b8cd66f1a at the start and at the end.
