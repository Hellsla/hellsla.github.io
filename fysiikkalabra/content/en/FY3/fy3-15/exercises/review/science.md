VERDICT: PASS
CONTENT-HASH: beeed81ac87012b6

## Blocking

## Polish
- solutions.md fy3-15-L1-05 — "all powers are given to the nearest megawatt" is not quite right, since $75.0\,\text{MW}$ is given to $0.1\,\text{MW}$. The three figures still hold — fix: say "the sum $225\,\text{MW}$ and $250\,\text{MW}$ have three figures".
- solutions.md fy3-15-L3-05 — the heading "Reading the graph" introduces a table, not a graph — fix: "Reading the table".
- solutions.md fy3-15-L1-09 — the answer is given as $13\,\text{MW}$ (2 s.f.), but the substitution row ends at $13.4\,\text{MW}$. Both are inside the $4\,\%$ tolerance — fix: end the row at $13\,382\,\text{kW} \approx 13\,\text{MW}$ so the two lines agree.
- exercises.json fy3-15-L1-01 — "kinetic energy of the water": what a hydro turbine mostly uses is the water's head (pressure/potential energy). This is a C simplification for FY3 (no $E_p$), so it is left as it is — optional: "energy of the flowing water".

## Checked
- I recomputed all 21 numeric answers with my own formulas in one script, independently of answers.py. All agree with answers.py and exercises.json and fall inside their tolerances.
- L2-08 distractors recomputed: $0.50$, $50.3$, $503$ and $14\,600\,\text{MW}$. Each one comes from the error its feedback names, and only $500\,\text{MW}$ is marked correct.
- L1-06: exactly one correct option, and each feedback is physically right. Electrical efficiency, total efficiency and recovered heat are kept apart, as the guardrail asks.
- L2-05 totals for 2021 and 2022 ($84.6\,\%$, $88.4\,\%$), L3-01 limits ($40\,\%$ and $88\,\%$) and $\eta_\text{tot} = 67.6\,\%$, and L3-04 saving $28\,\%$ all recomputed.
- L3-03 calls the heat pump's figure a coefficient of performance, not an efficiency (guardrail). The comparisons give $263\,\text{kWh}$ (direct electric) and $111\,\text{kWh}$ (oil), both correct.
- L3-05 condenser heat $1716\,\text{MW}$ against waste heat $1800\,\text{MW}$ ($95\,\%$): consistent, and the remainder is explained physically.
- Figure chain-bars: the bars are on 50 MW gridlines except $P_3 = 140\,\text{MW}$, which no answer needs. Its description gives the same values and does not state any answer.
- Every chain is solved symbolically before substitution. The products of efficiencies are justified by power passed on stage to stage.
- Scope: efficiency, energy chain, $Q = cm\Delta T$ and power. All inside FY3, with nothing from FY4.
- The exercise brief in the packet was empty, so notation was compared only within the set itself, where it is consistent ($P_\text{o}$, $P_\text{s}$, $P_\text{k}$, $P_\text{h}$, $\eta_\text{tot}$).
