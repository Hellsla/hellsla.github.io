VERDICT: DONE

Complete model solutions (teacher 2026-10-27).
- solutions.md: all 12 blocks now have Annettu, Kysytty, Periaate (with why it applies), Kaava ending in the solved unknown, Muunnokset, Sijoitus (unrounded), Vastaus (value, unit, significant-figure reason) and a real Järkevyys (estimate, relative change, recomputed balance, comparison with table values). L3-01/02/03 also answer their "perustele" parts. No numeric error found; all answers agree with answers.py. L2-03: the old note that each rail end moves by half was replaced by a remark that real neighbouring rails also grow, so the gap closes earlier.
- lesson.md Esimerkki: now the seven stages (Periaate, Yksikkömuunnokset, Tulos added; formula row first symbolic); result 86,4 mm unchanged.
- inquiry.json: siirto solution rewritten in the labelled step form; check-2 got a new solution (alpha = 23e-6 1/K). No other field touched.

## Rounding pass
- exercises.json (text only): L1-04 "200 l" -> "200,0 l"; L2-01 "50 mm" -> "50,0 mm"; L3-01 diameters 75,00/75,09 mm -> 75,000/75,090 mm (the difference 0,09 mm had one figure); L3-02 alpha 17 and 12 -> 17,0 and 12,0 (difference 17-12=5 had one figure, the stored 20 um needs two); L3-03 "20 l" -> "20,0 l". No value, answer, tolerance or answers.py changed.
- solutions.md: every Vastaus now names the real limiting datum (L1-01..L3-03); the same zeros carried into Annettu, Sijoitus, Järkevyys. L3-03: reason now says the petrol growth 475 cm³ is known to tens (gamma two figures), so the difference is rounded to tens (460).
- inquiry.json: siirto (ethanol) and check-2 Vastaus rewritten (check-2: limiting datum is dT = 40 K, not Delta L).
- lesson.md Esimerkki Tulos: limiting data named (alpha, dT = 60 K).
- Convention used: a difference of whole-degree readings is known to the unit (55-15 = 40 K has two figures); trailing-zero integers that would be ambiguous (200, 50, 20) got ",0".
