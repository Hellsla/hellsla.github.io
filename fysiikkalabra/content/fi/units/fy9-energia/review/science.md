VERDICT: PASS
CONTENT-HASH: e297d1ba1b8c1dd6
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 90beeadb37d7835e.

## Blocking
(none)

## Polish
- s1 d Periaate writes the line as $E = E_0 + kT$, while c writes $E = E_0 + k(T-T_0)$. This is correct because $T_0 = 0\,{}^\circ\text{C}$, but it could say so ("koska $T_0 = 0\,{}^\circ\text{C}$").

## Checked
- s1 c: $E = E_0 + k(T - T_0)$ with $(0\,{}^\circ\text{C}; 93\,\text{kWh})$ gives 230.2 kWh, so 230 kWh. d: $T = (E_\text{muu}-E_0)/k = 16.5\,{}^\circ\text{C}$.
- s2 a: $P_\text{ka} = kNP_\text{nim} = 0.60$ MW, 5.26 GWh a year, battery 1.7 h.
Every number in the changed lines was recomputed with an independent script (scratchpad fy9merge/sci_fi.py); `units.py hash` gave the same value at the start and the end. LaTeX in all added lines has balanced `$` and braces.
