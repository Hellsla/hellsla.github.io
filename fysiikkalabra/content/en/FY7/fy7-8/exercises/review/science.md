VERDICT: PASS
CONTENT-HASH: 08428ad3baa965be

## Blocking

## Polish
- exercises/exercises.json:16 — unit "kierrosta" is Finnish on the en page — "turns" (as done for fy3-3's "times").
- exercises/exercises.json:101 — unit "kertaa" is Finnish on the en page — "times".
- exercises/exercises.json:22 — "The substation of a residential area" for muuntamo; the lesson calls it "local substation" and keeps "substation" for sähköasema — use "local substation".
- exercises/solutions.md:120 — "331 MW give … 826 A": 331 MW / 400 kV = 828 A (826 A needs 330.6 MW); same slip in the Finnish — write 828 A or 330.6 MW.
- review packet (tooling) — the exercise brief is empty because scripts/review_packet.py looks for the Finnish headings.

## Checked
- All 12 answers recomputed in one script: 11.5 V, 1150, 5.0 A, 36 kW, 320 MW, 826.4 kW, 43.48 mA, 0.9917 %, 0.80 Ω, 0.75 %, 4.0 Ω, 3.306; all agree with exercises.json and answers.py.
- Every number, unit and tolerance matches the reviewed Finnish (script comparison).
- L2-04: least-squares k for P = kI² through the five points is 0.801 Ω, so reading 0.80 Ω from the curve at (5.0 A; 20 W) is right; the en figure description gives the same data and not R.
- Line loss always from I = P/U and P_h = RI², never U²/R; the solutions say why (L2-01).
- L3-01: the current is set by the 400 kV transmission voltage; the no-transformer check (7500 A, 450 MW > 150 MW) is right.
- L3-02, L3-03: R ≤ 0.010 U²/P = 4.0 Ω; same loss share gives P ∝ U², ratio 3.3.
- Ideal-transformer assumption stated in every task that needs it; magnitudes realistic.
- Hash identical at start and end.
