VERDICT: PASS
CONTENT-HASH: 6ea0dc78bb3acd02
## Blocking

## Polish
1. lesson.md, Hyötysuhde: $W_\text{a}$, $W_\text{o}$ are named without a unit; add (J), and (W) for $P_\text{a}$, $P_\text{o}$. Carried over.
2. lesson.md, Vesivoimala: the electric power is $P$ in $P = \eta\rho Q g h$ but $P_\text{a}$ in the efficiency; one clause ("sähköteho $P = P_\text{a}$") would tie them. Carried over.
3. lesson.md, Teho kertoo energiaa sekunnissa: "satoja kuutiometrejä" gives "satoja megawatteja" only near the top of the range ($235\,\text{kJ/m}^3$: $500\,\text{m}^3\text{/s}$ is $118\,\text{MW}$, $900\,\text{m}^3\text{/s}$ is $212\,\text{MW}$). Fix: "sata–kaksisataa megawattia".
4. lessons/FY4/fy4-15/lesson-answers.py, exit-ticket comment still says P_s. Carried over.

## Checked
- Changed row in the worked example's Järkevyys: $(120 : 82)^2 = 2{,}142$ and $2{,}14 \cdot 1{,}02\,\text{MW} = 2{,}18 \approx 2{,}2\,\text{MW}$; $1017\,\text{kW} \approx 1{,}02\,\text{MW}$. Correct, and consistent with the result $2{,}3\,\text{MW}$.
- Worked example recomputed: $A = 11\,309{,}7\,\text{m}^2$, $P = 2\,318\,849\,\text{W}$, reference power $5{,}15\,\text{MW}$; two figures justified by $9{,}0\,\text{m/s}$ and $0{,}45$.
- Theory: $P_\text{o} = \rho Q g h$ and $P_\text{tuuli} = \tfrac12\rho A v^3$ derived from $mgh$ and $\tfrac12 mv^2$; conditions stated (small kinetic energy in the head and tail water; undisturbed wind as reference; constant $\eta$ only in the model; rated power, cut-in and cut-out).
- Data: $1285 : 144 = 8{,}92$; share of the reference power $0{,}349$ at $5\,\text{m/s}$ and $0{,}389$ at $10\,\text{m/s}$, so "vähän parempi" holds; Betz $16/27 = 59\,\%$; $192 : 24 = 8{,}0$ and $62 : 7{,}8 = 7{,}9\,\text{MW/m}$; $1000 \cdot 9{,}81 \cdot 24 = 235\,\text{kJ}$.
- inquiry.json numerics: siirto $6{,}4246\,\text{m}^3\text{/s}$ (mistakes 6424,6; 5,461; 4,642), check-2 $800{,}496\,\text{kW}$ (941,8; 81,6), etsi-virhe $100{,}06\,\text{kW}$ and $2400\,\text{kWh}$, check-3 $(8 : 6)^3 = 2{,}37$: all agree.
- Every choice has exactly one correct option; each distractor is wrong and its feedback gives the right reason.
- Exit ticket: $50/0{,}90 \approx 56\,\text{MW}$, loss about $6\,\text{MW}$ becomes internal energy (not "lämmöksi") and the tail water's kinetic energy.
- Efficiency worded as the guardrails require; hydro about $90\,\%$, wind under half.
- Hash 6ea0dc78bb3acd02 at the start and at the end.
