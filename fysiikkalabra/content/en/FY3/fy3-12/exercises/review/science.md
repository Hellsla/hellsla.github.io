VERDICT: PASS
CONTENT-HASH: 771588436413fa23

## Blocking

## Polish
- solutions.md fy3-12-L3-02 Formula — the number of years enters as a bare factor 10 ($Q = 10fE_\text{v}$), so the symbolic chain is not fully symbolic. — Optional fix: write $Q = N f E_\text{v}$ with $N = 10$ (years in the Given).

## Checked
- Diff: only Formula steps changed. Each now starts from its basic law ($P = UA\Delta T$, $Q = cm\Delta T$, $Q = Pt$, $E = Pt$, the balance $P_\text{abs} = P_\text{in} - P_\text{refl}$, $\varepsilon = Q/W$) and ends in the form the unchanged Substitution uses.
- L2-01: the two parallel losses are combined as $(U_\text{s}A_\text{s} + U_\text{y}A_\text{y})\Delta T$ and solved for $T_\text{out}$ = −20 °C. This is correct.
- L2-03, L3-03: the difference of two losses is factored as $(U_1 - U_2)A\Delta T\,t$, then $W = Q/\varepsilon$. The results are 212 kWh and 984 kWh.
- L2-04, L3-04: the absorbed fraction is $(1 - r)$ (or $1 - a$), so the change is $(r_1 - r_2)P_\text{in}$ and $I\,\Delta A\,(a_\text{ice} - a_\text{sea})$. The signs are right: losing ice increases absorption. The results are 3.4 W/m² and 0.343 W/m².
- L3-05 (one-layer greenhouse): the top-of-atmosphere balance $(1 - f)S + fS/2 = P_\text{abs}$ gives $S = P_\text{abs}/(1 - f/2)$. With $f = 0.80$, the denominator is 0.60, which matches the Substitution's "1 − 0.40". The surface check $S = 239 + fS/2$ gives the same $S$ = 398.3 W/m², and T = 16.3 °C.
- L3-01, L3-02: equating $cm\Delta T = Pt$ is valid without a change of state, which the Principle states. ΔT = 20.0 K and 0.139 K.
- L2-05: the lid power is from $cm(T_\text{B} - T_\text{A})/t$ = 6.98 W.
- L2-07: the slope $k = UA$ gives U = 0.35 W/(m²·K).
- L1-09: $U = \lambda/d$, so P = 210 W.
- I recomputed every changed solution in one script, and all match. The hash is identical at start and end.
