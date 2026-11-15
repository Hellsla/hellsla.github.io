VERDICT: FAIL
CONTENT-HASH: a5df55e2a3587d91
Mode: full, round 1 (change: oikoluvun korjaus fy1-k3 c, 15 % → 14 %)

## Blocking
1. **A (internal consistency, assessment): fy1-k3 c rubric still says 15 %.** `tasks.json`, fy1-k3 part c, third criterion (2 p): "kohtaamispaikan suhteellinen epävarmuus (noin $15\,\%$)". The solution now says $\tfrac{0{,}3}{2{,}1} \approx 14\,\%$ in both places, and my own figures give $277\,\text{m} / 2057\,\text{m} = 13{,}5\,\%$ unrounded and $0{,}3/2{,}1 = 14{,}3\,\%$ rounded. So 15 % is wrong in the rubric that students grade themselves against, and it contradicts the corrected solution. Fix: "(noin $14\,\%$)" in that criterion. The fix covered two places in solutions.md but missed this third one in tasks.json.

## Polish
- fy1-k6 b: the rubric and the solution say the difference from $9{,}81\,\text{m/s}^2$ is "noin 1 %". With the line actually read ($9{,}675$) it is $1{,}4\,\%$. "Noin 1–2 %" or "noin $1{,}4\,\%$" would match better (C, not blocking).

## Checked
- I recomputed every answer in one script from the task data and compared it with the answers.py output. All agree: k2 $0{,}118\,\text{cm/min}$ and $110\,\text{min}$; k3 $643\,\text{s}$ and $2057\,\text{m}$; the bounds $1800$ and $2354\,\text{m}$ (half-range $277\,\text{m}$); the lead $6{,}25\,\%$ plus the closing speed $7{,}1\,\%$ gives $13{,}4\,\%$; k4 $1{,}422\,\text{s}$ and $\pm 0{,}03\,\text{s}$, ratio $11{,}8$, pendulum length $0{,}50\,\text{m}$; k5 $7{,}68$ and $7{,}11$–$8{,}35\,\text{g/cm}^3$, brass outside the range; k6 $9{,}675\,\text{m/s}^2$ and $41{,}8$ ($42{,}4$ with $9{,}81$) → $42\,\text{km/h}$; k7 $102 \pm 2\,\mu\text{m}$ (fit through the origin $102{,}0$) and $784\,\text{kg/m}^3$.
- Osa 1: each item has exactly one correct option. Checked: the unit analysis of every option in d, the prefix in e, the significant figures in f, the overlapping ranges in g, the walk figure's slopes in h (1,5, 0 and 2,0 m/s, ending at 2 m), equal speeds in i, and the order A, C, B, D in j. The distractors and their reasons are right.
- Physics and causality: extrapolation (k2 d, k6 d); systematic vs random error (k4 d); reaction time divided over ten swings (k4 c); air resistance relative to weight, and the filter's speed levelling off at about $1{,}5\,\text{m/s}$ (k6 c, tanh data); paper's density below water's because of the air between the fibres (k7 d).
- Scope: everything is FY1 (linear models, $v = gt$, $\rho = m/V$, uncertainty as half the range). Air resistance is qualitative only.
- Rubrics: the criteria ask only what each task gives and asks. Alternative methods are accepted in k3 (Hyväksytään myös) and k6 d ($9{,}81$). The data are marked as example data.
- The hash is the same at the start and the end.
