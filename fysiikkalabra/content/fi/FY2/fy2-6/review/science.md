VERDICT: FAIL
CONTENT-HASH: 3d67762731586994
## Blocking
- inquiry.json:194 — Etsi virhe feedback: "$123\,000\,\text{GW}$ olisi tuhat kertaa koko maailman sähköntuotanto" is wrong. World generation is about $3\cdot10^{4}\,\text{TWh}$ a year, an average of about $3{,}4\cdot10^{3}\,\text{GW}$, so the ratio is about 36, not 1000 — write "kymmeniä kertoja koko maailman voimaloiden keskiteho".
- inquiry.json:94 — the feedback for mistake 2306 says "oikea kilowatteina ja megawatteina". 2306 is the answer in MW only; in kW it is $2{,}3\cdot10^{6}$ — say "oikea megawatteina".
- inquiry.json:101 — data-fi solution: "kaksi merkitsevää numeroa, koska … energia tunnetaan kolmen numeron tarkkuudella" contradicts itself. $20{,}2\,\text{TWh}$ has three figures, so the answer is $2{,}31\,\text{GW}$ (the tolerance already accepts it); fix the answer line and its justification.
- lesson.md:70 (from figures.py:30) — the aria-label says nuclear is "noin kolmannes kokonaistuotannosta". Tilastokeskus gives 39 % (31/79,9), about two fifths — change it to "noin kaksi viidesosaa".
- Teacher rule, all numbers in LaTeX: plain-text quantities at lesson.md:68 ("80 TWh"), lesson.md:204 ("5 MW"), inquiry.json:60 ("31 TWh"), :136 ("31 TWh, 20 TWh, 14 TWh"), :223 Järkevyys ("79,9 TWh"), :292 ("1600 MW", "5 MW") — put each in `$…\,\text{…}$`.
- Teacher rule, conversions by substitution: inquiry.json:269 and :278 "$1{,}0\,\text{MW} = 1000\,\text{kW}$", and :101 "$2\,305\,936\,\text{kW} = 2{,}31\,\text{GW}$" — show $1{,}0\cdot1000\,\text{kW}$ and $2{,}31\cdot10^{6}\,\text{kW} = 2{,}31\,\text{GW}$.
## Polish
- inquiry.json:79 — the parts sum to $79{,}1\,\text{TWh}$, not $79{,}9$. The $0{,}6$–$0{,}8\,\text{TWh}$ gap is other sources (Tilastokeskus' total includes them), not rounding: add a "muut" row or say so.
- lesson.md:13–41 — all arrows use the heat gradient (fy26-heat), even into the electricity box; a neutral or electric colour would not suggest heat.
## Checked
- Data verified at stat.fi "Sähkön ja lämmön tuotanto 2024": total 79,9; wind 20,2; hydro 14,1; fossil and peat 3,4; solar 0,9 TWh. Nuclear 39 % gives 31,2; wood fuels are 21 % of the 45,1 TWh renewable total, which gives 9,5.
- Recomputed all of lesson-answers.py in one script: worked example 1598 kW, 0,32, 43,8 GWh; 2,306 GW; 320; 14,016 TWh; 17,5 %; 8,76 GWh — all match.
- fi-bars is to scale at 10,5 px/TWh; the log chart's decades are 70 px and its bars match log10(P).
- Worked example: all seven stages, symbolic first; the check is real. Scope: E = P·t only, no FY3/FY4 content.
- Every correct option and the physics of every feedback (hydro is adjustable, nuclear is base load); OL3 1600 MW and the 5 MW turbine are realistic.
- No × and no "/" division anywhere.
