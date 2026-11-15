VERDICT: PASS
CONTENT-HASH: 497a340498947abb

## Blocking

## Polish
- solutions.md:149 (fy6-14-L2-05) and :169 (L2-07) — the answers $210\,\Omega$ and $390\,\Omega$ are called two significant figures. Under the teacher's rule P7b the written numbers read as three. Write $2{,}1 \cdot 10^{2}\,\Omega$ and $3{,}9 \cdot 10^{2}\,\Omega$, as this round did for L2-06.
- solutions.md:158 (L2-06, Sijoitus) — for $15\,\Omega$, $1{,}48\,\text{V} \cdot 99\,\text{mA} = 146{,}5\,\text{mW}$, which rounds to $147\,\text{mW}$, not $146\,\text{mW}$. The maximum is unaffected.
- solutions.md:192 (L3-04) — "noin $4700\,\text{kWh}$" reads as four figures under P7b. Write $4{,}7 \cdot 10^{3}\,\text{kWh}$ or $4{,}7\,\text{MWh}$ (the Järkevyys line already says 4,7 MWh).

## Checked
- Hash 497a340498947abb at start and end. The only change since the last PASS is the L2-06 answer step (git c40cc4fbb); I still reviewed the whole set.
- Recomputed all 19 numeric answers in one script. Every one agrees with answers.py and exercises.json, and so do the 8 table powers of L2-06 and the 9 of L3-02.
- L3-05: I found the operating point with my own bisection on a linearly interpolated characteristic: U_D = 2,020 V and I = 13,78 mA. The threshold from the 2,05–2,10 V line is 2,00 V.
- L2-06 change: 1,99 V · 91 mA = 181 mW. Two figures (91 mA is limiting) is right. The shown 1,8·10² mW gives a step of 10, so a student's 180 passes.
- Sig figs follow P7b: 260 W, 800 W/m², 1000 W/m², 100 mA and 120 Ω count as three or more figures, and every stated limiting datum is truly the limiting one.
- Physics: Kirchhoff's loop with U_R = RI, P = UI for the LED and the cell, η = P/(GA), the reverse direction giving U_D = U (L2-01 states its assumption), and parallel branches being independent (L2-08). In every choice task exactly one option and one reason are correct.
- L3-04: ΣH = 1027 kWh/m², production 4683 kWh, consumption 5340 kWh, 87,7 %. The deficit months are Jan–Mar and Oct–Dec: 853 vs 3370 kWh, a 2517 kWh shortfall.
- Figures: in ex-led the model passes (2,20 V; 10 mA) exactly. In ex-kenno the current at 4,0 V is 198,7 mA, which reads as 200 mA, inside the 4 % tolerance.
- Scope: components only, no p–n junction microphysics.
