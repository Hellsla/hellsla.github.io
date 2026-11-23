VERDICT: PASS
CONTENT-HASH: 5cc65374e69c3347
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from 05fd3289498b07ef base 29cd249

## Blocking

## Polish

## Checked
- I ran the hash `--exercises --lang en` at the start and at the end. Both times it was 5cc65374e69c3347.
- I recomputed all 21 numeric answers against answers.py and exercises.json, and all are within tolerance. My own values:
  - L2-04: $6 \cdot 1.5\,\text{W} \cdot 8760\,\text{h} = 78.84\,\text{kWh}$
  - L3-01: $0.052\,\text{kW} \cdot 1460\,\text{h} \cdot 0.20\,\text{€/kWh} = 15.18\,\text{€}$
  - L3-02: $3.0\,\text{MWh} : 8760\,\text{h} = 342\,\text{W}$
  - L3-03: $2.3 \cdot 8.0 : 18 \cdot 100\,\text{km} = 102\,\text{km}$
  - L3-04: $2.8\,\text{GWh}$
  - L3-05: fraction $47.0/119.0 = 0.395$, $346\,\text{kWh}$, $43.2\,\text{€}$
  - L2-07: $1.50\,\text{kWh} : (5/6)\,\text{h} = 1800\,\text{W}$
  - L1-10: $(60\,\text{kJ}/40\,\text{s}) : (40\,\text{kJ}/80\,\text{s}) = 3.0$
  - L2-09: $-40\,\text{snt}$
- The rewritten Formula lines all start from $P = \Delta E/\Delta t$ (or $E = Pt$) and then solve symbolically. Each derivation is right:
  - L2-01: $\text{cost} = Pt \cdot \text{unit price}$
  - L2-04: $E = 6Pt$
  - L3-01: $\Delta E = (P_1 - P_2)t$
  - L2-05: $E_\text{tot} = \sum P_i t_i$
  - L3-04: $E = (P_\text{c} - P_\text{p})\Delta t$
  - L3-05: $E = \text{fraction} \cdot Pt$
  - L1-10: the power ratio from two slopes
- L3-03: the consumption $k = (E/s) \cdot 100\,\text{km}$, given in kWh per hundred kilometres, rearranges correctly to $s = (Pt/k) \cdot 100\,\text{km}$.
- L1-06, L1-07, L1-08, L2-07, L3-02, L3-04, L3-05 and L2-09: only paragraph splits. The numbers, the claims and the guardrail P1 wording in L2-09 d) are unchanged.
- Scope: everything stays within $P = E/t$ and energy cost, inside FY2. The diff introduces no guardrail break (A or B).
