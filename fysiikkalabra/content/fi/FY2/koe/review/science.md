VERDICT: PASS
CONTENT-HASH: de592b8af351e9f4

## Blocking

## Polish
- [Minor] fy2-k7 c), rubric against solution: the criterion `math` (1 p) reads "Hyödyksi saadaan $0{,}80 \cdot 500\,\text{Wh} = 400\,\text{Wh}$". The rewritten Sijoitus now substitutes straight into $t = \eta E_\text{akku}/P$ and no longer shows $400\,\text{Wh}$. A grader should accept $0{,}80 \cdot 500\,\text{Wh}$ written in the numerator. Either add "(tai $\eta E_\text{akku}$ sijoitettuna)" to the criterion, or keep the $E_\text{hyöty}$ value in Sijoitus (category 6/7, no wrong physics).
- [Minor] fy2-k2 a) Kaava: the first row $E_\text{akku} = 0{,}60 \cdot E_\text{kapasiteetti}$ puts a number into the symbolic step. $(0{,}80 - 0{,}20)\,E_\text{kapasiteetti}$, or a symbol for the change in charge, would keep the step symbolic. This is form only.

## Checked
- Round 1, full packet. The change is the Kaava steps (and in k3 and k7 the Sijoitus) of k2 a), k3 a) and b), k5 c), k6 d), k7 b) and c) (git diff ce7c397be2..eda9e57628). Each now starts from its basic law and derives the combined form:
  - $\eta = E_\text{hyöty}/E$;
  - $E = Hm$;
  - $E = P_\text{ka}t$ with $P_\text{ka} = \text{osuus} \cdot P$;
  - $P = E/t$.

  Every derivation is algebraically right and the substitution goes into the final form. All of it is FY2 physics (no FY3 content).
- I recomputed every number with my own formulas: k1 c), d), e), i) $54\,\text{kJ}$, $50$ and $60\,\text{Wh}$, $70\,\%$, $12{,}5\,\text{MW}$. The others:
  - k2: $38{,}4$, $42{,}7$ and $4{,}3\,\text{kWh}$; $3{,}88\,\text{h}$ (53 min); $5{,}12\,€$.
  - k3: $64\,800\,\text{MJ}$; $4484$ and $1686\,\text{kg}$; heating-value ratio $2{,}51$; the efficiencies make $6\,\%$; $12\,\text{kg/d}$.
  - k4: $5325\,\text{kWh}$, $35{,}5\,\%$, $0{,}61\,\text{kW}$, $10{,}1\,\%$, $888\,\text{kWh/kW}$.
  - k5: $175{,}2$ and $122{,}6\,\text{GWh}$, $8176 \approx 8200$ homes, $14\,\text{MW}$.
  - k6: $13\,700$ and $11\,600\,\text{MW}$; $40{,}9$ and $7{,}8\,\%$; export $3500$, import $1900\,\text{MW}$; $69{,}6\,\text{GWh}$, $4640$ homes; $23{,}7$ and $34{,}7\,\text{TWh}$; shares of consumption $55$ and $7\,\%$.
  - k7: $2{,}16\,\text{MJ}$, $4{,}8$ bananas, $2{,}67\,\text{h}$, without $\eta$ $3{,}3\,\text{h}$, $500\,\text{Wh} = 1{,}8\,\text{MJ}$.

  All agree with answers.py and tasks.json.
- k1: each item has exactly one correct option, and the distractor explanations are right. In j) the effective temperature is $-18\,{}^\circ\text{C}$ against $+15\,{}^\circ\text{C}$ at the surface.
- k3 c): IPCC defaults wood $112\,\text{g/MJ}$ and oil $74\,\text{g/MJ}$; the time-horizon reasoning is correct and no claim of carbon neutrality is made. k6 c) mechanisms are right, and the k7 a) energy chain is right.
- Rubric points are unchanged. Apart from the k7 c) note above, every other rubric criterion still matches the solution steps.
- The hash was the same at the start and at the end.
