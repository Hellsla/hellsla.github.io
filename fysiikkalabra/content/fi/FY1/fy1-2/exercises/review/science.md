VERDICT: PASS
CONTENT-HASH: 6e11a95160d708c6

> Carried over from the lesson's review (content/fi/FY1/fy1-2/review/science.md) when the exercises got a folder and reviews
> of their own (2026-10-28). That review passed the whole lesson, these exercises, solutions and answers.py included,
> at the CONTENT-HASH above; `reviews.py carry --exercises` recorded that the PASS holds for the moved files. The report
> below is the original, word for word: findings about the lesson text are not about this exercise set.

## Blocking

## Polish
- lessons/FY1/fy1-2/answers.py:21 — the comment still says "9,461e12 km". 2,998·10⁵ · 3,156·10⁷ = 9,4617·10¹² km, so it should read 9,462e12 (solutions.md now says 9,462). The computed value is unaffected. Fix: change the comment to 9,462e12.

## Checked
- Hash 6e11a95160d708c6 at the start and at the end (full review, round 2).
- Round-1 blocker fixed: inquiry.json:116 (Mallin oletukset) now says "heliopaussin eli aurinkotuulen kuplan rajan ylityksestä". This matches the hook ("aurinkotuulen puhaltaman kuplan rajan … yhä Auringon painovoiman piirissä") and `voyager-malli` ("Auringon hiukkastuuli ei enää hallitse"). No "vaikutusalue" is left in the built page.
- solutions.md L3-01 now gives 9,462·10¹² km → 6,325·10⁴ AU, which is correct.
- One Python run recomputed all 12 exercise answers independently. Each one matches exercises.json within tolerance (L1-03 1,702 → 1,7 m², L3-01 63 247 → 63 250 AU, L3-03 40,20 h). It also matched the worked example (4,503·10⁹ km, 15 020 s = 4,17 h), siirto 3,236 AU/a and tarkistus-2 193,1 s = 3,22 min.
- Lesson physics: SI base table, the prefix ladder figure (n…T, ×10³ steps), and the km² = 10⁶ m² conversion. The scale table (H atom 0,11 nm, proton 1,7 fm, Earth 1,27·10⁷ m), 1 AU = 499 s = 8,32 min, and ly ≈ 9,46·10¹² km are all correct. The scope stays at s = ct and t = s/c.
- Prediction feedback: 1 h ≈ 7,2 AU, 1 week ≈ 1212 AU, 1 ly ≈ 63 000 AU; the exit ticket gives 9,5 · 8,3 min = 79 min.
- Voyager model (d0 = 119,7 AU on 2018-11-05, v = 15,341 km/s) gives 142,86 AU and 19,80 h on 1.1.2026, and 143,26 AU in mid-February 2026 (JPL gives 143,05). The table rows 119,7/132,6/145,6/158,5 AU and 16,6/18,4/20,2/22,0 h are right. The ≤ 8 min Earth–Sun caveat is correct.
- In Playwright on the preview page: date 2026-01-01 → simState vAU 142,86 and vTh 19,80, as the feedback states. The slider at n = 7/8/9 gives dAU 0,0668/0,668/6,68 and tLight 33,4/334/3336 s, which matches koe-1 and johtopaatos. Koe-1 locks the date; neither experiment's measured keys depend on the other variable.
- sim.js uses c = 299 792,458 km/s and 1 px = 3474 km (Sun 401 px, 86,3 px/s). The light pulse runs in simulated time, so the speed setting changes only the pace. Its limits are stated: planets on one line, an enlarged Voyager marker, and model values rather than measurements.
