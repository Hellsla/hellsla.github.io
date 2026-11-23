VERDICT: PASS
CONTENT-HASH: 582d44321836547e
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from a72da2feb382aa9f base 5b3ca4f

## Blocking

## Polish

## Checked
- The hash `--exercises --lang en` was 582d44321836547e both at the start and at the end.
- I recomputed all 20 numeric answers. All are within tolerance of answers.py and exercises.json. My own values:
  - L1-04: $21.1/79.9 = 26.4\,\%$
  - L2-01: $0.32 \cdot 25 \cdot 8760 = 70.08\,\text{GWh}$
  - L2-04: $1.6 \cdot 10^{6} \cdot 8760 / 5000 = 2.80$ million
  - L2-05: $25.0 - 2.21 = 22.8$ points
  - L2-07: $808 \cdot 2.0 \cdot 10^{9}\,\text{g} = 1.616$ Mt
  - L3-01: $11 - 3.5 - 0.36 = 7.14\,\text{GW}$
  - L3-02: $0.90/0.33 = 2.73$
  - L3-03: $0.90 \cdot 1600 / 0.11 = 13.1\,\text{GW}$
  - L3-04: wind share $20.4 \cdot 24 / 168 / 9.0 = 0.32$
  - L3-05: $16.6$ and $10.6$ €/MWh
- The rewritten Formula lines start from $E = Pt$, from share = part/whole, from $m = kE$ or from the power balance $P_\text{cons} = P_\text{nuc} + P_\text{wind} + P_\text{other}$. Each is reduced symbolically and correctly to the form that is substituted.
- L3-02 and L3-03: $E = o\,P_\text{rated}\,t$ gives the ratio $o_\text{nuc}/o_\text{wind}$ because the rated power and the time cancel. The solar-park equality $o_\text{a}P_\text{a}t = o_\text{O}P_\text{O}t$ is also right.
- L2-07: $\Delta m = (k_\text{coal} - k_\text{wind})E$ follows from $m = kE$ for the same energy.
- L3-04: the balance equation also covers Sunday's negative $P_\text{other}$ (export or surplus), and the answer says so.
- L1-06, L1-07, L1-09, L2-05, L3-03 and L3-05: only paragraph splits; claims and numbers are unchanged. Wind is renewable but weather-dependent, hydro is regulating power and nuclear is base load, as the glossary has it.
- Scope: production methods and $E = Pt$ orders of magnitude, inside FY2. The diff introduces no guardrail break (A or B).
