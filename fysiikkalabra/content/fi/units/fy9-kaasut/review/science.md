VERDICT: PASS
CONTENT-HASH: c4d5780e8f5b63b7

Delta review: only the new `hints` in `content/fi/units/fy9-kaasut/sovella/tasks.json` (git diff origin/main), language fi. 27 parts, 3 hints each.

## Blocking
None.

## Polish
1. s6 a, hint 3 (fi): the symbols are not the ones the solution uses: the solution writes $m = \rho\,l\,b\,h$, and in the same task $d$ is the cup's diameter. Replacement: "Laske ensin levyn massa tiheydestä ja mitoista, $m = \rho\,l\,b\,h$, ja muunna mitat metreiksi. Laikan pinta-ala saadaan sisähalkaisijasta $d$, joten käytä sädettä $d/2$, ei halkaisijaa."
2. s1 b, hint 2 (fi): "Kaasun paine-eron tekemä työ" is loose wording, because a pressure difference is not a gas. The solution says the work is done by the net force $\Delta p\,A$. Replacement: "Auton ja lavan saama työ on $W = mgh$. Mäntään vaikuttava nettovoima $\Delta p\,A$ tekee saman työn: $W = \Delta p\,A h = \Delta p\,\Delta V$, missä $\Delta V = Ah$ on sylinterin tilavuuden kasvu."
3. s3 a, hint 3 (fi): the hint is correct and matches the solution, where the vertical axis starts at $36\,\text{ml}$. But b needs a second graph whose axes start at zero, so the line can be extended to $V = 0$. Suggest adding: "b-kohtaa varten tarvitset toisen kuvaajan, jossa akselit ulottuvat nollaan."

## Checked
- One script recomputed every number a hint states or leads to, from the task data with my own formulas:
  - s1: 562 kPa; 21.19 kJ (both ways); air work 25.0 kJ; gauge 650 kPa.
  - s2: 34.9 kg; 174.5 kW; 84 %.
  - s3 c: 1.645 mmol.
  - s4: 6.0 %; 470 kW; 25 kW from the sea; ratio 3.5.
  - s5 a: 25.46 g/mol.
  - s6: 11.21 kPa; 18.69 kPa; safety factor 1.6 < 2.
  - s7: 37.2 %; 64.8 GWh; 11.3 K.
  - s8 c: 63.3 kPa.
  - s9: 750 J; 0.1026 mol; 1172.6 K.

  All agree with answers.py and the solutions.
- The conversions stated in the hints are correct: 298.15 K, 104 000 Pa, 0.0160 kg/mol, 3600 s, $(-20 + 273{,}15)\,\text{K}$, 1 ml = $10^{-6}\,\text{m}^3$.
- Models, symbols and sign conventions match the solutions:
  - s1 c: total pressures and $p_\text{c}$.
  - s3 b: $\theta_0 = -V_0/k$ and the steepest and shallowest lines.
  - s6 a: $F_\text{p} - mg = ma$ with zero rim force at the limit.
  - s6 b: $N = F_\text{p}$ and $F_{\mu 0} \le \mu_0 N$.
  - s7 b: the significant-figure reason.
  - s7 d and e: the Kelvin comparison and the district-heating temperature argument, as in the rubric.
  - s9 d: $Q = \Delta U + W$.
- No hint states a part's final answer. Evaluation parts (s4 a, s5 b, s6 c, s7 e, s3 d) guide the reasoning without giving the conclusion.
- Hints that ask for comparisons point the way the rubric does: s2 c heat rejection, s4 b $\Delta T / T_1$, s5 c the $(\Delta p, \Delta m)$ slope $MV/(RT)$.
- Every number with a unit is LaTeX and uses a decimal comma. No decimal points found.
