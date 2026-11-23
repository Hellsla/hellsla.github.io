VERDICT: PASS
CONTENT-HASH: 297ca9a235b33434
SCOPE: delta numbers from e4698eb90a6f28b3 base 3076572
Delta from the version I passed (e4698eb90a6f28b3): I judged only the diff in the packet, which rewrites the Formula steps so they start from the basic equations.

## Blocking
(none)

## Polish
- solutions.md fy6-10-L2-09 (Reading the graph): this is still open from earlier. "about 0.06 mN over the fifth grid line" claims more precision than a 1 mN grid can give. Say "about 5.0–5.1 mN".
- solutions.md (hanging-sphere task, Formula): $G = mg$ is the weight here, but the electron–proton task in the same set uses $G$ for the gravitational constant. Both are correct within their own task. Using $G$ for weight follows the house notation, so this is only a note.

## Checked
- Charge sharing (L1 contact tasks): $Q_1 + Q_2 = Q + Q$ before $Q = (Q_1+Q_2)/2$ states conservation of charge plus equal sharing between identical spheres. The derivation is correct.
- Distance task: Coulomb's law is solved step by step through $r^2$ to $r$. Ratio task: the law is written for $r_1$ and $r_2$ and the two are divided, so the charges cancel. Both derivations are correct.
- Hanging sphere: $F_\text{e} = G$, then $F_\text{e} = kq^2/r^2$ and $G = mg$, giving $q = r\sqrt{mg/k}$. The balance comes first, as the house rule requires.
- Threads task: $T\cos\theta = mg$ and $T\sin\theta = F$ give $F = mg\tan\theta$, which is right for a sphere hanging at angle $\theta$ to the vertical. $r = 2L\sin\theta$ holds for two threads of length $L$ hung from one point.
- Three charges: $F = F_1 + F_2$ adds the forces only when they point the same way. The surrounding text says so.
- Zero points: between the charges, $F_1 = F_2$ gives $x/(d-x) = \sqrt{Q_1/Q_2}$. Beyond $q_2$, it gives $x/(x-d) = s$ and $x = ds/(s-1)$. Both are correct, and $q$ cancels.
- Electron–proton ratio: both laws are written with $r^2$, so $r^2$ cancels and the ratio is $ke^2/(Gm_\text{e}m_\text{p})$. This is correct.
- Fit task L2-05: $F = kq^2 \cdot (1/r^2)$, so the slope is $s = kq^2$ and $q = \sqrt{s/k}$. Pair table L2-06: at the same $r$, $F_\text{B}/F_\text{A} = q_\text{B}/20\,\text{nC}$, which matches its Principle step.
- Pair graph L2-10: setting $F_\text{A} = F_\text{B}$ at $4.0\,\text{mN}$ gives $q_\text{A}/r_\text{A}^2 = q_\text{B}/r_\text{B}^2$, so $q_\text{B} = q_\text{A}(r_\text{B}/r_\text{A})^2$. This is correct.
- No Substitution, Answer, answers.py value or figure changed, so the recomputations from my earlier reviews still hold.
