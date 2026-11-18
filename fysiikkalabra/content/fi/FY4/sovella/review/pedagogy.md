VERDICT: PASS
CONTENT-HASH: 8714d203727c4572
## Blocking
(none)
## Polish
- solutions.md fy4-s2 c, Sijoitus — the Kaava ends in $v = \sqrt{\dfrac{2\,(mgh - F_\text{vast}\,s)}{m}}$, but the substitution first computes $E_\text{k} = 8745\,\text{J}$ and then $v = \sqrt{2E_\text{k}/m}$; substitute into the last symbolic form: $v = \sqrt{\dfrac{2\,(13\,979\,\text{J} - 5234\,\text{J})}{95\,\text{kg}}}$.
- solutions.md fy4-s1 c, Kaava — the line "$a$ = suoran kulmakerroin" lives in Periaate and Kuvaajan lukeminen; say once in Kaava that $a$ is the slope read in the previous row, so the chain from graph to $\mu = \dfrac{g\sin\alpha - a}{g\cos\alpha}$ is unbroken.
- solutions.md fy4-s3 e — the second and third assumptions ("kitkakerroin $0{,}75$", "pyörät lukossa") each state a direction but only the first is quantified; one number for the second ($\mu = 0{,}6$ gives $v_\text{B} \approx 12\,\text{m/s}$) would show the margin to the $40\,\text{km/h}$ limit.
## Checked
- Round 1, full (the packet gives no delta). The edited part is the Kaava step of every model solution: all start from the basic law ($\Sigma F = ma$, $F_\mu = \mu N$, $E_\text{p0} + E_\text{k0} + W = E_\text{p} + E_\text{k}$, $E_{\text{k}0} + W = E_\text{k}$, $p_\text{ennen} = p_\text{jälkeen}$, $I = \Delta p$), then solve the asked quantity in symbols (mass cancelled where it does), then substitute.
- Numbers recomputed from the solutions: $\mu_\text{A} = 0{,}030$, $\mu_\text{B} = 0{,}045$, $\mu_\text{A,korj.} = 0{,}024$; $17{,}2\,\text{m/s}$, $29\,\text{N}$, $13{,}6\,\text{m/s}$; $7{,}86\,\text{m/s}$, $13{,}6\,\text{m/s}$, $4{,}5\,\text{kN}$, $6{,}7\,\text{mg}$: all consistent with answers.py and the rubric's tolerances.
- Three tasks follow the module goals (graph and measurement, conservation laws, safety); authentic contexts, no formula named in the task texts, sources marked simulated or invented.
- Progression within tasks: read data, draw force diagram, model, judge reliability; the two-model comparison in s2 d and the assumptions in s3 e train transfer.
- Model answers are complete and followable, with Hyväksytään myös and Yleisiä virheitä per task; the force-diagram solution in s1 b explains choices (components not forces, why no forward force).
- Finnish in the solutions correct; glossary terms kept ("liukukitka", "mekaniikan energiaperiaate", "impulssiperiaate").
- Captures opened: content/fi/FY4/sovella/review/shots/FY4-sovella-page-390-8.png (s1 d and e, figure and formula blocks fit at 390 px) and -10.png (common mistakes and the self-assessment rows, nothing clipped). Fi only; no en or fi-easy judged here.
