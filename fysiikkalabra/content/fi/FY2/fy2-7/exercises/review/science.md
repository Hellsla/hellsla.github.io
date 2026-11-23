VERDICT: FAIL
CONTENT-HASH: 68b89c13fead066f

## Blocking
- solutions.md:150–151 (L3-01 Sijoitus) — A: the rewrite introduced $E_\text{sent,1}$ and $E_\text{sent,2}$, an English subscript that is defined nowhere, while the Kaava line just above names the same quantity $E_\text{lähtö,1}$, $E_\text{lähtö,2}$. The solution's symbols now disagree, and a student cannot tell what "sent" is. Fix: use $E_\text{lähtö,1}$ and $E_\text{lähtö,2}$, and preferably substitute into the final symbolic form the Kaava derives: $\Delta E = 600\,\text{MWh} \cdot \left(\dfrac{1}{0{,}910} - \dfrac{1}{0{,}940}\right) = 659{,}3\,\text{MWh} - 638{,}3\,\text{MWh} = 21{,}0\,\text{MWh}$.

## Polish
- solutions.md L2-09 Vastaus — with 9 % and 4 % rounded to whole percents, the 5 % difference is uncertain by about ±1 percentage point (C; still open).
- solutions.md L2-10 c) — add "ja sähkövarastojen" to the balance sentence (C; still open).

## Checked
- Hash 68b89c13fead066f at the start and the end; solutions.md changed since base 5b3ca4f, plus the teacher-approved figure fy2-7/sankey (its 96/4 % and 91/9 % shares are what L1-02 and L2-09 read); exercises.json and answers.py untouched.
- Every other rewritten Kaava starts from $E_\text{lähtö} = E_\text{perille} + E_\text{häviö}$ (or with powers), $\eta = E_\text{perille}/E_\text{lähtö}$, the loss share $p = E_\text{häviö}/E_\text{lähtö}$ or $P = E/t$, and combines symbolically before substitution; every combination is algebraically right, and the loss percentage is always taken of the energy sent.
- L3-04: plant saving $= r P_\text{häviö} t / \eta$ is right (the house saving is delivered energy, so the plant saves it divided by the network efficiency).
- Recomputed every numeric answer in one script with my own formulas: 32,4 MWh; 120 MW; 150 MWh; 10,96 MW; 1200 kWh; 21,0 MWh; 13,0 MWh; 65,7 houses; 4,8 %; 6,59 MWh; 72 MJ; 12,5 MWh, plus the rest of the set: all agree with answers.py and exercises.json within tolerance, units unchanged.
- The md-paragraph splits (L2-05, L3-04, L3-05, L2-10) move no number and change no claim; L3-05 keeps the correct reason (loss grows faster than the current, about fourfold for double current).
