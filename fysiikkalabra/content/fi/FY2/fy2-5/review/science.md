VERDICT: PASS
CONTENT-HASH: e86af0276dd261d7

## Blocking

## Polish
- lesson.md (Kaava, sources paragraph) and inquiry.json (taulukko, source_note) — Problem: puupelletti ("julkaistu tyypillinen arvo" / "tyypillinen arvo") and the Finnish ethanol-blended bensiini value 43 name no publisher or year, which the FY2 data rule asks for. — Fix: name a source, e.g. Tilastokeskus, Polttoaineluokitus (2017) for moottoribensiini and puupelletti.
- lessons/FY2/fy2-5/lesson-answers.py:23 — Problem: the comment still says "ratkaistu esimerkki", but the 3,0 kg petrol example is in the Kaava section; the worked example uses 6,0 kg of wood. — Fix: "lesson.md, Kaava: bensiini 3,0 kg".

## Checked
- The hash was e86af0276dd261d7 at the start and the end.
- The round-5 contradiction is gone. The taulukko source_note now matches lesson.md: IPCC 2006 for maakaasu, kivihiili and diesel; bensiini 43 MJ/kg as Finnish ethanol-blended petrol, with IPCC 44,3 MJ/kg for pure petrol. Ethanol (about 27 MJ/kg) lowers the blend to about 42–43 MJ/kg, so this is right.
- I recomputed every number in lesson.md, inquiry.json and the exit ticket in one script, and all match lesson-answers.py: 2,87; 90 MJ and 25 kWh (with 4,17 kWh/kg ≈ 4 in the check); 129 ≈ 130 MJ; 22 MJ/kg; 1500 kJ; 15/30/60/120 MJ; 3,75 and 3750 MJ; siirto 10,58 → 6,348 → 6,3 MJ, with mistakes 10,6, 4,2 and 6350; tark-2 11,94 → 12 kWh, with mistake 154,8 ≈ 155; tark-3 170 and 430 MJ, ratio 2,5; exit 75 MJ and 15 MJ/kg.
- Figure 2 is to scale at 6,80 px per MJ/kg, every bar within 0,01 px/(MJ/kg). The ticks and the "noin viisi kertaa" in the aria-label (48 : 10 = 4,8) are right. Figures 1 and 3 are physically correct.
- The worked example has seven stages and solves symbolically first. Its kWh conversion substitutes, its 2 s.f. are justified, and its check is real.
- Physics is right throughout: net (lower) heating values; the moisture explanation; dry wood about 19 MJ/kg; label energy is metabolisable and so slightly less than combustion energy; released energy differs from useful energy.
- Every correct option and every feedback in kertaus, ennuste-1/2, taulukko, rakenna, virhe, tarkistus-1 and the explain model answers is physically right. No option is keyed wrong.
- The numeric solutions (ruoka, siirto, tarkistus-2) are complete, solve symbolically first, convert by substitution and do a real check.
- Scope is FY2: E = Hm, one efficiency, kWh. There is no Q = cmΔT, no efficiency chain and no FY4 content.
