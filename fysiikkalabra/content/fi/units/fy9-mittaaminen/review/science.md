VERDICT: PASS
CONTENT-HASH: bdef44d88ed5bb2a

Delta review (work queue 11c): the `hints` added to `sovella/tasks.json`, 32 parts (s1 a–s8 c). Each hint checked against its part's rubric, answer and `sovella/solutions.md`.

## Blocking
None.

## Polish
1. s4 b, hint 2 (fi): the hint calls $k$ a "kulmakerroin", but the slope only comes up in c, and it writes $m_\text{tod}$ where the solution has $m_\text{punnus}$ (c) or $m$ (b). Replacement: "… todellinen massa on lukema jaettuna suhteella $k$: $m = \dfrac{m_\text{lukema}}{k}$, missä punnuksilla $k = \dfrac{m_\text{lukema}}{m_\text{punnus}}$."
2. s5 c, hint 2 (fi): the symbol $c$ for the scale factor is new (the solution names no symbol) and can be confused with "c-kohta". This is not wrong. A possible replacement is "$c_\text{m}$" or no symbol at all.

## Checked
- Models and symbols match the solutions: $v = s/\bar t$ and $\Delta t$ as half the range (s1); $t_\text{mitattu} = t_\text{tod} + \tau_\text{p} - \tau_\text{k}$ (s1 d); $d = h/N$, $\sigma = M/(Nab)$, $\rho = \sigma/d$ (s2); $m = kV + b$, ±1 ml horizontal bars, $\Delta\rho = (k_\text{max}-k_\text{min})/2$ (s3); $m = m_\text{lukema}/k$ (s4); $x = x_0 + vt$, not forced through the origin (s5); $V = C/p - V_0$, $C = nRT$, MPa·ml = J, kelvins (s6); $F_\text{v} = kx$, ±0,2 cm, $\Delta x/x = \Delta k/k$ (s7); $s = \tfrac12 gt^2$, $g = 2\,\Delta s/\Delta(t^2)$, ±0,01 m (s8).
- Recomputed with my own script: s1 a 7,294 m/s / 26,26 km/h; s1 b relative-sum route 0,1230 against max–min 0,1230 m/s (the two routes the hint offers agree); s1 c Mira $13{,}96 \pm 0{,}16$ s; s2 31,19 m², 79,85 g/m², 783 kg/m³; s7 c 0,150 m, 4,2 %; s8 c 5,5 %, √(10,35/9,81) = 1,027. The values the hints state (13,52…13,90 s, 1000 m, 3600 s, 1000 µm, 80 g/m², 1000 kg/m³, 9,81 m/s²) agree with the task data.
- Direction claims: the hints on τ_k/τ_p signs, air resistance lowering $g$, leakage and heating in s6 d, and the zero crossing of the limit lines in s7 b agree with the rubric.
- No hint states a part's final answer. LaTeX and decimal commas are correct.
- Content hash: the same at the start and at the end.
