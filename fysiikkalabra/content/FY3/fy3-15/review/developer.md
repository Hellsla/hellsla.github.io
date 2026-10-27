VERDICT: DONE

Complete model solutions (teacher 2026-10-27). check_solutions and check_lesson all ok.

- solutions.md: all 12 blocks now have Periaate (why it applies) and Muunnokset, Kaava solved in symbols, unrounded Sijoitus, Vastaus with the limiting datum, and a real Järkevyys (estimate, balance, limiting case). L3-01 Vastaus now gives both asked results (206 MW, 67,6 %).
- lesson.md Esimerkki: rebuilt into the seven stages (new Periaate and Yksikkömuunnokset; one display per stage; a \dfrac made \tfrac).
- inquiry.json: solutions written for siirto (rewritten), check-2, and the numeric questions of ketju, kaukolampo and kaukolampo-tarve (the last had none).
- exercises.json (rounding rule, values unchanged): L1-05 "75" to "75,0 MW"; L2-04 "9,0 K" to "9,00 K". inquiry siirto prompt: efficiencies written 0,900 / 0,450 / 0,960 / 0,950, so the answer is "8,6 MW" (difference 0,050 has two figures).
- No numeric error found in the old solutions. ketju: 0,92 and 0,46 have two figures; the table is not a prompt, so the solution states this instead of editing it.

## Rounding pass
- Inquiry ketju: table 0,92/0,46 changed to 0,920/0,460 (hints, solution, mistake feedbacks) so 248 MW has three figures; removed the "kolmas pidetään mukana" reason and the 2,5 · 10² rewrite.
- Reasons rewritten to name the real datum (all are three figures or whole-MW differences): L1-03, L1-04, L1-05 (summa 225 MW), L2-01..L2-04, L3-01 (60 MW difference, ones place), L3-02, L3-03, Esimerkki Tulos (600 MW added).
- Inquiry siirto keeps Vastaus 8,6 MW (difference 0,950 − 0,900 = 0,050 has two figures; stored 8,64 is inside tolerance 0,03), so no zeros added.
- Järkevyys numbers recomputed (67,6 %, 87,7 %, 306 MW, 273 wagons, ratios) and ok.
