VERDICT: FAIL
CONTENT-HASH: 44505a13028017fe
SCOPE: delta: new tasks s7 (Jousen kalibrointi) and s8 (Pudotettu teräskuula videolla), the s8-kuvaaja model graph and the changed intro; older tasks s1-s6 untouched (not re-judged).

## Blocking
1. **A, s8 c, the frame-interval cause is backwards** (solution "Aikaskaalan virhe", rubric `error_sources` detail; answers.py `c-tscale` computes the same wrong quantity). We have $g = 2s/t^2$. If the real frame interval were $0{,}0487\,\text{s}$ but $0{,}05\,\text{s}$ was assumed, the times would be *over*estimated and the computed $g$ too *small*: with a real interval of $0{,}0487\,\text{s}$ the true $g$ would be $10{,}35 \cdot (0{,}05/0{,}0487)^2 \approx 10{,}9\,\text{m/s}^2$. For the measured $10{,}35$ to be really $9{,}81\,\text{m/s}^2$, the real interval has to be *longer*: $0{,}05\,\text{s} \cdot \sqrt{10{,}35/9{,}81} \approx 0{,}0514\,\text{s}$, about $2{,}7\,\%$ longer (the camera's real frame rate lower than nominal, about 19,5 instead of 20 frames per second). Fix the solution, the rubric detail and `c-tscale` (use $\sqrt{g/9{,}81}$).
2. **A, s8 a, "vakiotermi ei ole merkitsevä"** (5th criterion, model answer). Checked with the test the task itself uses in b (lines through every $\pm 0{,}01\,\text{m}$ bar): every such line crosses the $s$ axis between $+0{,}003$ and $+0{,}012\,\text{m}$. No line through the origin fits, so the data do not show the constant term to be insignificant (s7 b uses the right test and says "nolla kuuluu välille"; here zero does not). Reword, for example: the constant term is small, about the size of the reading uncertainty and since the line is not forced through the origin, it does not change the slope.

## Polish
- s8 b: "$g = 2 \cdot 5{,}18 = 10{,}35$" (solution and rubric `calculation`). $2 \cdot 5{,}18 = 10{,}36$. Carry $5{,}177$ in the chain, or show $0{,}673/0{,}130 = 5{,}177$.
- s8 c rubric: "pituuskaavan virhe" should probably be "mittakaavan virhe", the solution's own word.

## Checked
- One script recomputed every number from the source figures' data (fy5-8 `MIT_X`, $F = mg$; fy4-2 `FALL_T/FALL_S`) beside answers.py: s7 $k$, bounds $28{,}83$/$31{,}27$, $\Delta k$, intercept range, $15{,}0 \pm 0{,}61\,\text{cm}$, offset $-1{,}0\,\text{cm}$; s8 slope $5{,}175$, intercept $0{,}010\,\text{m}$, residuals, bounds $5{,}094$/$5{,}242$, the difference ($5{,}5\,\%$, $3{,}7\Delta g$). All agree except item 1.
- Physics: $F_\text{v} = kx$, a pre-tensioned spring and a misread zero as causes of an offset, the extrapolation and elastic-limit warning, $s = \tfrac12 gt^2$ from rest, air resistance only lowers $g$, a scale error enters $g$ one to one. Scope: FY1/FY4/FY5.
- Rubric points add up (5+4+4, 5+5+4). The tolerances accept the rounded answers.
- The s8-kuvaaja figure in figures.py has the read slope and the fitted intercept, and its alt text matches the solution's numbers.
- Intro: eight tasks, two with a ready graph (s7, s8), one with the gas law (s6): true.
- `practice.py check` OK. The hash is the same at the start and the end.
