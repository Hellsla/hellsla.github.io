VERDICT: PASS
CONTENT-HASH: 1044d5e0eb32dd28

## Blocking

## Polish
- solutions.md (fy3-3-L2-08, Formula): $p_0$ here is the intercept at $0\,{}^\circ\text{C}$, but in L3-05 $p_0$ is the atmospheric pressure. The two tasks are separate, but $p_{0\,{}^\circ\text{C}}$ or $p_1$ (as in L2-02) would avoid the clash.

## Checked
- The diff changes only the Formula steps and splits paragraphs. I compared the non-Formula text with whitespace removed: it is identical before and after.
- The Kelvin–Celsius conversion is written with numerical values, $T/\text{K} = \theta/{}^\circ\text{C} + 273.15$, and is solved correctly for $\theta$ (L1-02, L1-03, L1-05, L2-01). In L1-04 the derivation $\Delta T = \Delta\theta$ cancels 273.15 correctly.
- L3-01 and L3-02: $p_2/p_1 = T_2/T_1$ is solved for $p_2$ and for $T_2$. Its conditions (constant volume and amount of gas) are stated in each principle.
- L3-03: $E_2/E_1 = T_2/T_1$ for the mean kinetic energy uses kelvins, which is correct.
- L3-05: the total pressure $p = p_\text{g} + p_0$ is used in the proportionality, and the relative change $\Delta E_\text{k}/E_\text{k,1} = (T_2 - T_1)/T_1$ is right.
- L2-02 and L2-04: the linear model and the temperature ratio are derived symbolically to their final forms.
- Recomputed: L3-05 $\theta_3 = 145.46\,{}^\circ\text{C}$, L2-04 ratio $3.9955$. Both match.
- The hash was the same at the start and the end.
