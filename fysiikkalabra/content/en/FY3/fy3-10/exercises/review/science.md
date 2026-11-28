VERDICT: PASS
CONTENT-HASH: d779c3fd22d3a1e2

## Blocking

## Polish
- solutions.md:206 (helium cylinder and balloons, Formula): part c) also computes the balloons still available, $(n_3 - n_\text{end})/n_\text{b}$, but the chain does not show it. Fix: add the rows $n_\text{end} = p_\text{b}V/(RT_3)$ and $N' = (n_3 - n_\text{end})/n_\text{b}$.

## Checked
- The Round 1 Blocking item is fixed. The balloon chain now uses $n_\text{b} = p_\text{b}V_\text{b}/(RT_\text{b})$ and $N = \Delta n/n_\text{b}$, the same symbols as the Given, Conversions and Substitution. No $\text{p}$-subscript symbol is left in the file.
- Every changed Formula step is an aligned block that starts from $pV = nRT$ (or $M = m/n$) and solves symbolically to the form the Substitution uses.
- Combined gas law (diesel, $V_2$): derived from two equations of state with $n$ and $R$ constant. The results are $555\,{}^\circ\text{C}$ and $2.31\,\textsf{l}$.
- The molar mass $27.9\,\text{g/mol}$ is correct. Argon window: $d = \Delta m\,RT/(pA(M_\text{Ar} - M_\text{air}))$, which is correct.
- Leaking tyre $5.47\,\%$, cylinder refill $0.719\,\text{kg}$ and the $(T, V)$ series $n = kp/R = 4.95\,\text{mmol}$ are all correct.
- Isochores: $n_\text{A} - n_\text{B} = 0.0241\,\text{mol}$ and $n_\text{A}/n_\text{B} = p_\text{A}/p_\text{B}$ are correct.
- Helium recomputed: $n_1 = 12.29\,\text{mol}$, $n_3 = 5.318\,\text{mol}$, $m = 27.9\,\text{g}$, $33.7$ balloons used and $21.7$ still available. Each matches.
- Weather balloon: $105.4\,\text{mol}$, $7.38\,\text{m}^3$, $15.69\,\text{m}^3$ and $12.8\,\text{km}$ match. The argon cylinder's $3.05\,\text{MPa}$ matches.
- The hash was the same at the start and the end.
