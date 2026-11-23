VERDICT: PASS
CONTENT-HASH: ab1a8e6751c19379
SCOPE: delta md-paragraphs,numbers,typography from 09e49c1d1adb4b79 base 5b3ca4f

## Blocking

## Polish

## Checked
- The hash `--exercises --lang en` was ab1a8e6751c19379 at the start and at the end.
- I recomputed all 22 numeric answers. answers.py and exercises.json agree within tolerance. My own values:
  - L1-04: $490/41 = 11.95$
  - L2-04: $69 \cdot 3.6 = 248.4\,\text{g/kWh}$
  - L3-01: $69 \cdot 6.0 \cdot 32 / 18 = 736\,\text{g/kWh}$
  - L3-02: $0.50/0.010 = 50$
  - L3-03: $13\,248 \cdot 25 / 79\,920 = 4.14$
  - L1-09: $55 \cdot 47 \cdot 2.0 = 5.17\,\text{kg}$
  - L2-09: $(820 - 490) \cdot 20\,000\,\text{g} = 6.6\,\text{t}$
  - L2-05: $34/15 = 2.27\,\text{ppm/a}$
  - L3-04: $414 + 2.2 \cdot 20 = 458\,\text{ppm}$
  - L3-05: $52.22\,\text{kt}$ to $24.68\,\text{kt}$, $-52.7\,\%$
  - L2-10: $588.6 \cdot 5.0 = 2.94\,\text{kg}$, ratio $16.7$
  - L3-06: $-76.7\,\%$
  - L2-11: $150\,\text{g}$
- The rewritten Formula lines start from $m = eE$ (with $E = Vh$ or $E = Hm$ where fuel is involved) and are reduced symbolically and correctly:
  - L1-04: ratio $e_2/e_1$ (same $E$ cancels)
  - L2-01 and L2-09: $(e_1 - e_2)E$
  - L3-01: $e = e_\text{p}Vh/E$ from equal emissions
  - L3-03: $e_\text{c}V_\text{c}h_\text{c}N/(e_\text{b}V_\text{b}h_\text{b})$
  - L1-09: $m_\text{CO2} = eHm$
- L2-04: deriving $e_\text{kWh} = e_\text{MJ} \cdot 3.6\,\text{MJ/kWh}$ from $m = e_\text{MJ}E_\text{MJ}$ is right. The Reasonableness line still separates fuel-energy factors from the lifecycle factors of electricity.
- L3-02: area ratio $q_\text{a}/q_\text{b}$, because the same energy cancels.
- L1-06: the greenhouse mechanism is unchanged and right (solar radiation passes, outgoing thermal radiation is slowed; $+15\,{}^\circ\text{C}$ vs $-18\,{}^\circ\text{C}$, 33 K). It matches the teacher's worksheet wording.
- L2-08: the uncertainty reasoning follows the guardrail (overlapping intervals mean a difference cannot be shown).
- L3-04: the conclusion on the limits of extrapolation follows the guardrail.
- The rest of the diff is paragraph splits only (L2-05, L1-10, L3-04, L3-05, L2-08, L2-10, L2-11, L3-06); numbers and claims are unchanged.
- The diff introduces no guardrail break (A or B).
