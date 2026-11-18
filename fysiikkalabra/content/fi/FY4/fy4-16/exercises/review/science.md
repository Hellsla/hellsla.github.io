VERDICT: PASS
CONTENT-HASH: 06be6c204f936543
## Blocking

## Polish
- solutions.md:354 (L3-05) — "tasaisesti muuttuvassa liikkeessä välin keskinopeus on päätenopeuksien keskiarvo": the motion is not uniformly decelerated (the table shows it); say the trapezoid sum is an approximation on each $0{,}5\,\text{s}$ interval (carried over).
- solutions.md L2-07 (line ~318) — "Keskinopeus $v = \Delta x/\Delta t$" is added to Kaava but the solution reads velocities from the table; drop it or show where it is used (carried over).
- solutions.md:155 (L2-04, crane) — "$E = Pt$ ja $E = W$" is right; "$P = W/t$" directly would be shorter (carried over).

## Checked
- Round-1 Blocking fixed: friction and air-resistance work is now signed as the chapter teaches, $W_\mu = -F_\mu L$ (L2-02, :121), $W_\mu = -F_\mu s$ with each part $-\mu m g x$ (L3-01, :179), $W_\text{v} = -F_\text{v} h$ (L3-03, :214; L3-05, :354), $W_\mu = -F_\mu s$ (L3-04, :334), and every balance is written $E_\text{alku} + W = E_\text{loppu}$, consistent with L1-04 ($W = -F_\mu s$, :64) and L3-03 Periaate (:206).
- Each signed form expands to the same equation as before: $mgL\sin\alpha - \mu mg\cos\alpha L = \tfrac12 mv_2^2$; $mgh - \mu mg(x_\text{a}+x_\text{b}+x_\text{c}) = 0 \Rightarrow x = h/\mu$; $E_{\text{k}0} + mgh - F_\text{v} h = E_\text{k} \Rightarrow F_\text{v} = mg + (E_{\text{k}0} - E_\text{k})/h$; L3-04 $L = \mu_2 d/(\sin\alpha - \mu_1\cos\alpha)$, $v = \sqrt{2gL(\sin\alpha - \mu_1\cos\alpha)}$. Algebra right; numbers and answers unchanged.
- Grep of every $W$ in solutions.md: no positive resisting-force work left; the positive ones are the crane's lifting force ($W = Th = mgh$), right.
- L2-03 $|\Delta E_\text{mek}| = 221\,\text{kJ}$ stays a magnitude as Kysytty asks.
- No other change since round 1 (git diff d97ccea596..HEAD: Kaava rows of L2-02, L3-01, L3-03, L3-04, L3-05 only); no task, answer, tolerance or id changed.
- Captures: none opened (text-only fix, judged from the source).
- Hash 06be6c204f936543 at start and end.
