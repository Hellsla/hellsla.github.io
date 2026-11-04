VERDICT: PASS
CONTENT-HASH: c5bca088a553be97

## Blocking

## Polish
- exercises.json:192 and solutions.md:155,158 fy5-13-L2-06 — the term is "pään korjaus" while the lesson says "pääkorjaus". Also e = 0,45 cm implies a tube only about 1,5 cm wide (e ≈ 0,6r). — Use "pääkorjaus".- exercises.json:281 fy5-13-L3-04 c) — "toisen suhteen keskiarvoa" can be read as "the other ratio". — Write "suhteen $\tfrac{f_1^2}{F}$ keskiarvoa".
- exercises.json:223 fy5-13-L2-07 — this conceptual MC repeats the lesson's own "Soitin ja sävelkorkeus" paragraph almost word for word, so it is closer to level 1 than level 2. — Acceptable. Could be lifted by asking for the new f when L is shortened by a given fraction.
- solutions.md:177 fy5-13-L3-05 a) and c) — the closed-pipe-from-odd-harmonics idea reappears in the existing fy5-14-L3-03 (clarinet spectrum). The tasks are not near-duplicates: here the answer is v from two pipes in a cold hall. Note: c) uses "sointiväri", which is taught in the next chapter. — No change needed. Optionally say "yläsävelet ovat erilaiset" first.

## Checked
- Recomputed all 20 answers in one script with my own formulas: L2-05 f/n mean 95,96 Hz → v = 122,8 → 123 m/s; L2-06 λ = 67,0 cm → 343,0 m/s, e = 0,45 cm; L3-04 f²/F = 328,1/333,5/326,7/332,1, mean 330,1 → 199,0 Hz; L3-05 v_A = 330,9, v_B = 330,7 → 331 m/s; L1-08 100 Hz. All of them match answers.py and exercises.json.
- L1-06 phase claim is right: for counter-propagating waves the two displacements are equal at an antinode at all times and opposite at a node. Exactly one option is correct, and each distractor's feedback is right.
- L1-07: only 3f1 = 450 Hz is valid; the 600 Hz and 75 Hz feedback is correct.
- L2-06 b): the antinode above the mouth makes L1 shorter than λ/4, so the stated cause gives the observed direction (L1 < λ/4); L2, L3 predicted within 0,1 cm.
- L3-04: extrapolation to 120 N (+50 % past the range) is named and qualified; 1 % scatter claim checked.
- L3-05: 331 m/s ≈ 0 °C is consistent with the "cold hall" assumption; swapping the types gives 165/662 m/s (correct).
- Scope: standing waves, string and pipe eigenfrequencies; f ∝ √F tested empirically, not taught as a formula. Plan items (data → f1 and v, resonance tube + end correction, √F test, open vs closed reasoning) are all covered.
- No new task duplicates a fy5-12 or fy5-14 task or answer; the earlier resonance tasks L2-02 and L3-03 are distinct.
