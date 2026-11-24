VERDICT: PASS
CONTENT-HASH: 561d3e679af9f6d9

## Blocking

## Polish
- solutions.md (fy3-8-L3-03, Formula): the block stops at $\Delta V_\text{over} = \Delta V_\text{petrol} - \Delta V_\text{can}$. A last row $= (\gamma_\text{petrol} - 3\alpha_\text{steel})V_0\Delta T$ would simplify it to the end, as L3-02 does.

## Checked
- The diff changes only the Formula steps. Its added lines ("Here $\Delta d = d - d_0$", "Here $\Delta T = T - T_0$", "$g_\text{limit}$ is…", "The area $A$ cancels") define the symbols those steps use.
- Each block starts from $\Delta l = \alpha l_0\Delta T$ or $\Delta V = \gamma V_0\Delta T$ and solves for the unknown in symbols. Checked: L2-01, L2-03, L2-04, L2-05, L2-06, L2-07 c), L3-01, L3-02 ($(\alpha_\text{Cu} - \alpha_\text{Fe})l_0\Delta T$) and L2-09.
- In L2-02, L3-03 and L3-05, $\gamma \approx 3\alpha$ is labelled as an approximation.
- L3-01: the hole widens like a linear dimension of the steel, which is correct.
- L3-04: the gap rules are right. The gap must be at least the summer extension, and the gap plus the winter contraction must not exceed $g_\text{limit}$.
- L3-05: $h = (\Delta V_\text{ethanol} - \Delta V_\text{bulb})/(\pi r^2)$ is correct, with the bulb's volume equal to $V_0$.
- L2-10 c): the column model $V_0 = Ah_0$, $\Delta V = A\Delta h$ gives $\Delta h = \gamma h_0\Delta T$. This is correct for a constant cross-section, which the task states.
- Recomputed: L3-03 $457\,\text{cm}^3$, L3-04 $18\,\text{mm}$, L3-05 $75.9\,\text{mm}$, L2-10 $60\,\text{mm}$. Each matches.
- The hash was the same at the start and the end.
