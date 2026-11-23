VERDICT: PASS
CONTENT-HASH: 0847076788133655
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 0f91b2baf35388df base 08d90eab0b

## Blocking

## Polish

## Checked
- I ran the hash `--exercises --lang en` at the start and at the end. Both times it was 0847076788133655, the same as in the packet.
- The round-1 blocking item is fixed. The Substitution of L3-02 (solutions.md:173) now uses $E_\text{arrived,A}$ and $E_\text{arrived,B}$, as its Formula line does. No Finnish symbols are left in the English set.
- The round-1 Polish item is fixed. The substitution of L3-01 is now one aligned chain (solutions.md:157–) that starts from $\Delta E$.
- I recomputed 15 numeric answers from the task data in one script. All of them agree with answers.py and with exercises.json within tolerance:
  - L1-02: 32.4 MWh
  - L1-04: 120 MW
  - L2-01: 150 MWh
  - L2-03: 10.96 MW
  - L2-04: 1200 kWh
  - L3-01: 21.0 MWh
  - L3-02: 13.0 MWh
  - L3-03: 65.7
  - L1-07: 4.8 %
  - L1-08: 72 kW
  - L3-04: 6.59 MWh
  - L1-09: 72 MJ
  - L2-09: 12.5 MWh
  - L2-06: 0.0625 MW
  - L2-10: 11.6 GWh
- Each rewritten Formula line starts from the basic relation and reduces symbolically to the substituted form. The relations are $E_\text{sent} = E_\text{arrived} + E_\text{loss}$, $\eta = E_\text{arrived}/E_\text{sent}$, $p = E_\text{loss}/E_\text{sent}$ and $P = E/t$. The substituted forms are $pE_\text{sent}/t$, $P_\text{arrived}t/\eta$, $E_\text{arrived}(1/\eta_1 - 1/\eta_2)$, $rP_\text{loss}t/\eta$ and $(p_\text{dh} - p_\text{el})E_\text{in}$.
- Every loss share is still taken of the sent energy.
- The P1 wording is kept: electrical energy becomes internal energy of the conductors, which is transferred to the surroundings as heat.
- fy2-7/sankey (the teacher-approved picture): 96/4 % and 91/9 %, which agrees with L1-02 and L2-09.
- The paragraph splits leave the claims and the numbers unchanged. No guardrail break (A or B).
