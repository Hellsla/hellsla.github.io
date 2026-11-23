VERDICT: PASS
CONTENT-HASH: 823f6d310477ff2b
Mode: full (round 1; change under review: Kaava steps rewritten from the basic equations as aligned rows, work queue 8g)

## Blocking
- none

## Polish
- fy1-k5 c Kaava: the row $\Delta V = 2 \cdot 0{,}5\,\text{ml}$ puts a number into the symbolic step. Better: $\Delta V = 2\,\Delta V_\text{lukema}$.
- fy1-k7 d: "neliömassa $80\,\text{g/m}^2$ on tarkka arvo" is a nominal package value with a manufacturing tolerance. Better: "oletetaan tarkaksi"; the answer does not change.
- fy1-k6 b: the deviation is $1{,}4\,\%$ (answers.py `fy1-k6-b-dev`), but the text and the rubric say "noin $1\,\%$". Acceptable (C).
- fy1-k1 i: a display `aligned` block sits mid-sentence (presentation, the visual reviewer's call).

## Checked
- New Kaava steps, each symbolic before substitution and algebraically right:
  - k2 b and c, k3 b ($s_\text{E} = s_\text{A}$, solved for $t$), k4 b, k5 a and c.
  - k6 b: $v = gt \Rightarrow g = v/t = \Delta v/\Delta t$, valid because the line goes through the origin, as the text states.
  - k7 c and d: $d/N$, $\Delta d/N$, $V = A d_1$, $\rho = m/(A d_1)$.
- Recomputed in my own script:
  - Osa 1: f $16{,}8 \to 17\,\text{km/h}$; j $0{,}80 / 2{,}7 / 2{,}0 / 7{,}9\,\text{g/cm}^3$ (order A, C, B, D); i $4{,}9\,\text{m/s}$.
  - The units in d, the intervals in g and the speeds in h ($1{,}5$, $0$, $2{,}0\,\text{m/s}$) are right. Each item has exactly one correct option.
  - k2: least squares $-0{,}1174\,\text{cm/min}$; the line read gives $-0{,}1176$; $t = 110\,\text{min}$.
  - k3: $642{,}9\,\text{s}$ and $2057\,\text{m}$; the extremes are $1800$ and $2354\,\text{m}$. The relative uncertainty $6{,}25\,\% + 7{,}14\,\% = 13{,}4\,\%$ matches the explanation.
  - k4: $\bar{t}_{10} = 14{,}22\,\text{s}$, $T = (1{,}42 \pm 0{,}03)\,\text{s}$; $16{,}8/1{,}422 = 11{,}8$ swings; a pendulum length of about $0{,}50\,\text{m}$ matches "puolen metrin".
  - k5: $7{,}68\,\text{g/cm}^3$, range $7{,}11$–$8{,}35$ (given as $8{,}3$), $8\,\%$; brass is just outside.
  - k6: least squares $9{,}70$; $3{,}87/0{,}40 = 9{,}675\,\text{m/s}^2$; $41{,}8$ (with $9{,}81$: $42{,}4$) → $42\,\text{km/h}$. The filter data reproduce $v_\text{t}\tanh(gt/v_\text{t})$ with $v_\text{t} = 1{,}5\,\text{m/s}$.
  - k7: least squares through the origin $0{,}1020\,\text{mm}$, residuals at most $0{,}6\,\text{mm}$, $784\,\text{kg/m}^3$.
- Causality (drag relative to weight, systematic error not revealed by repeats, air between fibres) is right. Scope is FY1 only; drag stays qualitative.
- The rubric criteria match the parts. Points: 15 per Osa 2 task, 20 per Osa 3 task, maximum 70. All data are marked `source: example`.
