VERDICT: PASS
CONTENT-HASH: 6afbe5a6243e4487

## Blocking

## Polish
- exercises.json fy3-16-L2-01 — the tolerance of 0.06 around 1.7 accepts 1.6, which is $5.9\,\%$ off, although the task says to round up and the solution says $1{,}6\,\text{kg}$ "ei riittäisi". This is not wrong physics — optional: tolerance 0.04, or accept it knowingly.
- solutions.md fy3-16-L2-09 — "Oletus häviöttömyydestä tekee todellisesta arvosta hieman pienemmän" is right but reads backwards — fix: "Jos häviöitä on, todellinen $c$ on hieman laskettua pienempi."
- solutions.md fy3-16-L2-06 — "helmikuun kaltaisella kuukaudella" names a month, but the table has no months — fix: "kuukaudella, jolloin $T_\text{ulko} = -8\,{}^\circ\text{C}$".

## Checked
- I recomputed all 19 numeric answers with my own formulas in one script. They agree with answers.py and exercises.json within tolerance. For L2-01 and L3-03 the rounded-up minimums (1.617 → 1.7 and 1.511 → 1.6) follow the task text's "pyöristä ylöspäin".
- L2-06: my least-squares slope is $-99{,}8\,\text{kWh/K}$, so $UA = 139\,\text{W/K}$, and the x-intercept is $20{,}1\,{}^\circ\text{C}$. The two line points the solution uses are on the fitted line, as the guardrail asks, and "eivät ole täsmälleen suoralla" follows it.
- L3-02: all the ice melts ($251\,400\,\text{J} > 167\,000\,\text{J}$), so $T = 8{,}06\,{}^\circ\text{C}$. The boundary case is stated correctly.
- L2-07: the student's $0{,}253\,\text{h}$ and the ratio $11{,}5$ check out.
- L2-08: the ratio is 2 and only one option is correct. The three distractors come from the errors their feedback names.
- L1-06 and L1-07: one correct option each. The feedback uses the guardrails' net-transfer wording and the wording on melting as a change in interaction energy, and says that ice has a smaller $c$ than water.
- L2-05: the period efficiencies (82, 75 and 70 %) are right, and the explanation that losses grow with the temperature difference is physically right.
- L3-04: season energy $5443\,\text{kWh}$, saving $480{,}6\,\text{€}$, break-even wood price $0{,}44\,\text{€/kg}$. L3-05: $592\,\text{kW}$, of which freezing is $85\,\%$, and "alaraja" is correct.
- Figures heating-line and melting-curve (20,2 + 200 kJ ≈ 220 kJ; water slope 80/251): to scale, they give the needed values, and they state no answer.
- Notation and model match the brief ($UA\Delta T\,t = sm$, $\Delta T$ as a difference, 0 °C inside while there is ice). Scope is FY3.
