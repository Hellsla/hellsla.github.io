VERDICT: FAIL
CONTENT-HASH: 496ce1f4ea7cc86f

## Blocking
- lesson.md:43 (taulukon otsake `$H$ (MJ/kg)`); inquiry.json:139 (`15 MJ/kg`), :175 (`yksikössä MJ/kg`), :187 (`kJ`, `100 g`), :203 (`yksiköissä MJ/kg`), :226 (`kJ-luku`), :311 (`yksikkö MJ/kg`); exit-ticket.json:11 (`yksikössä MJ/kg`) — Problem: these units and quantities are plain text. The teacher's rule is everything in LaTeX. — Fix: write `$\text{MJ/kg}$`, `$100\,\text{g}$`, `$\text{kJ}$` and so on, as in the inquiry table at :107. While editing :139, also change "kuivan polttopuun" to "ilmakuivan polttopuun" so the note matches the 15 MJ/kg it cites.

## Polish
- lesson-answers.py:19–20 — Problem: the line labelled "misconception: wet wood" computes 10 kg of *wood* (150 MJ). The only task that uses it, tarkistus-3 (inquiry.json:360), uses *pellets*: 17 · 10 = 170 MJ, with a ratio of 430 : 170 ≈ 2,5. Neither number is computed. The text the students see is correct. — Fix: compute `17 * 10` and `430 / 170` under a tarkistus-3 comment.
- lesson-answers.py — Problem: lesson.md:39 (129 MJ) and exit-ticket q2–q3 (75 MJ, 15 MJ/kg) are not computed (all right). — Fix: add a line each.
- lesson.md:53 — Problem: the bensiini note says ethanol is the reason for rounding to 43. It is plausible (E10 ≈ 42,5 MJ/kg) but unsourced. — Fix: keep it, but label it "tyypillinen arvo" as for the pellets, or cite Tilastokeskus' moottoribensiini value.

## Checked
- The data with a named source is verified. IPCC 2006 NCV (via EU MRR Annex VI): maakaasu 48,0, motor gasoline 44,3, gas/diesel oil 43,0 and other bituminous coal 25,8 TJ/Gg, all as cited. Tilastokeskus *Polttoaineluokitus*: jyrsinturve 9–11 GJ/t at 40–50 % moisture, halot/pilkkeet 13–15 GJ/t at 20–25 %, as cited. Pellet 17, food values and dry wood ≈ 19 MJ/kg are realistic.
- Every lesson and inquiry number, the siirto and tarkistus-2 mistake values included, was recomputed in one script. All match.
- Figure 2 is to scale at 6,8 px per MJ/kg, and every bar is right. Figures 1 and 3 are right.
- Every correct option and feedback is physically right, and so is the food-label caveat.
- The worked example has all seven stages. It is symbolic first, the kWh conversion is by substitution, its 2 s.f. are justified and its check is real.
- Scope: E = Hm, one efficiency, P = E : t and kWh. There is no Q = cmΔT, no chain product and no FY3/FY4 content. There is no ×, division uses a colon, and the Miksi premise is fixed.
