VERDICT: PASS
CONTENT-HASH: 2d5871271805ce79
SCOPE: delta numbers,reflow from c6b17c0a5ccb80ab base c48271b

## Blocking

## Polish

## Checked
- Delta round 1 (Formula steps simplified symbolically to the end): hash `2d5871271805ce79` identical at start and end.
- L3-04 Formula: $E = P_\text{h} t = R P^2 t / U^2$ and saving $= R P^2 t\,(1/U_\text{A}^2 - 1/U_\text{B}^2)\cdot\text{price}$ re-derived; algebra correct, and the starting laws $P = UI$, $P_\text{h} = RI^2$ still come before the combined form.
- L3-04 recomputed by script from the closed form: $R = 6.0\,\Omega$, $E_\text{A} = 43\,438\,\text{MWh}$, $E_\text{B} = 13\,140\,\text{MWh}$, saving $1.515 \cdot 10^{6}\,\text{€}$, the same as the substitution chain.
- L2-09 Formula: $R = P_\text{h}/I^2 = 0.030\,P/(P/U)^2 = 0.030\,U^2/P$ correct; $0.030 \cdot (200 \cdot 10^{3})^2 / (200 \cdot 10^{6}) = 6.0\,\Omega$ matches the answer and the curve in `loss-graph-curve` (which is drawn with $R = 6.0\,\Omega$).
- Substitution, answer, rounding, exercises.json and answers.py unchanged; the earlier recomputation stands.
