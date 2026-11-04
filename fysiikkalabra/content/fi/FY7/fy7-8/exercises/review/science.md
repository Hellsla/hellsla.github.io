VERDICT: PASS
CONTENT-HASH: 851f5dc3356412a5

## Blocking

## Polish
- exercises.json:20 / solutions.md:21 (L1-03) — the brief's lesson says the substation lowers 20 kV to 230 V; this task uses 400 V. Both right (400 V between phases); "vaiheiden välinen jännite" would prevent a seeming contradiction.
- exercises.json:54 (L2-02) — a phone charges with DC; "tasasuuntausta ei oteta huomioon" would close the gap (C).
- exercises.json:97 / solutions.md:112 (L3-03) — loss share is treated as the only limit; conductor heating also limits current (C). The Järkevyys example gives 826 A for 331 MW at 400 kV; 331 MW gives 827,5 A (826 A belongs to 330,6 MW). Trivial.

## Checked
- Round-1 blocker fixed: L1-04 Järkevyys now "noin viiden sähkökiukaan tehoa" (36 kW : 5 ≈ 7 kW, a real home stove).
- All 12 answers recomputed from the task text with own formulas: identical to answers.py and exercises.json (L2-01 826,4 kW, L2-02 43,5 mA, L2-03 0,992 %, L3-01 0,75 %, L3-02 4,0 Ω, L3-03 3,306).
- L2-04: least-squares fit P = k I² through the origin of the five plotted points gives k = 0,801 Ω; curve through (5,0 A; 20 W) and R = 0,80 Ω right; description gives the same data and no R; solution reads the curve, not a raw point.
- Every line-loss task uses I = P : U then R I², never U²/R; L3-01 uses the transmission voltage, with a correct "450 MW > 150 MW, impossible" check.
- Ideal-transformer ratios used the right way round (L1-01, L1-02, L1-03, L2-02).
- Units, conversions, symbolic solving before substitution, significant figures and tolerances consistent; notation matches the brief.
