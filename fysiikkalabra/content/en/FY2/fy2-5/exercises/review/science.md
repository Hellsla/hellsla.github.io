VERDICT: FAIL
CONTENT-HASH: 020a2d39a5af90ba

## Blocking
- content/en/FY2/fy2-5/exercises/solutions.md:269 (fy2-5-L2-09) — The new Formula line calls $E_\text{w} = E_\text{p}$ "conservation of energy". That is the wrong principle (kind A). The task asks how much firewood releases the same energy as $12\,\text{kg}$ of petrol, so the equality is the condition the task sets, as the Principle line itself says ("The energies must be equal"). Two separate burnings are not one system whose energy is conserved. Calling it conservation teaches that different fuels "conserve" to equal energies. — Write: "$E = Hm$ for each fuel, and the same energy is required from both, $E_\text{w} = E_\text{p}$, so …". The Finnish source has the same wording ("energian säilyminen $E_\text{p} = E_\text{b}$"), and its reviewer should get the same fix.

## Polish

## Checked
- The hash `--exercises --lang en` was 020a2d39a5af90ba at the start and at the end.
- I recomputed all 20 numeric answers. answers.py and exercises.json agree within tolerance. My own values:
  - L2-01: $1.2\,\text{MJ} \cdot 0.040/0.100 = 480\,\text{kJ}$
  - L2-03: $0.85 \cdot 17 \cdot 40 = 578\,\text{MJ}$
  - L2-04: $48 : (0.25 \cdot 43) = 4.47\,\text{kg}$
  - L3-01: $120/15 - 120/40.6 = 5.04\,\text{kg}$
  - L3-02: $3.6$
  - L3-03: $35\,\text{MW}$
  - L2-05: $5.63\,\text{kg}$
  - L2-07: $18.4\,\text{kW}$
  - L3-04: $3313\,\text{kg}$
  - L3-05: $937\,\text{kg}$
  - L2-09: $34.4\,\text{kg}$
  - L2-06: $78\,000\,\text{MJ}$
- The other rewritten Formula lines are right. Each starts from $\eta = E_\text{useful}/E_\text{in}$, $E_\text{in} = Hm$ or $P = E/t$ and reduces symbolically to the final form ($\eta Hm$, $E_\text{useful}/(\eta H)$, $\eta Hm/t$, $E(1/H_1 - 1/H_2)$) before substituting.
- L2-01: $e = E_\text{label}/m_\text{label}$ keeps the guardrail distinction. A food label gives the energy the body can use, not a heat of combustion, and the Principle line still says so.
- L2-05 and L3-01: $\Delta m = E(1/H_{40} - 1/H_{20})$ has the right sign (a smaller $H$ needs a larger mass). Its substitution shows both masses.
- L3-04 and L3-05: the substitutions now go straight into $m = E_\text{useful}/(\eta H)$. The values are unchanged: 3313, 1310, 4024 and 710 kg; 3429, 2491, 985, 938 and 2824 kg.
- exercises.json: only the "esimerkkiaineisto" marker was removed from captions, with the teacher's approval of 2026-11-15/16. No number changed.
- fy2-5/lampoarvot: the bar values agree with the heats of combustion that L1-09 and L2-09 use (43, 15, 26, 10).
- Apart from the item above, the diff introduces no other guardrail break.
