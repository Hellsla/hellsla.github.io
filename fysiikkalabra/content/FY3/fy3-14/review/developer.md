VERDICT: DONE

Complete model solutions (teacher 2026-10-27).

- solutions.md: all 12 solutions now have Annettu, Kysytty, Periaate (why the principle fits: constant temperature, no latent heat, insulated vessel, limiting case), Kaava ending with the unknown solved in symbols, Muunnokset, unrounded Sijoitus, Vastaus with significant-figure reason, and a real Järkevyys (estimate, energy balance recomputed, comparison). No numeric error found; all values agree with answers.py. Corrected a loose wording: L1-05 now compares with 66,8 kJ melting energy.
- lesson.md ## Esimerkki: seven stages (Tunnetut ja kysytty, Periaate, Kaava ratkaistuna, Yksikkömuunnokset, Sijoitus, Tulos, Järkevyys); former stage 2 comparison moved into formula and substitution; energy balance recomputed in Järkevyys.
- inquiry.json: complete `solution` for koe-1 and koe-2 questions, siirto and tarkistus-2 (no other field changed).

## Rounding pass
- Zeros added (values, answers, tolerances, answers.py unchanged): L2-04 0,0500 kg ice; L3-01 0,600 kg and 35,0 °C; L3-02 0,200 kg, 15,0 °C, 0,300 kg, −10,0 °C; L3-03 0,100 kg, 10,0 °C, 0,500 kg, −40,0 °C (c_j = 2100 treated as a table value that does not limit); inquiry siirto 0,250 kg and 22,0 °C. Same in solutions and hints.
- Reasons rewritten to name the limiting datum: L1-03, L1-05, L2-01 (water terms, not ice mass), L2-02, L2-03, L2-04, L3-01..L3-03, inquiry siirto, Esimerkki Tulos (ice mass fixes Q_j, difference loses figures).
- Inquiry koe-1 and koe-2: Vastaus rounded to 27 °C (tarkasti 26,57) and 13 g (tarkasti 12,6), inside tolerances 0,05; the simulation fixes the masses so zeros cannot be added.
- Removed the "kolmas numero pidetään mukana" arguments (L3-01, L3-02).
