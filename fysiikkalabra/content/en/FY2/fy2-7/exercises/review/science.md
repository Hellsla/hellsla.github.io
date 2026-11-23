VERDICT: FAIL
CONTENT-HASH: 5ecba3d8a8b1b63d

## Blocking
- content/en/FY2/fy2-7/exercises/solutions.md:169 (fy2-7-L3-02) — The rewritten Substitution uses the Finnish symbols $E_\text{perille,A}$ and $E_\text{perille,B}$. The Formula line two lines above, and the rest of the English set, call the same quantities $E_\text{arrived,A}$ and $E_\text{arrived,B}$. So one solution now names one quantity with two symbols, and the English text never defines the Finnish ones. This breaks the notation rule (internal consistency, item 6). — Write $E_\text{arrived,A}$ and $E_\text{arrived,B}$ in the Substitution.

## Polish
- solutions.md:157–159 (fy2-7-L3-01): the three substitution rows are on consecutive source lines with no separator, which Markdown may join into one paragraph ("… 659.3 MWh $E_\text{sent,2}$ = …"). The physics is right; the visual reviewer should check the rendering.

## Checked
- I ran the hash `--exercises --lang en` at the start and at the end. Both times it was 5ecba3d8a8b1b63d.
- I recomputed all 21 numeric answers. answers.py and exercises.json agree within tolerance. My own values:
  - L1-02: $0.09 \cdot 360 = 32.4\,\text{MWh}$
  - L1-04: $0.960 \cdot 125 = 120\,\text{MW}$
  - L2-01: $600/0.80 - 600 = 150\,\text{MWh}$
  - L2-03: $0.040 \cdot 2.4 \cdot 10^{6} / 8760 = 10.96\,\text{MW}$
  - L2-04: $40.0 \cdot 24 / 0.80 = 1200\,\text{kWh}$
  - L3-01: $600(1/0.91 - 1/0.94) = 21.0\,\text{MWh}$
  - L3-02: $455.0 - 442.0 = 13.0\,\text{MWh}$
  - L3-03: $65.7$ houses
  - L1-07: $4.8\,\%$
  - L1-08: $72\,\text{kW}$
  - L2-05: $9.62\,\%$
  - L2-06: $0.0625\,\text{MW}$
  - L3-04: $6.59\,\text{MWh}$
  - L1-09: $72\,\text{MJ}$
  - L2-09: $12.5\,\text{MWh}$
  - L3-05: energy-weighted loss share $4.14\,\%$
- The rewritten Formula lines start from $E_\text{sent} = E_\text{arrived} + E_\text{loss}$, from $\eta = E_\text{arrived}/E_\text{sent}$, from $p = E_\text{loss}/E_\text{sent}$ or from $P = E/t$. Each reduces symbolically and correctly to the form that is substituted: $E_\text{arrived}/\eta - E_\text{arrived}$, $pE_\text{sent}/t$, $P_\text{arrived}t/\eta$, $E_\text{arrived}(1/\eta_1 - 1/\eta_2)$, $rP_\text{loss}t/\eta$ and $(p_\text{dh} - p_\text{el})E_\text{in}$.
- Every loss share is taken of the sent energy, as the lesson model requires.
- The P1 wording is kept in L2-08 and L2-07: electrical energy becomes internal energy of the conductors, which is transferred to the surroundings as heat.
- fy2-7/sankey (a picture the teacher approved): the 96/4 % and 91/9 % shares agree with L1-02 and L2-09, and the widths are to scale.
- The paragraph splits in L2-08, L1-06, L2-05, L2-06, L2-07, L3-04, L3-05 and L2-10 leave the claims and numbers unchanged.
- No guardrail break (A or B) apart from the item above.
