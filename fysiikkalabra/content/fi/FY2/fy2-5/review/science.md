VERDICT: PASS
CONTENT-HASH: 3e35103094aaa58b

## Blocking

## Polish
- inquiry.json:106 (taulukko, source_note) — Problem: bensiini is attributed to IPCC 2006, but lesson.md:53 says that IPCC gives 44,3 MJ/kg for pure petrol and that 43 is the value for Finnish petrol containing ethanol. The two notes contradict each other. — Fix: move bensiini out of the IPCC list, e.g. "bensiini: tyypillinen suomalaisen bensiinin arvo".
- lesson.md:53 — Problem: the values for bensiini (43) and puupelletti ("julkaistu tyypillinen arvo") name no source, which the FY2 data rule asks for. — Fix: name the source, e.g. Tilastokeskus' polttoaineluokitus for moottoribensiini and for puupelletti.
- lessons/FY2/fy2-5/lesson-answers.py:23 — Problem: the comment says "ratkaistu esimerkki", but the 3,0 kg petrol example is in the Kaava section. The worked example uses 6,0 kg of wood. — Fix: "lesson.md, Kaava: bensiini 3,0 kg".

## Checked
- The hash was 3e35103094aaa58b at the start and the end.
- The round-3 blocking items are fixed. lesson.md:30 now gives $43 \cdot 10^{6}\,\text{J}$. The g → kg steps in ruoka (solution, hint) and in exit-ticket q3 are substitutions, and so is the kJ → MJ step.
- I recomputed every number in lesson.md, inquiry.json and the exit ticket in one script, and all match lesson-answers.py: 2,87; 90 MJ and 25 kWh (with 4,17 kWh/kg ≈ 4 in the check); 129 ≈ 130 MJ; 22 MJ/kg; 1500 kJ; the table 15/30/60/120 MJ; 3,75 and 3750 MJ; siirto 10,58 → 6,35 → 6,3 MJ, with mistakes 10,6 / 4,23 / 6348; tark-2 11,94 → 12 kWh, with mistake 154,8; tark-3 170 and 430 MJ, ratio 2,5; exit 75 MJ and 15 MJ/kg.
- Figure 2 is to scale at 6,8 px per MJ/kg, every bar within 0,4 px, and the ticks are correct. The aria "noin viisi kertaa" is right (48 : 10 = 4,8). Figures 1 and 3 are physically correct.
- The worked example has seven stages and solves symbolically first. Its kWh conversion substitutes, its 2 s.f. are justified, and its check is real (1 kW for 25 h).
- Physics is right throughout: lower (net) heating values; the moisture explanation; dry wood about 19 MJ/kg; the label energy is metabolisable and so less than the combustion energy; released energy differs from useful energy.
- Every correct option and every feedback in kertaus, ennuste-1/2, taulukko, rakenna, virhe and tarkistus-1 is physically right. No option is keyed wrong.
- The data is realistic: LPG 46 MJ/kg, Fineli-level food values, peat and wood moisture ranges.
- Scope is FY2: E = Hm, one efficiency, kWh. There is no FY3 heat (Q = cmΔT), no efficiency chain and no FY4 content.
