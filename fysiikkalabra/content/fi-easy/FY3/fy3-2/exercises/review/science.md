VERDICT: PASS
CONTENT-HASH: 29156fe03d1e4462

## Blocking

## Polish
- solutions.md:98 (fy3-2-L3-01): the Kaava block stops at $F_\text{ka} = W/s$. The block could end in the one final form $F_\text{ka} = \dfrac{F\,(\tfrac12 s_1 + s_2 + \tfrac12 s_3)}{s}$ (house rule "simplify to the end"). The two-stage Sijoitus is correct as it stands.
- solutions.md:201 (fy3-2-L3-04): the block could end in $h = \dfrac{F s}{2 m g}$. The block also writes $s$ and $F$, but Annettu names them $s_\text{max}$ and $F(s_\text{max})$; one notation in both places would read better.
- solutions.md:122 and 171 (L3-03 check sentence, L2-07 order) are carried over from the previous report.

## Checked
- I read every changed Kaava block on disk. Each starts from a basic law ($W = Fs$, $P = W/t$, $G = mg$, $F = G$ at constant velocity, $s = vt$, $m = \rho V$, area under $(s,F)$). Each combines the laws in symbols, and its last row is what the Sijoitus evaluates.
- L1-05: $P = Fvt/t = Fv$. The derivation is correct.
- L2-03, L2-07, L1-09: $W = Fh$, $F = G$ and $G = mg$ give $W = mgh$ ($= \rho Vgh$). The constant-velocity condition is in each Periaate.
- L2-04: $W = F_1s_1 + \tfrac12(F_1+F_2)s_2 = 100\,\text{J}$. L2-05: the trapezoid sum gives $55{,}3\,\text{J}$. L2-09: $190\,\text{J}/10\,\text{m} = 19\,\text{N}$. All correct.
- L2-06: $P = mgnh_1/t_\text{ka} = 62 \cdot 9{,}81 \cdot 18 \cdot 0{,}17/8{,}1 = 229{,}8\,\text{W}$. Correct.
- L3-01: $\tfrac12 \cdot 40 \cdot 0{,}5 + 40 \cdot 1{,}0 + \tfrac12 \cdot 40 \cdot 0{,}5 = 60\,\text{J}$, so $F_\text{ka} = 30\,\text{N}$. Correct.
- L3-02: $\Delta U = nmgh = 588{,}6\,\text{J}$. The no-loss assumption is in the Periaate, and it speaks of internal energy, not heat.
- L3-04: the triangle area $\tfrac12 \cdot 10{,}0 \cdot 0{,}100 = 0{,}500\,\text{J}$ gives $h = 0{,}2548\,\text{m}$. L3-05: $P = mgv = 3598\,\text{W}$, and $Pt$ against $mgh$ is $28{,}78$ against $28{,}69\,\text{kJ}$. Both correct.
- The set stays in FY3 scope: no $E_k$, no $\cos\alpha$, no Newton's laws beyond "lifting force = weight at constant velocity".
- exercises.json: only caption markers changed. The hash was the same at the start and the end.
