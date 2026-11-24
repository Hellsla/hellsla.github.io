VERDICT: PASS
CONTENT-HASH: 5e6541ff07793d7a

## Blocking

## Polish
- solutions.md:224 (fy3-1-L3-04): the Kaava block now labels $c$ in the formula itself as "jousen vakio". In $x/m = c\,g$ the constant $c$ is the stretch per newton, the inverse of a spring constant. Write "$c$: venymä newtonia kohti" so it matches L1-02. The algebra and the result do not depend on the name.
- exercises.json (fy3-1-L1-10): the stored 316,2 N still carries one figure more than the solution's 316 N. This is carried over and is inside the tolerance.

## Checked
- I read every changed Kaava block on disk as an aligned block (the packet's diff shows the rows joined). L1-02, L1-04, L2-01, L2-03, L2-04, L2-05, L2-06, L2-07, L2-08, L3-01, L3-02, L3-03, L3-04 and L3-05 each start from the basic relation ($G = mg$ or the proportionality $x \propto F$). Each then isolates the unknown in symbols, and the last symbolic row is the form the Sijoitus uses.
- L2-03: $\Delta G = G_\text{Maa} - G_\text{Kuu} = m(g_\text{Maa} - g_\text{Kuu})$ is correct, and $145 \cdot 8{,}19 = 1187{,}55\,\text{N}$.
- L2-04: from $F/G = x/x_1$ to $F = mgx/x_1$ is correct and gives $5{,}886\,\text{N}$.
- L3-02: equating the same lifting force gives $m_\text{Kuu} = m_\text{Maa}g_\text{Maa}/g_\text{Kuu} = 133{,}2\,\text{kg}$. Correct.
- L3-03: the scale reading $L = G/g_\text{Maa}$, then $m = Lg_\text{Maa}/g_\text{Mars} = 68{,}75\,\text{kg}$. The model is right: the scale measures force.
- L3-05: $F_\text{max} = m_\text{max}g_\text{Mars}$, then $m_\text{lisä} = F_\text{max}/g_\text{Mars} - m_\text{yht}$. The leg limit is treated as a force. Correct.
- L3-04: dividing the two calibration relations cancels $c$. $g_\text{X} = 9{,}81 \cdot 3{,}8/10{,}38 = 3{,}59\,\text{m/s}^2$.
- L1-09: the paragraph split leaves the physics unchanged. The option figures carry the teacher's approval, and the feedback reasoning is the same as before.
- exercises.json: only caption markers were removed. No number, answer or tolerance changed.
- The hash was the same at the start and the end.
