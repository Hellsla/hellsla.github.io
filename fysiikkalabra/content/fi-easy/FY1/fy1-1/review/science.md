VERDICT: PASS
CONTENT-HASH: eee3497ff21144ab

## Blocking

## Polish
- lesson.md:272 — the aria-label of the object-types figure says "Jokainen askel akselilla on kymmenkertainen koko", but the ticks are two powers of ten apart (labels $10^{4}$, $10^{8}$, … every four), so one tick interval is a 100-fold step — say "jokainen kymmenpotenssi on kymmenkertainen koko" or name the 2-decade tick spacing.
- inquiry.json:115 (`howto`) — "Lähennä/Loitonna muuttavat näkymän leveyden kymmenesosaksi tai kymmenkertaiseksi": in the code (`goTo(ceil(L)-1)`, `goTo(floor(L)+1)`) the buttons go to the next whole power of ten, so from $10^{-9{,}4}\,\text{m}$ the view goes to $10^{-10}\,\text{m}$, not $10^{-10{,}4}\,\text{m}$. Say "siirtää näkymän seuraavaan kymmenpotenssiin".
- sim-spec.md — it gives the visibility range as "1/2000 – 3", while the `calc` box gives "1/1000–3". The code reaches 50 % opacity at $d/W \approx 1/1200$, so `calc` is right. Align the spec.

## Checked
- I recomputed everything in one script, side by side with lesson-answers.py, and all values agree. Exp-1 gives $\Delta n = 5$, exp-2 gives $8$, exp-3 gives $-4$ (hius $7{,}0\cdot10^{-5}\,\text{m}$ → $n=-4$). Siirto gives $d = 12\,732\,\text{km}$ (with the $40\,000$, $6366$ and $111$ mistakes), check-2 gives $57\,917$, and the example gives $k = 6{,}47\cdot10^{4}$ with 2 significant figures.
- Each experiment's start state gives the object its intro names, by the `mainObj` rule: $L=-9$ gives vesimolekyyli, $7{,}7$ gives Maa and $27{,}5$ gives havaittava maailmankaikkeus. `kohdeExp = round(log10 m)` is the same as the $\sqrt{10}$ magnitude rule. In exp-2 the Neptune row gives 13 whether the radius or the diameter is used.
- Physical numbers are right: the Sgr A* horizon diameter is $2{,}54\cdot10^{10}\,\text{m}$ from $4{,}3\cdot10^{6}$ solar masses. Also right: the Coulomb/gravity ratio for two protons ($1{,}2\cdot10^{36}$), $93$ billion light-years $= 8{,}8\cdot10^{26}\,\text{m}$ and the Milky Way at $10^{5}$ light-years $= 9{,}5\cdot10^{20}\,\text{m}$. So are the heliopause at $120\,\text{AU}$, the Oort cloud at $\le 10^{5}\,\text{AU}$, Proxima at $4{,}0\cdot10^{16}\,\text{m}$, Sun/Earth $\approx 109$ (volume ratio $\approx 1{,}3\cdot10^{6}$), the nuclear mass fraction $>99{,}9\,\%$ and stadium/pea $\approx 4\cdot10^{4}$.
- The scale-axis figure, which says it is to scale, puts every object at its exponent within 0,03. The object-types axis puts each object within 0,01 of $\log_{10}$ of its stated size.
- Every sim OBJ size against the literature, within rounding. The `model` box names upper limits, the event horizon, and radius versus diameter for the orbits.
- Interactions: gravity, electromagnetic (including the magnet), the residual strong force, and the weak force for β⁻ decay of K-40. Every distractor's feedback is correct, and exactly one option is right in each choice.
- Tunnista: the pulsar, the mass of $1{,}4$ suns and $20\,\text{km}$ point uniquely to a neutron star. The "about 3 solar masses" lower bound for stellar black holes is fair at this level.
- Observable versus whole universe: the expansion explains why the size exceeds $2\cdot13{,}8$ billion light-years. Planck length is described as calculated, not measured.
- Model answers in the exit ticket and check-3 match the theory.
- Scope: qualitative structure of matter, astronomy and interactions, as in the 2026-10-28 brief. No equations beyond ratios.
