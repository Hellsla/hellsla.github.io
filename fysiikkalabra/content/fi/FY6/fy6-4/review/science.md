VERDICT: PASS
CONTENT-HASH: 25bd8e6cddcd5332

## Blocking

## Polish
- lessons/FY6/fy6-4/figures.py:123 — `mixed_circuit` puts a node dot at (R, T), and in the lesson figure "mixed" there is one at (278, 84). Both are plain corners where nothing branches; the real junction is at (R, ym). The sim and the parallel figure were fixed in round 1, but the mixed, task and siirto figures still draw this dot. Fix: drop `node(f, xa, ym)` and `node(f, R, T)`, keeping only the dots at the two real branch points.

## Checked
- Round-1 blocking fixed: sim.js:1345 now uses one common factor `kk = min(1, 0.6/I)` for every wire, so the branch dots still add up to the main-wire dots above 0.6 A. The two branches carry I1, I2 ≤ I, and spacing is equal in every wire.
- Round-1 polish taken: the voltage sentence is now energy per charge (lesson.md:200); "ihanteelliseen" is in ennuste-2; the siirto 0.6 A feedback covers both the parallel-only error and the not-inverted error (0.5985 A); the sim's node dots are only at the branch points.
- I recomputed in one script with my own formulas, and everything agrees with lesson-answers.py: example 0.225 → 0.23 A, virhe 12 Ω, siirto 0.30 A (mistakes 0.109/0.60/0.598), tarkistus-2 5.4 V (3.6/4.5/9.0), exit ticket 115 Ω and 40 Ω, kertaus 60 mA, misconception 0.20 A, and the koe-1 and koe-2 rows.
- The johtopäätös model values (40/20 mA; 4.00 + 2.00 V; 60 + 30 = 90 mA; 50.0 Ω) match the sim's solve() and its three-significant-figure formatting.
- Every choice item has exactly one correct option. All distractor feedback is correct, and tarkistus-1 assumes mains voltage and no wire resistance.
- The graph is to scale: the series line runs 100→300 Ω, the parallel curve reaches 66.7 Ω at 200 Ω, and the markers at R2 = 100 Ω sit at 200 Ω and 50 Ω.
- Circuit figures: polarity, conventional current, I = I1 + I2, and the R2 || R3 topology in the mixed and siirto figures are correct.
- Conditions are stated: ideal battery, ideal wires and ammeter, constant resistance. The mechanism given is charge conservation plus a new path per branch.
- Scope is FY6 "vastusten kytkennät". Power appears only qualitatively, as the glow, and is deferred to its own chapter.
