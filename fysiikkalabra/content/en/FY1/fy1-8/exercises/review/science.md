VERDICT: PASS
CONTENT-HASH: a9ca591a0e693d7d

## Blocking
- none

## Polish
- content/en/FY1/fy1-8/exercises/solutions.md:225 — in fy1-8-L3-05 one aligned block uses $\Delta T$ for the temperature change and $\Delta T_\text{fall}$ for the uncertainty of the fall — consider a different symbol for the uncertainty (for example $\delta T_\text{fall}$). The symbols are defined, so this is not an error.

## Checked
- The packet's diff flattens the aligned blocks. I read the real rows in solutions.md: 25, 55, 65, 75, 95, 105, 115, 157, 185, 201, 225 and 241. Each one starts from its basic equation and every rearrangement is valid algebra.
- L3-02 (:105) and L3-05 (:225) now have $r = -\Delta T/\Delta t$. With $\Delta T = T_\text{end} - T_\text{start}$ this equals the next row exactly. The round-1 Blocking item (A) is fixed, and the Finnish rows (:105, :187) have the same fix.
- I recomputed in my own script: $0.417\,\text{m/s}$; $2.5\,\%$; $10\,\%$; $0.42\,\text{m/s}$; $0.033\,\text{m/s}$; $r_1 = 2.4$, $r_2 = 1.0$ and $\Delta r = 1.4\,\text{K/min}$; $n = 4.0$; $k = 3.75$, about 3.8; $r = 2.0\,\text{K/min}$, $T_\text{fall} \ge 20\,\text{K}$ and $t = 10\,\text{min}$. All of them match the Substitution and Answer lines.
- The other changes in the diff only split paragraphs, in L1-06, L1-07, L1-09, L2-05, L2-06, L2-07, L3-04 and L3-05. No claim, number, sign or unit changed in them.
- In L3-04 the split puts every sentence of the old text in a paragraph of its own. The physics is unchanged: intervals overlap, so a difference cannot be shown, and that is no proof that there is no effect.
- The pictures and figures in the diff are approved by the teacher. Their content is not changed.
- answers.py, the answers, units and tolerances are unchanged.
- The hash was a9ca591a0e693d7d at the start and at the end.
