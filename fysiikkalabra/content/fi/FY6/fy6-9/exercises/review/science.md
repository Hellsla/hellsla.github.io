VERDICT: FAIL
CONTENT-HASH: d7c2734da8dd122f

## Blocking
- solutions.md:19 — L1-02 (A, sig-fig justification): under P7 (b), $3000\,\text{mAh}$ has four significant figures. The Muunnokset step cuts it to $3{,}0\,\text{Ah}$, and the answer line contradicts itself: "$1{,}08 \cdot 10^{4}$" (three figures) "eli noin $11\,000$" (five figures) "kaksi merkitsevää numeroa" — fix: convert to $3{,}000\,\text{Ah}$, answer $1{,}080 \cdot 10^{4}\,\text{C}$, four figures as in $3000\,\text{mAh}$. The task's tolerance already allows it.
- solutions.md:29 — L1-03 (A, P7 b): $470\,\text{Wh}$ "kaksi merkitsevää numeroa" reads as three figures — fix: $4{,}7 \cdot 10^{2}\,\text{Wh}$ (or $0{,}47\,\text{kWh}$).
- solutions.md:70 — L2-02 (A, rounding reason): "sadasosaohmin tarkkuudella kuten resistanssi $0{,}80\,\Omega$" is not the limiting datum. The term $(5{,}0 - 3{,}8)\,\text{V} : 1{,}2\,\text{A} = 1{,}0\,\Omega$ is known only to $0{,}1\,\Omega$ (and the sentence itself says the difference limits it), so the result is $0{,}2\,\Omega$ — fix: answer $0{,}2\,\Omega$, to tenths of an ohm as in $(U_\text{lat} - E) : I = 1{,}0\,\Omega$. The key's 0,2 is unchanged.

## Polish
- solutions.md:175 — L2-06: the reason names $2{,}0\,\text{A}$ and $1{,}5\,\text{h}$, but the factor that limits the result is the difference $4{,}2\,\text{V} - 3{,}7\,\text{V} = 0{,}5\,\text{V}$, known to tenths. You could justify it from the energies: $12{,}6\,\text{Wh} - 11{,}1\,\text{Wh}$, to tenths of a watt-hour.
- solutions.md L1-08 Muunnokset — $2600\,\text{mAh}$ is four figures under P7 (b), so you could write $2{,}600\,\text{Ah}$. The result $5{,}2\,\text{h}$ ("kuten virrassa $0{,}50\,\text{A}$") is right.

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas (Q = It, W = UQ, I = (U_lat − E)/(R + R_s), R_s I² t, a trapezoid sum, a least-squares slope, staged charging). All agree with answers.py and exercises.json. The fit for L2-07 gives slope $2{,}50\,\text{A/V}$, so $R_\text{kok} = 0{,}40\,\Omega$, with intercept $E = 12{,}39\,\text{V}$; the solution's two points lie on that line.
- L3-04: the source voltage is the same at both currents, $3{,}75\,\text{V}$, as the model assumes. $R_\text{s} = 0{,}10\,\Omega$; the efficiencies are $77\,\%$ and $87\,\%$, both below $100\,\%$ as the guardrails require.
- L3-05: the stage currents are $4{,}75$, $4{,}25$ and $3{,}75\,\text{A}$, giving $7{,}12\,\text{h}$. The bounds $6{,}0\,\text{h}$ and $8{,}6\,\text{h}$ are right.
- The charging-circuit physics follows the brief everywhere: current through the battery from + to −, $U = E + R_\text{s}I$, losses become internal energy, and the battery stores chemical energy, not charge.
- P7 (b) is applied correctly elsewhere: 40 mΩ, 60 Ah and 80 % have two figures, 600 Wh three. The limiting data are named correctly in L2-03, L2-04, L3-01, L3-04 and L3-05.
- No limits are rounded and no 230 V appears, so P7 (a) and (c) do not apply.
- L1-06, L1-07, L1-09: exactly one correct option. Every distractor's feedback is right, including the unit analysis Wh, W and Wh·h.
- Figures ex-current (4,0 Ah) and ex-current2 (5,5 Ah, 61 Wh) are drawn to scale with 0,5 grid steps; they give every value needed and do not reveal the answers.
- Scope (Ah, Wh, the charging circuit, efficiency) and notation ($U_\text{lat}$, $E$, $R_\text{s}$, $W$) match the brief.
