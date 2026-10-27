VERDICT: DONE

Complete model solutions (teacher 2026-10-27). No numeric error found in the old solutions; no value changed, no ",0" added to any data.

solutions.md: all 12 blocks now have Annettu, Kysytty, Periaate, Kaava (ends with the unknown solved in symbols), Muunnokset, Sijoitus, Vastaus (value, then which datum limits the figures; differences of readings treated as such) and Järkevyys (back-substitution, estimate, sign, limiting case). L1-04 and L3-03 (graph tasks) also have Kuvaajan lukeminen naming the points read and how the slope or displacement follows. L3-03's old "Annettu" now lists the graph points.

lesson.md Esimerkki: problem and figure kept; solution rebuilt as the seven stages (Tunnetut ja kysytty, Periaate, Kaava ratkaistuna, Yksikkömuunnokset, Sijoitus, Tulos, Järkevyys), one display block per stage, symbolic first rows.

inquiry.json: complete solutions for exp-1, exp-3 and data (with Kuvaajan lukeminen) questions, and siirto; check-2 had none and now has one. Only the `solution` fields changed.

## Rounding pass
- Inquiry siirto: t = 10 s changed to 10,0 s (prompt, hints, mistake feedbacks, solution) because 10 s − 7,0 s = 3 s has one figure and 39 m needs two.
- Reasons rewritten to the real limiting datum: L1-04 (24 m − 4,0 m = 20 m), L1-05, L2-01 (3,6 exact), L2-03, L3-01 (ajat 20 min/30 min, not the distances), L3-02, L3-03, inquiry data (10 s limits, Δx = 15,0 m does not), check-2.
- Esimerkki Tulos: removed "kahdella tai kolmella", x = 170 m now also written 1,7 · 10² m with the reason (2,5 · 60 = 150 m has two figures).
- Järkevyys numbers (km/h conversions, 4,8 s, 5,2 s, 0,67 m/s) checked and ok. No answers, tolerances or answers.py changed.
