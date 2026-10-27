VERDICT: PASS
CONTENT-HASH: 210c78e492d3e439

## Blocking

## Polish
- assets/sims/fy1/fy1-3/sim.js:1316 (packet line) — side effect of the round-1 fix: dots are now drawn at their exact reading but still stacked per 0,04 s bin, so two readings 0,01 s apart in neighbouring bins sit at the same height 2,4 px apart and one dot (d ≈ 8,6 px) mostly hides the other (6–7 such pairs at n = 40 in exp-1/2/3). The plot shows fewer dots than n. — Stack by collision (raise a dot while it overlaps an earlier one within d px) instead of by bin.
- solutions.md:58 (L2-01 Vastaus) — "kaksi merkitsevää numeroa kuten virhe-arviossa 0,09 s": 0,09 s has one significant figure, so by the worked example's own rule the answer would be 5 %, which the 2 % tolerance rejects (exit-ticket 3 has the same pattern, 2,0 % from 0,09 s). — Justify 4,8 % differently (e.g. computed from the exact half-range) or note that as a stated relative error it is about 5 %.
- solutions.md:63–67 (L2-02) — the signed systematic error is called $\Delta L$, the symbol the lesson keeps for the half-range; the lesson writes $\Delta x_\text{sys}$. — Write $\Delta L_\text{sys}$.
- inquiry.json sim `model` — "useamman lukeman vaihteluvälin puolikas on sitä suurempi" is not true for two readings (n = 2 gives 0,135 s < 0,15 s). — Say "monen lukeman".

## Checked
- Round-1 blocking fixed: measurement error is $e = x - x_\text{oikea}$ in lesson.md, L1-02 and the exp-2 solution; $\Delta x$ is only the half-range estimate.
- Round-1 blocking fixed: L3-02 now "250-osaan" (1/n), correct.
- Round-1 polish fixed: L1-03 notes 0,35 s exact / 0,4 s stated; summary has the "two figures if first is 1" rule; L1-02 calls 1,5 % large for a tape; sim `model` explains δ_sat vs half-range; L3-01 states constant delays.
- All 12 exercise answers recomputed independently: match answers.py and exercises.json.
- Sim series recomputed: exp-1 n = 1/5/40 error −0,22/0,076/−0,0005 s, half-range 0/0,25/0,26 s (key text "about 0,25 s" fine); exp-2 n = 40 mean 2,6995 s, error 0,2995 s; exp-3 0,525/0,085 = 6,18.
- Hook readings 2,18 / 2,45 / 2,68 / 2,67 / 2,40 s are the sim's first five readings.
- Siirto 5,44 g and its four mistake values; check-2 2,1 %; thermometer 1,5 / 0,1 °C; exit ticket 19,9 g.
- Worked example 19,09 s, 3,18 ± 0,12 s, 3,8 %, five of six inside: correct.
- Experiments isolate the varied parameter; simState gives mean, puoli, vir.
- Scope within FY1 central contents; hash identical at start and end.
