VERDICT: DONE

solutions.md: all 17 blocks now have Annettu, Kysytty, Periaate (why the law fits: closed rigid vessel, absolute pressure, bounding lines), Kaava ending in the solved unknown, Muunnokset, unrounded Sijoitus, Vastaus (value, unit, why those significant figures) and a real Järkevyys (estimate, recomputed check, kelvin ratio, limiting case). L3-01 Järkevyys now answers the "why larger than seven points" question; L3-02 adds the 67 K condensation check; L2-03 explains the gauge-to-absolute conversion.
lesson.md: Esimerkki restructured into the seven stages (the old "Epävarmuus" and "Tulos ja järkevyys" stages were split and folded in; Periaate and Yksikkömuunnokset added); one display block per stage, first row symbolic; problem text and figures untouched.
inquiry.json: solutions rewritten in the labelled form for suora and epavarmuus (with Kuvaajan lukeminen) and siirto, new for tarkistus-2.
No numeric error found in the old solutions. Note (not fixable here): the answers.py comment for L2-01 says -255,9 although the value is -255,97 (-256 rounded; the answer itself is right).

## Rounding pass
- Added trailing zeros so the data supports the stored answer (values, answers, tolerances, answers.py unchanged): L1-02 105,0/127,0 kPa; L1-03 −267,90 °C; L2-01 1,050/1,360 bar; L2-03 ilmanpaine 101,0 kPa; L2-04 ±0,50 °C; L3-02 100,0 kPa and 77,0 K; L3-03 −262,00 ± 6,00 °C. Same in solutions. Inquiry: suora (20,0/90,0 °C), siirto (30,0/90,0 °C), tarkistus-2 (15,0/95,0 °C, 108,0/137,0 kPa).
- Reasons rewritten to name the real limiting datum (differences of readings, not "kuten arvoissa"): L1-02..L3-03, inquiry suora/epavarmuus/siirto/tarkistus-2, Esimerkki Tulos.
- L3-01: Vastaus rounded to 20 °C (tarkasti 20,3), inside tolerance 0,03: the zeros needed (θ and p to 0,01) would contradict the ±1,0 kPa uncertainty.
- Removed "5,3 on yhtä hyvä" (L1-03) and "0,37 on myös tarkkuuden rajoissa" (L1-02), "epävarmuus on arvio" arguments.
- Järkevyys numbers checked (2 %, 1,86, 0,772/0,783 ratios ok).
