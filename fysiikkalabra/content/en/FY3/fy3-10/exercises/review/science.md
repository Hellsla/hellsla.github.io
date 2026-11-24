VERDICT: FAIL
CONTENT-HASH: 00e765f40c13f50c

## Blocking
- solutions.md:234 (the helium cylinder and balloons task, Formula) — category A, internal consistency. The new Formula chain writes the balloon quantities as $n_\text{p}$, $p_\text{p}$, $V_\text{p}$ and $T_\text{p}$, which is the Finnish subscript for *pallo*. The Given (line 227), the Conversions (line 235) and the Substitution (line 236) of the same solution use $p_\text{b}$, $V_\text{b}$, $T_\text{b}$ and $n_\text{b}$. In the English version, $p_\text{p}$ also reads like "pressure p" twice, so the chain does not visibly say that it is the balloon's quantity. The student cannot match the symbolic result with the substitution. — Fix: in the English Formula, write `n_\text{b} = \dfrac{p_\text{b}V_\text{b}}{RT_\text{b}}` and `N = \dfrac{\Delta n}{n_\text{b}}`.

## Polish
- solutions.md:234 — part c) also computes the balloons still available, $(n_3 - n_\text{end})/n_\text{b}$, and the Formula chain does not show it (it was missing in the passed version too). — Fix: add the rows $n_\text{end} = p_\text{b}V/(RT_3)$ and $N' = (n_3 - n_\text{end})/n_\text{b}$.

## Checked
- Diff: only the Formula steps changed, and each now starts from $pV = nRT$ (or $M = m/n$) and solves symbolically. Every final form equals the expression the unchanged Substitution uses.
- Combined gas law (diesel task, the $V_2$ task): the chain from $p_1V_1 = nRT_1$ and $p_2V_2 = nRT_2$ to the ratio form is correct ($n$ and $R$ constant). The answers recompute to 555 °C and 2.31 l.
- Molar mass task: $pV = (m/M)RT$ gives $M = mRT/(pV) = 27.9$ g/mol. This is correct.
- Argon window task: the chain $pAd = nRT$ gives $d = \Delta m\,RT/(pA(M_\text{Ar} - M_\text{air}))$. This is correct.
- Leaking tyre: $n_2/n_1 = p_2T_1/(p_1T_2)$, and the leaked share $1 - n_2/n_1 = 5.47$ %. This is correct.
- Cylinder refill: $\Delta p\,V = \Delta n\,RT$ holds at constant $V$ and $T$, giving $\Delta m = 0.719$ kg.
- $(T, V)$ series: $V = (nR/p)\,T$, so $k = nR/p$ and $n = kp/R = 4.95$ mmol.
- Isochore graphs: $n_\text{A} - n_\text{B}$ = 0.0241 mol, and the ratio $n_\text{A}/n_\text{B} = p_\text{A}/p_\text{B}$ is derived correctly.
- Weather balloon: $n = 105.4$ mol, $V_{10} = 7.38$ m³, $V_{15} = 15.69$ m³, $h = 12.8$ km. These match.
- I recomputed every changed solution in one script, and all match. The hash is identical at start and end.
