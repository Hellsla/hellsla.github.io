VERDICT: PASS
CONTENT-HASH: 4a1fda197003179c
## Blocking

## Polish
- solutions.md fy4-k4 a) Kaava — "$W = Fs$" without a sign, then $\tfrac12 mv^2 - \mu mg\,s = 0$; the same task's Yleisiä virheitä calls positive friction work an error. Fix: "kitkan työ $W = -F_\mu s = -\mu mg\,s$", and the chapter's form $E_{\text{k}0} + W = E_\text{k}$.
- solutions.md fy4-k7 d) Kaava — "$W = Fs$ ja $F = ma$" uses $F$, which in c) is the helmet's force $F = m(a + g)$; here it must be the total force. Periaate says $v^2 = 2as$. Fix: "$\Sigma F = ma$" or derive from $v^2 = v_0^2 + 2as$ as the Periaate does; numbers unchanged.
- solutions.md fy4-k6 e) Sijoitus — "$0{,}52\,\text{s}$ … $0{,}34\,\text{m}$": $9{,}81 \cdot 0{,}52^2 / 8 = 0{,}33\,\text{m}$; $0{,}34$ comes from $0{,}49 + \tfrac{1}{30} = 0{,}523\,\text{s}$. Fix: write $0{,}523\,\text{s}$ and $0{,}457\,\text{s}$, or $0{,}33\,\text{m}$.
- solutions.md fy4-k5 a) Kaava — not rewritten: starts from the combined $m_\text{A}v_\text{A} = (m_\text{A} + m_\text{B})u$. Fix: "$p_\text{ennen} = p_\text{jälkeen}$, missä $p = mv$ ja $v_\text{B} = 0$" first, as in the other tasks.
- solutions.md fy4-k7 c) Annettu gives $a = 600\,\text{m/s}^2$, Sijoitus uses $603\,\text{m/s}^2$. Fix: give $603$ in Annettu.

## Checked
- Captures: none opened (judged from the packet text).
- Rewritten Kaava rows (commit fcc9aacbfc): k2 c $s = s_1 + s_2$ from the areas; k3 b $\Sigma F = ma$ with $F_{\mu 0} \le \mu_0 N$ (lepokitka/lähtökitka terms right); k3 d, k6 a, k6 c ($I = \Sigma F\,\Delta t$, $\Sigma F = F - G$), k6 d, k6 e (free fall over $t/2$), k7 a, k7 c ($F - mg = ma$): each starts from the basic law and simplifies symbolically; correct.
- Recomputed in one script: $\mu = 0{,}249$ ($0{,}234$–$0{,}265$); $v = 2{,}46\,\text{m/s}$, $h = 0{,}309\,\text{m}$, $0{,}294\,\text{m}$; $v = 5{,}425\,\text{m/s}$, $\bar a = 603\,\text{m/s}^2$, $F = 3063\,\text{N}$, $a_1 = 613$, $a_\text{huippu,2} = 2280\,\text{m/s}^2$ (margin $6{,}9\,\%$), $25\,\text{km/h} = 6{,}94\,\text{m/s}$, energy ratio $1{,}6$; k1 h $6{,}0\,\text{N·s}$, $14\,\text{m/s}$; k1 i $67\,\%$; k2 $0{,}95$, $76\,\text{m}$, $30\,\text{kN}$; k3 $3{,}9$, $5{,}0$, $2{,}9\,\text{m/s}^2$; k5 $0{,}60\,\text{m/s}$, $16{,}2\,\text{kJ}$, $27\,\text{kN}$. All agree with answers.py.
- Osa 1: each item has one correct option; distractor reasons are real errors.
- Physics: weight's impulse subtracted in the jump; momentum over the coupling only; Newton III equal forces with unequal $\Delta v$; static friction only as large as needed; "sisäenergiaksi" (P1).
- Hash 4a1fda197003179c at the start and at the end.
