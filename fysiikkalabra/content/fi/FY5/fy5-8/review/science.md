VERDICT: PASS
CONTENT-HASH: b54730130df2648e

## Blocking

## Polish
- lesson.md:468 — In the worked example, $F$ in $F - mg = 0$ is a magnitude, while the Kaava section defines $F = -kx$ as an $x$-component. This is fine at this level (C). If you want to say it, one clause such as "jousen voiman suuruus $F = kx$" would do it.
- lesson.md:332 — "Suora kulkee origon kautta, koska ilman venyttävää voimaa jousi on lepopituudessaan" is a fair simplification (C). Some school coil springs have initial tension, and then the line misses the origin. You could add this to the linked investigation, but nothing in this lesson needs to change.
- inquiry.json mittaus, mistake 3.06 — The value is in kg/m, not N/m. The feedback names the error correctly. Only the number shown in the unit N/m looks odd.

## Checked
- Recomputed every number in one script with my own formulas: exp-3 $k_C = 80\,\text{N/m}$; worked example $k = 392{,}4\,\text{N/m}$ and $E_\text{p} = 0{,}1766\,\text{J}$ (the triangle check agrees); kulmakerroin $40\,\text{N/m}$; mittaus least squares through the origin $29{,}95\,\text{N/m}$ (free fit $29{,}98$, point by point $28{,}9$–$30{,}7$), so $30\,\text{N/m}$ with ±7 % is sound; siirto $3{,}354\,\text{m/s}$ and its three mistakes ($4{,}743$, $0{,}1061$, $335{,}4$); check-2 $+10\,\text{N}$; check-3 $0{,}15\,\text{m}$ and $N \approx 59\,\text{N}$; exit ticket $1{,}0\,\text{J}$. All match lesson-answers.py.
- The kulmakerroin graph is to scale as it claims (3100 px/m, 47,2 px/N). Its line slope is $39{,}9\,\text{N/m}$ and the five points lie on it within reading accuracy. The pinta-ala figure's $x$, $2x$, $kx$ and $2kx$ are in exact proportion. In the suunta and pari figures the arrows are equally long and the geometry is consistent (stretch and compression both $70\,\text{px}$).
- Force diagrams: in the esimerkki diagram $G$ (from the centre) and $F$ (from the top face) are equal, with $y$ up. The virhe figure has exactly one error ($\overline{F}_2$ acting on the spring, drawn on the block), $F_1 = G$, so the "twice the weight" distractor really is wrong. In malli-laatikko $N = G$ and $F = F_\mu$, $v$ is drawn apart from the forces, and no stretching force is drawn.
- sim.js implements $F = -kx$, $F_\text{k} = kx$, $F_\text{v} = kx$ and $E_\text{p} = \tfrac{1}{2}kx^2$. The arrow directions and the push/pull drawing are right for $x$ of either sign. simState has F, Fk, Fv and Ep. Each experiment locks the right parameter and isolates its varied one. The readout gives $0{,}0625$ as $0{,}063\,\text{J}$, matching the feedback.
- The model's limits are stated: no friction, the cart held at rest, the law holds over the whole slider range, no permanent stretch, the spring constants are model values.
- Predictions 1–3, the retrieval item, virhe and check-1 each have exactly one correct option, and each distractor's feedback names the right physics with the sim's numbers.
- Third-law wording agrees across the theory, summary, misconception, exit ticket and sim boxes. The Hooke condition ("ei venytetä liikaa") is stated in the theory and the glossary.
- Scope: harmonic force and its potential energy belong to FY5. There is no $\omega$ and no period.
- Significant figures: the worked example is limited by $3{,}0\,\text{cm}$ and siirto by $6{,}0\,\text{cm}$ and $80\,\text{g}$, each with the right reason.
- The content hash is the same at the start and the end.
