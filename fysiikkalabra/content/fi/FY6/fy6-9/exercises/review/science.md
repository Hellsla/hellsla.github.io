VERDICT: PASS
CONTENT-HASH: cf9236e40e5a36de

## Blocking

## Polish
- solutions.md L1-08 Muunnokset — under P7 (b), $2600\,\text{mAh}$ has four figures, so you could write $2{,}600\,\text{Ah}$. The result $5{,}2\,\text{h}$ ("kuten virrassa $0{,}50\,\text{A}$") is right.

## Checked
- I re-reviewed after the hash changed mid-review: d7c2734da8dd122f became cf9236e40e5a36de with commit 068cd7beb, which edits four answer lines of solutions.md and nothing in exercises.json or answers.py.
- The fixed lines are now right. L1-02: $1{,}080 \cdot 10^{4}\,\text{C}$ with four figures from $3000\,\text{mAh}$, under P7 (b). L1-03: $4{,}7 \cdot 10^{2}\,\text{Wh}$. L2-02: $0{,}2\,\Omega$, limited by $(U_\text{lat} - E) : I = 1{,}0\,\Omega$. L2-06: the precision is justified from $12{,}6\,\text{Wh} - 11{,}1\,\text{Wh}$.
- I recomputed all 19 numeric answers in one script with my own formulas (Q = It, W = UQ, I = (U_lat − E)/(R + R_s), R_s I² t, a trapezoid sum, a least-squares slope, staged charging). All agree with answers.py and exercises.json; L2-07's fit gives $R_\text{kok} = 0{,}40\,\Omega$ and $E = 12{,}39\,\text{V}$.
- L3-04: the source voltage is the same at both currents, $3{,}75\,\text{V}$; $R_\text{s} = 0{,}10\,\Omega$; the efficiencies are $77\,\%$ and $87\,\%$, both below $100\,\%$.
- L3-05: the stage currents are $4{,}75$, $4{,}25$ and $3{,}75\,\text{A}$, giving $7{,}12\,\text{h}$; the bounds $6{,}0\,\text{h}$ and $8{,}6\,\text{h}$ are right.
- The charging-circuit physics follows the brief: current through the battery from + to −, $U = E + R_\text{s}I$, losses become internal energy, and the battery stores chemical energy, not charge.
- P7 (b): 40 mΩ, 60 Ah and 80 % have two figures, 600 Wh and 3000 mAh their full figures. The limiting data are named correctly in L2-03, L2-04, L3-01, L3-04 and L3-05. No limits are rounded and no 230 V appears.
- L1-06, L1-07, L1-09: exactly one correct option. Every distractor's feedback is right, including the unit analysis Wh, W and Wh·h.
- Figures ex-current (4,0 Ah) and ex-current2 (5,5 Ah, 61 Wh) are drawn to scale with 0,5 grid steps; they give every value needed and do not reveal the answers.
- Scope and notation ($U_\text{lat}$, $E$, $R_\text{s}$, $W$) match the brief.
