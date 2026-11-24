VERDICT: PASS
CONTENT-HASH: 33e918c155d2be7b

## Blocking

## Polish
- inquiry.json:339 (data, solution "Vastaus") — "Mittauspisteet poikkeavat suorasta noin $0{,}1\,\text{m/s}$" overstates it: the largest deviation from the fitted line ($k \approx 9{,}78\,\text{m/s}^2$) is $0{,}04\,\text{m/s}$, which is below the data's resolution of $0{,}1\,\text{m/s}$. The estimate of about $0{,}2\,\text{m/s}^2$ therefore rests on a wrong premise — fix: "poikkeavat suorasta alle $0{,}05\,\text{m/s}$ (lukemien tarkkuus $0{,}1\,\text{m/s}$)", or drop the uncertainty figure.
- lesson.md:122 (vt-graph) — the figure shows $\dfrac{19{,}6\,\text{m/s}}{2{,}0\,\text{s}} = 9{,}81\,\text{m/s}^2$, but the arithmetic gives $9{,}8$ — fix: "$\approx 9{,}8\,\text{m/s}^2$", or use the unrounded $19{,}62\,\text{m/s}$.
- assets/sims/fy1/fy1-6/sim.js:941 — the pace control is labelled "Nopeus" and sits right above the readout "nopeus $v = …$". In a chapter about velocity, a student can read it as the balls' speed. The file's own header calls it "Nopeus (toisto)" — fix: use that label (or "Toistonopeus") in lang.
- exit-ticket.json — the ratio $6{,}06$ has three figures while the times have two. It is a ratio of the two $g$ values, so this is defensible; the answer could say so in five words.

## Checked
- One script recomputed every number from the task data: kertaus $1{,}08$ (distractors $1{,}82$, $0{,}93$ and $2{,}7$ are right; and $1{,}4\,\text{m}$ in $1{,}3\,\text{s}$ fits the Moon's $g$, since $t = 1{,}31\,\text{s}$), exp-1 $9{,}81$, data slope $9{,}8$ (least squares through the origin $9{,}78$), transfer task $11{,}1$ with mistakes $29{,}4$ / $22{,}2$ / $3{,}7$, check-2 $3{,}058\,\text{s}$ with mistakes $11{,}0$ / $30$ / $0{,}327$, worked example $14{,}715\,\text{m/s}$ = $52{,}97\,\text{km/h}$, pause boxes $39{,}2$ and $24{,}6$, exit ticket $4{,}86$ / $29{,}4$ / $6{,}06$. All match lesson-answers.py.
- Sim physics: quadratic drag $K = \tfrac12\rho C_d A$; $v = v_T\tanh(gt/v_T)$ and $s = (v_T^2/g)\ln\cosh(gt/v_T)$ are the exact solutions. In a vacuum $v = gt$ and $s = \tfrac12 gt^2$, and $78{,}5\,\text{m}$ fits on the $0$–$80\,\text{m}$ scale.
- The explain model answer's air values ($10{,}5$ and $37{,}5\,\text{m/s}$ at $4{,}0\,\text{s}$) match the sim. The exp-3 capture shows $27{,}5\,\text{m/s}$ for $1\,\text{kg}$, which also matches.
- Experiments: exp-1 locks the air setting and both masses and varies $t$. exp-2 and exp-3 lock the air setting, $t$ and $m_\text{A}$ and vary $m_\text{B}$ (balls of equal size, so mass is the only thing that changes). simState gives vA and vB, and the slider ranges cover every initial value.
- Predictions: exactly one option is correct in pred-1, pred-2, exp-2, exp-3, virhe, check-1 and check-c2, and every distractor's feedback names the right reason.
- Figures: free-fall positions $0$ / $4{,}9$ / $19{,}6$ / $44{,}1\,\text{m}$ and the vt-graph points are to scale. The data-plot points and the fitted line match the table, and the line passes through the origin with a physical reason given (time counted from release).
- Conditions: "no air resistance" is stated with $v = gt$, in the summary, in the "mass does not matter" section and in the sim's model box. The air-resistance mechanism stays qualitative, which suits FY1 (C).
- Scope: $v = gt$ as a linear model and slope reading, within FY1. Forces are explicitly deferred.
- The Kaava section names the law (keskikiihtyvyys, then $v = gt$). The worked example is solved symbolically first, the conversion is explained, and the two figures follow from $1{,}5\,\text{s}$.
- Hash identical at start and end.
