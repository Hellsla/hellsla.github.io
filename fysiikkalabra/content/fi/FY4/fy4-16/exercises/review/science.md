VERDICT: FAIL
CONTENT-HASH: 8ad3639f61897685
## Blocking
- solutions.md:179 (L3-01, $x = h/\mu$), :334 (L3-04), :214 (L3-03) and :354 (L3-05) Kaava — the new text defines the work of a resisting force as positive ("kitkan työ on $W_\mu = F_\mu s$", "ilmanvastuksen työ $W_\text{v} = F_\text{v} h$", "jokaisen osan kitkatyö on $\mu mg x$") and writes $E_\text{alku} = E_\text{loppu} + W$. The chapter teaches $W_\mu = -\mu m g x$ and $E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}$ with $W$ negative for a force against the motion; L1-04 (line 64, $W = -F_\mu s$) and L1-07 ("ilmanvastus tekee negatiivista työtä") in this same set say so too. A student who takes the chapter's $W_\mu$ into these equations gets the sign wrong. Fix: $W_\mu = -F_\mu s$ (each part $-\mu m g x$), $W_\text{v} = -F_\text{v} h$, and the chapter's form $E_\text{alku} + W = E_\text{loppu}$; the resulting equations and all numbers stay as they are.
- solutions.md:121 (L2-02, $\mu = 0{,}1373$) — "Kitkan työ on $F_\mu L$": same sign error. Fix: "$W = -F_\mu L$".

## Polish
- solutions.md:354 (L3-05) — "$s = v\Delta t$ … tasaisesti muuttuvassa liikkeessä välin keskinopeus on päätenopeuksien keskiarvo": the motion is not uniformly decelerated (the table shows it); say the trapezoid sum is an approximation on each $0{,}5\,\text{s}$ interval.
- solutions.md L2-07 (line ~318) — "Keskinopeus $v = \Delta x/\Delta t$" is added to Kaava but the solution reads velocities from the table; drop it or show where it is used.
- solutions.md L2-04 (crane) — "Työ $W = Fs$ … Energia $E = Pt$ ja $E = W$" is right; "$P = W/t$" directly would be shorter.

## Checked
- Captures: none opened (judged from text; the diff is text-only).
- Newton's-law Kaava rows (lift $N = m(g + a)$, scale reading, elevator graphs, constant-speed slope $\tan\alpha = \mu$, incline $F_\mu = \mu mg\cos\alpha$): start from $\Sigma F = ma$ or $\Sigma F = 0$ with a stated positive direction; correct.
- Chute: $E_\text{alku} = mgh$, $E_\text{loppu} = \tfrac12 m v_2^2$, $v_2 = \sqrt{2gh} = 7{,}924\,\text{m/s}$; right.
- L1-04: $0 = \tfrac12 m v_1^2 - \mu m g s$ with $W = -F_\mu s$, $22{,}94\,\text{m}$; right and in the chapter's form.
- L2-03 $|\Delta E_\text{mek}| = 221\,\text{kJ}$; L3-04 $v = \sqrt{2gL(\sin\alpha - \mu_1\cos\alpha)} = 7{,}67\,\text{m/s}$ now symbolic before substitution; right.
- The equations actually solved in the flagged tasks are numerically right; only the sign convention of $W$ is wrong.
- Paragraph splits change no wording or number; no answer, tolerance or id changed.
- Hash 8ad3639f61897685 at the start and at the end.
