VERDICT: PASS
CONTENT-HASH: c467bcc940349896

## Blocking

## Polish
- exercises/solutions.md (L2-01 Järkevyys) — the "average about 0,5 kW" check is still the answer divided back; the 0,50 kWh heating stage as more than half is the real check already given.

## Checked
- Round-1 Blocking fixed: L1-05 Järkevyys now says a year of one LED lamp (11 kWh) is about the same as, slightly more than, one 1,5 h session on a 6 kW stove (9,0 kWh). Correct.
- New L1-03 (iron 1200 W, 230 V): a resistive heating device, so P = UI with the effective 230 V applies as the lesson states; I = 1200 W : 230 V = 5,217 A → 5,2 A, two significant figures; estimate 6 A is a real check; the fuse sentence (10 A or 16 A circuit, nothing else heavy on) is exact. exercises.json 5.217391, answers.py and solution agree.
- L2-01 wording "käyttää yli puolet energiasta" fixed; answers.py comment names `fy6-7/washer`.
- All 12 answers recomputed in one script with my own formulas: 0,18; 0,54; 5,22; 52,5; 10,95; 0,80; 480,24; 6,70; 75,92; 7,33; 371,3; 4,99. All agree with answers.py and exercises.json.
- washer figure: 2,0 / 0,2 / 0,4 kW and the 0,25 h breaks on gridlines; the description gives the same data and no energy.
- L3-03: constant resistance stated; I = U : R, P = UI, E = Pt symbolic first; "sisäenergiaksi, joka siirtyy lämpönä" correct. No "lämmöksi" in the set.
- L3-02 solved symbolically; check 64,15 € ≈ 64,20 €; the 428 kWh mistake correct.
- Units, tolerances and significant-figure reasons fit the data; magnitudes realistic.
- Notation E, P, t, a, K, K_perus as in the brief; all inside FY6 "sähköteho ja Joulen laki".
