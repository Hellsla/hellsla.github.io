VERDICT: FAIL
CONTENT-HASH: a3cdfb4c90cc3589

## Blocking
- exercises/solutions.md:39 (fy7-8-L1-04 Järkevyys) — **A**: "Häviö vastaa noin kymmenen sähkökiukaan tehoa": a home sauna stove is about 6–9 kW, so 36 kW is about four to six stoves, not ten; the reasonableness check rests on a wrong comparison. — Write "noin viiden sähkökiukaan tehoa" or another comparison that is true.

## Polish
- exercises.json:20 / solutions.md:29 (L1-03) — the brief's lesson says the local substation lowers 20 kV to the homes' 230 V; this task uses 400 V. Both are right (400 V between phases), but say so ("vaiheiden välinen jännite 400 V") or the student sees a contradiction. The single-phase power check 100 kW is fine in the course's model.
- exercises.json:54 (L2-02) — a phone charges with DC; the task already says the transformer is idealised "suoraan latausjännitteeksi". Adding "tasasuuntausta ei oteta huomioon" would close the gap (C).
- exercises.json:97 (L3-03) — the answer treats loss share as the only limit; a real line's current (here 1,8-fold) is also limited by heating of the conductors. One clause in the Järkevyys would keep that picture right (C).

## Checked
- All 12 answers recomputed from the task text with own formulas: identical to answers.py and exercises.json (L2-01 826,4 kW, L2-03 0,992 %, L3-01 0,75 %, L3-02 4,0 Ω, L3-03 3,306).
- L2-04 figure: least-squares fit P = k I² through the origin of the five plotted points gives k = 0,801 Ω, so the curve through (5,0 A; 20 W) and R = 0,80 Ω are right; the description gives the same data and no R; the solution reads the curve, not a raw point, as the guardrails ask.
- Every line-loss task uses I = P : U then R I², never U²/R; L3-01 uses the transmission voltage, not the generator's, with a correct "R I > U, impossible" check.
- Ideal-transformer ratios used the right way round (L1-01, L1-02, L1-03, L2-02).
- Units, conversions (kV, MW, kW, mA), symbolic solving before substitution, significant figures and tolerances consistent.
- Notation matches the brief's lesson (U₁, N₁, I₁, P_h, "johtimien yhteinen resistanssi").
