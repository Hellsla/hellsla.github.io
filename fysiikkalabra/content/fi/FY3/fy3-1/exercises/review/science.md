VERDICT: PASS
CONTENT-HASH: 8361d8c133f37f03

## Blocking

## Polish
- solutions.md:283 (fy3-1-L2-08): the Kaava stops at two separate forms, $g = G_1/m_1$ and $G = m g$. It could finish the symbolic step as $G = m\,G_1/m_1$ before the Sijoitus. Sijoitus did not change, so this is optional.
- solutions.md:19 (fy3-1-L1-02), carried over: the check's product $0{,}50 \cdot 12 = 6{,}0$ still has no units.

## Checked
- The packet's diff shows the aligned blocks flattened. I read the real multi-row `aligned` blocks on disk (solutions.md:15–283), and every row is a separate equation.
- All 14 changed Kaava blocks start from the basic law ($G = m g$, or the proportionality $x \propto F$) and solve symbolically for the asked quantity. The last symbolic form is the one Sijoitus evaluates.
- Algebra checked row by row: $x = x_1F/F_1$, $F = F_1x/x_1$, $m = G/g$, $\Delta G = m(g_\text{Maa}-g_\text{Kuu})$, $F = mgx/x_1$, $G_\text{Mars} = G_\text{Maa}g_\text{Mars}/g_\text{Maa}$, $m_\text{Kuu} = m_\text{Maa}g_\text{Maa}/g_\text{Kuu}$, $m = Lg_\text{Maa}/g_\text{Mars}$, $g_\text{Mars} = g_\text{Maa}G_\text{Mars}/G_\text{Maa}$, $g_\text{X} = g_\text{Maa}(x_\text{X}/m_\text{X})/(x/m)_\text{Maa}$, $m_\text{lisä} = F_\text{max}/g_\text{Mars} - m_\text{yht}$. All are correct, with no sign or power-of-ten slips.
- I evaluated each final form again with the task data: 6,0 cm, 7,0 N, 4,99 kg, 1,19 kN, 5,89 N, 6,81 N, 133 kg, 68,8 kg, 3,7 m/s², 3,59 m/s² and 60 N. These match the unchanged Sijoitus and answers.
- L1-09: the paragraph split changes no physics. The figure descriptions still match the option figures (G and F equal, F_k acts on the meter).
- Scope: the set uses only $G = mg$ and spring proportionality, with no Hooke's $k$ and no Newton's laws.
- The hash was the same at the start and the end.
