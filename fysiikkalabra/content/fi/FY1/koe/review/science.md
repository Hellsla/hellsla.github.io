VERDICT: PASS
CONTENT-HASH: f48efeab59580980
Mode: full, round 2 (change: fy1-k3 c rubric "(noin 15 %)" → "(noin 14 %)")

## Blocking
None. The round 1 finding is fixed. The fy1-k3 c rubric (2 p criterion) now says "noin $14\,\%$". That matches both places in solutions.md ($\tfrac{0{,}3}{2{,}1} \approx 14\,\%$) and my own figures: $277\,\text{m}/2057\,\text{m} = 13{,}5\,\%$ unrounded, $14{,}3\,\%$ from the rounded bounds, and $6{,}25\,\% + 7{,}1\,\% = 13{,}4\,\%$ for the two summed effects.

## Polish
- fy1-k6 b (C): the rubric and the solution give the difference from $9{,}81\,\text{m/s}^2$ as "noin 1 %". The line as read ($9{,}675\,\text{m/s}^2$) gives $1{,}4\,\%$. "Noin 1–2 %" would fit better.
- fy1-k7 d (C): calling $80\,\text{g/m}^2$ "tarkka arvo" goes a little too far. It is a nominal value with a manufacturing tolerance of a few per cent. "Oletetaan tarkaksi" would be more honest. The result $780\,\text{kg/m}^3$ does not change.

## Checked
- I recomputed every number in one script from the task data, side by side with answers.py. All agree: k1 f $16{,}8 \to 17\,\text{km/h}$; k1 j order A, C, B, D; k2 $0{,}118\,\text{cm/min}$ (LSQ $0{,}1174$) and $110\,\text{min}$; k3 $643\,\text{s}$ and $2057\,\text{m}$, bounds $1800$ and $2354\,\text{m}$; k4 $(1{,}42 \pm 0{,}03)\,\text{s}$; k5 $7{,}68$ and $7{,}11$–$8{,}35\,\text{g/cm}^3$; k6 the filter data match $1{,}5\tanh(gt/1{,}5)$, $g = 9{,}675\,\text{m/s}^2$ and $42\,\text{km/h}$ (also with $9{,}81$); k7 $(102 \pm 2)\,\mu\text{m}$ (residuals at most $0{,}6\,\text{mm}$) and $784\,\text{kg/m}^3$.
- Osa 1: each item has exactly one correct option, and the distractors are real errors (dimensions, prefix, significant figures, interval overlap, the walk slopes $1{,}5$, $0$ and $2{,}0\,\text{m/s}$, mass-independent fall).
- Guardrails: the outlier is dropped only once its cause is found; half the range is used as a scatter estimate; repetition does not reveal a systematic error; slopes come from the line; extrapolation is flagged; the origin constraint has a physical reason. Causality holds (air resistance relative to weight, reaction time over ten swings, air between the paper fibres).
- Scope is FY1 only. Every rubric criterion asks only what its task gives; the points sum (check OK); alternative methods are accepted; the data are marked as example data. The hash is the same at the start and the end.
