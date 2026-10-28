VERDICT: DONE

Complete model solutions (teacher 2026-10-27), no numbers changed.
- solutions.md: all 12 exercise solutions now have Annettu, Kysytty, Periaate (with why it applies), Kaava ending in the solved unknown, Muunnokset, unrounded Sijoitus, Vastaus (value, unit, why that many figures) and a real Järkevyys (estimate, balance or back-calculation, limiting case). Old L3-01 value shown as 20,05 K unrounded (rounds to the same 20 K). No numeric error found in the old solutions.
- lesson.md Esimerkki: restaged into the seven stages (Tunnetut ja kysytty to Järkevyys); figures and problem text untouched; Sijoitus now shows 20,4 + 20 = 1454,4 W and 34,9 kWh.
- inquiry.json: solutions written for the numeric tasks tase-ennusta, epatasapaino (question), siirto and check-2 (replaced the short ones); two long display formulas split in two for 360 px.
Checks: check_solutions ok, check_lesson all ok.

## Rounding pass
- exercises.json (text only): L1-05 340 W/30 % -> 340,0 W/30,0 %; L2-01 roof 50 m² -> 50,0 m²; L2-04 30 %/29 % -> 30,0 %/29,0 % (the difference 1 % had one figure, stored 3,4 needs two); L3-01 10 h -> 10,0 h.
- Not fixable with ≤3 zeros, so the Vastaus is rounded to what the data support (all inside the 2 % tolerance, stored answers unchanged): L1-01 430 W (stored 432), L2-02 150 € (149), L2-03 210 kWh (212), L3-02 0,14 K (0,139), L3-03 980 kWh (984), inquiry jääkaappi 0,46 kWh (0,461). These solutions already carried the rounded value; the reasons now name the limiting data and say the calculator result is rounded.
- solutions.md: L1-05 Vastaus now 238 W/m² (three figures after the zeros); L2-04 reason now explains the difference 0,300 - 0,290; L2-03 explains 2,8 - 0,80 = 2,0.
- inquiry.json: tase-ennuste and tase-siirto (150, 140 W/m²) reasons say the example values are whole W/m²; epatasapaino reason names 240,0 - 236,4 = 3,6.
- lesson.md Esimerkki: window area 20 m² -> 20,0 m² (it was ambiguous and would have limited the sum to one figure); Tulos names U-values and dT as limiting.
