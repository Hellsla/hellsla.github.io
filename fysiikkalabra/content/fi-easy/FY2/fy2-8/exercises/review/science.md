VERDICT: PASS
CONTENT-HASH: 9c09b92bedc2b843
SCOPE: delta md-paragraphs,numbers,typography from 08eba19797a49a39 base 5b3ca4f

## Blocking

## Polish
- solutions.md:248 (fy2-8-L1-09): the result $m_\text{CO2} = e \cdot H \cdot m$ uses $m$ both for the fuel mass and, with a subscript, for the emission. The algebra is correct. Writing "$m_\text{CO2} = e\,H\,m_\text{kaasu}$" would avoid the clash.

## Checked
- Every rewritten Kaava line starts from $m = eE$, the lesson's emission law, or from $E = Hm$, $E = Vh$ and $E = qA$. It combines them symbolically and cancels the common $E$ before any number:
  - solar/gas ratio: $e_2/e_1$
  - switching production methods: $(e_1 - e_2)E$
  - coal and gas from the figure: $(e_\text{kivihiili} - e_\text{kaasu})E$
  - area ratio: $q_\text{a}/q_\text{b}$
- g/MJ to g/kWh: the derivation $m = e_\text{MJ} E_\text{MJ}$ with $E_\text{MJ} = 3{,}6\,\text{MJ/kWh} \cdot E_\text{kWh}$ gives $e_\text{kWh} = 3{,}6\,e_\text{MJ}$. It is correct, and the units work out ($\text{g/MJ} \cdot \text{MJ/kWh}$). $69 \cdot 3{,}6 = 248{,}4\,\text{g/kWh}$.
- Petrol car against electric car: equal emissions give $e = e_\text{b} V h/E = 69 \cdot 6{,}0 \cdot 32/18 = 736\,\text{g/kWh}$, which is correct.
- Car against bus: the ratio per passenger is $e_\text{a}V_\text{a}h_\text{a}N/(e_\text{b}V_\text{b}h_\text{b}) = 4{,}14$, which is correct.
- Also recomputed: $490/41 = 11{,}95$; $q_\text{a}/q_\text{b} = 0{,}50/0{,}010 = 50$; $55 \cdot 47 \cdot 2{,}0 = 5170\,\text{g}$; $(820 - 490) \cdot 20\,000\,\text{kWh} = 6{,}6\,\text{t}$.
- The paragraph splits (L2-08, L2-10, L2-11, L3-04, L3-05, L3-06) change no claim, number, sign or unit. The L2-11 lists for a) to d), with $59{,}7/53{,}4/50{,}7\,\%$, 98, 137 and 150 g, 4,2 and $1{,}6\,\text{g/kWh}$, and 52 g or 35 %, match round 1.
- answers.py matches every numeric answer in exercises.json within its tolerance. No answer changed.
- Hash 9c09b92bedc2b843 at the start and at the end.
