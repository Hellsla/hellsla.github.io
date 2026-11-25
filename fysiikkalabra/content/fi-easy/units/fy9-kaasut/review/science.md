VERDICT: PASS
CONTENT-HASH: 0ad61480ae1b2f96

Delta review (work queue 11c): only the new `hints` in `sovella/tasks.json` (fi-easy), diff against origin/main. Task texts, answers, rubrics and solutions are unchanged and were reviewed in full before.

## Blocking

None.

## Polish

1. s1 b, hint 3 (fi-easy, the same in fi): "Muunna tilavuus kuutiometreiksi ja paine pascaleiksi" names only one route, but the rubric's units_precision also accepts $\text{kPa} \cdot \textsf{l} = \text{J}$. This is optional. A possible replacement: "Muunna tilavuus kuutiometreiksi ja paine pascaleiksi. Voit myös käyttää sitä, että $1\,\text{kPa} \cdot 1\,\textsf{l} = 1\,\text{J}$. …" (rest unchanged).

## Shared issues

None.

## Checked

- 27 parts (s1–s9), each with three hints. Every relation agrees with its part's rubric and model solution, using the same symbols and conventions: $\Delta p\,A = mg$ (s1 a); $W = mgh = \Delta p\,\Delta V$ and the remainder going to pushing back the outside air (s1 b); $p_1V_\text{s} = p_2V_\text{s} + p_\text{c}\,\Delta V$ with absolute pressures (s1 c); $n = pV/(RT)$, $m = nM$, $P_0 = Hm/t$, $P_\text{s} = \eta_\text{s}P_0$ and $\eta_\text{kok}$ (s2); $V = V_0 + k\theta$, $\theta_0 = -V_0/k$, $k = nR/p$ and a systematic offset that changes $V_0$ but not $k$ (s3); $W = Q_1 - Q_2$, $P_1 = P_W + P_2$ and the heat pump's energy balance (s4); $\Delta n = \Delta p\,V/(RT)$, $M = \Delta m/\Delta n$ and $\Delta m = \tfrac{MV}{RT}\Delta p$ (s5); $F_\text{p} - mg = ma$, $N = F_\text{p}$, $F_{\mu0} \le \mu_0 N$ with the limiting case and the safety factor (s6); $P_2 = P_1 - P_\text{s}$, $Q_2 = P_2t$, $\Delta T = P_2t/(c\rho V)$, the upper-bound assumption and the second-law argument (s7); $p/T$ constant and the ratio method (s8); $W = p\,\Delta V$, $V/T$ constant and $Q = \Delta U + W$ (s9).
- Numbers the hints state, checked by script: $104\,\text{kPa} = 104\,000\,\text{Pa}$, $298{,}15\,\text{K}$, $0{,}0160\,\text{kg/mol}$, $3600\,\text{s}$, $1\,\text{ml} = 10^{-6}\,\text{m}^3$, $(-20 + 273{,}15)\,\text{K}$, $\pm 0{,}3\,\text{ml}$ and $75\,\%$. The answers recomputed from the hints' route: 562 kPa, 650 kPa, 34,9 kg, 1,64 mmol, 18,7 kPa, 63,3 kPa and 1173 K. All match.
- No hint states a part's final answer. The s9 c "moninkertaiseksi" check leaves the calculation to the student.
- Number formatting: all LaTeX, with a decimal comma.
- Hint by hint, fi-easy has the same physics as fi. Only the sentences are split, and no condition is dropped.
