VERDICT: PASS
CONTENT-HASH: 47ef9f21a9aab27e
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography,wording from 6bfe5ddbe100df3b base e7c438cb69

## Blocking

## Polish

## Checked
- I ran the hash `--exercises --lang en` at the start and at the end. Both times it was 47ef9f21a9aab27e, the same as in the packet.
- The round-1 blocking item is fixed. In solutions.md:285 (L2-09), $E_\text{w} = E_\text{p}$ is now "the condition that both fuels release the same energy". It is no longer called conservation of energy, and it matches the Principle line.
- I recomputed 11 numeric answers from the task data in one script. All of them agree with answers.py and with exercises.json within tolerance:
  - L2-01: 480 kJ
  - L2-03: 578 MJ
  - L2-04: 4.47 kg
  - L3-01: 5.04 kg
  - L3-02: 3.6
  - L3-03: 35 MW
  - L2-05: 5.63 kg
  - L2-07: 18.4 kW
  - L3-04: 3313 kg
  - L3-05: 937 kg
  - L2-09: 34.4 kg
- Each rewritten Formula line starts from $\eta = E_\text{useful}/E_\text{in}$, $E_\text{in} = Hm$ or $P = E/t$. It reduces symbolically to the form that is substituted: $\eta Hm$, $E_\text{useful}/(\eta H)$, $\eta Hm/t$, $Hm/t$, $E(1/H_1 - 1/H_2)$ or $em/(12\,\text{MJ})$. The substitution then goes into that last form.
- Substitution rows of L2-05 and L3-01 (solutions.md:98–106 and 172–180): on disk they are aligned rows, one quantity per row. The run-together text in the packet diff is only how the diff shows them. The numbers are unchanged: 8.0, 2.96 and 5.04 kg; 19.23, 13.61 and 5.62 kg.
- L2-01: the food-label principle (the energy the body can use, not a heat of combustion) is kept.
- L3-04 and L3-05: the per-fuel masses are unchanged (3313, 1310 and 4024 kg; 3429, 2491, 985 and 2824 kg), and so are the differences 710 kg and 938 kg.
- No guardrail break (A or B). Efficiency stays below 100 %, and the scope is within FY2 ($E = Hm$ and the efficiency of one device).
