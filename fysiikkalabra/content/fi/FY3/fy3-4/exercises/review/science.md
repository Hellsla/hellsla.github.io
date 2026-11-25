VERDICT: PASS
CONTENT-HASH: 193be784ebdb32a8

## Blocking

## Polish
- solutions.md:249 (dam task, part c): the Kaava stops at $\dfrac{0 + \rho g H}{2} \cdot H w$. One more row would simplify it to $F_\text{kok} = \tfrac12 \rho g H^2 w$ before the Sijoitus. The result does not change.

## Checked
- All 11 changed Kaava blocks are correct, with the right law for each situation:
  - $h = \Delta p/(\rho g)$ for the water tower
  - $F = \Delta p A$ for the lid
  - $A = m g/p_\text{max}$ for the snowshoe
  - $\Delta F = \rho g h A$ for the barrel and hose
  - $\Delta p = \rho_1 g h_1 + \rho_2 g h_2$ for the layered well
  - $\rho = k/g$ and $p_0 = p_\text{ka} - k h_\text{ka}$ for the fitted line
  - $\Delta p_\text{a} = g\sum\rho_i d_i$ and $\delta h = h - \Delta p_\text{a}/(\rho g)$ for the lake layers
  - $p_\text{ka} = \rho g(h_1+h_2)/2$ and $F = p_\text{ka}A$ for the dam strips
  - $\rho_\text{B} = k_\text{B}/g$ for liquid B
- The two-liquid comparison now writes $p_\text{A} = p_\text{B}$ first. $p_0$ cancels, and $h_\text{A} = (k_\text{B}/k_\text{A}) h_\text{B}$ is right.
- Each block starts from $p = F/A$ or $p = p_0 + \rho g h$ (the lesson's two laws) and simplifies symbolically. Every last form is the one the Sijoitus evaluates.
- I evaluated each final form again with the task data:
  - water tower 35,7 m, two liquids 6,0 m, lid 3,23 kN, snowshoe 0,139 m², barrel 9,81 kN, well 19,0 kPa
  - fitted line $\rho$ = 997 kg/m³
  - lake layers $\Delta p_\text{a}$ = 196,08 kPa and $\delta p$ = 118 Pa
  - dam strips $F_1$ = 122,6 kN
  - $\rho_\text{B}$ = 1529 kg/m³
  - All match the unchanged Sijoitus.
- Units and powers of ten in the unchanged Muunnokset still hold (bar → Pa, cm² → m², kPa/m → N/m³).
- Overpressure versus total pressure is kept apart everywhere. Air pressure cancels on the lid and the dam, as each Periaate says.
- Only Kaava lines changed. No number, answer or tolerance changed.
- The hash was the same at the start and the end.
