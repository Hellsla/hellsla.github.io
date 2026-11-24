VERDICT: FAIL
CONTENT-HASH: 0d8ceb3846b7e870

## Blocking
- solutions.md:274 (fy3-8-L3-04, Vastaus a) — A, safe-side rounding. "$g_\text{min} = 13{,}2\,\text{mm}$, käytännössä $13\,\text{mm}$" rounds a minimum ("rako ei saa sulkeutua") down. By the task's own model, a 13 mm gap closes at $T = 8\,{}^\circ\text{C} + 13/(0{,}30\,\text{mm/K}) \approx 51\,{}^\circ\text{C}$, which is below the summer maximum of $52\,{}^\circ\text{C}$. The guardrails (P7) and CLAUDE.md say a "vähintään" value is rounded up. The Finnish version has the same sentence (content/fi/FY3/fy3-8/exercises/solutions.md:277) — fix: write "käytännössä vähintään $14\,\text{mm}$" (two figures, rounded up), or drop "käytännössä 13 mm". The stored answer, 13,2 mm with 3 % tolerance, can stay. $g_\text{max} = 18\,\text{mm}$ (an "enintään" value, 18,0) is right.

## Polish
- solutions.md:263 (L3-04): the block writes $g_\text{max} = g_\text{raja} - \alpha l_0 \Delta T_\text{talvi}$. This holds only with $\Delta T_\text{talvi} = T_\text{as} - T_\text{min} > 0$; the Sijoitus uses $+40\,\text{K}$. State "$\Delta T_\text{talvi} = T_\text{as} - T_\text{min}$" under the block, as the block already does for $g_\text{raja}$.

## Checked
- I read every changed Kaava block on disk: L2-01, L2-02, L2-03, L2-04, L3-01, L3-02, L3-03, L2-05, L2-06, L2-07, L3-04, L3-05, L2-09 and L2-10. Each starts from $\Delta l = \alpha l_0\Delta T$ or $\Delta V = \gamma V_0\Delta T$ and solves in symbols.
- Rearrangements: L2-01 $l_0 = 52{,}08\,\text{m}$; L2-03 $\Delta T = 24\,\text{K}$, so $36\,{}^\circ\text{C}$; L2-04 $\alpha = 12 \cdot 10^{-6}\,\text{1/K}$ (steel); L2-06 $22{,}9 \cdot 10^{-6}\,\text{1/K}$ (aluminium). All correct.
- L2-02, L3-03 and L3-05: $\gamma \approx 3\alpha$ is used only for solids, and the condition is stated. L3-03: $475 - 18 = 457\,\text{cm}^3$. L3-05: $h = (22{,}0 - 0{,}54)\,\text{mm}^3/(\pi \cdot 0{,}30^2\,\text{mm}^2) = 75{,}9\,\text{mm}$. A container's inner volume expanding like the solid is correctly argued.
- L3-01: the hole expands like the material, $T = 20\,{}^\circ\text{C} + 100\,\text{K} = 120\,{}^\circ\text{C}$. The physics is correct.
- L3-02: $(\alpha_\text{Cu} - \alpha_\text{Fe})l_0\Delta T = 20\,\mu\text{m}$, and copper is on the convex side. Correct.
- L2-05: $\gamma = 0{,}00027/(1{,}00003 \cdot 6) = 45 \cdot 10^{-6}\,\text{1/K}$. The density maximum at $4\,{}^\circ\text{C}$ is correctly read.
- L2-07 c): $0{,}5\,\text{mm} \le 0{,}050\,\Delta l$ gives $\Delta l \ge 10\,\text{mm}$, so $l_0 \ge 10{,}4\,\text{m}$. L2-09: $k = 0{,}060\,\text{mm/K}$, so $T = 53{,}3\,{}^\circ\text{C}$. Both correct.
- L2-10 c): $A$ cancels, and $\Delta h = \gamma h_0\Delta T = 60\,\text{mm}$. The conditions (uniform warming, constant $\gamma$, constant area) are stated in the Periaate.
- The hash was the same at the start and the end.
