VERDICT: PASS
CONTENT-HASH: 88d0b27454005691

Delta review of the new `hints` in `sovella/tasks.json` (English), 30 parts × 3 hints, against each part's criteria, `sovella/solutions.md` and `lessons/units/fy9-liike/sovella/answers.py`.

## Blocking
None.

## Polish
None from the science side. (s2 c hint 3 and s8 c hint 2 come close to the reasoning the part asks for; that is a pedagogy judgement, not a physics error.)

## Checked
1. Physics and models: every hint uses the part's own model and sign convention: trapezium area $\Delta x = \frac{v_0+v}{2}t$ (s1 a, d), $a = \Delta v/\Delta t$, equal speeds at the smallest gap (s1 c), up positive with $v = v_0 - gt$ (s2), cancelling $\tfrac12 g t^2$ (s2 b, c), slope as velocity/acceleration and area as distance (s3, s7, s8), $v_\text{ka} = \Delta x/(t_1+t_2)$ (s4 b), the circularity of $a = 2x/t^2$ (s5), $A = \tfrac12 a$, $\Delta a = 2\Delta A$ and the distance-ratio scale correction (s6), $x = x_0 + v(t-t_0)$ (s7 c), $x_\text{A} = x_\text{B}$ (s8). Same symbols as the rubric criteria.
2. Numbers recomputed in one Python call: $54$, $108$, $81$, $72\,\text{km/h}$ = $15$, $30$, $22{,}5$, $20\,\text{m/s}$; division by $3{,}6$; $3000\,\text{m}$ and $100\,\text{m}$ at $80\,\text{km/h}$ = $135\,\text{s}$ and $4{,}5\,\text{s}$; two readings of $0{,}5\,\text{s}$ → about $1\,\text{s}$; times $1{,}4$ and $1{,}8\,\text{s}$ (= $1{,}6 \pm 0{,}2\,\text{s}$); ratio $3{,}30 : 3{,}00$; $16\,\text{m}$ closing at $3{,}0\,\text{m/s}$; $v_\text{B} = -1{,}0\,\text{m/s}$; $y_0 = 1{,}5\,\text{m}$. All agree with the task data and answers.py (s1 a $12{,}0\,\text{s}$, s1 d $15{,}4\,\text{s}$, s4 c, s5 a, s6 d $8{,}92\,\text{m/s}^2$, s8 d $5{,}33\,\text{s}$).
3. Causality and claims in hints: truck initially faster (22,5 > 15 m/s), truck faster for the whole lane in s1 d (20 < 22,5 m/s), the passing time independent of $g$, the extrapolation beyond $40\,\text{s}$ (s3 d), the one-way logic of average-speed enforcement (s4 a): all correct.
4. No hint states a part's final answer; every number with a unit is LaTeX with the decimal point. The en hints match fi one to one (lorry = rekka, symbols $x_\text{R}$, $v_\text{ka}$, $t_\text{l}$ kept as in the en tasks and solutions).
