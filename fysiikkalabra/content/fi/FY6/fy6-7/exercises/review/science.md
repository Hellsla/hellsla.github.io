VERDICT: FAIL
CONTENT-HASH: 570d72a678666d58

## Blocking
- solutions.md:69 — L2-02 (A, sig-fig justification): the answer is written $480\,\text{kJ}$ and called "kaksi merkitsevää numeroa". Under the teacher's rule P7 (b), trailing zeros are significant, so $480$ reads as three figures. The stated precision and the written number disagree — fix: write $4{,}8 \cdot 10^{2}\,\text{kJ}$ (or $0{,}48\,\text{MJ}$) with the same justification.
- solutions.md:154 and :156 — L2-05 (A, same rule): $730\,\text{kWh}$ "kaksi merkitsevää numeroa" reads as three figures — fix: $7{,}3 \cdot 10^{2}\,\text{kWh}$ in both lines. Also name the limiting data exactly: $90\,\text{W}$, $60\,\text{W}$ and the times. Under P7 (b), $110\,\text{W}$, $800\,\text{W}$ and $1200\,\text{W}$ have three or more figures, so "kuten tehoissa" is not accurate.
- solutions.md:184 and :186 — L2-07 (A, same rule): $300\,\text{kWh}$ "kaksi merkitsevää numeroa" reads as three figures — fix: $3{,}0 \cdot 10^{2}\,\text{kWh}$ in both lines.

## Polish
- solutions.md L1-10 Vastaus — the sentence "Vastaus kelpaa, kun se on noin ±4 % sisällä" talks about the checker, not the physics. You could drop it.
- solutions.md L2-07 Kuvaajan lukeminen — the claim that the line "kulkee pisteen (48 h; 1,64 kWh) kohdalle" holds for the fitted line: the least-squares slope through the origin gives $1{,}639\,\text{kWh}$ there. You could word it "suora kulkee lähes pisteen kautta", so it is not read as joining raw points.

## Checked
- I recomputed all 20 numeric answers in one script with my own formulas (E = Pt, E = UIt, P = U²/R, K = aE + K_perus, meter differences, least-squares slope through the origin, payback H/(aΔE)). All agree with answers.py and exercises.json; my own fit gives $299{,}1\,\text{kWh}$ against the key's $299{,}3\,\text{kWh}$, inside its 5 % tolerance.
- P7 (a): every solution treats $230\,\text{V}$ as three significant figures (L1-03 $5{,}22\,\text{A}$, L3-03 $4{,}99\,\text{kWh}$).
- P7 (b) elsewhere: 40 W (2 figures), 350 kWh, 320 kWh and 489 € (3 figures), and 1200 W and 2200 W are never named as the limiting datum. The other justifications name the real limiting datum (L3-05: 17 snt and 98 kWh; L2-06: $56{,}3\,\text{kWh}$).
- No limits (maximum or minimum) are rounded in this set, so P7 (c) does not apply.
- Figures: washer gives 0,80 kWh and dryer 2,5 kWh, so 0,45 €. Both are drawn to scale with the stated grid steps; neither shows the energy.
- L1-06, L1-09: exactly one correct option. Each distractor's number is the error its feedback names (÷3600, minutes as hours, W as kW, W·min).
- L1-08: the error analysis by units is right.
- L3-04: the saving $6{,}0\,\text{kWh} \cdot 15{,}5\,\text{snt/kWh} = 0{,}93\,\text{€}$; the mean price $14{,}08\,\text{snt/kWh}$.
- L3-05 c): the waste-heat point (the old fridge heats the home in winter) is right physics; the gain $77\,\text{€}$ is $16\,\%$ of the price.
- Scope (sähköteho, kWh, the electricity bill) and notation (E, P, t, a, K_perus) match the brief.
