VERDICT: FAIL
CONTENT-HASH: d824b9bf6afb9a24

## Blocking
- exercises/solutions.md:609 (fy7-11-L3-01), A, internal consistency: the task tells the student to round the intermediate angles to hundredths, but the Sijoitus row does not follow its own printed values. $1{,}5143 \cdot \sin 22{,}16^\circ = 0{,}57119$, not $0{,}57127$, which gives $\alpha_4 = 34{,}83^\circ$, not $34{,}84^\circ$. $1{,}5302 \cdot \sin 22{,}48^\circ = 0{,}58509$, not $0{,}58502$, which gives $\alpha_4 = 35{,}81^\circ$, not $35{,}80^\circ$. A student who follows the instruction gets $0{,}98^\circ$, while the solution shows $0{,}96^\circ$ from numbers that do not produce it. Both results are inside the tolerance. Fix: substitute the rounded $\alpha_3$ and show $0{,}57119 \to 34{,}83^\circ$ and $0{,}58509 \to 35{,}81^\circ$, then $\Delta\delta = 0{,}98^\circ$, and note that unrounded intermediates give $0{,}966^\circ$. Or drop the hundredths instruction from the task and keep the unrounded chain. Correct δ_p, δ_v on line 611 to match.

## Polish
- exercises/solutions.md:711 (L3-05 Järkevyys): "Yhden pinnan ero olisi vain noin $1^\circ$". At $\alpha_1 = 50{,}0^\circ$ in flint the gap is $28{,}32^\circ - 27{,}67^\circ = 0{,}65^\circ$. Write "noin $0{,}65^\circ$".
- exercises/solutions.md:540 (L1-03 Järkevyys): it compares with "taulukon kruunulasin" values, but the task names only "lasikappale" and gives no table. Say "kruunulasin tyypilliset arvot".
- exercises/solutions.md:698 (L3-04): the water column's largest table value is $42{,}25^\circ$. "noin $42{,}3^\circ$" is fine, but the $8{,}99^\circ$ difference is computed from $42{,}25^\circ$, so state it the same way in both places.

## Checked
- All 19 numeric answers recomputed with my own formulas. They match answers.py and exercises.json; L2-03 and L2-07 match within reading accuracy: flint $n(450) = 1{,}6387$, BK7 $n(600) = 1{,}5163$.
- L3-04 (the reported fix): each row's $n$ is 1,3997–1,4002 and the mean is 1,4000, so "$1{,}40$, three significant figures" is right. The water column follows $n = 1{,}3315$ to $\pm 0{,}005^\circ$. The solution's peak is $33{,}25^\circ$ at $55{,}6^\circ$, consistent with the table. The model answer's differences ($0{,}10^\circ$, $5{,}03^\circ$) and "inside the bow" are right. The data is labelled esimerkkiaineisto.
- Rainbow maxima: red $42{,}30^\circ$ at $59{,}5^\circ$, violet $40{,}63^\circ$ at $58{,}8^\circ$. These match L2-04, L2-06, L3-03 and the brief.
- L3-05: $A_\text{max}$ is $64{,}98^\circ$ for violet and $66{,}57^\circ$ for red. At $A = 65^\circ$ violet gives $n \sin\alpha_3 = 1{,}0005$. The deviations at 64° and 60° and their differences ($7{,}42^\circ$, $3{,}91^\circ$) are right.
- L1-04 and L1-05 data are physically consistent (implied $n \approx 1{,}496$ and $1{,}33$).
- L2-01 states its assumption $v = c : n$ and the group-velocity caveat. $\Delta t = 265\,\text{ns}$.
- L1-06 has exactly one correct option, and each distractor's feedback is right. L1-09: all six statements and their feedback are right ($42^\circ - 45^\circ = -3^\circ$).
- L2-05: the three glasses' $\Delta\alpha$ values and the $\Delta n / n \tan\alpha_2$ check are right.
- Figures: the flint curve gives $1{,}6150$ at 656 nm, consistent with the L2-05 table. Neither figure nor its description gives an answer away.
- Scope (FY7 refraction and dispersion), notation, symbolic-first solutions and unit conversions checked.
