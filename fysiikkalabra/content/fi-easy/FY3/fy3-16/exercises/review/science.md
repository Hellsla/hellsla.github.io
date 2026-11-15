VERDICT: PASS
CONTENT-HASH: 9d4d47952b34a428

## Blocking

## Polish
- solutions.md fy3-16-L2-09 — "Oletus häviöttömyydestä tekee todellisesta arvosta hieman pienemmän" is right but reads backwards — fix: "Jos häviöitä on, todellinen $c$ on hieman laskettua pienempi."
- solutions.md fy3-16-L2-06 — "helmikuun kaltaisella kuukaudella" names a month, but the table has no months — fix: "kuukaudella, jolloin $T_\text{ulko} = -8\,{}^\circ\text{C}$".

## Checked
- Round 2 fix: L2-01 (1,7 kg) and L3-03 (1,6 kg) now have tolerance 0,04. The accepted ranges are 1,632–1,768 and 1,536–1,664. The rounded-down 1,6 (−5,9 %) and 1,5 (−6,3 %) are now rejected, which matches the task's "pyöristä ylöspäin" and the solutions' "ei riittäisi". answers.py rounds them up with `math.ceil`. The unrounded 1,617 shows "Lähellä" and the unrounded 1,511 is rejected. Both are consistent with a task that asks for a rounded-up minimum.
- I recomputed all 19 numeric answers with my own formulas in one script. They agree with answers.py and exercises.json within tolerance (largest gap among the others: L2-05 +0,6 %).
- L2-10: the exact $20{,}16 + 200{,}4 = 220{,}6\,\text{kJ}$ gives 2,451 h. The graph value 220 kJ gives 2,444 h. Both are inside the 0,03 tolerance.
- L2-06: least-squares slope $-99{,}8\,\text{kWh/K}$, so $UA = 139\,\text{W/K}$. The x-intercept is $20{,}1\,{}^\circ\text{C}$. The slope is read from points on the fitted line, as the guardrail asks.
- L3-02: the check that all the ice melts ($251\,400 > 167\,000\,\text{J}$) comes first, and $T = 8{,}06\,{}^\circ\text{C}$. The case where ice is left is stated.
- L2-07 ($26\,\text{K}$ against $299\,\text{K}$, ratio 11,5) and L2-08 (ratio 2, one correct option, each distractor's feedback names its real error).
- L1-06 and L1-07: one correct option each. The net-transfer wording and the wording on melting as interaction energy follow the guardrails.
- L2-05: the period efficiencies (82, 75, 70 %) are right, and so is the explanation that losses grow with the temperature difference.
- L3-04: $E = 5443\,\text{kWh}$, saving $480{,}6\,\text{€}$, break-even price $0{,}44\,\text{€/kg}$. L3-05: $592\,\text{kW}$, freezing $85\,\%$, the result is correctly a lower limit.
- The figures heating-line and melting-curve give the needed grid values and state no answer. The notation matches the brief. Scope is FY3.
