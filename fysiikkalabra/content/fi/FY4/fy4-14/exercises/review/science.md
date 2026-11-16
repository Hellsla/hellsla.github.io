VERDICT: PASS
CONTENT-HASH: 7fdde13b611ba03f
## Blocking

## Polish
- solutions.md fy4-14-L2-08 Vastaus — three figures "kuten massassa" overstates it: $\Delta v = 6{,}0\,\text{m/s}$ read from the graph limits the result to two. Fix: $F_\text{v} \approx 6{,}2 \cdot 10^2\,\text{N}$, justified by the reading (tolerance 5 % already covers it). Carried over.
- solutions.md fy4-14-L2-08 Järkevyys — "koska tämä hyppääjä putoaa leveämmässä asennossa" states one cause as fact. The data show only a larger drag at the same speed ($k = mg/v^2 \approx 0{,}32$ against $0{,}26\,\text{kg/m}$). Fix: "esimerkiksi koska".
- solutions.md fy4-14-L2-04 Vastaus — $1200\,\text{kg}$ has four significant figures under the trailing-zero rule; the limiting data are $450\,\text{N}$ and $180\,\text{N}$. Fix: name those two.
- solutions.md fy4-14-L2-08 Periaate — "käyrä on siinä lähes suora": the chord gives $1{,}50\,\text{m/s}^2$, the model behind the points about $1{,}38\,\text{m/s}^2$ at $8{,}0\,\text{s}$. Fix: "likimain".

## Checked
- All 18 numeric answers recomputed with my own formulas beside `python -I answers.py` and exercises.json: all agree (L1-03 $3{,}523 \to 3{,}52\,\text{m/s}^2$).
- New sentence in L2-08: $v = \sqrt{mg/k} = \sqrt{735{,}75/0{,}26} = 53{,}2\,\text{m/s}$, "noin 53" correct; $k = 0{,}26\,\text{kg/m}$ is the value in lesson-answers.py. The points follow $48\tanh(gt/48)$ within $0{,}05\,\text{m/s}$, so the limit $48\,\text{m/s}$ is right.
- L1-09: $G = 0{,}270 \cdot 9{,}81 = 2{,}649 \approx 2{,}65\,\text{N}$; statements 1 and 3 true, 2, 4 and 5 false, each feedback correct.
- Choices L1-06, L1-07, L2-07: exactly one correct option; each distractor is wrong and its feedback names the reason.
- Force diagrams: $\overline{G}$ down, $\overline{F}_\text{v}$ against the velocity (down for a rising ball), lengths agree with the acceleration, velocity never drawn as a force; equations follow the stated positive direction. L1-08's error is exactly the misdirected drag.
- Figure ex-tangentti: the tangent through $(0;\,2{,}0)$ and $(2{,}0;\,15{,}0)$ touches the curve at P ($0{,}96\,\text{s}$; $8{,}2\,\text{m/s}$), slope $6{,}5\,\text{m/s}^2$.
- L3-04: $2{,}78\,mg$, $\Sigma F = -1435\,\text{N}$; L3-05: $171{,}55\,\text{m/s} \approx 620\,\text{km/h}$, $0{,}82\,\text{s}$, about $190\,\text{s}$, drop size realistic for $8{,}0\,\text{m/s}$.
- Scope: drag is given or deduced from the motion, never computed from speed.
- Hash 7fdde13b611ba03f at the start and at the end.
