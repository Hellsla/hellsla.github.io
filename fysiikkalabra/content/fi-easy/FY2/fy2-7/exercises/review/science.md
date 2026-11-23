VERDICT: FAIL
CONTENT-HASH: 1592588b5f48206f

## Blocking
- solutions.md:150–151 (fy2-7-L2-03 … the 9 % → 6 % network-improvement task, the section after line 145), Sijoitus: this round's rewrite brought in $E_\text{sent,1}$ and $E_\text{sent,2}$, English subscripts copied from the en version. The Kaava on line 148 and the lesson use $E_\text{lähtö,1}$ and $E_\text{lähtö,2}$, so the substitution works with symbols the solution never defines. This breaks internal consistency (the notation of the Kaava and the lesson). The Finnish solutions.md:150–151 has the same lines. Fix: "**Sijoitus:** $E_\text{lähtö,1} = \dfrac{600\,\text{MWh}}{0{,}910} = 659{,}3\,\text{MWh}$" and "$E_\text{lähtö,2} = \dfrac{600\,\text{MWh}}{0{,}940} = 638{,}3\,\text{MWh}$". The Kaava ends in $E_\text{perille}\left(\frac{1}{\eta_1} - \frac{1}{\eta_2}\right)$, so the substitution can also go straight into that form: "$\Delta E = 600\,\text{MWh}\left(\dfrac{1}{0{,}910} - \dfrac{1}{0{,}940}\right) = 21{,}0\,\text{MWh}$".

## Polish
- solutions.md (L2-10 c)), carried from round 1: "joten nettovienti oli 2142 MW" reads as a value derived from $12\,791 - 10\,647 = 2144\,\text{MW}$. Fix: "Fingridin mukaan nettovienti oli $2142\,\text{MW}$".

## Checked
- Every rewritten Kaava line starts from a basic relation: conservation $E_\text{lähtö} = E_\text{perille} + E_\text{häviö}$ (or the same with powers), the definition $\eta = E_\text{perille}/E_\text{lähtö}$, the share $p = E_\text{häviö}/E_\text{lähtö}$, or $P = E/t$. Each solves symbolically and substitutes into the final form.
- Recomputed:
  - $0{,}09 \cdot 360 = 32{,}4\,\text{MWh}$
  - $0{,}960 \cdot 125 = 120{,}0\,\text{MW}$
  - $600/0{,}80 - 600 = 150\,\text{MWh}$
  - $0{,}040 \cdot 2\,400\,000/8760 = 10{,}96\,\text{MW}$
  - $40{,}0 \cdot 24/0{,}80 = 1200\,\text{kWh}$
  - $600(1/0{,}910 - 1/0{,}940) = 21{,}0\,\text{MWh}$
  - $455{,}0 - 442{,}0 = 13{,}0\,\text{MWh}$
  - $150 \cdot 8760/20\,000 = 65{,}7$
  - $12/250 = 4{,}8\,\%$
  - $800 - 728 = 72\,\text{kW}$
  - $0{,}50 \cdot 2{,}4 \cdot 5000/0{,}910 = 6{,}593\,\text{MWh}$
  - $0{,}040 \cdot 500 \cdot 3{,}6 = 72\,\text{MJ}$
  - $(0{,}09 - 0{,}04) \cdot 250 = 12{,}5\,\text{MWh}$

  All agree with the solutions.
- Heat-plant improvement: $\Delta E_\text{laitos} = r P_\text{häviö} t/\eta$ is the correct reasoning. The house saving is energy that arrives, and the 9 % loss is taken from the energy sent.
- `fy2-7/sankey`, the figure the teacher approved: it shows only the shares 96/4 and 91/9 %, which are the values the tasks read. The widths are to scale and the same for both networks, and the alt text agrees.
- The paragraph splits change no claim or number.
- answers.py matches every numeric answer in exercises.json within its tolerance. No answer changed.
- Hash 1592588b5f48206f at the start and at the end.
