VERDICT: DONE
Complete model solutions (teacher 2026-10-27).
- solutions.md: all 12 blocks now have Annettu, Kysytty, Periaate (why the law fits: which quantity is constant, closed sample), Kaava ending in the solved unknown, Muunnokset (or why none), unrounded Sijoitus, Vastaus with significant-figure reason, and a real Järkevyys. L2-03 has Kuvaajan lukeminen. L3-01/02/03 keep their justification parts (why breath is not held, why gauge pressure cannot be used directly, why hard tyres pump poorly).
- lesson.md Esimerkki: seven stages (added Periaate and Yksikkömuunnokset, Tulos and Järkevyys now include the pV check); text and figures untouched.
- inquiry.json: solutions of siirto and check-2 rewritten in the full step order (exp-2 and ruisku are choice questions, not numeric).
- No numeric error found in the old solutions; all values match answers.py and exercises.json.

## Rounding pass
- exercises.json (text only): L1-02 160/280 kPa -> 160,0/280,0 kPa; L2-01 300 bar -> 300,0 bar; L3-02 250 kPa -> 250,0 kPa; L3-03 300 kPa -> 300,0 kPa (ambiguous trailing zeros, answers carry three or two figures). No value or answer changed.
- solutions.md: all Vastaus reasons rewritten to name the limiting data. L2-02: 90 °C is justified as "to the unit" (T2 = 363 K minus 273,15), not by the 20 °C figure count. L2-03: the limiting data are the two-figure pressures 99, 81, 66 kPa, not "hand-drawn line". L2-04: limiting datum is dT = 90 K, not "10 °C". L3-02: p1 = 250,0 + 101 and the subtraction explained by decimals.
- inquiry.json: siirto Vastaus names 72,0/1,50/101; check-2: "30 ml" -> "30,0 ml" (prompt, hints, mistakes, solution; 0,030 l -> 0,0300 l).
- lesson.md Esimerkki Tulos left as is (it already names 0,80 l and 78 kPa correctly).
