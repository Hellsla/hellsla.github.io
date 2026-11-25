VERDICT: PASS
CONTENT-HASH: dbd4509c7fbbbf79

Delta review of the new `hints` in `sovella/tasks.json` (s1–s8, 32 parts, 96 hints; git diff origin/main). Nothing else changed.

## Blocking
None.

## Polish
1. s8 c, hint 3 (fi): the offset $0{,}04\,\text{mT}$ is already in the measured points, so "lisätään" asks the student to imagine a second offset. The physics conclusion (slope unchanged, intercept shifts) is the same, but correcting the data matches part d and the solution better. Replacement: "Lue kuvaajalta $B$ virroilla $0{,}50\,\text{A}$ ja $2{,}5\,\text{A}$ ja laske osuus kummallakin. Kuvittele sitten, että kaikista pisteistä vähennetään $0{,}04\,\text{mT}$: miten suora muuttuu?"

## Checked
- Every hint uses the same model, symbols and sign conventions as its part's rubric and `solutions.md`: $\mu_0 = \tan\alpha_0$ and $F_{\mu 0} \le \mu_0 N$ (s1, s6 c, inequality direction kept), $Pt = cm\,\Delta T$ and $c = P/(mk)$ (s2), $g = 2h/t^2$ with $\Delta g$ as half the extreme spread (s3 b), $T^2 = \tfrac{4\pi^2}{g}(l + r)$ and $b = kr$ (s4), $\Delta V$ as the sum of two reading uncertainties (s5 b), $s = v^2/(2a)$ and $a = 1/(2k)$ (s6), $F_\mu = F_\text{lukema} - F_0$ (s7 c), $B = \mu_0 n I = kI$ (s8).
- Recomputed every number a hint states or leads to: $10\,\text{km/h} = 2{,}78\,\text{m/s} \approx 2{,}8\,\text{m/s}$; s2 c $t = 160\,\text{s}$; s3 b $g_\text{max} = 10{,}67$, $g_\text{min} = 8{,}92$, $\Delta g = 0{,}87\,\text{m/s}^2$; s4 d first row $g = 8{,}87\,\text{m/s}^2$; s5 $\rho = 2{,}677\,\text{g/cm}^3$, $\Delta\rho = 78\,\text{kg/m}^3$, relative $0{,}05\,\%$ against $2{,}9\,\%$; s6 d $1{,}05^2 = 1{,}1025$; s7 c $0{,}24$, $0{,}21$, $14\,\%$; s8 $k = 2{,}47\,\text{mT/A}$, $n = 1{,}96 \cdot 10^3\,\text{1/m}$, $I = 4{,}9\,\text{A}$, $3{,}1\,\%$ and $0{,}65\,\%$. All agree with the rubric.
- No hint states a part's final answer. Hint 3 of s1 b, s3 b, s4 d and s6 c names a step or a limit's direction but leaves the result to compute.
- Unit conversions in hints (g to kg, kJ to J, mT to T, km/h to m/s before squaring, ml to cm³) are right and in the order the solution uses.
- Numbers with units are LaTeX with decimal commas.
