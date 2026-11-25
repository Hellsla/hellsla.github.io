VERDICT: FAIL
CONTENT-HASH: cddfd08f0802bd10

Delta review (work queue 11c): the `hints` added to `sovella/tasks.json`, 32 parts. Each hint checked against its part's rubric, answer and `sovella/solutions.md`, and against the fi hints.

## Blocking
1. s1 d, hint 2 (en), symbol inconsistency (category 6). The hint names the delays $\tau_\text{k}$ and $\tau_\text{p}$, the Finnish subscripts. The en rubric criteria and the en model solution use $\tau_\text{start}$ and $\tau_\text{stop}$, so a student who follows the hint writes symbols that do not match the rubric and the model answer. Replacement: "Write the measured time using the true time and two delays: $\tau_\text{start}$ at the start and $\tau_\text{stop}$ at the stop. Which delay adds to the measured time and which one subtracts from it?"

## Polish
1. s4 b, hint 2 (en): the hint calls $k$ "the slope" before the slope comes up in c, and $m_\text{true}$ differs from the solution's $m_\text{weight}$. Replacement: "… the true mass is the reading divided by the ratio $k$: $m = \dfrac{m_\text{reading}}{k}$, where $k = \dfrac{m_\text{reading}}{m_\text{weight}}$ for the weights."
2. s5 c, hint 2 (en): the symbol $c$ for the scale factor can be confused with "part c". This is optional.

## Checked
- Apart from item 1, every hint says the same physics as fi, with the same models, symbols, signs and values. Checked: $\bar t$ and half-range $\Delta t$; $d = h/N$, $\sigma = M/(Nab)$, $\rho = \sigma/d$; $m = kV + b$ with ±1 ml bars; $x = x_0 + vt$; $V = C/p - V_0$ with $C = nRT$ and the conversion to J; $F_\text{v} = kx$ with ±0.2 cm; $g = 2\,\Delta s/\Delta(t^2)$ with ±0.01 m.
- Recomputed with my own script: s1 7.294 m/s and 26.26 km/h, Δv 0.123 m/s by both suggested routes; s2 31.19 m², 79.85 g/m², 783 kg/m³; s7 c 0.150 m; s8 c 5.5 %. These agree with the rubric.
- No hint states a final answer. LaTeX and decimal points are correct.
- Content hash: the same at the start and at the end.
